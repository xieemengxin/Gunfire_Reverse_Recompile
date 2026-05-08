#include <cstring>
#include <cstdint>
#include <stdexcept>
#include <unordered_set>
#include "ASTree.h"
#include "FastStack.h"
#include "pyc_numeric.h"
#include "bytecode.h"

// This must be a triple quote (''' or """), to handle interpolated string literals containing the opposite quote style.
// E.g. f'''{"interpolated "123' literal"}'''    -> valid.
// E.g. f"""{"interpolated "123' literal"}"""    -> valid.
// E.g. f'{"interpolated "123' literal"}'        -> invalid, unescaped quotes in literal.
// E.g. f'{"interpolated \"123\' literal"}'      -> invalid, f-string expression does not allow backslash.
// NOTE: Nested f-strings not supported.
#define F_STRING_QUOTE "'''"

static void append_to_chain_store(const PycRef<ASTNode>& chainStore,
        PycRef<ASTNode> item, FastStack& stack, const PycRef<ASTBlock>& curblock);

/* Use this to determine if an error occurred (and therefore, if we should
 * avoid cleaning the output tree) */
static bool cleanBuild;

/* Use this to prevent printing return keywords and newlines in lambdas. */
static bool inLambda = false;

/* Use this to keep track of whether we need to print out any docstring and
 * the list of global variables that we are using (such as inside a function). */
static bool printDocstringAndGlobals = false;

/* Use this to keep track of whether we need to print a class or module docstring */
static bool printClassDocstring = true;

// shortcut for all top/pop calls
static PycRef<ASTNode> StackPopTop(FastStack& stack)
{
    const auto node(stack.top());
    stack.pop();
    return node;
}

static void append_tuple_unpack_item(ASTTuple::value_t& values, const PycRef<ASTNode>& item)
{
    if (item != nullptr && item.type() == ASTNode::NODE_TUPLE) {
        const auto tuple = item.cast<ASTTuple>();
        for (const auto& value : tuple->values())
            values.emplace_back(value);
        return;
    }

    values.emplace_back(new ASTStarred(item));
}

static void append_list_unpack_item(ASTList::value_t& values, const PycRef<ASTNode>& item)
{
    if (item != nullptr && item.type() == ASTNode::NODE_LIST) {
        const auto list = item.cast<ASTList>();
        for (const auto& value : list->values())
            values.emplace_back(value);
        return;
    }

    values.emplace_back(new ASTStarred(item));
}

static void append_set_unpack_item(ASTSet::value_t& values, const PycRef<ASTNode>& item)
{
    if (item != nullptr && item.type() == ASTNode::NODE_SET) {
        const auto set = item.cast<ASTSet>();
        for (const auto& value : set->values())
            values.emplace_back(value);
        return;
    }

    values.emplace_back(new ASTStarred(item));
}

static void append_map_unpack_item(ASTMap* map, const PycRef<ASTNode>& item)
{
    if (item != nullptr && item.type() == ASTNode::NODE_MAP) {
        const auto src = item.cast<ASTMap>();
        for (const auto& entry : src->values())
            map->add(entry.first, entry.second);
        return;
    }

    map->add_unpack(item);
}

static void append_call_ex_args(ASTCall::pparam_t& params, const PycRef<ASTNode>& args)
{
    if (args != nullptr && args.type() == ASTNode::NODE_TUPLE) {
        const auto tuple = args.cast<ASTTuple>();
        for (const auto& value : tuple->values())
            params.emplace_back(value);
        return;
    }

    params.emplace_back(new ASTStarred(args));
}

static PycRef<ASTNode> maybe_make_class(
        const PycRef<ASTNode>& func,
        const ASTCall::pparam_t& pparams,
        const ASTCall::kwparam_t& kwparams)
{
    if (func == nullptr || func->type() != ASTNode::NODE_LOADBUILDCLASS || pparams.size() < 2)
        return nullptr;

    auto it = pparams.begin();
    PycRef<ASTNode> class_body = *it++;
    PycRef<ASTNode> class_name = *it++;

    ASTTuple::value_t bases;
    for (; it != pparams.end(); ++it)
        bases.emplace_back(*it);

    PycRef<ASTNode> class_call = new ASTCall(class_body, ASTCall::pparam_t(), ASTCall::kwparam_t());
    return new ASTClass(class_call, new ASTTuple(bases), class_name,
        ASTClass::kwparam_t(kwparams.begin(), kwparams.end()));
}

static void rewrite_named_function_args(ASTCall::pparam_t& params, const PycRef<ASTBlock>& curblock)
{
    for (auto it = params.begin(); it != params.end(); ++it) {
        PycRef<ASTNode> param = *it;
        if (param == nullptr || param->type() != ASTNode::NODE_FUNCTION)
            continue;

        PycRef<ASTNode> fun_code = param.cast<ASTFunction>()->code();
        PycRef<PycCode> code_src = fun_code.cast<ASTObject>()->object().cast<PycCode>();
        PycRef<PycString> function_name = code_src->name();
        if (function_name->isEqual("<lambda>"))
            continue;

        PycRef<ASTNode> decor_name = new ASTName(function_name);
        curblock->append(new ASTStore(param, decor_name));
        *it = decor_name;
    }
}

static int import_level_from_node(const PycRef<ASTNode>& level_node)
{
    if (level_node == nullptr || level_node->type() != ASTNode::NODE_OBJECT)
        return 0;

    PycRef<PycObject> obj = level_node.cast<ASTObject>()->object();
    if (obj == nullptr)
        return 0;

    if (obj.type() == PycObject::TYPE_INT) {
        return obj.cast<PycInt>()->value();
    }

    if (obj.type() == PycObject::TYPE_LONG) {
        PycRef<PycLong> value = obj.cast<PycLong>();
        if (value->size() == 0 || value->value().empty())
            return 0;
        return value->value().front();
    }

    return 0;
}

static bool is_default_dotted_import_binding(const PycRef<ASTImport>& import, const PycRef<ASTNode>& dest)
{
    if (import == nullptr || import->fromlist() != NULL || dest == nullptr || dest->type() != ASTNode::NODE_NAME)
        return false;

    PycRef<ASTName> import_name = import->name().try_cast<ASTName>();
    PycRef<ASTName> dest_name = dest.try_cast<ASTName>();
    if (import_name == nullptr || dest_name == nullptr)
        return false;

    const char* full_name = import_name->name()->value();
    const char* bound_name = dest_name->name()->value();
    const char* dot = strchr(full_name, '.');
    if (dot == nullptr)
        return false;

    size_t bound_len = strlen(bound_name);
    return bound_len == static_cast<size_t>(dot - full_name)
        && strncmp(full_name, bound_name, bound_len) == 0;
}

static PycRef<ASTNode> recover_empty_literal_after_restore(int prev_opcode, const PycRef<ASTNode>& value)
{
    if (value.type() != PycObject::TYPE_NULL)
        return value;

    switch (prev_opcode) {
    case Pyc::BUILD_LIST_A:
        return new ASTList(ASTList::value_t());
    case Pyc::BUILD_TUPLE_A:
        return new ASTTuple(ASTTuple::value_t());
    case Pyc::BUILD_SET_A:
        return new ASTSet(ASTSet::value_t());
    case Pyc::BUILD_MAP_A:
        return new ASTMap();
    default:
        return value;
    }
}

/* compiler generates very, VERY similar byte code for if/else statement block and if-expression
 *  statement
 *      if a: b = 1
 *      else: b = 2
 *  expression:
 *      b = 1 if a else 2
 *  (see for instance https://stackoverflow.com/a/52202007)
 *  here, try to guess if just finished else statement is part of if-expression (ternary operator)
 *  if it is, remove statements from the block and put a ternary node on top of stack
 */
static void CheckIfExpr(FastStack& stack, PycRef<ASTBlock> curblock)
{
    if (stack.empty())
        return;
    if (curblock->nodes().size() < 2)
        return;
    auto rit = curblock->nodes().crbegin();
    // the last is "else" block, the one before should be "if" (could be "for", ...)
    if ((*rit)->type() != ASTNode::NODE_BLOCK ||
        (*rit).cast<ASTBlock>()->blktype() != ASTBlock::BLK_ELSE)
        return;
    ++rit;
    if ((*rit)->type() != ASTNode::NODE_BLOCK ||
        (*rit).cast<ASTBlock>()->blktype() != ASTBlock::BLK_IF)
        return;
    if ((*rit).cast<ASTBlock>()->size() != 0 || curblock->nodes().back().cast<ASTBlock>()->size() != 0)
        return;
    auto else_expr = StackPopTop(stack);
    curblock->removeLast();
    auto if_block = curblock->nodes().back();
    auto if_expr = StackPopTop(stack);
    curblock->removeLast();
    stack.push(new ASTTernary(std::move(if_block), std::move(if_expr), std::move(else_expr)));
}

static bool CollapseIfExprChain(FastStack& stack, PycRef<ASTBlock> curblock)
{
    if (stack.empty())
        return false;
    if (curblock->nodes().size() < 2)
        return false;

    std::vector<PycRef<ASTBlock>> rev_chain;
    for (auto rit = curblock->nodes().crbegin(); rit != curblock->nodes().crend(); ++rit) {
        PycRef<ASTBlock> block = (*rit).try_cast<ASTBlock>();
        if (block == nullptr)
            break;
        if ((block->blktype() != ASTBlock::BLK_IF
                && block->blktype() != ASTBlock::BLK_ELIF
                && block->blktype() != ASTBlock::BLK_ELSE)
                || block->size() != 0) {
            break;
        }
        rev_chain.push_back(block);
        if (block->blktype() == ASTBlock::BLK_IF)
            break;
    }

    if (rev_chain.size() < 2)
        return false;
    if (rev_chain.front()->blktype() != ASTBlock::BLK_ELSE)
        return false;
    if (rev_chain.back()->blktype() != ASTBlock::BLK_IF)
        return false;
    for (size_t i = 1; i + 1 < rev_chain.size(); ++i) {
        if (rev_chain[i]->blktype() != ASTBlock::BLK_ELIF)
            return false;
    }
    if (stack.size() < static_cast<int>(rev_chain.size()))
        return false;

    PycRef<ASTNode> expr = StackPopTop(stack);
    for (size_t i = 1; i < rev_chain.size(); ++i) {
        PycRef<ASTNode> branch_expr = StackPopTop(stack);
        expr = new ASTTernary(rev_chain[i].cast<ASTNode>(), branch_expr, expr);
    }
    for (size_t i = 0; i < rev_chain.size(); ++i)
        curblock->removeLast();
    stack.push(expr);
    return true;
}

static void TrimCollapsedIfExprHistory(FastStack& stack, stackhist_t& stack_hist)
{
    while (!stack_hist.empty() && stack_hist.top().size() > stack.size())
        stack_hist.pop();
}

PycRef<ASTNode> BuildFromCode(PycRef<PycCode> code, PycModule* mod)
{
    PycBuffer source(code->code()->value(), code->code()->length());

    FastStack stack((mod->majorVer() == 1) ? 20 : code->stackSize());
    stackhist_t stack_hist;

    std::stack<PycRef<ASTBlock> > blocks;
    PycRef<ASTBlock> defblock = new ASTBlock(ASTBlock::BLK_MAIN);
    defblock->init();
    PycRef<ASTBlock> curblock = defblock;
    blocks.push(defblock);

    int opcode, operand;
    int curpos = 0;
    int pos = 0;
    struct UnpackFrame {
        int remaining;
        int after;
    };
    int unpack = 0;
    int unpack_after = -1;
    std::vector<UnpackFrame> unpack_frames;
    auto sync_unpack = [&]() {
        if (unpack_frames.empty()) {
            unpack = 0;
            unpack_after = -1;
        } else {
            unpack = unpack_frames.back().remaining;
            unpack_after = unpack_frames.back().after;
        }
    };
    bool else_pop = false;
    bool need_try = false;
    bool variable_annotations = false;
    int prev_opcode = Pyc::NOP;
    bool prev_terminal_flow = false;
    auto collapse_empty_comprehension_condition_blocks = [&]() {
        bool has_comprehension_parent = false;
        std::stack<PycRef<ASTBlock> > probe = blocks;
        while (probe.size() > 1) {
            PycRef<ASTBlock> block = probe.top();
            probe.pop();
            if (block->blktype() == ASTBlock::BLK_FOR
                    && block.cast<ASTIterBlock>()->isComprehension()) {
                has_comprehension_parent = true;
                break;
            }
        }

        if (!has_comprehension_parent)
            return;

        while ((curblock->blktype() == ASTBlock::BLK_IF
                || curblock->blktype() == ASTBlock::BLK_ELIF
                || curblock->blktype() == ASTBlock::BLK_ELSE)
                && curblock->size() == 0
                && blocks.size() > 1) {
            blocks.pop();
            if (!stack_hist.empty())
                stack_hist.pop();
            curblock = blocks.top();
        }
    };

    while (!source.atEof()) {
#if defined(BLOCK_DEBUG) || defined(STACK_DEBUG)
        fprintf(stderr, "%-7d", pos);
    #ifdef STACK_DEBUG
        fprintf(stderr, "%-5d", (unsigned int)stack_hist.size() + 1);
    #endif
    #ifdef BLOCK_DEBUG
        for (unsigned int i = 0; i < blocks.size(); i++)
            fprintf(stderr, "    ");
        fprintf(stderr, "%s (%d)", curblock->type_str(), curblock->end());
    #endif
        fprintf(stderr, "\n");
#endif

        curpos = pos;
        bc_next(source, mod, opcode, operand, pos);

        bool except_cleanup_or_handler =
            opcode == Pyc::LOAD_CONST_A
            || opcode == Pyc::STORE_FAST_A
            || opcode == Pyc::DELETE_FAST_A
            || opcode == Pyc::END_FINALLY
            || opcode == Pyc::POP_BLOCK
            || opcode == Pyc::DUP_TOP
            || opcode == Pyc::POP_TOP;
        bool prev_except_end_flow =
            prev_opcode == Pyc::RETURN_VALUE ||
            prev_opcode == Pyc::RETURN_CONST_A ||
            prev_opcode == Pyc::INSTRUMENTED_RETURN_VALUE_A ||
            prev_opcode == Pyc::INSTRUMENTED_RETURN_CONST_A ||
            prev_opcode == Pyc::BREAK_LOOP ||
            prev_opcode == Pyc::CONTINUE_LOOP_A ||
            prev_opcode == Pyc::JUMP_ABSOLUTE_A ||
            prev_opcode == Pyc::JUMP_BACKWARD_A ||
            prev_opcode == Pyc::JUMP_BACKWARD_NO_INTERRUPT_A;

        while (curblock->blktype() == ASTBlock::BLK_EXCEPT
                && curblock->end() != 0
                && (curblock->end() < curpos
                    || (curblock->end() == curpos && prev_except_end_flow)
                    || (prev_except_end_flow
                        && curblock->end() > curpos
                        && !except_cleanup_or_handler))
                && blocks.size() > 1) {
            if (!stack_hist.empty()) {
                bool preserve_current_stack = !stack.empty()
                    && stack.top().type() != PycObject::TYPE_NULL;
                if (!preserve_current_stack && stack.size() <= stack_hist.top().size())
                    stack = stack_hist.top();
                stack_hist.pop();
            }
            PycRef<ASTBlock> done = curblock;
            blocks.pop();
            curblock = blocks.top();
            curblock->append(done.cast<ASTNode>());
        }

        while (curblock->blktype() == ASTBlock::BLK_WHILE
                && curblock->end() != 0
                && curblock->end() <= curpos
                && blocks.size() > 1) {
            if (!stack_hist.empty()) {
                stack = stack_hist.top();
                stack_hist.pop();
            }
            PycRef<ASTBlock> done = curblock;
            blocks.pop();
            curblock = blocks.top();
            curblock->append(done.cast<ASTNode>());
        }

        while (curblock->blktype() == ASTBlock::BLK_CONTAINER
                && curblock->end() != 0
                && curblock->end() <= curpos
                && blocks.size() > 1) {
            if (!stack_hist.empty()) {
                stack = stack_hist.top();
                stack_hist.pop();
            }
            PycRef<ASTBlock> done = curblock;
            blocks.pop();
            curblock = blocks.top();
            curblock->append(done.cast<ASTNode>());
        }

        while ((curblock->blktype() == ASTBlock::BLK_IF
                || curblock->blktype() == ASTBlock::BLK_ELIF
                || curblock->blktype() == ASTBlock::BLK_ELSE)
                && curblock->end() != 0
                && curblock->end() < curpos
                && curblock->size() > 0
                && blocks.size() > 1) {
            bool loop_local_filter = false;
            std::stack<PycRef<ASTBlock> > probe = blocks;
            probe.pop();
            while (!probe.empty()) {
                PycRef<ASTBlock> parent = probe.top();
                if (parent->blktype() == ASTBlock::BLK_IF
                        || parent->blktype() == ASTBlock::BLK_ELIF
                        || parent->blktype() == ASTBlock::BLK_ELSE) {
                    probe.pop();
                    continue;
                }
                if ((parent->blktype() == ASTBlock::BLK_FOR
                        || parent->blktype() == ASTBlock::BLK_ASYNCFOR)
                        && curblock->end() <= parent.cast<ASTIterBlock>()->start()) {
                    loop_local_filter = true;
                }
                break;
            }
            if (loop_local_filter)
                break;

            if (!stack_hist.empty()) {
                stack = stack_hist.top();
                stack_hist.pop();
            }

            PycRef<ASTBlock> done = curblock;
            blocks.pop();
            curblock = blocks.top();
            curblock->append(done.cast<ASTNode>());
            CheckIfExpr(stack, curblock);
        }

        while ((curblock->blktype() == ASTBlock::BLK_IF
                || curblock->blktype() == ASTBlock::BLK_ELIF)
                && curblock->end() != 0
                && curblock->end() == curpos
                && curblock->size() == 0
                && blocks.size() > 1
                && !stack_hist.empty()
                && stack.size() > stack_hist.top().size()) {
            PycRef<ASTBlock> done = curblock;
            blocks.pop();
            curblock = blocks.top();
            curblock->append(done.cast<ASTNode>());
            CheckIfExpr(stack, curblock);
        }

        while (curblock->blktype() == ASTBlock::BLK_ELSE
                && curblock->end() != 0
                && curblock->end() == curpos
                && curblock->size() == 0
                && blocks.size() > 1
                && !stack_hist.empty()
                && stack.size() > stack_hist.top().size()) {
            PycRef<ASTBlock> done = curblock;
            blocks.pop();
            curblock = blocks.top();
            curblock->append(done.cast<ASTNode>());
            if (!CollapseIfExprChain(stack, curblock))
                break;
            TrimCollapsedIfExprHistory(stack, stack_hist);
        }

        if (curblock->blktype() == ASTBlock::BLK_CONTAINER
                && curblock.cast<ASTContainerBlock>()->hasFinally()
                && !curblock.cast<ASTContainerBlock>()->hasExcept()
                && curblock.cast<ASTContainerBlock>()->finally() == curpos) {
            stack_hist.push(stack);

            PycRef<ASTBlock> final = new ASTBlock(ASTBlock::BLK_FINALLY, 0, true);
            blocks.push(final);
            curblock = blocks.top();
        }

        // Enter a bare finally suite as soon as control reaches its target.
        // Waiting until POP_BLOCK is too late for Python 3.6 patterns like
        // "with ...: try: return ... finally: cleanup()", because the cleanup
        // bytecode would already have been appended to the try block.
        if (curblock->blktype() == ASTBlock::BLK_TRY
                && curblock->end() == curpos
                && blocks.size() > 1) {
            PycRef<ASTBlock> tryblock = curblock;
            blocks.pop();
            PycRef<ASTBlock> parent = blocks.top();
            if (parent->blktype() == ASTBlock::BLK_CONTAINER) {
                PycRef<ASTContainerBlock> cont = parent.cast<ASTContainerBlock>();
                if (cont->hasExcept()
                        && cont->except() == curpos) {
                    parent->append(tryblock.cast<ASTNode>());

                    PycRef<ASTBlock> except = new ASTCondBlock(ASTBlock::BLK_EXCEPT, 0, NULL, false);
                    except->init();
                    blocks.push(except);
                    curblock = blocks.top();
                } else if (cont->hasFinally()
                        && !cont->hasExcept()
                        && cont->finally() == curpos) {
                    parent->append(tryblock.cast<ASTNode>());
                    stack_hist.push(stack);

                    PycRef<ASTBlock> final = new ASTBlock(ASTBlock::BLK_FINALLY, 0, true);
                    blocks.push(final);
                    curblock = blocks.top();
                } else {
                    blocks.push(tryblock);
                    curblock = blocks.top();
                }
            } else {
                blocks.push(tryblock);
                curblock = blocks.top();
            }
        }

        if (need_try && opcode != Pyc::SETUP_EXCEPT_A) {
            need_try = false;

            /* Store the current stack for the except/finally statement(s) */
            stack_hist.push(stack);
            int try_end = curblock->end();
            if (curblock->blktype() == ASTBlock::BLK_CONTAINER) {
                PycRef<ASTContainerBlock> cont = curblock.cast<ASTContainerBlock>();
                if (cont->hasExcept()) {
                    try_end = cont->except();
                } else if (cont->hasFinally()) {
                    try_end = cont->finally();
                }
            }
            PycRef<ASTBlock> tryblock = new ASTBlock(ASTBlock::BLK_TRY, try_end, true);
            blocks.push(tryblock);
            curblock = blocks.top();
        } else if ((curblock->blktype() == ASTBlock::BLK_IF
                    || curblock->blktype() == ASTBlock::BLK_ELIF
                    || curblock->blktype() == ASTBlock::BLK_ELSE)
                && curblock->end() != 0
                && curblock->end() == curpos
                && curblock->size() > 0
                && blocks.size() > 1) {
            while ((curblock->blktype() == ASTBlock::BLK_IF
                    || curblock->blktype() == ASTBlock::BLK_ELIF
                    || curblock->blktype() == ASTBlock::BLK_ELSE)
                    && curblock->end() != 0
                    && curblock->end() == curpos
                    && curblock->size() > 0
                    && blocks.size() > 1) {
                if (!stack_hist.empty()) {
                    stack = stack_hist.top();
                    stack_hist.pop();
                }

                PycRef<ASTBlock> prev = curblock;
                blocks.pop();
                curblock = blocks.top();
                curblock->append(prev.cast<ASTNode>());
                CheckIfExpr(stack, curblock);
            }
        } else if (else_pop
                && opcode != Pyc::POP_BLOCK
                && opcode != Pyc::JUMP_FORWARD_A
                && opcode != Pyc::JUMP_IF_FALSE_A
                && opcode != Pyc::JUMP_IF_FALSE_OR_POP_A
                && opcode != Pyc::POP_JUMP_IF_FALSE_A
                && opcode != Pyc::POP_JUMP_FORWARD_IF_FALSE_A
                && opcode != Pyc::JUMP_IF_TRUE_A
                && opcode != Pyc::JUMP_IF_TRUE_OR_POP_A
                && opcode != Pyc::POP_JUMP_IF_TRUE_A
                && opcode != Pyc::POP_JUMP_FORWARD_IF_TRUE_A) {
            else_pop = false;

            PycRef<ASTBlock> prev = curblock;
            while (prev->end() < pos
                    && prev->blktype() != ASTBlock::BLK_MAIN) {
                if (prev->blktype() != ASTBlock::BLK_CONTAINER) {
                    if (prev->end() == 0) {
                        break;
                    }

                    /* We want to keep the stack the same, but we need to pop
                     * a level off the history. */
                    //stack = stack_hist.top();
                    if (!stack_hist.empty())
                        stack_hist.pop();
                }
                blocks.pop();

                if (blocks.empty())
                    break;

                curblock = blocks.top();
                curblock->append(prev.cast<ASTNode>());

                prev = curblock;

                CheckIfExpr(stack, curblock);
            }
        }

        switch (opcode) {
        case Pyc::BINARY_OP_A:
            {
                ASTBinary::BinOp op = ASTBinary::from_binary_op(operand);
                if (op == ASTBinary::BIN_INVALID)
                    fprintf(stderr, "Unsupported `BINARY_OP` operand value: %d\n", operand);
                PycRef<ASTNode> right = stack.top();
                stack.pop();
                PycRef<ASTNode> left = stack.top();
                stack.pop();
                stack.push(new ASTBinary(left, right, op));
            }
            break;
        case Pyc::BINARY_ADD:
        case Pyc::BINARY_AND:
        case Pyc::BINARY_DIVIDE:
        case Pyc::BINARY_FLOOR_DIVIDE:
        case Pyc::BINARY_LSHIFT:
        case Pyc::BINARY_MODULO:
        case Pyc::BINARY_MULTIPLY:
        case Pyc::BINARY_OR:
        case Pyc::BINARY_POWER:
        case Pyc::BINARY_RSHIFT:
        case Pyc::BINARY_SUBTRACT:
        case Pyc::BINARY_TRUE_DIVIDE:
        case Pyc::BINARY_XOR:
        case Pyc::BINARY_MATRIX_MULTIPLY:
        case Pyc::INPLACE_ADD:
        case Pyc::INPLACE_AND:
        case Pyc::INPLACE_DIVIDE:
        case Pyc::INPLACE_FLOOR_DIVIDE:
        case Pyc::INPLACE_LSHIFT:
        case Pyc::INPLACE_MODULO:
        case Pyc::INPLACE_MULTIPLY:
        case Pyc::INPLACE_OR:
        case Pyc::INPLACE_POWER:
        case Pyc::INPLACE_RSHIFT:
        case Pyc::INPLACE_SUBTRACT:
        case Pyc::INPLACE_TRUE_DIVIDE:
        case Pyc::INPLACE_XOR:
        case Pyc::INPLACE_MATRIX_MULTIPLY:
            {
                ASTBinary::BinOp op = ASTBinary::from_opcode(opcode);
                if (op == ASTBinary::BIN_INVALID)
                    throw std::runtime_error("Unhandled opcode from ASTBinary::from_opcode");
                PycRef<ASTNode> right = stack.top();
                stack.pop();
                PycRef<ASTNode> left = stack.top();
                stack.pop();
                stack.push(new ASTBinary(left, right, op));
            }
            break;
        case Pyc::BINARY_SUBSCR:
            {
                PycRef<ASTNode> subscr = stack.top();
                stack.pop();
                PycRef<ASTNode> src = stack.top();
                stack.pop();
                stack.push(new ASTSubscr(src, subscr));
            }
            break;
        case Pyc::BREAK_LOOP:
            curblock->append(new ASTKeyword(ASTKeyword::KW_BREAK));
            break;
        case Pyc::BUILD_CLASS:
            {
                PycRef<ASTNode> class_code = stack.top();
                stack.pop();
                PycRef<ASTNode> bases = stack.top();
                stack.pop();
                PycRef<ASTNode> name = stack.top();
                stack.pop();
                stack.push(new ASTClass(class_code, bases, name));
            }
            break;
        case Pyc::BUILD_FUNCTION:
            {
                PycRef<ASTNode> fun_code = stack.top();
                stack.pop();
                stack.push(new ASTFunction(fun_code, {}, {}));
            }
            break;
        case Pyc::BUILD_LIST_A:
            {
                ASTList::value_t values;
                for (int i=0; i<operand; i++) {
                    values.push_front(stack.top());
                    stack.pop();
                }
                stack.push(new ASTList(values));
            }
            break;
        case Pyc::BUILD_LIST_UNPACK_A:
            {
                ASTList::value_t values;
                std::vector<PycRef<ASTNode>> items;
                items.reserve(operand);
                for (int i = 0; i < operand; ++i) {
                    items.emplace_back(stack.top());
                    stack.pop();
                }
                for (auto it = items.rbegin(); it != items.rend(); ++it)
                    append_list_unpack_item(values, *it);
                stack.push(new ASTList(values));
            }
            break;
        case Pyc::BUILD_SET_A:
            {
                ASTSet::value_t values;
                for (int i=0; i<operand; i++) {
                    values.push_front(stack.top());
                    stack.pop();
                }
                stack.push(new ASTSet(values));
            }
            break;
        case Pyc::BUILD_SET_UNPACK_A:
            {
                ASTSet::value_t values;
                std::vector<PycRef<ASTNode>> items;
                items.reserve(operand);
                for (int i = 0; i < operand; ++i) {
                    items.emplace_back(stack.top());
                    stack.pop();
                }
                for (auto it = items.rbegin(); it != items.rend(); ++it)
                    append_set_unpack_item(values, *it);
                stack.push(new ASTSet(values));
            }
            break;
        case Pyc::BUILD_MAP_A:
            if (mod->verCompare(3, 5) >= 0) {
                auto map = new ASTMap;
                for (int i=0; i<operand; ++i) {
                    PycRef<ASTNode> value = stack.top();
                    stack.pop();
                    PycRef<ASTNode> key = stack.top();
                    stack.pop();
                    map->add(key, value);
                }
                stack.push(map);
            } else {
                if (stack.top().type() == ASTNode::NODE_CHAINSTORE) {
                    stack.pop();
                }
                stack.push(new ASTMap());
            }
            break;
        case Pyc::BUILD_MAP_UNPACK_A:
        case Pyc::BUILD_MAP_UNPACK_WITH_CALL_A:
            {
                auto map = new ASTMap;
                const int unpackCount = (opcode == Pyc::BUILD_MAP_UNPACK_WITH_CALL_A && mod->verCompare(3, 6) < 0)
                    ? (operand & 0xFF)
                    : operand;
                std::vector<PycRef<ASTNode>> items;
                items.reserve(unpackCount);
                for (int i = 0; i < unpackCount; ++i) {
                    items.emplace_back(stack.top());
                    stack.pop();
                }
                for (auto it = items.rbegin(); it != items.rend(); ++it)
                    append_map_unpack_item(map, *it);
                stack.push(map);
            }
            break;
        case Pyc::BUILD_CONST_KEY_MAP_A:
            // Top of stack will be a tuple of keys.
            // Values will start at TOS - 1.
            {
                PycRef<ASTNode> keys = stack.top();
                stack.pop();

                ASTConstMap::values_t values;
                values.reserve(operand);
                for (int i = 0; i < operand; ++i) {
                    PycRef<ASTNode> value = stack.top();
                    stack.pop();
                    values.push_back(value);
                }

                stack.push(new ASTConstMap(keys, values));
            }
            break;
        case Pyc::STORE_MAP:
            {
                PycRef<ASTNode> key = stack.top();
                stack.pop();
                PycRef<ASTNode> value = stack.top();
                stack.pop();
                PycRef<ASTMap> map = stack.top().cast<ASTMap>();
                map->add(key, value);
            }
            break;
        case Pyc::BUILD_SLICE_A:
            {
                if (operand == 2) {
                    PycRef<ASTNode> end = stack.top();
                    stack.pop();
                    PycRef<ASTNode> start = stack.top();
                    stack.pop();

                    if (start.type() == ASTNode::NODE_OBJECT
                            && start.cast<ASTObject>()->object() == Pyc_None) {
                        start = NULL;
                    }

                    if (end.type() == ASTNode::NODE_OBJECT
                            && end.cast<ASTObject>()->object() == Pyc_None) {
                        end = NULL;
                    }

                    if (start == NULL && end == NULL) {
                        stack.push(new ASTSlice(ASTSlice::SLICE0));
                    } else if (start == NULL) {
                        stack.push(new ASTSlice(ASTSlice::SLICE2, start, end));
                    } else if (end == NULL) {
                        stack.push(new ASTSlice(ASTSlice::SLICE1, start, end));
                    } else {
                        stack.push(new ASTSlice(ASTSlice::SLICE3, start, end));
                    }
                } else if (operand == 3) {
                    PycRef<ASTNode> step = stack.top();
                    stack.pop();
                    PycRef<ASTNode> end = stack.top();
                    stack.pop();
                    PycRef<ASTNode> start = stack.top();
                    stack.pop();

                    if (start.type() == ASTNode::NODE_OBJECT
                            && start.cast<ASTObject>()->object() == Pyc_None) {
                        start = NULL;
                    }

                    if (end.type() == ASTNode::NODE_OBJECT
                            && end.cast<ASTObject>()->object() == Pyc_None) {
                        end = NULL;
                    }

                    if (step.type() == ASTNode::NODE_OBJECT
                            && step.cast<ASTObject>()->object() == Pyc_None) {
                        step = NULL;
                    }

                    /* We have to do this as a slice where one side is another slice */
                    /* [[a:b]:c] */

                    if (start == NULL && end == NULL) {
                        stack.push(new ASTSlice(ASTSlice::SLICE0));
                    } else if (start == NULL) {
                        stack.push(new ASTSlice(ASTSlice::SLICE2, start, end));
                    } else if (end == NULL) {
                        stack.push(new ASTSlice(ASTSlice::SLICE1, start, end));
                    } else {
                        stack.push(new ASTSlice(ASTSlice::SLICE3, start, end));
                    }

                    PycRef<ASTNode> lhs = stack.top();
                    stack.pop();

                    if (step == NULL) {
                        stack.push(new ASTSlice(ASTSlice::SLICE1, lhs, step));
                    } else {
                        stack.push(new ASTSlice(ASTSlice::SLICE3, lhs, step));
                    }
                }
            }
            break;
        case Pyc::BUILD_STRING_A:
            {
                // Nearly identical logic to BUILD_LIST
                ASTList::value_t values;
                for (int i = 0; i < operand; i++) {
                    values.push_front(stack.top());
                    stack.pop();
                }
                stack.push(new ASTJoinedStr(values));
            }
            break;
        case Pyc::BUILD_TUPLE_A:
            {
                // if class is a closure code, ignore this tuple
                PycRef<ASTNode> tos = stack.top();
                if (tos && tos->type() == ASTNode::NODE_LOADBUILDCLASS) {
                    break;
                }

                ASTTuple::value_t values;
                values.resize(operand);
                for (int i=0; i<operand; i++) {
                    values[operand-i-1] = stack.top();
                    stack.pop();
                }
                stack.push(new ASTTuple(values));
            }
            break;
        case Pyc::BUILD_TUPLE_UNPACK_A:
        case Pyc::BUILD_TUPLE_UNPACK_WITH_CALL_A:
            {
                ASTTuple::value_t values;
                std::vector<PycRef<ASTNode>> items;
                items.reserve(operand);
                for (int i = 0; i < operand; ++i) {
                    items.emplace_back(stack.top());
                    stack.pop();
                }
                for (auto it = items.rbegin(); it != items.rend(); ++it)
                    append_tuple_unpack_item(values, *it);
                stack.push(new ASTTuple(values));
            }
            break;
        case Pyc::KW_NAMES_A:
            {

                int kwparams = code->getConst(operand).cast<PycTuple>()->size();
                ASTKwNamesMap kwparamList;
                std::vector<PycRef<PycObject>> keys = code->getConst(operand).cast<PycSimpleSequence>()->values();
                for (int i = 0; i < kwparams; i++) {
                    kwparamList.add(new ASTObject(keys[kwparams - i - 1]), stack.top());
                    stack.pop();
                }
                stack.push(new ASTKwNamesMap(kwparamList));
            }
            break;
        case Pyc::CALL_A:
        case Pyc::CALL_FUNCTION_A:
        case Pyc::INSTRUMENTED_CALL_A:
            {
                int kwparams = (operand & 0xFF00) >> 8;
                int pparams = (operand & 0xFF);
                ASTCall::kwparam_t kwparamList;
                ASTCall::pparam_t pparamList;

                /*
                KW_NAMES(i)
                    Stores a reference to co_consts[consti] into an internal variable for use by CALL.
                    co_consts[consti] must be a tuple of strings.
                    New in version 3.11.
                */
                if (mod->verCompare(3, 11) >= 0) {
                    PycRef<ASTNode> object_or_map = stack.top();
                    if (object_or_map.type() == ASTNode::NODE_KW_NAMES_MAP) {
                        stack.pop();
                        PycRef<ASTKwNamesMap> kwparams_map = object_or_map.cast<ASTKwNamesMap>();
                        for (ASTKwNamesMap::map_t::const_iterator it = kwparams_map->values().begin(); it != kwparams_map->values().end(); it++) {
                            kwparamList.push_front(std::make_pair(it->first, it->second));
                            pparams -= 1;
                        }
                    }
                }
                else {
                    for (int i = 0; i < kwparams; i++) {
                        PycRef<ASTNode> val = stack.top();
                        stack.pop();
                        PycRef<ASTNode> key = stack.top();
                        stack.pop();
                        kwparamList.push_front(std::make_pair(key, val));
                    }
                }
                for (int i=0; i<pparams; i++) {
                    pparamList.push_front(stack.top());
                    stack.pop();
                }
                PycRef<ASTNode> func = stack.top();
                stack.pop();
                if ((opcode == Pyc::CALL_A || opcode == Pyc::INSTRUMENTED_CALL_A) &&
                        stack.top() == nullptr) {
                    stack.pop();
                }

                PycRef<ASTNode> class_node = maybe_make_class(func, pparamList, kwparamList);
                if (class_node != nullptr) {
                    stack.push(class_node);
                    break;
                }

                rewrite_named_function_args(pparamList, curblock);
                stack.push(new ASTCall(func, pparamList, kwparamList));
            }
            break;
        case Pyc::CALL_FUNCTION_VAR_A:
            {
                PycRef<ASTNode> var = stack.top();
                stack.pop();
                int kwparams = (operand & 0xFF00) >> 8;
                int pparams = (operand & 0xFF);
                ASTCall::kwparam_t kwparamList;
                ASTCall::pparam_t pparamList;
                for (int i=0; i<kwparams; i++) {
                    PycRef<ASTNode> val = stack.top();
                    stack.pop();
                    PycRef<ASTNode> key = stack.top();
                    stack.pop();
                    kwparamList.push_front(std::make_pair(key, val));
                }
                for (int i=0; i<pparams; i++) {
                    pparamList.push_front(stack.top());
                    stack.pop();
                }
                PycRef<ASTNode> func = stack.top();
                stack.pop();

                PycRef<ASTNode> call = new ASTCall(func, pparamList, kwparamList);
                call.cast<ASTCall>()->setVar(var);
                stack.push(call);
            }
            break;
        case Pyc::CALL_FUNCTION_KW_A:
            {
                PycRef<ASTNode> kw = stack.top();
                stack.pop();
                ASTCall::kwparam_t kwparamList;
                ASTCall::pparam_t pparamList;
                if (mod->verCompare(3, 6) >= 0
                        && kw.type() == ASTNode::NODE_OBJECT
                        && (kw.cast<ASTObject>()->object().type() == PycObject::TYPE_TUPLE
                            || kw.cast<ASTObject>()->object().type() == PycObject::TYPE_SMALL_TUPLE)) {
                    PycRef<PycTuple> names = kw.cast<ASTObject>()->object().cast<PycTuple>();
                    int kwparams = names->size();
                    int pparams = operand - kwparams;

                    for (int i = 0; i < kwparams; i++) {
                        PycRef<ASTNode> val = stack.top();
                        stack.pop();
                        kwparamList.push_front(std::make_pair(new ASTObject(names->get(kwparams - i - 1)), val));
                    }
                    for (int i = 0; i < pparams; i++) {
                        pparamList.push_front(stack.top());
                        stack.pop();
                    }
                } else {
                    int kwparams = (operand & 0xFF00) >> 8;
                    int pparams = (operand & 0xFF);
                    for (int i=0; i<kwparams; i++) {
                        PycRef<ASTNode> val = stack.top();
                        stack.pop();
                        PycRef<ASTNode> key = stack.top();
                        stack.pop();
                        kwparamList.push_front(std::make_pair(key, val));
                    }
                    for (int i=0; i<pparams; i++) {
                        pparamList.push_front(stack.top());
                        stack.pop();
                    }
                }
                PycRef<ASTNode> func = stack.top();
                stack.pop();

                PycRef<ASTNode> class_node = maybe_make_class(func, pparamList, kwparamList);
                if (class_node != nullptr) {
                    stack.push(class_node);
                    break;
                }

                rewrite_named_function_args(pparamList, curblock);
                PycRef<ASTNode> call = new ASTCall(func, pparamList, kwparamList);
                stack.push(call);
            }
            break;
        case Pyc::CALL_FUNCTION_VAR_KW_A:
            {
                PycRef<ASTNode> kw = stack.top();
                stack.pop();
                PycRef<ASTNode> var = stack.top();
                stack.pop();
                int kwparams = (operand & 0xFF00) >> 8;
                int pparams = (operand & 0xFF);
                ASTCall::kwparam_t kwparamList;
                ASTCall::pparam_t pparamList;
                for (int i=0; i<kwparams; i++) {
                    PycRef<ASTNode> val = stack.top();
                    stack.pop();
                    PycRef<ASTNode> key = stack.top();
                    stack.pop();
                    kwparamList.push_front(std::make_pair(key, val));
                }
                for (int i=0; i<pparams; i++) {
                    pparamList.push_front(stack.top());
                    stack.pop();
                }
                PycRef<ASTNode> func = stack.top();
                stack.pop();

                PycRef<ASTNode> call = new ASTCall(func, pparamList, kwparamList);
                call.cast<ASTCall>()->setKW(kw);
                call.cast<ASTCall>()->setVar(var);
                stack.push(call);
            }
            break;
        case Pyc::CALL_FUNCTION_EX_A:
            {
                PycRef<ASTNode> kw;
                if (operand & 0x1) {
                    kw = stack.top();
                    stack.pop();
                }

                PycRef<ASTNode> args = stack.top();
                stack.pop();
                PycRef<ASTNode> func = stack.top();
                stack.pop();

                ASTCall::pparam_t pparamList;
                append_call_ex_args(pparamList, args);

                PycRef<ASTNode> class_node = maybe_make_class(func, pparamList, ASTCall::kwparam_t());
                if (class_node != nullptr) {
                    stack.push(class_node);
                    break;
                }

                rewrite_named_function_args(pparamList, curblock);
                PycRef<ASTNode> call = new ASTCall(func, pparamList, ASTCall::kwparam_t());
                if (kw != nullptr)
                    call.cast<ASTCall>()->setKW(kw);
                stack.push(call);
            }
            break;
        case Pyc::CALL_METHOD_A:
            {
                ASTCall::pparam_t pparamList;
                for (int i = 0; i < operand; i++) {
                    PycRef<ASTNode> param = stack.top();
                    stack.pop();
                    if (param.type() == ASTNode::NODE_FUNCTION) {
                        PycRef<ASTNode> fun_code = param.cast<ASTFunction>()->code();
                        PycRef<PycCode> code_src = fun_code.cast<ASTObject>()->object().cast<PycCode>();
                        PycRef<PycString> function_name = code_src->name();
                        if (function_name->isEqual("<lambda>")) {
                            pparamList.push_front(param);
                        } else {
                            // Decorator used
                            PycRef<ASTNode> decor_name = new ASTName(function_name);
                            curblock->append(new ASTStore(param, decor_name));

                            pparamList.push_front(decor_name);
                        }
                    } else {
                        pparamList.push_front(param);
                    }
                }
                PycRef<ASTNode> func = stack.top();
                stack.pop();
                stack.push(new ASTCall(func, pparamList, ASTCall::kwparam_t()));
            }
            break;
        case Pyc::CONTINUE_LOOP_A:
            curblock->append(new ASTKeyword(ASTKeyword::KW_CONTINUE));
            break;
        case Pyc::COMPARE_OP_A:
            {
                PycRef<ASTNode> right = stack.top();
                stack.pop();
                PycRef<ASTNode> left = stack.top();
                stack.pop();
                auto arg = operand;
                if (mod->verCompare(3, 12) == 0)
                    arg >>= 4; // changed under GH-100923
                else if (mod->verCompare(3, 13) >= 0)
                    arg >>= 5;
                stack.push(new ASTCompare(left, right, arg));
            }
            break;
        case Pyc::CONTAINS_OP_A:
            {
                PycRef<ASTNode> right = stack.top();
                stack.pop();
                PycRef<ASTNode> left = stack.top();
                stack.pop();
                // The operand will be 0 for 'in' and 1 for 'not in'.
                stack.push(new ASTCompare(left, right, operand ? ASTCompare::CMP_NOT_IN : ASTCompare::CMP_IN));
            }
            break;
        case Pyc::DELETE_ATTR_A:
            {
                PycRef<ASTNode> name = stack.top();
                stack.pop();
                curblock->append(new ASTDelete(new ASTBinary(name, new ASTName(code->getName(operand)), ASTBinary::BIN_ATTR)));
            }
            break;
        case Pyc::DELETE_GLOBAL_A:
            code->markGlobal(code->getName(operand));
            /* Fall through */
        case Pyc::DELETE_NAME_A:
            {
                PycRef<PycString> varname = code->getName(operand);

                if (varname->length() >= 2 && varname->value()[0] == '_'
                        && varname->value()[1] == '[') {
                    /* Don't show deletes that are a result of list comps. */
                    break;
                }

                PycRef<ASTNode> name = new ASTName(varname);
                curblock->append(new ASTDelete(name));
            }
            break;
        case Pyc::DELETE_FAST_A:
            {
                PycRef<ASTNode> name;

                if (mod->verCompare(1, 3) < 0)
                    name = new ASTName(code->getName(operand));
                else
                    name = new ASTName(code->getLocal(operand));

                if (name.cast<ASTName>()->name()->value()[0] == '_'
                        && name.cast<ASTName>()->name()->value()[1] == '[') {
                    /* Don't show deletes that are a result of list comps. */
                    break;
                }

                curblock->append(new ASTDelete(name));
            }
            break;
        case Pyc::DELETE_SLICE_0:
            {
                PycRef<ASTNode> name = stack.top();
                stack.pop();

                curblock->append(new ASTDelete(new ASTSubscr(name, new ASTSlice(ASTSlice::SLICE0))));
            }
            break;
        case Pyc::DELETE_SLICE_1:
            {
                PycRef<ASTNode> upper = stack.top();
                stack.pop();
                PycRef<ASTNode> name = stack.top();
                stack.pop();

                curblock->append(new ASTDelete(new ASTSubscr(name, new ASTSlice(ASTSlice::SLICE1, upper))));
            }
            break;
        case Pyc::DELETE_SLICE_2:
            {
                PycRef<ASTNode> lower = stack.top();
                stack.pop();
                PycRef<ASTNode> name = stack.top();
                stack.pop();

                curblock->append(new ASTDelete(new ASTSubscr(name, new ASTSlice(ASTSlice::SLICE2, NULL, lower))));
            }
            break;
        case Pyc::DELETE_SLICE_3:
            {
                PycRef<ASTNode> lower = stack.top();
                stack.pop();
                PycRef<ASTNode> upper = stack.top();
                stack.pop();
                PycRef<ASTNode> name = stack.top();
                stack.pop();

                curblock->append(new ASTDelete(new ASTSubscr(name, new ASTSlice(ASTSlice::SLICE3, upper, lower))));
            }
            break;
        case Pyc::DELETE_SUBSCR:
            {
                PycRef<ASTNode> key = stack.top();
                stack.pop();
                PycRef<ASTNode> name = stack.top();
                stack.pop();

                curblock->append(new ASTDelete(new ASTSubscr(name, key)));
            }
            break;
        case Pyc::DUP_TOP:
            {
                if (stack.empty() && curblock->blktype() == ASTBlock::BLK_EXCEPT) {
                    stack.push(new ASTObject(Pyc_None));
                    stack.push(new ASTObject(Pyc_None));
                }

                PycBuffer next_source = source;
                int next_opcode = 0, next_operand = 0, next_pos = pos;
                if (!next_source.atEof())
                    bc_next(next_source, mod, next_opcode, next_operand, next_pos);

                if (next_opcode == Pyc::ROT_THREE) {
                    stack.push(stack.top());
                    break;
                }

                if (stack.top().type() == PycObject::TYPE_NULL) {
                    stack.push(stack.top());
                } else if (stack.top().type() == ASTNode::NODE_CHAINSTORE) {
                    auto chainstore = stack.top();
                    stack.pop();
                    stack.push(stack.top());
                    stack.push(chainstore);
                } else {
                    stack.push(stack.top());
                    ASTNodeList::list_t targets;
                    stack.push(new ASTChainStore(targets, stack.top()));
                }
            }
            break;
        case Pyc::DUP_TOP_TWO:
            {
                PycRef<ASTNode> first = stack.top();
                stack.pop();
                PycRef<ASTNode> second = stack.top();

                stack.push(first);
                stack.push(second);
                stack.push(first);
            }
            break;
        case Pyc::DUP_TOPX_A:
            {
                std::stack<PycRef<ASTNode> > first;
                std::stack<PycRef<ASTNode> > second;

                for (int i = 0; i < operand; i++) {
                    PycRef<ASTNode> node = stack.top();
                    stack.pop();
                    first.push(node);
                    second.push(node);
                }

                while (first.size()) {
                    stack.push(first.top());
                    first.pop();
                }

                while (second.size()) {
                    stack.push(second.top());
                    second.pop();
                }
            }
            break;
        case Pyc::END_FINALLY:
            {
                bool isFinally = false;
                if (curblock->blktype() == ASTBlock::BLK_FINALLY) {
                    PycRef<ASTBlock> final = curblock;
                    blocks.pop();

                    stack = stack_hist.top();
                    stack_hist.pop();

                    curblock = blocks.top();
                    curblock->append(final.cast<ASTNode>());
                    isFinally = true;
                } else if (curblock->blktype() == ASTBlock::BLK_EXCEPT) {
                    blocks.pop();
                    PycRef<ASTBlock> prev = curblock;

                    bool isUninitAsyncFor = false;
                    if (blocks.top()->blktype() == ASTBlock::BLK_CONTAINER) {
                        auto container = blocks.top();
                        blocks.pop();
                        auto asyncForBlock = blocks.top();
                        isUninitAsyncFor = asyncForBlock->blktype() == ASTBlock::BLK_ASYNCFOR && !asyncForBlock->inited();
                        if (isUninitAsyncFor) {
                            auto tryBlock = container->nodes().front().cast<ASTBlock>();
                            if (!tryBlock->nodes().empty() && tryBlock->blktype() == ASTBlock::BLK_TRY) {
                                auto store = tryBlock->nodes().front().try_cast<ASTStore>();
                                if (store) {
                                    asyncForBlock.cast<ASTIterBlock>()->setIndex(store->dest());
                                }
                            }
                            curblock = blocks.top();
                            stack = stack_hist.top();
                            stack_hist.pop();
                            if (!curblock->inited())
                                fprintf(stderr, "Error when decompiling 'async for'.\n");
                        } else {
                            blocks.push(container);
                        }
                    }

                    if (!isUninitAsyncFor) {
                        if (curblock->size() != 0) {
                            blocks.top()->append(curblock.cast<ASTNode>());
                        }

                        curblock = blocks.top();
                        /* Turn it into an else statement. */
                        if (curblock->end() != pos || curblock.cast<ASTContainerBlock>()->hasFinally()) {
                            PycRef<ASTBlock> elseblk = new ASTBlock(ASTBlock::BLK_ELSE, prev->end());
                            elseblk->init();
                            blocks.push(elseblk);
                            curblock = blocks.top();
                        }
                        else {
                            stack = stack_hist.top();
                            stack_hist.pop();
                        }
                    }
                }

                if (curblock->blktype() == ASTBlock::BLK_CONTAINER) {
                    /* This marks the end of the except block(s). */
                    PycRef<ASTContainerBlock> cont = curblock.cast<ASTContainerBlock>();
                    if (!cont->hasFinally() || isFinally) {
                        /* If there's no finally block, pop the container. */
                        blocks.pop();
                        curblock = blocks.top();
                        curblock->append(cont.cast<ASTNode>());
                    }
                }
            }
            break;
        case Pyc::EXEC_STMT:
            {
                if (stack.top().type() == ASTNode::NODE_CHAINSTORE) {
                    stack.pop();
                }
                PycRef<ASTNode> loc = stack.top();
                stack.pop();
                PycRef<ASTNode> glob = stack.top();
                stack.pop();
                PycRef<ASTNode> stmt = stack.top();
                stack.pop();

                curblock->append(new ASTExec(stmt, glob, loc));
            }
            break;
        case Pyc::FOR_ITER_A:
        case Pyc::INSTRUMENTED_FOR_ITER_A:
            {
                PycRef<ASTNode> iter = stack.top(); // Iterable
                if (mod->verCompare(3, 12) < 0) {
                    // Do not pop the iterator for py 3.12+
                    stack.pop();
                }
                /* Pop it? Don't pop it? */

                int end;
                bool comprehension = false;

                // before 3.8, there is a SETUP_LOOP instruction with block start and end position,
                //    the operand is usually a jump to a POP_BLOCK instruction
                // after 3.8, block extent has to be inferred implicitly; the operand is a jump to a position after the for block
                if (mod->majorVer() == 3 && mod->minorVer() >= 8) {
                    end = operand;
                    if (mod->verCompare(3, 10) >= 0)
                        end *= sizeof(uint16_t); // // BPO-27129
                    end += pos;
                    comprehension = strcmp(code->name()->value(), "<listcomp>") == 0;
                } else {
                    PycRef<ASTBlock> top = blocks.top();
                    end = top->end(); // block end position from SETUP_LOOP
                    if (top->blktype() == ASTBlock::BLK_WHILE) {
                        blocks.pop();
                    } else {
                        comprehension = true;
                    }
                }

                PycRef<ASTIterBlock> forblk = new ASTIterBlock(ASTBlock::BLK_FOR, curpos, end, iter);
                forblk->setComprehension(comprehension);
                blocks.push(forblk.cast<ASTBlock>());
                curblock = blocks.top();

                stack.push(NULL);
            }
            break;
        case Pyc::FOR_LOOP_A:
            {
                PycRef<ASTNode> curidx = stack.top(); // Current index
                stack.pop();
                PycRef<ASTNode> iter = stack.top(); // Iterable
                stack.pop();

                bool comprehension = false;
                PycRef<ASTBlock> top = blocks.top();
                if (top->blktype() == ASTBlock::BLK_WHILE) {
                    blocks.pop();
                } else {
                    comprehension = true;
                }
                PycRef<ASTIterBlock> forblk = new ASTIterBlock(ASTBlock::BLK_FOR, curpos, top->end(), iter);
                forblk->setComprehension(comprehension);
                blocks.push(forblk.cast<ASTBlock>());
                curblock = blocks.top();

                /* Python Docs say:
                      "push the sequence, the incremented counter,
                       and the current item onto the stack." */
                stack.push(iter);
                stack.push(curidx);
                stack.push(NULL); // We can totally hack this >_>
            }
            break;
        case Pyc::GET_AITER:
            {
                // Logic similar to FOR_ITER_A
                PycRef<ASTNode> iter = stack.top(); // Iterable
                stack.pop();

                PycRef<ASTBlock> top = blocks.top();
                if (top->blktype() == ASTBlock::BLK_WHILE) {
                    blocks.pop();
                    PycRef<ASTIterBlock> forblk = new ASTIterBlock(ASTBlock::BLK_ASYNCFOR, curpos, top->end(), iter);
                    blocks.push(forblk.cast<ASTBlock>());
                    curblock = blocks.top();
                    stack.push(nullptr);
                } else {
                     fprintf(stderr, "Unsupported use of GET_AITER outside of SETUP_LOOP\n");
                }
            }
            break;
        case Pyc::GET_ANEXT:
            break;
        case Pyc::FORMAT_VALUE_A:
            {
                auto conversion_flag = static_cast<ASTFormattedValue::ConversionFlag>(operand);
                PycRef<ASTNode> format_spec = nullptr;
                if (conversion_flag & ASTFormattedValue::HAVE_FMT_SPEC) {
                    format_spec = stack.top();
                    stack.pop();
                }
                auto val = stack.top();
                stack.pop();
                stack.push(new ASTFormattedValue(val, conversion_flag, format_spec));
            }
            break;
        case Pyc::GET_AWAITABLE:
            {
                PycRef<ASTNode> object = stack.top();
                stack.pop();
                stack.push(new ASTAwaitable(object));
            }
            break;
        case Pyc::GET_ITER:
        case Pyc::GET_YIELD_FROM_ITER:
            /* We just entirely ignore this */
            break;
        case Pyc::IMPORT_NAME_A:
            if (mod->majorVer() == 1) {
                stack.push(new ASTImport(new ASTName(code->getName(operand)), NULL));
            } else {
                PycRef<ASTNode> fromlist = stack.top();
                stack.pop();
                int level = 0;
                if (mod->verCompare(2, 5) >= 0) {
                    level = import_level_from_node(stack.top());
                    stack.pop();
                }
                stack.push(new ASTImport(new ASTName(code->getName(operand)), fromlist, level));
            }
            break;
        case Pyc::IMPORT_FROM_A:
            stack.push(new ASTName(code->getName(operand)));
            break;
        case Pyc::IMPORT_STAR:
            {
                PycRef<ASTNode> import = stack.top();
                stack.pop();
                curblock->append(new ASTStore(import, NULL));
            }
            break;
        case Pyc::IS_OP_A:
            {
                PycRef<ASTNode> right = stack.top();
                stack.pop();
                PycRef<ASTNode> left = stack.top();
                stack.pop();
                // The operand will be 0 for 'is' and 1 for 'is not'.
                stack.push(new ASTCompare(left, right, operand ? ASTCompare::CMP_IS_NOT : ASTCompare::CMP_IS));
            }
            break;
        case Pyc::JUMP_IF_FALSE_A:
        case Pyc::JUMP_IF_TRUE_A:
        case Pyc::JUMP_IF_FALSE_OR_POP_A:
        case Pyc::JUMP_IF_TRUE_OR_POP_A:
        case Pyc::POP_JUMP_IF_FALSE_A:
        case Pyc::POP_JUMP_IF_TRUE_A:
        case Pyc::POP_JUMP_FORWARD_IF_FALSE_A:
        case Pyc::POP_JUMP_FORWARD_IF_TRUE_A:
        case Pyc::INSTRUMENTED_POP_JUMP_IF_FALSE_A:
        case Pyc::INSTRUMENTED_POP_JUMP_IF_TRUE_A:
            {
                PycRef<ASTNode> cond = stack.top();
                PycRef<ASTCondBlock> ifblk;
                int popped = ASTCondBlock::UNINITED;

                if (opcode == Pyc::POP_JUMP_IF_FALSE_A
                        || opcode == Pyc::POP_JUMP_IF_TRUE_A
                        || opcode == Pyc::POP_JUMP_FORWARD_IF_FALSE_A
                        || opcode == Pyc::POP_JUMP_FORWARD_IF_TRUE_A
                        || opcode == Pyc::INSTRUMENTED_POP_JUMP_IF_FALSE_A
                        || opcode == Pyc::INSTRUMENTED_POP_JUMP_IF_TRUE_A) {
                    /* Pop condition before the jump */
                    stack.pop();
                    popped = ASTCondBlock::PRE_POPPED;
                }

                bool prev_hist_top_empty = stack_hist.empty() || stack_hist.top().empty();
                /* Store the current stack for the else statement(s) */
                stack_hist.push(stack);

                if (opcode == Pyc::JUMP_IF_FALSE_OR_POP_A
                        || opcode == Pyc::JUMP_IF_TRUE_OR_POP_A) {
                    /* Pop condition only if condition is met */
                    stack.pop();
                    popped = ASTCondBlock::POPPED;
                }

                /* "Jump if true" means "Jump if not false" */
                bool neg = opcode == Pyc::JUMP_IF_TRUE_A
                        || opcode == Pyc::JUMP_IF_TRUE_OR_POP_A
                        || opcode == Pyc::POP_JUMP_IF_TRUE_A
                        || opcode == Pyc::POP_JUMP_FORWARD_IF_TRUE_A
                        || opcode == Pyc::INSTRUMENTED_POP_JUMP_IF_TRUE_A;

                int offs = operand;
                if (mod->verCompare(3, 10) >= 0)
                    offs *= sizeof(uint16_t); // // BPO-27129
                if (mod->verCompare(3, 12) >= 0
                        || opcode == Pyc::JUMP_IF_FALSE_A
                        || opcode == Pyc::JUMP_IF_TRUE_A
                        || opcode == Pyc::POP_JUMP_FORWARD_IF_TRUE_A
                        || opcode == Pyc::POP_JUMP_FORWARD_IF_FALSE_A) {
                    /* Offset is relative in these cases */
                    offs += pos;
                }

                if (cond.type() == ASTNode::NODE_COMPARE
                        && cond.cast<ASTCompare>()->op() == ASTCompare::CMP_EXCEPTION) {
                    if (curblock->blktype() == ASTBlock::BLK_EXCEPT
                            && curblock.cast<ASTCondBlock>()->cond() == NULL) {
                        blocks.pop();
                        curblock = blocks.top();

                        stack_hist.pop();
                    }

                    ifblk = new ASTCondBlock(ASTBlock::BLK_EXCEPT, offs, cond.cast<ASTCompare>()->right(), false);
                } else if (curblock->blktype() == ASTBlock::BLK_ELSE
                           && curblock->size() == 0) {
                    bool can_collapse_to_elif = false;
                    bool building_outer_else_value_chain = !stack.empty() && prev_hist_top_empty;
                    if (blocks.size() > 1) {
                        std::stack<PycRef<ASTBlock> > probe = blocks;
                        probe.pop();
                        PycRef<ASTBlock> parent = probe.top();
                        if (parent->size() > 0) {
                            PycRef<ASTNode> prev = parent->nodes().back();
                            PycRef<ASTBlock> prev_block = prev.try_cast<ASTBlock>();
                            if (prev_block != nullptr
                                    && (prev_block->blktype() == ASTBlock::BLK_IF
                                        || prev_block->blktype() == ASTBlock::BLK_ELIF))
                                can_collapse_to_elif = true;
                        }
                    }
                    if (building_outer_else_value_chain)
                        can_collapse_to_elif = false;

                    if (can_collapse_to_elif) {
                        /* Collapse into elif statement */
                        blocks.pop();
                        stack = stack_hist.top();
                        stack_hist.pop();
                        ifblk = new ASTCondBlock(ASTBlock::BLK_ELIF, offs, cond, neg);
                    } else {
                        ifblk = new ASTCondBlock(ASTBlock::BLK_IF, offs, cond, neg);
                    }
                } else if (curblock->size() == 0 && !curblock->inited()
                           && curblock->blktype() == ASTBlock::BLK_WHILE
                           && offs >= curblock->end()) {
                    /* The condition for a while loop */
                    PycRef<ASTBlock> top = blocks.top();
                    blocks.pop();
                    ifblk = new ASTCondBlock(top->blktype(), offs, cond, neg);

                    /* We don't store the stack for loops! Pop it! */
                    stack_hist.pop();
                } else if (curblock->size() == 0 && curblock->end() <= offs
                           && (curblock->blktype() == ASTBlock::BLK_IF
                           || curblock->blktype() == ASTBlock::BLK_ELIF
                           || curblock->blktype() == ASTBlock::BLK_WHILE)) {
                    PycRef<ASTNode> newcond;
                    PycRef<ASTCondBlock> top = curblock.cast<ASTCondBlock>();
                    PycRef<ASTNode> cond1 = top->cond();
                    blocks.pop();

                    if (curblock->blktype() == ASTBlock::BLK_WHILE) {
                        stack_hist.pop();
                    } else {
                        FastStack s_top = stack_hist.top();
                        stack_hist.pop();
                        stack_hist.pop();
                        stack_hist.push(s_top);
                    }

                    if (curblock->end() == offs && top->negative() && neg) {
                        /* if blah or blah */
                        newcond = new ASTBinary(cond1, cond, ASTBinary::BIN_LOG_OR);
                    } else if (curblock->end() < curpos && offs > curpos
                            && !top->negative() && !neg) {
                        /*
                         * Mixed-direction short-circuit guards can show up as
                         * a backward/loop-local condition followed by a forward
                         * condition guarding the same block. Collapsing these to
                         * "or" produces incorrect output such as:
                         *     if oEquip or oEquip.IsInitWeapon():
                         * Preserve the guard semantics with a conservative "and".
                         */
                        newcond = new ASTBinary(cond1, cond, ASTBinary::BIN_LOG_AND);
                    } else if (curblock->end() == offs
                            || (curblock->end() == curpos && !top->negative())) {
                        /* if blah and blah */
                        newcond = new ASTBinary(cond1, cond, ASTBinary::BIN_LOG_AND);
                    } else {
                        /* if blah or blah */
                        newcond = new ASTBinary(cond1, cond, ASTBinary::BIN_LOG_OR);
                    }
                    ifblk = new ASTCondBlock(top->blktype(), offs, newcond, neg);
                } else if (curblock->blktype() == ASTBlock::BLK_FOR
                            && curblock.cast<ASTIterBlock>()->isComprehension()
                            && mod->verCompare(2, 7) >= 0
                            && offs <= curpos) {
                    /* Comprehension condition */
                    curblock.cast<ASTIterBlock>()->setCondition(cond);
                    stack_hist.pop();
                    // TODO: Handle older python versions, where condition
                    // is laid out a little differently.
                    break;
                } else {
                    /* Plain old if statement */
                    ifblk = new ASTCondBlock(ASTBlock::BLK_IF, offs, cond, neg);
                }

                if (popped)
                    ifblk->init(popped);

                blocks.push(ifblk.cast<ASTBlock>());
                curblock = blocks.top();
            }
            break;
        case Pyc::JUMP_ABSOLUTE_A:
        // bpo-47120: Replaced JUMP_ABSOLUTE by the relative jump JUMP_BACKWARD.
        case Pyc::JUMP_BACKWARD_A:
        case Pyc::JUMP_BACKWARD_NO_INTERRUPT_A:
            {
                if (prev_opcode == Pyc::RAISE_VARARGS_A) {
                    break;
                }
                int offs = operand;
                if (mod->verCompare(3, 10) >= 0)
                    offs *= sizeof(uint16_t); // // BPO-27129 

                if (offs < pos) {
                    if (prev_opcode == Pyc::JUMP_FORWARD_A
                            || prev_opcode == Pyc::INSTRUMENTED_JUMP_FORWARD_A) {
                        break;
                    }
                    if (curblock->blktype() == ASTBlock::BLK_CONTAINER) {
                        break;
                    } else if (curblock->blktype() == ASTBlock::BLK_FOR) {
                        bool is_jump_to_start = offs == curblock.cast<ASTIterBlock>()->start();
                        bool should_pop_for_block = curblock.cast<ASTIterBlock>()->isComprehension();
                        // in v3.8, SETUP_LOOP is deprecated and for blocks aren't terminated by POP_BLOCK, so we add them here
                        bool should_add_for_block = mod->majorVer() == 3 && mod->minorVer() >= 8 && is_jump_to_start && !curblock.cast<ASTIterBlock>()->isComprehension();

                        if (should_pop_for_block || should_add_for_block) {
                            PycRef<ASTNode> top = stack.top();

                            if (top.type() == ASTNode::NODE_COMPREHENSION) {
                                PycRef<ASTComprehension> comp = top.cast<ASTComprehension>();

                                comp->addGenerator(curblock.cast<ASTIterBlock>());
                            }

                            PycRef<ASTBlock> tmp = curblock;
                            blocks.pop();
                            curblock = blocks.top();
                            if (should_add_for_block) {
                                curblock->append(tmp.cast<ASTNode>());
                            }
                        }
                    } else if (curblock->blktype() == ASTBlock::BLK_ELSE) {
                        stack = stack_hist.top();
                        stack_hist.pop();

                        blocks.pop();
                        blocks.top()->append(curblock.cast<ASTNode>());
                        curblock = blocks.top();

                        if (curblock->blktype() == ASTBlock::BLK_CONTAINER
                                && !curblock.cast<ASTContainerBlock>()->hasFinally()) {
                            blocks.pop();
                            blocks.top()->append(curblock.cast<ASTNode>());
                            curblock = blocks.top();
                        }
                    } else {
                        bool collapse_loop_filter = false;
                        if ((curblock->blktype() == ASTBlock::BLK_IF
                                || curblock->blktype() == ASTBlock::BLK_ELIF
                                || curblock->blktype() == ASTBlock::BLK_ELSE)
                                && curblock->end() == offs) {
                            std::stack<PycRef<ASTBlock> > probe = blocks;
                            while (probe.size() > 1) {
                                probe.pop();
                                PycRef<ASTBlock> parent = probe.top();
                                if ((parent->blktype() == ASTBlock::BLK_IF
                                        || parent->blktype() == ASTBlock::BLK_ELIF
                                        || parent->blktype() == ASTBlock::BLK_ELSE)
                                        && parent->end() == offs) {
                                    continue;
                                }
                                if (parent->blktype() == ASTBlock::BLK_FOR
                                        || parent->blktype() == ASTBlock::BLK_WHILE
                                        || parent->blktype() == ASTBlock::BLK_ASYNCFOR) {
                                    collapse_loop_filter = true;
                                }
                                break;
                            }
                        }

                        if (collapse_loop_filter) {
                            while ((curblock->blktype() == ASTBlock::BLK_IF
                                    || curblock->blktype() == ASTBlock::BLK_ELIF
                                    || curblock->blktype() == ASTBlock::BLK_ELSE)
                                    && curblock->end() == offs
                                    && blocks.size() > 1) {
                                PycRef<ASTBlock> child = curblock;
                                blocks.pop();
                                PycRef<ASTBlock> parent = blocks.top();
                                parent->append(child.cast<ASTNode>());

                                if (!stack_hist.empty()) {
                                    stack = stack_hist.top();
                                    stack_hist.pop();
                                }

                                curblock = parent;
                            }
                            break;
                        }

                        bool skip_dead_continue = false;
                        if (curblock->size() > 0) {
                            PycRef<ASTNode> last = curblock->nodes().back();
                            if (last != nullptr && last->type() == ASTNode::NODE_KEYWORD
                                    && last.cast<ASTKeyword>()->key() == ASTKeyword::KW_BREAK) {
                                skip_dead_continue = true;
                            }
                        }

                        if (!skip_dead_continue) {
                            curblock->append(new ASTKeyword(ASTKeyword::KW_CONTINUE));

                            while ((curblock->blktype() == ASTBlock::BLK_IF
                                    || curblock->blktype() == ASTBlock::BLK_ELIF
                                    || curblock->blktype() == ASTBlock::BLK_ELSE)
                                    && blocks.size() > 1) {
                                PycRef<ASTBlock> child = curblock;
                                blocks.pop();
                                PycRef<ASTBlock> parent = blocks.top();
                                parent->append(child.cast<ASTNode>());

                                if (!stack_hist.empty()) {
                                    stack = stack_hist.top();
                                    stack_hist.pop();
                                }

                                curblock = parent;
                                if ((curblock->blktype() == ASTBlock::BLK_IF
                                        || curblock->blktype() == ASTBlock::BLK_ELIF
                                        || curblock->blktype() == ASTBlock::BLK_ELSE)
                                        && curblock->end() == child->end()) {
                                    curblock->append(new ASTKeyword(ASTKeyword::KW_CONTINUE));
                                    continue;
                                }

                                break;
                            }
                        }
                    }

                    /* We're in a loop, this jumps back to the start */
                    /* I think we'll just ignore this case... */
                    break; // Bad idea? Probably!
                }

                if (curblock->blktype() == ASTBlock::BLK_CONTAINER) {
                    PycRef<ASTContainerBlock> cont = curblock.cast<ASTContainerBlock>();
                    if (cont->hasExcept() && pos < cont->except()) {
                        PycRef<ASTBlock> except = new ASTCondBlock(ASTBlock::BLK_EXCEPT, 0, NULL, false);
                        except->init();
                        blocks.push(except);
                        curblock = blocks.top();
                    }
                    break;
                }

                if (!stack_hist.empty()) {
                    stack = stack_hist.top();
                    stack_hist.pop();
                } else {
                    fprintf(stderr, "Warning: Stack history is empty, something wrong might have happened\n");
                }

                PycRef<ASTBlock> prev = curblock;
                PycRef<ASTBlock> nil;
                bool push = true;

                do {
                    blocks.pop();

                    blocks.top()->append(prev.cast<ASTNode>());

                    if (prev->blktype() == ASTBlock::BLK_IF
                            || prev->blktype() == ASTBlock::BLK_ELIF) {
                        if (push) {
                            stack_hist.push(stack);
                        }
                        PycRef<ASTBlock> next = new ASTBlock(ASTBlock::BLK_ELSE, blocks.top()->end());
                        if (prev->inited() == ASTCondBlock::PRE_POPPED) {
                            next->init(ASTCondBlock::PRE_POPPED);
                        }

                        blocks.push(next.cast<ASTBlock>());
                        prev = nil;
                    } else if (prev->blktype() == ASTBlock::BLK_EXCEPT) {
                        if (push) {
                            stack_hist.push(stack);
                        }
                        PycRef<ASTBlock> next = new ASTCondBlock(ASTBlock::BLK_EXCEPT, blocks.top()->end(), NULL, false);
                        next->init();

                        blocks.push(next.cast<ASTBlock>());
                        prev = nil;
                    } else if (prev->blktype() == ASTBlock::BLK_ELSE) {
                        /* Special case */
                        prev = blocks.top();
                        if (!push) {
                            stack = stack_hist.top();
                            stack_hist.pop();
                        }
                        push = false;

                        if (prev->blktype() == ASTBlock::BLK_MAIN) {
                            prev = nil;
                        }
                    } else {
                        prev = nil;
                    }

                } while (prev != nil);

                curblock = blocks.top();
            }
            break;
        case Pyc::JUMP_FORWARD_A:
        case Pyc::INSTRUMENTED_JUMP_FORWARD_A:
            {
                if (prev_terminal_flow) {
                    break;
                }
                int offs = operand;
                if (mod->verCompare(3, 10) >= 0)
                    offs *= sizeof(uint16_t); // // BPO-27129

                bool collapse_loop_common_tail = false;
                int jump_target = pos + offs;
                if ((curblock->blktype() == ASTBlock::BLK_IF
                        || curblock->blktype() == ASTBlock::BLK_ELIF
                        || curblock->blktype() == ASTBlock::BLK_ELSE)
                        && blocks.size() > 1) {
                    std::stack<PycRef<ASTBlock> > probe = blocks;
                    PycRef<ASTBlock> child = probe.top();
                    probe.pop();
                    bool saw_same_end_parent = false;
                    while (!probe.empty()) {
                        PycRef<ASTBlock> parent = probe.top();
                        if ((parent->blktype() == ASTBlock::BLK_IF
                                || parent->blktype() == ASTBlock::BLK_ELIF
                                || parent->blktype() == ASTBlock::BLK_ELSE)
                                && parent->end() == child->end()) {
                            saw_same_end_parent = true;
                            child = parent;
                            probe.pop();
                            continue;
                        }
                        if (saw_same_end_parent
                                && (parent->blktype() == ASTBlock::BLK_FOR
                                    || parent->blktype() == ASTBlock::BLK_WHILE
                                    || parent->blktype() == ASTBlock::BLK_ASYNCFOR)
                                && jump_target < parent->end()) {
                            collapse_loop_common_tail = true;
                        }
                        break;
                    }
                }

                if (collapse_loop_common_tail) {
                    int chain_end = curblock->end();
                    while ((curblock->blktype() == ASTBlock::BLK_IF
                            || curblock->blktype() == ASTBlock::BLK_ELIF
                            || curblock->blktype() == ASTBlock::BLK_ELSE)
                            && curblock->end() == chain_end
                            && blocks.size() > 1) {
                        PycRef<ASTBlock> child = curblock;
                        blocks.pop();
                        PycRef<ASTBlock> parent = blocks.top();
                        parent->append(child.cast<ASTNode>());

                        if (!stack_hist.empty()) {
                            stack = stack_hist.top();
                            stack_hist.pop();
                        }

                        curblock = parent;
                    }
                    break;
                }

                if ((curblock->blktype() == ASTBlock::BLK_FOR
                        || curblock->blktype() == ASTBlock::BLK_ASYNCFOR
                        || curblock->blktype() == ASTBlock::BLK_WHILE)
                        && jump_target < curblock->end()) {
                    break;
                }

                if (curblock->blktype() == ASTBlock::BLK_CONTAINER) {
                    PycRef<ASTContainerBlock> cont = curblock.cast<ASTContainerBlock>();
                    if (cont->hasExcept()) {
                        stack_hist.push(stack);

                        curblock->setEnd(pos+offs);
                        PycRef<ASTBlock> except = new ASTCondBlock(ASTBlock::BLK_EXCEPT, pos+offs, NULL, false);
                        except->init();
                        blocks.push(except);
                        curblock = blocks.top();
                    }
                    break;
                }

                if (!stack_hist.empty()) {
                    if (stack.empty()) // if it's part of if-expression, TOS at the moment is the result of "if" part
                        stack = stack_hist.top();
                    stack_hist.pop();
                }

                PycRef<ASTBlock> prev = curblock;
                PycRef<ASTBlock> nil;
                bool push = true;

                do {
                    blocks.pop();

                    if (!blocks.empty())
                        blocks.top()->append(prev.cast<ASTNode>());

                    if (prev->blktype() == ASTBlock::BLK_IF
                            || prev->blktype() == ASTBlock::BLK_ELIF) {
                        if (offs == 0) {
                            prev = nil;
                            continue;
                        }

                        if (push) {
                            stack_hist.push(stack);
                        }
                        PycRef<ASTBlock> next = new ASTBlock(ASTBlock::BLK_ELSE, pos+offs);
                        if (prev->inited() == ASTCondBlock::PRE_POPPED) {
                            next->init(ASTCondBlock::PRE_POPPED);
                        }

                        blocks.push(next.cast<ASTBlock>());
                        prev = nil;
                    } else if (prev->blktype() == ASTBlock::BLK_EXCEPT) {
                        if (offs == 0) {
                            prev = nil;
                            continue;
                        }

                        if (push) {
                            stack_hist.push(stack);
                        }
                        PycRef<ASTBlock> next = new ASTCondBlock(ASTBlock::BLK_EXCEPT, pos+offs, NULL, false);
                        next->init();

                        blocks.push(next.cast<ASTBlock>());
                        prev = nil;
                    } else if (prev->blktype() == ASTBlock::BLK_ELSE) {
                        /* Special case */
                        prev = blocks.top();
                        if (!push) {
                            stack = stack_hist.top();
                            stack_hist.pop();
                        }
                        push = false;

                        if (prev->blktype() == ASTBlock::BLK_MAIN) {
                            /* Something went out of control! */
                            prev = nil;
                        }
                    } else if (prev->blktype() == ASTBlock::BLK_TRY
                            && prev->end() < pos+offs) {
                        /* Need to add an except/finally block */
                        stack = stack_hist.top();
                        stack_hist.pop();

                        if (blocks.top()->blktype() == ASTBlock::BLK_CONTAINER) {
                            PycRef<ASTContainerBlock> cont = blocks.top().cast<ASTContainerBlock>();
                            if (cont->hasExcept()) {
                                if (push) {
                                    stack_hist.push(stack);
                                }

                                PycRef<ASTBlock> except = new ASTCondBlock(ASTBlock::BLK_EXCEPT, pos+offs, NULL, false);
                                except->init();
                                blocks.push(except);
                            }
                        } else {
                            fprintf(stderr, "Something TERRIBLE happened!!\n");
                        }
                        prev = nil;
                    } else {
                        prev = nil;
                    }

                } while (prev != nil);

                if (!blocks.empty()) {
                    curblock = blocks.top();
                    if (curblock->blktype() == ASTBlock::BLK_EXCEPT)
                        curblock->setEnd(pos+offs);
                }
            }
            break;
        case Pyc::LIST_APPEND:
        case Pyc::LIST_APPEND_A:
            {
                collapse_empty_comprehension_condition_blocks();
                PycRef<ASTNode> value = stack.top();
                stack.pop();

                PycRef<ASTNode> list = stack.top();


                if (curblock->blktype() == ASTBlock::BLK_FOR
                        && curblock.cast<ASTIterBlock>()->isComprehension()) {
                    stack.pop();
                    stack.push(new ASTComprehension(value));
                } else {
                    stack.push(new ASTSubscr(list, value)); /* Total hack */
                }
            }
            break;
        case Pyc::SET_ADD_A:
            {
                collapse_empty_comprehension_condition_blocks();
                PycRef<ASTNode> value = stack.top();
                stack.pop();

                PycRef<ASTNode> set = stack.top();

                if (curblock->blktype() == ASTBlock::BLK_FOR
                        && curblock.cast<ASTIterBlock>()->isComprehension()) {
                    stack.pop();
                    ASTSet::value_t values;
                    values.push_back(value);
                    stack.push(new ASTComprehension(new ASTSet(values)));
                } else {
                    stack.push(new ASTSubscr(set, value)); /* Total hack */
                }
            }
            break;
        case Pyc::MAP_ADD_A:
            {
                collapse_empty_comprehension_condition_blocks();
                PycRef<ASTNode> value = stack.top();
                stack.pop();
                PycRef<ASTNode> key = stack.top();
                stack.pop();

                PycRef<ASTNode> map = stack.top();

                if (curblock->blktype() == ASTBlock::BLK_FOR
                        && curblock.cast<ASTIterBlock>()->isComprehension()) {
                    stack.pop();
                    PycRef<ASTMap> dict = new ASTMap();
                    dict->add(key, value);
                    stack.push(new ASTComprehension(dict.cast<ASTNode>()));
                } else {
                    stack.push(new ASTSubscr(map, key)); /* Total hack */
                }
            }
            break;
        case Pyc::SET_UPDATE_A:
            {
                PycRef<ASTNode> rhs = stack.top();
                stack.pop();
                PycRef<ASTSet> lhs = stack.top().cast<ASTSet>();
                stack.pop();

                if (rhs.type() != ASTNode::NODE_OBJECT) {
                    fprintf(stderr, "Unsupported argument found for SET_UPDATE\n");
                    break;
                }

                // I've only ever seen this be a TYPE_FROZENSET, but let's be careful...
                PycRef<PycObject> obj = rhs.cast<ASTObject>()->object();
                if (obj->type() != PycObject::TYPE_FROZENSET) {
                    fprintf(stderr, "Unsupported argument type found for SET_UPDATE\n");
                    break;
                }

                ASTSet::value_t result = lhs->values();
                for (const auto& it : obj.cast<PycSet>()->values()) {
                    result.push_back(new ASTObject(it));
                }

                stack.push(new ASTSet(result));
            }
            break;
        case Pyc::LIST_EXTEND_A:
            {
                PycRef<ASTNode> rhs = stack.top();
                stack.pop();
                PycRef<ASTList> lhs = stack.top().cast<ASTList>();
                stack.pop();

                if (rhs.type() != ASTNode::NODE_OBJECT) {
                    fprintf(stderr, "Unsupported argument found for LIST_EXTEND\n");
                    break;
                }

                // I've only ever seen this be a SMALL_TUPLE, but let's be careful...
                PycRef<PycObject> obj = rhs.cast<ASTObject>()->object();
                if (obj->type() != PycObject::TYPE_TUPLE && obj->type() != PycObject::TYPE_SMALL_TUPLE) {
                    fprintf(stderr, "Unsupported argument type found for LIST_EXTEND\n");
                    break;
                }

                ASTList::value_t result = lhs->values();
                for (const auto& it : obj.cast<PycTuple>()->values()) {
                    result.push_back(new ASTObject(it));
                }

                stack.push(new ASTList(result));
            }
            break;
        case Pyc::LOAD_ATTR_A:
            {
                PycRef<ASTNode> name = stack.top();
                if (name.type() != ASTNode::NODE_IMPORT) {
                    stack.pop();

                    if (mod->verCompare(3, 12) >= 0) {
                        if (operand & 1) {
                            /* Changed in version 3.12:
                            If the low bit of name is set, then a NULL or self is pushed to the stack
                            before the attribute or unbound method respectively. */
                            stack.push(nullptr);
                        }
                        operand >>= 1;
                    }

                    stack.push(new ASTBinary(name, new ASTName(code->getName(operand)), ASTBinary::BIN_ATTR));
                }
            }
            break;
        case Pyc::LOAD_BUILD_CLASS:
            stack.push(new ASTLoadBuildClass(new PycObject()));
            break;
        case Pyc::LOAD_CLOSURE_A:
            stack.push(new ASTName(code->getCellVar(mod, operand)));
            break;
        case Pyc::LOAD_CONST_A:
            {
                PycRef<ASTObject> t_ob = new ASTObject(code->getConst(operand));

                if ((t_ob->object().type() == PycObject::TYPE_TUPLE ||
                        t_ob->object().type() == PycObject::TYPE_SMALL_TUPLE) &&
                        !t_ob->object().cast<PycTuple>()->values().size()) {
                    ASTTuple::value_t values;
                    stack.push(new ASTTuple(values));
                } else if (t_ob->object().type() == PycObject::TYPE_NONE) {
                    stack.push(NULL);
                } else {
                    stack.push(t_ob.cast<ASTNode>());
                }
            }
            break;
        case Pyc::LOAD_DEREF_A:
        case Pyc::LOAD_CLASSDEREF_A:
            stack.push(new ASTName(code->getCellVar(mod, operand)));
            break;
        case Pyc::LOAD_FAST_A:
            if (mod->verCompare(1, 3) < 0)
                stack.push(new ASTName(code->getName(operand)));
            else
                stack.push(new ASTName(code->getLocal(operand)));
            break;
        case Pyc::LOAD_FAST_LOAD_FAST_A:
            stack.push(new ASTName(code->getLocal(operand >> 4)));
            stack.push(new ASTName(code->getLocal(operand & 0xF)));
            break;
        case Pyc::LOAD_GLOBAL_A:
            if (mod->verCompare(3, 11) >= 0) {
                // Loads the global named co_names[namei>>1] onto the stack.
                if (operand & 1) {
                    /* Changed in version 3.11: 
                    If the low bit of "NAMEI" (operand) is set, 
                    then a NULL is pushed to the stack before the global variable. */
                    stack.push(nullptr);
                }
                operand >>= 1;
            }
            stack.push(new ASTName(code->getName(operand)));
            break;
        case Pyc::LOAD_LOCALS:
            stack.push(new ASTNode(ASTNode::NODE_LOCALS));
            break;
        case Pyc::STORE_LOCALS:
            stack.pop();
            break;
        case Pyc::LOAD_METHOD_A:
            {
                // Behave like LOAD_ATTR
                PycRef<ASTNode> name = stack.top();
                stack.pop();
                stack.push(new ASTBinary(name, new ASTName(code->getName(operand)), ASTBinary::BIN_ATTR));
            }
            break;
        case Pyc::LOAD_NAME_A:
            stack.push(new ASTName(code->getName(operand)));
            break;
        case Pyc::MAKE_CLOSURE_A:
        case Pyc::MAKE_FUNCTION_A:
            {
                PycRef<ASTNode> fun_code = stack.top();
                stack.pop();

                /* Test for the qualified name of the function (at TOS) */
                int tos_type = fun_code.cast<ASTObject>()->object().type();
                if (tos_type != PycObject::TYPE_CODE &&
                    tos_type != PycObject::TYPE_CODE2) {
                    fun_code = stack.top();
                    stack.pop();
                }

                ASTFunction::defarg_t defArgs, kwDefArgs;
                if (mod->verCompare(3, 6) >= 0) {
                    if (operand & 0x08) {
                        // Closure tuple.
                        stack.pop();
                    }
                    if (operand & 0x04) {
                        // Annotations tuple/dict.
                        stack.pop();
                    }
                    if (operand & 0x02) {
                        PycRef<ASTNode> kwdefaults = stack.top();
                        stack.pop();
                        if (kwdefaults.type() == ASTNode::NODE_MAP) {
                            for (const auto& entry : kwdefaults.cast<ASTMap>()->values()) {
                                if (entry.first != nullptr)
                                    kwDefArgs.push_back(entry.second);
                            }
                        } else if (kwdefaults.type() == ASTNode::NODE_CONST_MAP) {
                            for (const auto& value : kwdefaults.cast<ASTConstMap>()->values())
                                kwDefArgs.push_back(value);
                        }
                    }
                    if (operand & 0x01) {
                        PycRef<ASTNode> defaults = stack.top();
                        stack.pop();
                        if (defaults.type() == ASTNode::NODE_TUPLE) {
                            for (const auto& value : defaults.cast<ASTTuple>()->values())
                                defArgs.push_back(value);
                        } else if (defaults.type() == ASTNode::NODE_OBJECT
                                && (defaults.cast<ASTObject>()->object().type() == PycObject::TYPE_TUPLE
                                    || defaults.cast<ASTObject>()->object().type() == PycObject::TYPE_SMALL_TUPLE)) {
                            for (const auto& value : defaults.cast<ASTObject>()->object().cast<PycTuple>()->values())
                                defArgs.push_back(new ASTObject(value));
                        } else {
                            defArgs.push_back(defaults);
                        }
                    } else {
                        sync_unpack();
                    }
                } else {
                    const int defCount = operand & 0xFF;
                    const int kwDefCount = (operand >> 8) & 0xFF;
                    for (int i = 0; i < defCount; ++i) {
                        defArgs.push_front(stack.top());
                        stack.pop();
                    }
                    for (int i = 0; i < kwDefCount; ++i) {
                        kwDefArgs.push_front(stack.top());
                        stack.pop();
                    }
                }
                stack.push(new ASTFunction(fun_code, defArgs, kwDefArgs));
            }
            break;
        case Pyc::NOP:
            break;
        case Pyc::POP_BLOCK:
            {
                PycRef<ASTBlock> popblock_start = curblock;
                while (curblock->blktype() == ASTBlock::BLK_IF
                        || curblock->blktype() == ASTBlock::BLK_ELIF
                        || curblock->blktype() == ASTBlock::BLK_ELSE) {
                    if (curblock->end() == 0 || curblock->end() > pos || blocks.size() <= 1)
                        break;

                    if (!stack_hist.empty()) {
                        stack = stack_hist.top();
                        stack_hist.pop();
                    }

                    PycRef<ASTBlock> prev = curblock;
                    blocks.pop();
                    curblock = blocks.top();
                    curblock->append(prev.cast<ASTNode>());
                }

                if (curblock->blktype() == ASTBlock::BLK_CONTAINER
                        && curblock != popblock_start
                        && popblock_start->blktype() == ASTBlock::BLK_ELSE
                        && curblock.cast<ASTContainerBlock>()->hasFinally()) {
                    stack_hist.push(stack);

                    PycRef<ASTBlock> final = new ASTBlock(ASTBlock::BLK_FINALLY, 0, true);
                    blocks.push(final);
                    curblock = blocks.top();
                    break;
                }

                if ((curblock->blktype() == ASTBlock::BLK_CONTAINER ||
                        curblock->blktype() == ASTBlock::BLK_FINALLY)
                        && curblock == popblock_start) {
                    /* These should only be popped by an END_FINALLY */
                    break;
                }

                if (curblock->blktype() == ASTBlock::BLK_WITH
                        && curblock == popblock_start) {
                    // This should only be popped by a WITH_CLEANUP
                    break;
                }

                if (curblock->blktype() != ASTBlock::BLK_TRY
                        && curblock->blktype() != ASTBlock::BLK_EXCEPT
                        && curblock->blktype() != ASTBlock::BLK_FINALLY
                        && curblock->nodes().size()
                        && curblock->nodes().back().type() == ASTNode::NODE_KEYWORD) {
                    curblock->removeLast();
                }

                if (curblock->blktype() == ASTBlock::BLK_IF
                        || curblock->blktype() == ASTBlock::BLK_ELIF
                        || curblock->blktype() == ASTBlock::BLK_ELSE
                        || curblock->blktype() == ASTBlock::BLK_TRY
                        || curblock->blktype() == ASTBlock::BLK_EXCEPT
                        || curblock->blktype() == ASTBlock::BLK_FINALLY) {
                    if (!stack_hist.empty()) {
                        stack = stack_hist.top();
                        stack_hist.pop();
                    } else {
                        fprintf(stderr, "Warning: Stack history is empty, something wrong might have happened\n");
                    }
                }
                PycRef<ASTBlock> tmp = curblock;
                blocks.pop();

                if (!blocks.empty())
                    curblock = blocks.top();

                if (!(tmp->blktype() == ASTBlock::BLK_ELSE
                        && tmp->nodes().size() == 0)) {
                    curblock->append(tmp.cast<ASTNode>());
                }

                if (tmp->blktype() == ASTBlock::BLK_FOR && tmp->end() >= pos) {
                    stack_hist.push(stack);

                    PycRef<ASTBlock> blkelse = new ASTBlock(ASTBlock::BLK_ELSE, tmp->end());
                    blocks.push(blkelse);
                    curblock = blocks.top();
                }

                if (curblock->blktype() == ASTBlock::BLK_TRY
                        && tmp->blktype() != ASTBlock::BLK_FOR
                        && tmp->blktype() != ASTBlock::BLK_ASYNCFOR
                        && tmp->blktype() != ASTBlock::BLK_WHILE) {
                    stack = stack_hist.top();
                    stack_hist.pop();

                    tmp = curblock;
                    blocks.pop();
                    curblock = blocks.top();

                    if (!(tmp->blktype() == ASTBlock::BLK_ELSE
                            && tmp->nodes().size() == 0)) {
                        curblock->append(tmp.cast<ASTNode>());
                    }
                }

                if (curblock->blktype() == ASTBlock::BLK_CONTAINER) {
                    PycRef<ASTContainerBlock> cont = curblock.cast<ASTContainerBlock>();

                    if (tmp->blktype() == ASTBlock::BLK_ELSE && !cont->hasFinally()) {

                        /* Pop the container */
                        blocks.pop();
                        curblock = blocks.top();
                        curblock->append(cont.cast<ASTNode>());

                    } else if ((tmp->blktype() == ASTBlock::BLK_ELSE && cont->hasFinally())
                            || (tmp->blktype() == ASTBlock::BLK_TRY && !cont->hasExcept())) {

                        /* Add the finally block */
                        stack_hist.push(stack);

                        PycRef<ASTBlock> final = new ASTBlock(ASTBlock::BLK_FINALLY, 0, true);
                        blocks.push(final);
                        curblock = blocks.top();
                    }
                }

                if ((curblock->blktype() == ASTBlock::BLK_FOR || curblock->blktype() == ASTBlock::BLK_ASYNCFOR)
                        && curblock->end() == pos) {
                    blocks.pop();
                    blocks.top()->append(curblock.cast<ASTNode>());
                    curblock = blocks.top();
                }
            }
            break;
        case Pyc::POP_EXCEPT:
            /* Do nothing. */
            break;
        case Pyc::END_FOR:
            {
                stack.pop();

                if ((opcode == Pyc::END_FOR) && (mod->majorVer() == 3) && (mod->minorVer() == 12)) {
                    // one additional pop for python 3.12
                    stack.pop();
                }

                // end for loop here
                /* TODO : Ensure that FOR loop ends here. 
                   Due to CACHE instructions at play, the end indicated in
                   the for loop by pycdas is not correct, it is off by
                   some small amount. */
                if (curblock->blktype() == ASTBlock::BLK_FOR) {
                    PycRef<ASTBlock> prev = blocks.top();
                    blocks.pop();

                    curblock = blocks.top();
                    curblock->append(prev.cast<ASTNode>());
                }
                else {
                    fprintf(stderr, "Wrong block type %i for END_FOR\n", curblock->blktype());
                }
            }
            break;
        case Pyc::POP_TOP:
            {
                PycRef<ASTNode> value = stack.top();
                stack.pop();

                if (curblock->blktype() == ASTBlock::BLK_FOR
                        && curblock.cast<ASTIterBlock>()->isComprehension()
                        && value.type() == ASTNode::NODE_COMPREHENSION) {
                    stack.push(value);
                    break;
                }

                if (!curblock->inited()) {
                    if (curblock->blktype() == ASTBlock::BLK_WITH) {
                        curblock.cast<ASTWithBlock>()->setExpr(value);
                        break;
                    } else if (curblock->size() == 0) {
                        curblock->init();
                        break;
                    }
                    curblock->init();
                }

                if (value == nullptr || value->processed()) {
                    break;
                }

                curblock->append(value);

                if (curblock->blktype() == ASTBlock::BLK_FOR
                        && curblock.cast<ASTIterBlock>()->isComprehension()) {
                    /* This relies on some really uncertain logic...
                     * If it's a comprehension, the only POP_TOP should be
                     * a call to append the iter to the list.
                     */
                    if (value.type() == ASTNode::NODE_CALL) {
                        auto& pparams = value.cast<ASTCall>()->pparams();
                        if (!pparams.empty()) {
                            PycRef<ASTNode> res = pparams.front();
                            stack.push(new ASTComprehension(res));
                        }
                    }
                }
            }
            break;
        case Pyc::PRINT_ITEM:
            {
                PycRef<ASTPrint> printNode;
                if (curblock->size() > 0 && curblock->nodes().back().type() == ASTNode::NODE_PRINT)
                    printNode = curblock->nodes().back().try_cast<ASTPrint>();
                if (printNode && printNode->stream() == nullptr && !printNode->eol())
                    printNode->add(stack.top());
                else
                    curblock->append(new ASTPrint(stack.top()));
                stack.pop();
            }
            break;
        case Pyc::PRINT_ITEM_TO:
            {
                PycRef<ASTNode> stream = stack.top();
                stack.pop();

                PycRef<ASTPrint> printNode;
                if (curblock->size() > 0 && curblock->nodes().back().type() == ASTNode::NODE_PRINT)
                    printNode = curblock->nodes().back().try_cast<ASTPrint>();
                if (printNode && printNode->stream() == stream && !printNode->eol())
                    printNode->add(stack.top());
                else
                    curblock->append(new ASTPrint(stack.top(), stream));
                stack.pop();
                if (stream)
                    stream->setProcessed();
            }
            break;
        case Pyc::PRINT_NEWLINE:
            {
                PycRef<ASTPrint> printNode;
                if (curblock->size() > 0 && curblock->nodes().back().type() == ASTNode::NODE_PRINT)
                    printNode = curblock->nodes().back().try_cast<ASTPrint>();
                if (printNode && printNode->stream() == nullptr && !printNode->eol())
                    printNode->setEol(true);
                else
                    curblock->append(new ASTPrint(nullptr));
                stack.pop();
            }
            break;
        case Pyc::PRINT_NEWLINE_TO:
            {
                PycRef<ASTNode> stream = stack.top();
                stack.pop();

                PycRef<ASTPrint> printNode;
                if (curblock->size() > 0 && curblock->nodes().back().type() == ASTNode::NODE_PRINT)
                    printNode = curblock->nodes().back().try_cast<ASTPrint>();
                if (printNode && printNode->stream() == stream && !printNode->eol())
                    printNode->setEol(true);
                else
                    curblock->append(new ASTPrint(nullptr, stream));
                stack.pop();
                if (stream)
                    stream->setProcessed();
            }
            break;
        case Pyc::RAISE_VARARGS_A:
            {
                ASTRaise::param_t paramList;
                for (int i = 0; i < operand; i++) {
                    paramList.push_front(stack.top());
                    stack.pop();
                }
                curblock->append(new ASTRaise(paramList));

                if ((curblock->blktype() == ASTBlock::BLK_IF
                        || curblock->blktype() == ASTBlock::BLK_ELSE)
                        && stack_hist.size()
                        && blocks.size() > 1
                        && (mod->verCompare(2, 6) >= 0)) {
                    stack = stack_hist.top();
                    stack_hist.pop();

                    PycRef<ASTBlock> prev = curblock;
                    blocks.pop();
                    curblock = blocks.top();
                    curblock->append(prev.cast<ASTNode>());
                }
            }
            break;
        case Pyc::RETURN_VALUE:
        case Pyc::INSTRUMENTED_RETURN_VALUE_A:
            {
                PycRef<ASTNode> value = stack.top();
                stack.pop();
                bool is_genexpr_sentinel = value == nullptr;
                if (!is_genexpr_sentinel && value.type() == ASTNode::NODE_OBJECT
                        && value.cast<ASTObject>()->object().type() == PycObject::TYPE_NONE) {
                    is_genexpr_sentinel = true;
                }
                if (code->name() != nullptr
                        && strcmp(code->name()->value(), "<genexpr>") == 0
                        && is_genexpr_sentinel
                        && !stack.empty()
                        && stack.top().type() == ASTNode::NODE_COMPREHENSION) {
                    value = stack.top();
                    stack.pop();
                }
                curblock->append(new ASTReturn(value));

                if ((curblock->blktype() == ASTBlock::BLK_IF
                        || curblock->blktype() == ASTBlock::BLK_ELSE)
                        && stack_hist.size()
                        && blocks.size() > 1
                        && (mod->verCompare(2, 6) >= 0)) {
                    stack = stack_hist.top();
                    stack_hist.pop();

                    PycRef<ASTBlock> prev = curblock;
                    blocks.pop();
                    curblock = blocks.top();
                    curblock->append(prev.cast<ASTNode>());
                }
            }
            break;
        case Pyc::RETURN_CONST_A:
        case Pyc::INSTRUMENTED_RETURN_CONST_A:
            {
                PycRef<ASTObject> value = new ASTObject(code->getConst(operand));
                curblock->append(new ASTReturn(value.cast<ASTNode>()));
            }
            break;
        case Pyc::ROT_TWO:
            {
                PycRef<ASTNode> one = stack.top();
                stack.pop();
                if (stack.top().type() == ASTNode::NODE_CHAINSTORE) {
                    stack.pop();
                }
                PycRef<ASTNode> two = stack.top();
                stack.pop();

                stack.push(one);
                stack.push(two);
            }
            break;
        case Pyc::ROT_THREE:
            {
                PycRef<ASTNode> one = stack.top();
                stack.pop();
                PycRef<ASTNode> two = stack.top();
                stack.pop();
                if (stack.top().type() == ASTNode::NODE_CHAINSTORE) {
                    stack.pop();
                }
                PycRef<ASTNode> three = stack.top();
                stack.pop();
                stack.push(one);
                stack.push(three);
                stack.push(two);
            }
            break;
        case Pyc::ROT_FOUR:
            {
                PycRef<ASTNode> one = stack.top();
                stack.pop();
                PycRef<ASTNode> two = stack.top();
                stack.pop();
                PycRef<ASTNode> three = stack.top();
                stack.pop();
                if (stack.top().type() == ASTNode::NODE_CHAINSTORE) {
                    stack.pop();
                }
                PycRef<ASTNode> four = stack.top();
                stack.pop();
                stack.push(one);
                stack.push(four);
                stack.push(three);
                stack.push(two);
            }
            break;
        case Pyc::SET_LINENO_A:
            // Ignore
            break;
        case Pyc::SETUP_WITH_A:
        case Pyc::WITH_EXCEPT_START:
            {
                PycRef<ASTBlock> withblock = new ASTWithBlock(pos+operand);
                blocks.push(withblock);
                curblock = blocks.top();
            }
            break;
        case Pyc::WITH_CLEANUP:
        case Pyc::WITH_CLEANUP_START:
            {
                // Stack top should be a None. Ignore it.
                PycRef<ASTNode> none = stack.top();
                stack.pop();

                if (none != NULL) {
                    fprintf(stderr, "Something TERRIBLE happened!\n");
                    break;
                }

                if (curblock->blktype() == ASTBlock::BLK_WITH
                        && curblock->end() == curpos) {
                    PycRef<ASTBlock> with = curblock;
                    blocks.pop();
                    curblock = blocks.top();
                    curblock->append(with.cast<ASTNode>());
                }
                else {
                    fprintf(stderr, "Something TERRIBLE happened! No matching with block found for WITH_CLEANUP at %d\n", curpos);
                }
            }
            break;
        case Pyc::WITH_CLEANUP_FINISH:
            /* Ignore this */
            break;
        case Pyc::SETUP_EXCEPT_A:
            {
                if (curblock->blktype() == ASTBlock::BLK_CONTAINER) {
                    curblock.cast<ASTContainerBlock>()->setExcept(pos+operand);
                } else {
                    PycRef<ASTBlock> next = new ASTContainerBlock(0, pos+operand);
                    blocks.push(next.cast<ASTBlock>());
                }

                /* Store the current stack for the except/finally statement(s) */
                stack_hist.push(stack);
                PycRef<ASTBlock> tryblock = new ASTBlock(ASTBlock::BLK_TRY, pos+operand, true);
                blocks.push(tryblock.cast<ASTBlock>());
                curblock = blocks.top();

                need_try = false;
            }
            break;
        case Pyc::SETUP_FINALLY_A:
            {
                PycRef<ASTBlock> next = new ASTContainerBlock(pos+operand);
                blocks.push(next.cast<ASTBlock>());
                curblock = blocks.top();

                need_try = true;
            }
            break;
        case Pyc::SETUP_LOOP_A:
            {
                PycRef<ASTBlock> next = new ASTCondBlock(ASTBlock::BLK_WHILE, pos+operand, NULL, false);
                blocks.push(next.cast<ASTBlock>());
                curblock = blocks.top();
            }
            break;
        case Pyc::SLICE_0:
            {
                PycRef<ASTNode> name = stack.top();
                stack.pop();

                PycRef<ASTNode> slice = new ASTSlice(ASTSlice::SLICE0);
                stack.push(new ASTSubscr(name, slice));
            }
            break;
        case Pyc::SLICE_1:
            {
                PycRef<ASTNode> lower = stack.top();
                stack.pop();
                PycRef<ASTNode> name = stack.top();
                stack.pop();

                PycRef<ASTNode> slice = new ASTSlice(ASTSlice::SLICE1, lower);
                stack.push(new ASTSubscr(name, slice));
            }
            break;
        case Pyc::SLICE_2:
            {
                PycRef<ASTNode> upper = stack.top();
                stack.pop();
                PycRef<ASTNode> name = stack.top();
                stack.pop();

                PycRef<ASTNode> slice = new ASTSlice(ASTSlice::SLICE2, NULL, upper);
                stack.push(new ASTSubscr(name, slice));
            }
            break;
        case Pyc::SLICE_3:
            {
                PycRef<ASTNode> upper = stack.top();
                stack.pop();
                PycRef<ASTNode> lower = stack.top();
                stack.pop();
                PycRef<ASTNode> name = stack.top();
                stack.pop();

                PycRef<ASTNode> slice = new ASTSlice(ASTSlice::SLICE3, lower, upper);
                stack.push(new ASTSubscr(name, slice));
            }
            break;
        case Pyc::STORE_ATTR_A:
            {
                if (unpack) {
                    PycRef<ASTNode> name = stack.top();
                    stack.pop();
                    PycRef<ASTNode> attr = new ASTBinary(name, new ASTName(code->getName(operand)), ASTBinary::BIN_ATTR);
                    if (unpack_after >= 0 && unpack == unpack_after + 1)
                        attr = new ASTStarred(attr);

                    PycRef<ASTNode> tup = stack.top();
                    if (tup.type() == ASTNode::NODE_TUPLE)
                        tup.cast<ASTTuple>()->add(attr);
                    else
                        fputs("Something TERRIBLE happened!\n", stderr);

                    if (--unpack_frames.back().remaining <= 0) {
                        stack.pop();
                        unpack_frames.pop_back();
                        sync_unpack();
                        if (unpack_frames.empty()) {
                            PycRef<ASTNode> seq = stack.top();
                            stack.pop();
                            if (seq.type() == ASTNode::NODE_CHAINSTORE) {
                                append_to_chain_store(seq, tup, stack, curblock);
                            } else {
                            curblock->append(new ASTStore(seq, tup));
                        }
                    } else {
                        sync_unpack();
                        }
                    } else {
                        sync_unpack();
                    }
                } else {
                    PycRef<ASTNode> name = stack.top();
                    stack.pop();
                    PycRef<ASTNode> value = stack.top();
                    stack.pop();
                    PycRef<ASTNode> attr = new ASTBinary(name, new ASTName(code->getName(operand)), ASTBinary::BIN_ATTR);
                    if (value.type() == ASTNode::NODE_CHAINSTORE) {
                        append_to_chain_store(value, attr, stack, curblock);
                    } else {
                        curblock->append(new ASTStore(value, attr));
                    }
                }
            }
            break;
        case Pyc::STORE_DEREF_A:
            {
                if (unpack) {
                    PycRef<ASTNode> name = new ASTName(code->getCellVar(mod, operand));
                    PycRef<ASTNode> target = name;
                    if (unpack_after >= 0 && unpack == unpack_after + 1)
                        target = new ASTStarred(name);

                    PycRef<ASTNode> tup = stack.top();
                    if (tup.type() == ASTNode::NODE_TUPLE)
                        tup.cast<ASTTuple>()->add(target);
                    else
                        fputs("Something TERRIBLE happened!\n", stderr);

                    if (--unpack_frames.back().remaining <= 0) {
                        stack.pop();
                        unpack_frames.pop_back();
                        sync_unpack();
                        if (unpack_frames.empty()) {
                            PycRef<ASTNode> seq = stack.top();
                            stack.pop();

                            if (curblock->blktype() == ASTBlock::BLK_FOR
                                    && !curblock->inited()) {
                                PycRef<ASTTuple> tuple = tup.try_cast<ASTTuple>();
                                if (tuple != NULL)
                                    tuple->setRequireParens(false);
                                curblock.cast<ASTIterBlock>()->setIndex(tup);
                            } else if (seq.type() == ASTNode::NODE_CHAINSTORE) {
                                append_to_chain_store(seq, tup, stack, curblock);
                            } else {
                            curblock->append(new ASTStore(seq, tup));
                        }
                    } else {
                        sync_unpack();
                    }
                    }
                } else {
                    PycRef<ASTNode> value = stack.top();
                    stack.pop();
                    PycRef<ASTNode> name = new ASTName(code->getCellVar(mod, operand));

                    if (curblock->blktype() == ASTBlock::BLK_FOR
                            && !curblock->inited()) {
                        curblock.cast<ASTIterBlock>()->setIndex(name);
                    } else if (!stack.empty() && stack.top().type() == ASTNode::NODE_IMPORT) {
                        PycRef<ASTImport> import = stack.top().cast<ASTImport>();
                        import->add_store(new ASTStore(value, name));
                    } else if (value.type() == ASTNode::NODE_CHAINSTORE) {
                        append_to_chain_store(value, name, stack, curblock);
                    } else {
                        curblock->append(new ASTStore(value, name));
                    }
                }
            }
            break;
        case Pyc::STORE_FAST_A:
            {
                if (unpack) {
                    PycRef<ASTNode> name;

                    if (mod->verCompare(1, 3) < 0)
                        name = new ASTName(code->getName(operand));
                    else
                        name = new ASTName(code->getLocal(operand));
                    PycRef<ASTNode> target = name;
                    if (unpack_after >= 0 && unpack == unpack_after + 1)
                        target = new ASTStarred(name);

                    PycRef<ASTNode> tup = stack.top();
                    if (tup.type() == ASTNode::NODE_TUPLE)
                        tup.cast<ASTTuple>()->add(target);
                    else
                        fputs("Something TERRIBLE happened!\n", stderr);

                    if (--unpack_frames.back().remaining <= 0) {
                        stack.pop();
                        unpack_frames.pop_back();
                        sync_unpack();
                        while (!unpack_frames.empty() && unpack_frames.back().remaining <= 0) {
                            tup = stack.top();
                            stack.pop();
                            unpack_frames.pop_back();
                            sync_unpack();
                        }
                        if (unpack_frames.empty()) {
                            PycRef<ASTNode> seq = stack.top();
                            stack.pop();

                            if (curblock->blktype() == ASTBlock::BLK_FOR
                                    && !curblock->inited()) {
                                PycRef<ASTTuple> tuple = tup.try_cast<ASTTuple>();
                                if (tuple != NULL)
                                    tuple->setRequireParens(false);
                                curblock.cast<ASTIterBlock>()->setIndex(tup);
                            } else if (seq.type() == ASTNode::NODE_CHAINSTORE) {
                                append_to_chain_store(seq, tup, stack, curblock);
                            } else {
                                curblock->append(new ASTStore(seq, tup));
                            }
                        }
                    }
                    sync_unpack();
                } else {
                    PycRef<ASTNode> value = stack.top();
                    stack.pop();
                    value = recover_empty_literal_after_restore(prev_opcode, value);
                    PycRef<ASTNode> name;

                    if (mod->verCompare(1, 3) < 0)
                        name = new ASTName(code->getName(operand));
                    else
                        name = new ASTName(code->getLocal(operand));

                    if (name.cast<ASTName>()->name()->value()[0] == '_'
                            && name.cast<ASTName>()->name()->value()[1] == '[') {
                        /* Don't show stores of list comp append objects. */
                        break;
                    }

                    if (curblock->blktype() == ASTBlock::BLK_FOR
                            && !curblock->inited()) {
                        curblock.cast<ASTIterBlock>()->setIndex(name);
                    } else if (curblock->blktype() == ASTBlock::BLK_WITH
                                   && !curblock->inited()) {
                        curblock.cast<ASTWithBlock>()->setExpr(value);
                        curblock.cast<ASTWithBlock>()->setVar(name);
                    } else if (!stack.empty() && stack.top().type() == ASTNode::NODE_IMPORT) {
                        PycRef<ASTImport> import = stack.top().cast<ASTImport>();
                        import->add_store(new ASTStore(value, name));
                    } else if (value.type() == ASTNode::NODE_CHAINSTORE) {
                        append_to_chain_store(value, name, stack, curblock);
                    } else {
                        curblock->append(new ASTStore(value, name));
                    }
                }
            }
            break;
        case Pyc::STORE_GLOBAL_A:
            {
                PycRef<ASTNode> name = new ASTName(code->getName(operand));

                if (unpack) {
                    PycRef<ASTNode> target = name;
                    if (unpack_after >= 0 && unpack == unpack_after + 1)
                        target = new ASTStarred(name);
                    PycRef<ASTNode> tup = stack.top();
                    if (tup.type() == ASTNode::NODE_TUPLE)
                        tup.cast<ASTTuple>()->add(target);
                    else
                        fputs("Something TERRIBLE happened!\n", stderr);

                    if (--unpack_frames.back().remaining <= 0) {
                        stack.pop();
                        unpack_frames.pop_back();
                        sync_unpack();
                        if (unpack_frames.empty()) {
                            PycRef<ASTNode> seq = stack.top();
                            stack.pop();

                            if (curblock->blktype() == ASTBlock::BLK_FOR
                                    && !curblock->inited()) {
                                PycRef<ASTTuple> tuple = tup.try_cast<ASTTuple>();
                                if (tuple != NULL)
                                    tuple->setRequireParens(false);
                                curblock.cast<ASTIterBlock>()->setIndex(tup);
                            } else if (seq.type() == ASTNode::NODE_CHAINSTORE) {
                                append_to_chain_store(seq, tup, stack, curblock);
                            } else {
                                curblock->append(new ASTStore(seq, tup));
                            }
                        }
                    } else {
                        sync_unpack();
                    }
                } else {
                    PycRef<ASTNode> value = stack.top();
                    stack.pop();
                    if (value.type() == ASTNode::NODE_CHAINSTORE) {
                        append_to_chain_store(value, name, stack, curblock);
                    } else {
                        curblock->append(new ASTStore(value, name));
                    }
                }

                /* Mark the global as used */
                code->markGlobal(name.cast<ASTName>()->name());
            }
            break;
        case Pyc::STORE_NAME_A:
            {
                if (unpack) {
                    PycRef<ASTNode> name = new ASTName(code->getName(operand));
                    PycRef<ASTNode> target = name;
                    if (unpack_after >= 0 && unpack == unpack_after + 1)
                        target = new ASTStarred(name);

                    PycRef<ASTNode> tup = stack.top();
                    if (tup.type() == ASTNode::NODE_TUPLE)
                        tup.cast<ASTTuple>()->add(target);
                    else
                        fputs("Something TERRIBLE happened!\n", stderr);

                    if (--unpack_frames.back().remaining <= 0) {
                        stack.pop();
                        unpack_frames.pop_back();
                        sync_unpack();
                        if (unpack_frames.empty()) {
                            PycRef<ASTNode> seq = stack.top();
                            stack.pop();

                            if (curblock->blktype() == ASTBlock::BLK_FOR
                                    && !curblock->inited()) {
                                PycRef<ASTTuple> tuple = tup.try_cast<ASTTuple>();
                                if (tuple != NULL)
                                    tuple->setRequireParens(false);
                                curblock.cast<ASTIterBlock>()->setIndex(tup);
                            } else if (seq.type() == ASTNode::NODE_CHAINSTORE) {
                                append_to_chain_store(seq, tup, stack, curblock);
                            } else {
                                curblock->append(new ASTStore(seq, tup));
                            }
                        }
                    } else {
                        sync_unpack();
                    }
                } else {
                    PycRef<ASTNode> value = stack.top();
                    stack.pop();

                    PycRef<PycString> varname = code->getName(operand);
                    if (varname->length() >= 2 && varname->value()[0] == '_'
                            && varname->value()[1] == '[') {
                        /* Don't show stores of list comp append objects. */
                        break;
                    }

                    // Return private names back to their original name
                    const std::string class_prefix = std::string("_") + code->name()->strValue();
                    if (varname->startsWith(class_prefix + std::string("__")))
                        varname->setValue(varname->strValue().substr(class_prefix.size()));

                    PycRef<ASTNode> name = new ASTName(varname);

                    if (curblock->blktype() == ASTBlock::BLK_FOR
                            && !curblock->inited()) {
                        curblock.cast<ASTIterBlock>()->setIndex(name);
                    } else if (stack.top().type() == ASTNode::NODE_IMPORT) {
                        PycRef<ASTImport> import = stack.top().cast<ASTImport>();

                        import->add_store(new ASTStore(value, name));
                    } else if (curblock->blktype() == ASTBlock::BLK_WITH
                               && !curblock->inited()) {
                        curblock.cast<ASTWithBlock>()->setExpr(value);
                        curblock.cast<ASTWithBlock>()->setVar(name);
                    } else if (value.type() == ASTNode::NODE_CHAINSTORE) {
                        append_to_chain_store(value, name, stack, curblock);
                    } else {
                        curblock->append(new ASTStore(value, name));

                        if (value.type() == ASTNode::NODE_INVALID)
                            break;
                    }
                }
            }
            break;
        case Pyc::STORE_SLICE_0:
            {
                PycRef<ASTNode> dest = stack.top();
                stack.pop();
                PycRef<ASTNode> value = stack.top();
                stack.pop();

                curblock->append(new ASTStore(value, new ASTSubscr(dest, new ASTSlice(ASTSlice::SLICE0))));
            }
            break;
        case Pyc::STORE_SLICE_1:
            {
                PycRef<ASTNode> upper = stack.top();
                stack.pop();
                PycRef<ASTNode> dest = stack.top();
                stack.pop();
                PycRef<ASTNode> value = stack.top();
                stack.pop();

                curblock->append(new ASTStore(value, new ASTSubscr(dest, new ASTSlice(ASTSlice::SLICE1, upper))));
            }
            break;
        case Pyc::STORE_SLICE_2:
            {
                PycRef<ASTNode> lower = stack.top();
                stack.pop();
                PycRef<ASTNode> dest = stack.top();
                stack.pop();
                PycRef<ASTNode> value = stack.top();
                stack.pop();

                curblock->append(new ASTStore(value, new ASTSubscr(dest, new ASTSlice(ASTSlice::SLICE2, NULL, lower))));
            }
            break;
        case Pyc::STORE_SLICE_3:
            {
                PycRef<ASTNode> lower = stack.top();
                stack.pop();
                PycRef<ASTNode> upper = stack.top();
                stack.pop();
                PycRef<ASTNode> dest = stack.top();
                stack.pop();
                PycRef<ASTNode> value = stack.top();
                stack.pop();

                curblock->append(new ASTStore(value, new ASTSubscr(dest, new ASTSlice(ASTSlice::SLICE3, upper, lower))));
            }
            break;
        case Pyc::STORE_SUBSCR:
            {
                if (unpack) {
                    PycRef<ASTNode> subscr = stack.top();
                    stack.pop();
                    PycRef<ASTNode> dest = stack.top();
                    stack.pop();

                    PycRef<ASTNode> save = new ASTSubscr(dest, subscr);
                    if (unpack_after >= 0 && unpack == unpack_after + 1)
                        save = new ASTStarred(save);

                    PycRef<ASTNode> tup = stack.top();
                    if (tup.type() == ASTNode::NODE_TUPLE)
                        tup.cast<ASTTuple>()->add(save);
                    else
                        fputs("Something TERRIBLE happened!\n", stderr);

                    if (--unpack_frames.back().remaining <= 0) {
                        stack.pop();
                        unpack_frames.pop_back();
                        sync_unpack();
                        if (unpack_frames.empty()) {
                            PycRef<ASTNode> seq = stack.top();
                            stack.pop();
                            if (seq.type() == ASTNode::NODE_CHAINSTORE) {
                                append_to_chain_store(seq, tup, stack, curblock);
                            } else {
                                curblock->append(new ASTStore(seq, tup));
                            }
                        }
                    } else {
                        sync_unpack();
                    }
                } else {
                    PycRef<ASTNode> subscr = stack.top();
                    stack.pop();
                    PycRef<ASTNode> dest = stack.top();
                    stack.pop();
                    PycRef<ASTNode> src = stack.top();
                    stack.pop();

                    // If variable annotations are enabled, we'll need to check for them here.
                    // Python handles a varaible annotation by setting:
                    // __annotations__['var-name'] = type
                    const bool found_annotated_var = (variable_annotations && dest->type() == ASTNode::Type::NODE_NAME
                                                      && dest.cast<ASTName>()->name()->isEqual("__annotations__"));

                    if (found_annotated_var) {
                        // Annotations can be done alone or as part of an assignment.
                        // In the case of an assignment, we'll see a NODE_STORE on the stack.
                        if (!curblock->nodes().empty() && curblock->nodes().back()->type() == ASTNode::Type::NODE_STORE) {
                            // Replace the existing NODE_STORE with a new one that includes the annotation.
                            PycRef<ASTStore> store = curblock->nodes().back().cast<ASTStore>();
                            curblock->removeLast();
                            curblock->append(new ASTStore(store->src(),
                                                          new ASTAnnotatedVar(subscr, src)));
                        } else {
                            curblock->append(new ASTAnnotatedVar(subscr, src));
                        }
                    } else {
                        if (dest.type() == ASTNode::NODE_MAP) {
                            dest.cast<ASTMap>()->add(subscr, src);
                        } else if (src.type() == ASTNode::NODE_CHAINSTORE) {
                            append_to_chain_store(src, new ASTSubscr(dest, subscr), stack, curblock);
                        } else {
                            curblock->append(new ASTStore(src, new ASTSubscr(dest, subscr)));
                        }
                    }
                }
            }
            break;
        case Pyc::UNARY_CALL:
            {
                PycRef<ASTNode> func = stack.top();
                stack.pop();
                stack.push(new ASTCall(func, ASTCall::pparam_t(), ASTCall::kwparam_t()));
            }
            break;
        case Pyc::UNARY_CONVERT:
            {
                PycRef<ASTNode> name = stack.top();
                stack.pop();
                stack.push(new ASTConvert(name));
            }
            break;
        case Pyc::UNARY_INVERT:
            {
                PycRef<ASTNode> arg = stack.top();
                stack.pop();
                stack.push(new ASTUnary(arg, ASTUnary::UN_INVERT));
            }
            break;
        case Pyc::UNARY_NEGATIVE:
            {
                PycRef<ASTNode> arg = stack.top();
                stack.pop();
                stack.push(new ASTUnary(arg, ASTUnary::UN_NEGATIVE));
            }
            break;
        case Pyc::UNARY_NOT:
            {
                PycRef<ASTNode> arg = stack.top();
                stack.pop();
                stack.push(new ASTUnary(arg, ASTUnary::UN_NOT));
            }
            break;
        case Pyc::UNARY_POSITIVE:
            {
                PycRef<ASTNode> arg = stack.top();
                stack.pop();
                stack.push(new ASTUnary(arg, ASTUnary::UN_POSITIVE));
            }
            break;
        case Pyc::UNPACK_LIST_A:
        case Pyc::UNPACK_TUPLE_A:
        case Pyc::UNPACK_SEQUENCE_A:
            {
                if (operand > 0) {
                    ASTTuple::value_t vals;
                    PycRef<ASTNode> tup = new ASTTuple(vals);
                    if (!unpack_frames.empty()) {
                        PycRef<ASTNode> parent = stack.top();
                        if (parent.type() == ASTNode::NODE_TUPLE)
                            parent.cast<ASTTuple>()->add(tup);
                        else
                            fputs("Something TERRIBLE happened!\n", stderr);
                        --unpack_frames.back().remaining;
                    }
                    stack.push(tup);
                    unpack_frames.push_back({ operand, -1 });
                    sync_unpack();
                } else {
                    // Unpack zero values and assign it to top of stack or for loop variable.
                    // E.g. [] = TOS / for [] in X
                    ASTTuple::value_t vals;
                    auto tup = new ASTTuple(vals);
                    if (curblock->blktype() == ASTBlock::BLK_FOR
                        && !curblock->inited()) {
                        tup->setRequireParens(true);
                        curblock.cast<ASTIterBlock>()->setIndex(tup);
                    } else if (stack.top().type() == ASTNode::NODE_CHAINSTORE) {
                        auto chainStore = stack.top();
                        stack.pop();
                        append_to_chain_store(chainStore, tup, stack, curblock);
                    } else {
                        curblock->append(new ASTStore(stack.top(), tup));
                        stack.pop();
                    }
                }
            }
            break;
        case Pyc::UNPACK_EX_A:
            {
                int before = operand & 0xFF;
                ASTTuple::value_t vals;
                PycRef<ASTNode> tup = new ASTTuple(vals);
                if (!unpack_frames.empty()) {
                    PycRef<ASTNode> parent = stack.top();
                    if (parent.type() == ASTNode::NODE_TUPLE)
                        parent.cast<ASTTuple>()->add(tup);
                    else
                        fputs("Something TERRIBLE happened!\n", stderr);
                    --unpack_frames.back().remaining;
                }
                stack.push(tup);
                unpack_frames.push_back({ before + (operand >> 8) + 1, operand >> 8 });
                sync_unpack();
            }
            break;
        case Pyc::YIELD_FROM:
            {
                PycRef<ASTNode> dest = stack.top();
                stack.pop();
                // TODO: Support yielding into a non-null destination
                PycRef<ASTNode> value = stack.top();
                if (value) {
                    value->setProcessed();
                    curblock->append(new ASTReturn(value, ASTReturn::YIELD_FROM));
                }
            }
            break;
        case Pyc::YIELD_VALUE:
        case Pyc::INSTRUMENTED_YIELD_VALUE_A:
            {
                collapse_empty_comprehension_condition_blocks();
                PycRef<ASTNode> value = stack.top();
                stack.pop();
                if (curblock->blktype() == ASTBlock::BLK_FOR
                        && curblock.cast<ASTIterBlock>()->isComprehension()) {
                    stack.push(new ASTComprehension(value, true));
                } else {
                    curblock->append(new ASTReturn(value, ASTReturn::YIELD));
                }
            }
            break;
        case Pyc::SETUP_ANNOTATIONS:
            variable_annotations = true;
            break;
        case Pyc::PRECALL_A:
        case Pyc::RESUME_A:
        case Pyc::INSTRUMENTED_RESUME_A:
            /* We just entirely ignore this / no-op */
            break;
        case Pyc::CACHE:
            /* These "fake" opcodes are used as placeholders for optimizing
               certain opcodes in Python 3.11+.  Since we have no need for
               that during disassembly/decompilation, we can just treat these
               as no-ops. */
            break;
        case Pyc::PUSH_NULL:
            stack.push(nullptr);
            break;
        case Pyc::GEN_START_A:
            stack.pop();
            break;
        case Pyc::SWAP_A:
            {
                unpack = operand;
                ASTTuple::value_t values;
                ASTTuple::value_t next_tuple;
                values.resize(operand);
                for (int i = 0; i < operand; i++) {
                    values[operand - i - 1] = stack.top();
                    stack.pop();
                }
                auto tup = new ASTTuple(values);
                tup->setRequireParens(false);
                auto next_tup = new ASTTuple(next_tuple);
                next_tup->setRequireParens(false);
                stack.push(tup);
                stack.push(next_tup);
            }
            break;
        case Pyc::BINARY_SLICE:
            {
                PycRef<ASTNode> end = stack.top();
                stack.pop();
                PycRef<ASTNode> start = stack.top();
                stack.pop();
                PycRef<ASTNode> dest = stack.top();
                stack.pop();

                if (start.type() == ASTNode::NODE_OBJECT
                        && start.cast<ASTObject>()->object() == Pyc_None) {
                    start = NULL;
                }

                if (end.type() == ASTNode::NODE_OBJECT
                        && end.cast<ASTObject>()->object() == Pyc_None) {
                    end = NULL;
                }

                PycRef<ASTNode> slice;
                if (start == NULL && end == NULL) {
                    slice = new ASTSlice(ASTSlice::SLICE0);
                } else if (start == NULL) {
                    slice = new ASTSlice(ASTSlice::SLICE2, start, end);
                } else if (end == NULL) {
                    slice = new ASTSlice(ASTSlice::SLICE1, start, end);
                } else {
                    slice = new ASTSlice(ASTSlice::SLICE3, start, end);
                }
                stack.push(new ASTSubscr(dest, slice));
            }
            break;
        case Pyc::STORE_SLICE:
            {
                PycRef<ASTNode> end = stack.top();
                stack.pop();
                PycRef<ASTNode> start = stack.top();
                stack.pop();
                PycRef<ASTNode> dest = stack.top();
                stack.pop();
                PycRef<ASTNode> values = stack.top();
                stack.pop();

                if (start.type() == ASTNode::NODE_OBJECT
                        && start.cast<ASTObject>()->object() == Pyc_None) {
                    start = NULL;
                }

                if (end.type() == ASTNode::NODE_OBJECT
                        && end.cast<ASTObject>()->object() == Pyc_None) {
                    end = NULL;
                }

                PycRef<ASTNode> slice;
                if (start == NULL && end == NULL) {
                    slice = new ASTSlice(ASTSlice::SLICE0);
                } else if (start == NULL) {
                    slice = new ASTSlice(ASTSlice::SLICE2, start, end);
                } else if (end == NULL) {
                    slice = new ASTSlice(ASTSlice::SLICE1, start, end);
                } else {
                    slice = new ASTSlice(ASTSlice::SLICE3, start, end);
                }

                curblock->append(new ASTStore(values, new ASTSubscr(dest, slice)));
            }
            break;
        case Pyc::COPY_A:
            {
                PycRef<ASTNode> value = stack.top(operand);
                stack.push(value);
            }
            break;
        default:
            fprintf(stderr, "Unsupported opcode: %s (%d)\n", Pyc::OpcodeName(opcode), opcode);
            cleanBuild = false;
            return new ASTNodeList(defblock->nodes());
        }

        prev_terminal_flow =
            opcode == Pyc::RETURN_VALUE ||
            opcode == Pyc::RETURN_CONST_A ||
            opcode == Pyc::INSTRUMENTED_RETURN_VALUE_A ||
            opcode == Pyc::INSTRUMENTED_RETURN_CONST_A ||
            opcode == Pyc::RAISE_VARARGS_A ||
            opcode == Pyc::BREAK_LOOP ||
            opcode == Pyc::CONTINUE_LOOP_A ||
            opcode == Pyc::JUMP_ABSOLUTE_A ||
            opcode == Pyc::JUMP_BACKWARD_A ||
            opcode == Pyc::JUMP_BACKWARD_NO_INTERRUPT_A;
        prev_opcode = opcode;

        else_pop =  ( (curblock->blktype() == ASTBlock::BLK_ELSE)
                      || (curblock->blktype() == ASTBlock::BLK_IF)
                      || (curblock->blktype() == ASTBlock::BLK_ELIF) )
                 && (curblock->end() == pos);
    }

    while (blocks.size() > 1) {
        curblock = blocks.top();
        if ((curblock->blktype() == ASTBlock::BLK_IF
                || curblock->blktype() == ASTBlock::BLK_ELIF
                || curblock->blktype() == ASTBlock::BLK_ELSE
                || curblock->blktype() == ASTBlock::BLK_TRY
                || curblock->blktype() == ASTBlock::BLK_EXCEPT
                || curblock->blktype() == ASTBlock::BLK_FINALLY)
                && !stack_hist.empty()) {
            stack = stack_hist.top();
            stack_hist.pop();
        }

        PycRef<ASTBlock> tmp = blocks.top();
        blocks.pop();
        blocks.top()->append(tmp.cast<ASTNode>());
        curblock = blocks.top();
        CheckIfExpr(stack, curblock);
    }

    if (blocks.empty()) {
        blocks.push(defblock);
    }
    if (stack_hist.size()) {
        if (blocks.size() == 1) {
            while (stack_hist.size()) {
                stack_hist.pop();
            }
        } else {
            fprintf(stderr, "Warning: Stack history is not empty! [%s]\n", code->name()->value());

            while (stack_hist.size()) {
                stack_hist.pop();
            }
        }
    }

    cleanBuild = true;
    return new ASTNodeList(defblock->nodes());
}

static void append_to_chain_store(const PycRef<ASTNode> &chainStore,
        PycRef<ASTNode> item, FastStack& stack, const PycRef<ASTBlock>& curblock)
{
    stack.pop();    // ignore identical source object.
    chainStore.cast<ASTChainStore>()->append(item);
    if (stack.top().type() == PycObject::TYPE_NULL) {
        curblock->append(chainStore);
    } else {
        stack.push(chainStore);
    }
}

static int cmp_prec(PycRef<ASTNode> parent, PycRef<ASTNode> child)
{
    /* Determine whether the parent has higher precedence than therefore
       child, so we don't flood the source code with extraneous parens.
       Else we'd have expressions like (((a + b) + c) + d) when therefore
       equivalent, a + b + c + d would suffice. */

    if (parent.type() == ASTNode::NODE_UNARY && parent.cast<ASTUnary>()->op() == ASTUnary::UN_NOT)
        return 1;   // Always parenthesize not(x)
    if (child.type() == ASTNode::NODE_BINARY) {
        PycRef<ASTBinary> binChild = child.cast<ASTBinary>();
        if (parent.type() == ASTNode::NODE_BINARY) {
            PycRef<ASTBinary> binParent = parent.cast<ASTBinary>();
            if (binParent->right() == child) {
                if (binParent->op() == ASTBinary::BIN_SUBTRACT &&
                    binChild->op() == ASTBinary::BIN_ADD)
                    return 1;
                else if (binParent->op() == ASTBinary::BIN_DIVIDE &&
                         binChild->op() == ASTBinary::BIN_MULTIPLY)
                    return 1;
            }
            return binChild->op() - binParent->op();
        }
        else if (parent.type() == ASTNode::NODE_COMPARE)
            return (binChild->op() == ASTBinary::BIN_LOG_AND ||
                    binChild->op() == ASTBinary::BIN_LOG_OR) ? 1 : -1;
        else if (parent.type() == ASTNode::NODE_UNARY)
            return (binChild->op() == ASTBinary::BIN_POWER) ? -1 : 1;
    } else if (child.type() == ASTNode::NODE_UNARY) {
        PycRef<ASTUnary> unChild = child.cast<ASTUnary>();
        if (parent.type() == ASTNode::NODE_BINARY) {
            PycRef<ASTBinary> binParent = parent.cast<ASTBinary>();
            if (binParent->op() == ASTBinary::BIN_LOG_AND ||
                binParent->op() == ASTBinary::BIN_LOG_OR)
                return -1;
            else if (unChild->op() == ASTUnary::UN_NOT)
                return 1;
            else if (binParent->op() == ASTBinary::BIN_POWER)
                return 1;
            else
                return -1;
        } else if (parent.type() == ASTNode::NODE_COMPARE) {
            return (unChild->op() == ASTUnary::UN_NOT) ? 1 : -1;
        } else if (parent.type() == ASTNode::NODE_UNARY) {
            return unChild->op() - parent.cast<ASTUnary>()->op();
        }
    } else if (child.type() == ASTNode::NODE_COMPARE) {
        PycRef<ASTCompare> cmpChild = child.cast<ASTCompare>();
        if (parent.type() == ASTNode::NODE_BINARY)
            return (parent.cast<ASTBinary>()->op() == ASTBinary::BIN_LOG_AND ||
                    parent.cast<ASTBinary>()->op() == ASTBinary::BIN_LOG_OR) ? -1 : 1;
        else if (parent.type() == ASTNode::NODE_COMPARE)
            return cmpChild->op() - parent.cast<ASTCompare>()->op();
        else if (parent.type() == ASTNode::NODE_UNARY)
            return (parent.cast<ASTUnary>()->op() == ASTUnary::UN_NOT) ? -1 : 1;
    }

    /* For normal nodes, don't parenthesize anything */
    return -1;
}

static void print_ordered(PycRef<ASTNode> parent, PycRef<ASTNode> child,
                          PycModule* mod, std::ostream& pyc_output)
{
    if (child.type() == ASTNode::NODE_BINARY ||
        child.type() == ASTNode::NODE_COMPARE) {
        if (cmp_prec(parent, child) > 0) {
            pyc_output << "(";
            print_src(child, mod, pyc_output);
            pyc_output << ")";
        } else {
            print_src(child, mod, pyc_output);
        }
    } else if (child.type() == ASTNode::NODE_UNARY) {
        if (cmp_prec(parent, child) > 0) {
            pyc_output << "(";
            print_src(child, mod, pyc_output);
            pyc_output << ")";
        } else {
            print_src(child, mod, pyc_output);
        }
    } else if (child.type() == ASTNode::NODE_TERNARY) {
        pyc_output << "(";
        print_src(child, mod, pyc_output);
        pyc_output << ")";
    } else {
        print_src(child, mod, pyc_output);
    }
}

static bool needs_attr_parens(const PycRef<ASTNode>& node)
{
    PycRef<ASTObject> obj = node.try_cast<ASTObject>();
    if (obj == nullptr)
        return false;

    int type = obj->object().type();
    return type == PycObject::TYPE_INT
        || type == PycObject::TYPE_INT64
        || type == PycObject::TYPE_LONG
        || type == PycObject::TYPE_FLOAT
        || type == PycObject::TYPE_BINARY_FLOAT
        || type == PycObject::TYPE_COMPLEX
        || type == PycObject::TYPE_BINARY_COMPLEX;
}

static void start_line(int indent, std::ostream& pyc_output)
{
    if (inLambda)
        return;
    for (int i=0; i<indent; i++)
        pyc_output << "    ";
}

static void end_line(std::ostream& pyc_output)
{
    if (inLambda)
        return;
    pyc_output << "\n";
}

static void print_block(PycRef<ASTBlock> blk, PycModule* mod,
                        std::ostream& pyc_output);

int cur_indent = -1;
static PycRef<ASTNode> condition_with_negation(const PycRef<ASTCondBlock>& blk)
{
    if (blk == nullptr)
        return nullptr;

    PycRef<ASTNode> cond = blk->cond();
    if (blk->negative())
        return new ASTUnary(cond, ASTUnary::UN_NOT);
    return cond;
}

static bool is_terminal_statement(const PycRef<ASTNode>& node);

static bool is_none_like_node(const PycRef<ASTNode>& node)
{
    if (node == nullptr)
        return true;

    PycRef<ASTObject> obj = node.try_cast<ASTObject>();
    return obj != nullptr && obj->object().type() == PycObject::TYPE_NONE;
}

static bool is_named_node(const PycRef<ASTNode>& node, const char* name)
{
    PycRef<ASTName> named = node.try_cast<ASTName>();
    return named != nullptr && strcmp(named->name()->value(), name) == 0;
}

static bool is_synthetic_except_marker(const PycRef<ASTNode>& node)
{
    return node == nullptr || node->type() == ASTNode::NODE_NAME;
}

struct ExceptRenderInfo {
    ASTBlock::list_t lines;
    PycRef<ASTName> alias;
};

static bool is_cleanup_for_name(const PycRef<ASTNode>& node, const char* alias_name)
{
    if (node != nullptr && node->type() == ASTNode::NODE_DELETE)
        return is_named_node(node.cast<ASTDelete>()->value(), alias_name);

    PycRef<ASTStore> cleanup_store = node.try_cast<ASTStore>();
    return cleanup_store != nullptr
        && cleanup_store->dest().type() == ASTNode::NODE_NAME
        && is_named_node(cleanup_store->dest(), alias_name)
        && is_none_like_node(cleanup_store->src());
}

static ExceptRenderInfo normalize_except_block(const PycRef<ASTBlock>& blk)
{
    ExceptRenderInfo info;
    info.lines = blk->nodes();

    if (blk == nullptr || blk->blktype() != ASTBlock::BLK_EXCEPT || info.lines.empty())
        return info;

    ASTBlock::list_t trimmed = info.lines;
    bool removed_cleanup = false;
    PycRef<ASTName> alias;
    const char* alias_name = nullptr;

    while (!trimmed.empty() && is_none_like_node(trimmed.front())) {
        trimmed.pop_front();
        removed_cleanup = true;
    }

    if (!trimmed.empty()) {
        PycRef<ASTStore> bind = trimmed.front().try_cast<ASTStore>();
        if (bind != nullptr && bind->dest().type() == ASTNode::NODE_NAME && is_none_like_node(bind->src())) {
            alias = bind->dest().cast<ASTName>();
            alias_name = alias->name()->value();
            trimmed.pop_front();
            removed_cleanup = true;
        }
    }

    if (!trimmed.empty()) {
        PycRef<ASTBlock> cleanup_container = trimmed.front().try_cast<ASTBlock>();
        if (cleanup_container != nullptr && cleanup_container->blktype() == ASTBlock::BLK_CONTAINER) {
            ASTBlock::list_t flattened;
            for (const auto& inner : cleanup_container->nodes()) {
                PycRef<ASTBlock> inner_try = inner.try_cast<ASTBlock>();
                if (inner_try != nullptr && inner_try->blktype() == ASTBlock::BLK_TRY) {
                    for (const auto& try_line : inner_try->nodes()) {
                        flattened.push_back(try_line);
                        if (is_terminal_statement(try_line))
                            break;
                    }
                    continue;
                }

                if (inner_try != nullptr && (inner_try->blktype() == ASTBlock::BLK_FINALLY
                        || (inner_try->blktype() == ASTBlock::BLK_ELSE && inner_try->size() == 0))) {
                    removed_cleanup = true;
                    continue;
                }

                if (is_cleanup_for_name(inner, alias_name))
                    continue;

                PycRef<ASTReturn> ret = inner.try_cast<ASTReturn>();
                if (ret != nullptr && is_none_like_node(ret->value()))
                    continue;

                flattened.push_back(inner);
                if (is_terminal_statement(inner))
                    break;
            }

            trimmed.pop_front();
            for (auto it = flattened.rbegin(); it != flattened.rend(); ++it)
                trimmed.push_front(*it);
            removed_cleanup = true;
        }
    }

    ASTBlock::list_t filtered;
    for (const auto& line : trimmed) {
        if (is_none_like_node(line)) {
            removed_cleanup = true;
            continue;
        }
        if (alias_name != nullptr && is_cleanup_for_name(line, alias_name)) {
            removed_cleanup = true;
            continue;
        }

        filtered.push_back(line);
    }

    if (!removed_cleanup)
        return info;

    if (!filtered.empty()) {
        PycRef<ASTBlock> inner_try = filtered.front().try_cast<ASTBlock>();
        if (inner_try != nullptr && inner_try->blktype() == ASTBlock::BLK_TRY) {
            ASTBlock::list_t flattened = inner_try->nodes();
            for (auto it = std::next(filtered.begin()); it != filtered.end(); ++it)
                flattened.push_back(*it);
            filtered = flattened;
        }
    }

    info.lines = filtered;
    info.alias = alias;
    return info;
}

static bool block_is_effectively_empty(const PycRef<ASTBlock>& blk)
{
    if (blk == nullptr)
        return true;

    if (blk->size() == 0)
        return true;

    if (blk->size() == 1) {
        PycRef<ASTNode> only = blk->nodes().front();
        if (only != nullptr && only->type() == ASTNode::NODE_KEYWORD
                && only.cast<ASTKeyword>()->key() == ASTKeyword::KW_PASS) {
            return true;
        }
    }

    return false;
}

static bool try_print_collapsed_compare_chain(ASTBlock::list_t::const_iterator& it,
                                              const ASTBlock::list_t& lines,
                                              PycModule* mod,
                                              std::ostream& pyc_output)
{
    PycRef<ASTBlock> first = (*it).try_cast<ASTBlock>();
    if (first == nullptr
            || (first->blktype() != ASTBlock::BLK_IF && first->blktype() != ASTBlock::BLK_ELIF)
            || !block_is_effectively_empty(first)) {
        return false;
    }

    PycRef<ASTCondBlock> first_cond = first.try_cast<ASTCondBlock>();
    if (first_cond == nullptr)
        return false;

    auto scan = std::next(it);
    if (scan == lines.end())
        return false;

    PycRef<ASTNode> merged = condition_with_negation(first_cond);
    auto body_it = lines.end();
    while (scan != lines.end()) {
        PycRef<ASTBlock> next = (*scan).try_cast<ASTBlock>();
        if (next == nullptr || next->blktype() != ASTBlock::BLK_ELIF)
            break;

        PycRef<ASTCondBlock> next_cond = next.try_cast<ASTCondBlock>();
        if (next_cond == nullptr)
            break;

        merged = new ASTBinary(merged, condition_with_negation(next_cond), ASTBinary::BIN_LOG_AND);
        if (!block_is_effectively_empty(next)) {
            body_it = scan;
            break;
        }
        ++scan;
    }

    if (body_it == lines.end())
        return false;

    pyc_output << first->type_str() << " ";
    print_src(merged, mod, pyc_output);
    pyc_output << ":\n";

    cur_indent++;
    print_block((*body_it).cast<ASTBlock>(), mod, pyc_output);
    cur_indent--;

    it = body_it;
    return true;
}

static bool is_terminal_statement(const PycRef<ASTNode>& node)
{
    if (node == nullptr)
        return false;

    if (node->type() == ASTNode::NODE_RETURN)
        return true;

    if (node->type() == ASTNode::NODE_KEYWORD) {
        ASTKeyword::Word key = node.cast<ASTKeyword>()->key();
        return key == ASTKeyword::KW_BREAK || key == ASTKeyword::KW_CONTINUE;
    }

    return false;
}

static void rewrite_lambda_blocks(PycRef<ASTNodeList> clean)
{
    if (clean == nullptr || clean->nodes().size() != 2)
        return;

    PycRef<ASTBlock> first = clean->nodes().front().try_cast<ASTBlock>();
    PycRef<ASTReturn> tail = clean->nodes().back().try_cast<ASTReturn>();
    if (first == nullptr || tail == nullptr)
        return;

    if (first->blktype() != ASTBlock::BLK_IF && first->blktype() != ASTBlock::BLK_ELIF)
        return;

    PycRef<ASTCondBlock> cond = first.try_cast<ASTCondBlock>();
    if (cond == nullptr || cond->cond() == nullptr)
        return;

    PycRef<ASTNode> expr;
    if (first->size() == 0) {
        expr = new ASTBinary(cond->cond(), tail->value(),
            cond->negative() ? ASTBinary::BIN_LOG_OR : ASTBinary::BIN_LOG_AND);
    } else if (first->size() == 1) {
        PycRef<ASTReturn> if_ret = first->nodes().front().try_cast<ASTReturn>();
        if (if_ret == nullptr)
            return;
        expr = new ASTTernary(first.cast<ASTNode>(), if_ret->value(), tail->value());
    } else {
        return;
    }

    while (clean->nodes().size() > 0)
        clean->removeFirst();
    clean->append(new ASTReturn(expr));
}

static void print_block_lines(const ASTBlock::list_t& lines, PycModule* mod,
                              std::ostream& pyc_output, bool emit_pass_if_empty = true)
{
    if (lines.empty()) {
        if (!emit_pass_if_empty)
            return;
        PycRef<ASTNode> pass = new ASTKeyword(ASTKeyword::KW_PASS);
        start_line(cur_indent, pyc_output);
        print_src(pass, mod, pyc_output);
        return;
    }

    for (auto ln = lines.cbegin(); ln != lines.cend();) {
        if ((*ln).type() != ASTNode::NODE_NODELIST)
            start_line(cur_indent, pyc_output);
        if (!try_print_collapsed_compare_chain(ln, lines, mod, pyc_output))
            print_src(*ln, mod, pyc_output);
        if (is_terminal_statement(*ln))
            break;
        if (++ln != lines.end())
            end_line(pyc_output);
    }
}

static void print_block(PycRef<ASTBlock> blk, PycModule* mod,
                        std::ostream& pyc_output)
{
    ASTBlock::list_t lines = blk->blktype() == ASTBlock::BLK_EXCEPT
        ? normalize_except_block(blk).lines
        : blk->nodes();

    if (blk->blktype() == ASTBlock::BLK_EXCEPT) {
        auto nested_except = lines.end();
        for (auto it = lines.begin(); it != lines.end(); ++it) {
            PycRef<ASTBlock> child = (*it).try_cast<ASTBlock>();
            if (child != nullptr && child->blktype() == ASTBlock::BLK_EXCEPT) {
                nested_except = it;
                break;
            }
        }

        if (nested_except != lines.end() && nested_except != lines.begin()) {
            ASTBlock::list_t try_lines(lines.begin(), nested_except);
            auto scan = nested_except;
            while (scan != lines.end()) {
                PycRef<ASTBlock> child = (*scan).try_cast<ASTBlock>();
                if (child == nullptr || child->blktype() != ASTBlock::BLK_EXCEPT)
                    break;
                ++scan;
            }
            ASTBlock::list_t tail_lines(scan, lines.end());

            start_line(cur_indent, pyc_output);
            pyc_output << "try:\n";
            cur_indent++;
            print_block_lines(try_lines, mod, pyc_output, true);
            cur_indent--;

            for (auto it = nested_except; it != scan; ++it) {
                end_line(pyc_output);
                start_line(cur_indent, pyc_output);
                print_src(*it, mod, pyc_output);
            }

            if (!tail_lines.empty()) {
                end_line(pyc_output);
                print_block_lines(tail_lines, mod, pyc_output, true);
            }
            return;
        }
    }

    if (blk->blktype() == ASTBlock::BLK_CONTAINER && !lines.empty()) {
        PycRef<ASTBlock> tryblk = lines.front().try_cast<ASTBlock>();
        PycRef<ASTContainerBlock> contblk = blk.try_cast<ASTContainerBlock>();
        bool direct_cleanup = false;
        bool nested_try_after_first = false;
        bool has_handler = false;
        for (auto it = std::next(lines.begin()); it != lines.end(); ++it) {
            if ((*it) != nullptr && ((*it)->type() == ASTNode::NODE_STORE || (*it)->type() == ASTNode::NODE_DELETE))
                direct_cleanup = true;
            PycRef<ASTBlock> child = (*it).try_cast<ASTBlock>();
            if (child != nullptr) {
                if (child->blktype() == ASTBlock::BLK_EXCEPT || child->blktype() == ASTBlock::BLK_FINALLY)
                    has_handler = true;
                else if (child->blktype() == ASTBlock::BLK_TRY)
                    nested_try_after_first = true;
            }
        }

        if (tryblk != nullptr && tryblk->blktype() == ASTBlock::BLK_TRY
                && !has_handler && lines.size() >= 2
                && ((contblk != nullptr && contblk->hasExcept()) || nested_try_after_first)) {
            ASTBlock::list_t except_lines(std::next(lines.begin()), lines.end());
            while (!except_lines.empty()
                    && (is_synthetic_except_marker(except_lines.front())
                        || is_none_like_node(except_lines.front()))) {
                except_lines.pop_front();
            }

            start_line(cur_indent, pyc_output);
            print_src(tryblk.cast<ASTNode>(), mod, pyc_output);
            end_line(pyc_output);
            start_line(cur_indent, pyc_output);
            pyc_output << "except:\n";
            cur_indent++;
            print_block_lines(except_lines, mod, pyc_output, true);
            cur_indent--;
            return;
        }

        if (tryblk != nullptr && tryblk->blktype() == ASTBlock::BLK_TRY
                && lines.size() >= 2) {
            auto marker = std::next(lines.begin());
            if (is_synthetic_except_marker(*marker)) {
                ASTBlock::list_t except_lines(std::next(marker), lines.end());
                while (!except_lines.empty() && is_synthetic_except_marker(except_lines.front()))
                    except_lines.pop_front();

                start_line(cur_indent, pyc_output);
                print_src(tryblk.cast<ASTNode>(), mod, pyc_output);
                end_line(pyc_output);
                start_line(cur_indent, pyc_output);
                pyc_output << "except:\n";
                cur_indent++;
                print_block_lines(except_lines, mod, pyc_output, true);
                cur_indent--;
                return;
            }
        }

        if (tryblk != nullptr && tryblk->blktype() == ASTBlock::BLK_TRY
                && has_handler && nested_try_after_first && !direct_cleanup) {
            ASTBlock::list_t except_lines(std::next(lines.begin()), lines.end());

            start_line(cur_indent, pyc_output);
            print_src(tryblk.cast<ASTNode>(), mod, pyc_output);
            end_line(pyc_output);
            start_line(cur_indent, pyc_output);
            pyc_output << "except:\n";
            cur_indent++;
            print_block_lines(except_lines, mod, pyc_output, true);
            cur_indent--;
            return;
        }

        if (tryblk != nullptr && tryblk->blktype() == ASTBlock::BLK_TRY
                && has_handler && !direct_cleanup && !nested_try_after_first) {
            ASTBlock::list_t excepts;
            ASTBlock::list_t finals;
            ASTBlock::list_t else_lines;

            for (auto it = std::next(lines.begin()); it != lines.end(); ++it) {
                PycRef<ASTBlock> child = (*it).try_cast<ASTBlock>();
                if (child != nullptr && child->blktype() == ASTBlock::BLK_EXCEPT) {
                    excepts.push_back(*it);
                } else if (child != nullptr && child->blktype() == ASTBlock::BLK_FINALLY) {
                    finals.push_back(*it);
                } else if (child != nullptr && child->blktype() == ASTBlock::BLK_ELSE) {
                    if (child->size() == 0)
                        continue;
                    for (const auto& else_line : child->nodes())
                        else_lines.push_back(else_line);
                } else {
                    else_lines.push_back(*it);
                }
            }

            start_line(cur_indent, pyc_output);
            print_src(tryblk.cast<ASTNode>(), mod, pyc_output);

            for (auto it = excepts.begin(); it != excepts.end(); ++it) {
                PycRef<ASTBlock> exblk = (*it).try_cast<ASTBlock>();
                PycRef<ASTCondBlock> excond = exblk.try_cast<ASTCondBlock>();
                if (excond != nullptr && excond->cond() == nullptr && std::next(it) != excepts.end()) {
                    ASTBlock::list_t ex_lines = normalize_except_block(exblk).lines;
                    if (ex_lines.size() == 1) {
                        PycRef<ASTNode> only = ex_lines.front();
                        PycRef<ASTReturn> ret = only.try_cast<ASTReturn>();
                        if (ret != nullptr && ret->rettype() == ASTReturn::RETURN && ret->value() == nullptr) {
                            PycRef<ASTBlock> nextblk = (*std::next(it)).try_cast<ASTBlock>();
                            PycRef<ASTCondBlock> nextcond = nextblk.try_cast<ASTCondBlock>();
                            if (nextcond != nullptr && nextcond->cond() == nullptr)
                                continue;
                        }
                    }
                }
                end_line(pyc_output);
                start_line(cur_indent, pyc_output);
                print_src(*it, mod, pyc_output);
            }

            if (!else_lines.empty()) {
                end_line(pyc_output);
                start_line(cur_indent, pyc_output);
                pyc_output << "else:\n";
                cur_indent++;
                print_block_lines(else_lines, mod, pyc_output, true);
                cur_indent--;
            }

            for (const auto& fin : finals) {
                end_line(pyc_output);
                start_line(cur_indent, pyc_output);
                print_src(fin, mod, pyc_output);
            }
            return;
        }

        if (tryblk != nullptr && tryblk->blktype() == ASTBlock::BLK_TRY
                && !has_handler && lines.size() >= 3) {
            auto it = std::next(lines.begin());
            PycRef<ASTNode> maybe_name = *it++;
            if (maybe_name != nullptr && maybe_name->type() == ASTNode::NODE_NAME && it != lines.end()) {
                PycRef<ASTReturn> except_ret = (*it).try_cast<ASTReturn>();
                if (except_ret != nullptr) {
                    ASTBlock::list_t tail_lines(std::next(it), lines.end());
                    start_line(cur_indent, pyc_output);
                    print_src(tryblk.cast<ASTNode>(), mod, pyc_output);
                    end_line(pyc_output);
                    start_line(cur_indent, pyc_output);
                    pyc_output << "except:\n";
                    cur_indent++;
                    ASTBlock::list_t except_lines;
                    except_lines.push_back(except_ret.cast<ASTNode>());
                    print_block_lines(except_lines, mod, pyc_output, true);
                    cur_indent--;
                    if (!tail_lines.empty()) {
                        end_line(pyc_output);
                        print_block_lines(tail_lines, mod, pyc_output, true);
                    }
                    return;
                }
            }
        }

    }

    print_block_lines(lines, mod, pyc_output, true);
}

void print_formatted_value(PycRef<ASTFormattedValue> formatted_value, PycModule* mod,
                           std::ostream& pyc_output)
{
    pyc_output << "{";
    print_src(formatted_value->val(), mod, pyc_output);

    switch (formatted_value->conversion() & ASTFormattedValue::CONVERSION_MASK) {
    case ASTFormattedValue::NONE:
        break;
    case ASTFormattedValue::STR:
        pyc_output << "!s";
        break;
    case ASTFormattedValue::REPR:
        pyc_output << "!r";
        break;
    case ASTFormattedValue::ASCII:
        pyc_output << "!a";
        break;
    }
    if (formatted_value->conversion() & ASTFormattedValue::HAVE_FMT_SPEC) {
        pyc_output << ":" << formatted_value->format_spec().cast<ASTObject>()->object().cast<PycString>()->value();
    }
    pyc_output << "}";
}

static std::unordered_set<ASTNode *> node_seen;
static std::vector<std::pair<std::string, PycRef<ASTNode>>> name_substitutions;

static bool is_inline_comprehension_name(const PycRef<PycString>& name)
{
    if (name == nullptr)
        return false;

    const char* value = name->value();
    return strcmp(value, "<listcomp>") == 0
        || strcmp(value, "<setcomp>") == 0
        || strcmp(value, "<dictcomp>") == 0
        || strcmp(value, "<genexpr>") == 0;
}

static bool try_print_inline_comprehension_call(PycRef<ASTCall> call, PycModule* mod,
                                                std::ostream& pyc_output)
{
    if (call == nullptr || call->func().type() != ASTNode::NODE_FUNCTION
            || !call->kwparams().empty() || call->hasVar() || call->hasKW()
            || call->pparams().empty()) {
        return false;
    }

    PycRef<ASTFunction> func = call->func().cast<ASTFunction>();
    if (func->code().type() != ASTNode::NODE_OBJECT)
        return false;

    PycRef<PycObject> obj = func->code().cast<ASTObject>()->object();
    if (obj.type() != PycObject::TYPE_CODE)
        return false;

    PycRef<PycCode> code = obj.cast<PycCode>();
    if (!is_inline_comprehension_name(code->name()) || code->argCount() < 1)
        return false;

    name_substitutions.emplace_back(code->getLocal(0)->value(), call->pparams().front());
    inLambda = true;
    print_src(func->code(), mod, pyc_output);
    inLambda = false;
    name_substitutions.pop_back();
    return true;
}

static bool extract_decorated_class(
        const PycRef<ASTNode>& node,
        PycRef<ASTClass>& klass,
        std::list<PycRef<ASTNode>>& decorators)
{
    if (node == nullptr)
        return false;

    PycRef<ASTClass> direct_class = node.try_cast<ASTClass>();
    if (direct_class != nullptr) {
        klass = direct_class;
        return true;
    }

    PycRef<ASTCall> call = node.try_cast<ASTCall>();
    if (call == nullptr || call->hasVar() || call->hasKW()
            || !call->kwparams().empty() || call->pparams().size() != 1) {
        return false;
    }

    if (!extract_decorated_class(call->pparams().front(), klass, decorators))
        return false;

    decorators.push_front(call->func());
    return true;
}

static void print_class_definition(
        const PycRef<ASTNode>& dest,
        const PycRef<ASTClass>& klass,
        const std::list<PycRef<ASTNode>>& decorators,
        PycModule* mod,
        std::ostream& pyc_output)
{
    for (const auto& decorator : decorators) {
        pyc_output << "\n";
        start_line(cur_indent, pyc_output);
        pyc_output << "@";
        print_src(decorator, mod, pyc_output);
    }

    pyc_output << "\n";
    start_line(cur_indent, pyc_output);
    pyc_output << "class ";
    print_src(dest, mod, pyc_output);

    PycRef<ASTTuple> bases = klass->bases().cast<ASTTuple>();
    const auto& keywords = klass->kwparams();
    if (!bases->values().empty() || !keywords.empty()) {
        pyc_output << "(";
        bool first = true;
        for (const auto& val : bases->values()) {
            if (!first)
                pyc_output << ", ";
            print_src(val, mod, pyc_output);
            first = false;
        }
        for (const auto& kw : keywords) {
            if (!first)
                pyc_output << ", ";
            if (kw.first.type() == ASTNode::NODE_NAME) {
                pyc_output << kw.first.cast<ASTName>()->name()->value();
            } else {
                pyc_output << kw.first.cast<ASTObject>()->object().cast<PycString>()->value();
            }
            pyc_output << " = ";
            print_src(kw.second, mod, pyc_output);
            first = false;
        }
        pyc_output << "):\n";
    } else {
        pyc_output << ":\n";
    }

    printClassDocstring = true;
    PycRef<ASTNode> code = klass->code().cast<ASTCall>()->func().cast<ASTFunction>()->code();
    print_src(code, mod, pyc_output);
}

void print_src(PycRef<ASTNode> node, PycModule* mod, std::ostream& pyc_output)
{
    if (node == NULL) {
        pyc_output << "None";
        cleanBuild = true;
        return;
    }

    if (node_seen.find((ASTNode *)node) != node_seen.end()) {
        fputs("WARNING: Circular reference detected\n", stderr);
        return;
    }
    node_seen.insert((ASTNode *)node);

    switch (node->type()) {
    case ASTNode::NODE_BINARY:
    case ASTNode::NODE_COMPARE:
        {
            PycRef<ASTBinary> bin = node.cast<ASTBinary>();
            if (bin->op() == ASTBinary::BIN_ATTR && needs_attr_parens(bin->left())) {
                pyc_output << "(";
                print_src(bin->left(), mod, pyc_output);
                pyc_output << ")";
            } else {
                print_ordered(node, bin->left(), mod, pyc_output);
            }
            pyc_output << bin->op_str();
            print_ordered(node, bin->right(), mod, pyc_output);
        }
        break;
    case ASTNode::NODE_UNARY:
        {
            PycRef<ASTUnary> un = node.cast<ASTUnary>();
            pyc_output << un->op_str();
            print_ordered(node, un->operand(), mod, pyc_output);
        }
        break;
    case ASTNode::NODE_CALL:
        {
            PycRef<ASTCall> call = node.cast<ASTCall>();
            if (try_print_inline_comprehension_call(call, mod, pyc_output))
                break;
            print_src(call->func(), mod, pyc_output);
            pyc_output << "(";
            bool first = true;
            for (const auto& param : call->pparams()) {
                if (!first)
                    pyc_output << ", ";
                print_src(param, mod, pyc_output);
                first = false;
            }
            for (const auto& param : call->kwparams()) {
                if (!first)
                    pyc_output << ", ";
                if (param.first.type() == ASTNode::NODE_NAME) {
                    pyc_output << param.first.cast<ASTName>()->name()->value() << " = ";
                } else {
                    PycRef<PycString> str_name = param.first.cast<ASTObject>()->object().cast<PycString>();
                    pyc_output << str_name->value() << " = ";
                }
                print_src(param.second, mod, pyc_output);
                first = false;
            }
            if (call->hasVar()) {
                if (!first)
                    pyc_output << ", ";
                pyc_output << "*";
                print_src(call->var(), mod, pyc_output);
                first = false;
            }
            if (call->hasKW()) {
                if (!first)
                    pyc_output << ", ";
                pyc_output << "**";
                print_src(call->kw(), mod, pyc_output);
                first = false;
            }
            pyc_output << ")";
        }
        break;
    case ASTNode::NODE_DELETE:
        {
            pyc_output << "del ";
            print_src(node.cast<ASTDelete>()->value(), mod, pyc_output);
        }
        break;
    case ASTNode::NODE_EXEC:
        {
            PycRef<ASTExec> exec = node.cast<ASTExec>();
            pyc_output << "exec ";
            print_src(exec->statement(), mod, pyc_output);

            if (exec->globals() != NULL) {
                pyc_output << " in ";
                print_src(exec->globals(), mod, pyc_output);

                if (exec->locals() != NULL
                        && exec->globals() != exec->locals()) {
                    pyc_output << ", ";
                    print_src(exec->locals(), mod, pyc_output);
                }
            }
        }
        break;
    case ASTNode::NODE_FORMATTEDVALUE:
        pyc_output << "f" F_STRING_QUOTE;
        print_formatted_value(node.cast<ASTFormattedValue>(), mod, pyc_output);
        pyc_output << F_STRING_QUOTE;
        break;
    case ASTNode::NODE_JOINEDSTR:
        pyc_output << "f" F_STRING_QUOTE;
        for (const auto& val : node.cast<ASTJoinedStr>()->values()) {
            switch (val.type()) {
            case ASTNode::NODE_FORMATTEDVALUE:
                print_formatted_value(val.cast<ASTFormattedValue>(), mod, pyc_output);
                break;
            case ASTNode::NODE_OBJECT:
                // When printing a piece of the f-string, keep the quote style consistent.
                // This avoids problems when ''' or """ is part of the string.
                print_const(pyc_output, val.cast<ASTObject>()->object(), mod, F_STRING_QUOTE);
                break;
            default:
                fprintf(stderr, "Unsupported node type %d in NODE_JOINEDSTR\n", val.type());
            }
        }
        pyc_output << F_STRING_QUOTE;
        break;
    case ASTNode::NODE_KEYWORD:
        pyc_output << node.cast<ASTKeyword>()->word_str();
        break;
    case ASTNode::NODE_LIST:
        {
            pyc_output << "[";
            bool first = true;
            cur_indent++;
            for (const auto& val : node.cast<ASTList>()->values()) {
                if (first)
                    pyc_output << "\n";
                else
                    pyc_output << ",\n";
                start_line(cur_indent, pyc_output);
                print_src(val, mod, pyc_output);
                first = false;
            }
            cur_indent--;
            pyc_output << "]";
        }
        break;
    case ASTNode::NODE_SET:
        {
            pyc_output << "{";
            bool first = true;
            cur_indent++;
            for (const auto& val : node.cast<ASTSet>()->values()) {
                if (first)
                    pyc_output << "\n";
                else
                    pyc_output << ",\n";
                start_line(cur_indent, pyc_output);
                print_src(val, mod, pyc_output);
                first = false;
            }
            cur_indent--;
            pyc_output << "}";
        }
        break;
    case ASTNode::NODE_STARRED:
        pyc_output << "*";
        print_src(node.cast<ASTStarred>()->value(), mod, pyc_output);
        break;
    case ASTNode::NODE_COMPREHENSION:
        {
            PycRef<ASTComprehension> comp = node.cast<ASTComprehension>();
            PycRef<ASTNode> result = comp->result();
            bool is_set = false;
            bool is_dict = false;

            if (!comp->isGenerator() && result != nullptr) {
                PycRef<ASTSet> set = result.try_cast<ASTSet>();
                if (set != nullptr && set->values().size() == 1) {
                    is_set = true;
                    pyc_output << "{ ";
                    print_src(set->values().front(), mod, pyc_output);
                } else {
                    PycRef<ASTMap> map = result.try_cast<ASTMap>();
                    if (map != nullptr && map->values().size() == 1
                            && map->values().front().first != nullptr) {
                        is_dict = true;
                        pyc_output << "{ ";
                        print_src(map->values().front().first, mod, pyc_output);
                        pyc_output << ": ";
                        print_src(map->values().front().second, mod, pyc_output);
                    }
                }
            }

            if (!is_set && !is_dict) {
                pyc_output << (comp->isGenerator() ? "(" : "[ ");
                print_src(result, mod, pyc_output);
            }

            for (const auto& gen : comp->generators()) {
                pyc_output << " for ";
                print_src(gen->index(), mod, pyc_output);
                pyc_output << " in ";
                print_src(gen->iter(), mod, pyc_output);
                if (gen->condition()) {
                    pyc_output << " if ";
                    print_src(gen->condition(), mod, pyc_output);
                }
            }
            if (comp->isGenerator())
                pyc_output << ")";
            else if (is_set || is_dict)
                pyc_output << " }";
            else
                pyc_output << " ]";
        }
        break;
    case ASTNode::NODE_MAP:
        {
            pyc_output << "{";
            bool first = true;
            cur_indent++;
            for (const auto& val : node.cast<ASTMap>()->values()) {
                if (first)
                    pyc_output << "\n";
                else
                    pyc_output << ",\n";
                start_line(cur_indent, pyc_output);
                if (val.first == nullptr) {
                    pyc_output << "**";
                    print_src(val.second, mod, pyc_output);
                } else {
                    print_src(val.first, mod, pyc_output);
                    pyc_output << ": ";
                    print_src(val.second, mod, pyc_output);
                }
                first = false;
            }
            cur_indent--;
            pyc_output << " }";
        }
        break;
    case ASTNode::NODE_CONST_MAP:
        {
            PycRef<ASTConstMap> const_map = node.cast<ASTConstMap>();
            PycTuple::value_t keys = const_map->keys().cast<ASTObject>()->object().cast<PycTuple>()->values();
            ASTConstMap::values_t values = const_map->values();

            auto map = new ASTMap;
            for (const auto& key : keys) {
                // Values are pushed onto the stack in reverse order.
                PycRef<ASTNode> value = values.back();
                values.pop_back();

                map->add(new ASTObject(key), value);
            }

            print_src(map, mod, pyc_output);
        }
        break;
    case ASTNode::NODE_LOADBUILDCLASS:
        pyc_output << "__build_class__";
        break;
    case ASTNode::NODE_NAME:
        {
            const char* name = node.cast<ASTName>()->name()->value();
            bool substituted = false;
            for (auto it = name_substitutions.rbegin(); it != name_substitutions.rend(); ++it) {
                if (it->first == name) {
                    print_src(it->second, mod, pyc_output);
                    substituted = true;
                    break;
                }
            }
            if (!substituted)
                pyc_output << name;
        }
        break;
    case ASTNode::NODE_NODELIST:
        {
            cur_indent++;
            const auto& lines = node.cast<ASTNodeList>()->nodes();
            for (auto ln = lines.cbegin(); ln != lines.cend();) {
                if ((*ln).type() != ASTNode::NODE_NODELIST) {
                    start_line(cur_indent, pyc_output);
                }
                if (!try_print_collapsed_compare_chain(ln, lines, mod, pyc_output))
                    print_src(*ln, mod, pyc_output);
                end_line(pyc_output);
                if (is_terminal_statement(*ln))
                    break;
                ++ln;
            }
            cur_indent--;
        }
        break;
    case ASTNode::NODE_BLOCK:
        {
            PycRef<ASTBlock> blk = node.cast<ASTBlock>();
            if (blk->blktype() == ASTBlock::BLK_ELSE && blk->size() == 0)
                break;

            if (blk->blktype() == ASTBlock::BLK_CONTAINER
                    || blk->blktype() == ASTBlock::BLK_MAIN) {
                end_line(pyc_output);
                print_block(blk, mod, pyc_output);
                end_line(pyc_output);
                break;
            }

            pyc_output << blk->type_str();
            if (blk->blktype() == ASTBlock::BLK_IF
                    || blk->blktype() == ASTBlock::BLK_ELIF
                    || blk->blktype() == ASTBlock::BLK_WHILE) {
                PycRef<ASTNode> cond = blk.cast<ASTCondBlock>()->cond();
                if (blk->blktype() == ASTBlock::BLK_WHILE && cond == nullptr) {
                    pyc_output << " True";
                } else {
                    if (blk.cast<ASTCondBlock>()->negative())
                        pyc_output << " not ";
                    else
                        pyc_output << " ";

                    print_src(cond, mod, pyc_output);
                }
            } else if (blk->blktype() == ASTBlock::BLK_FOR || blk->blktype() == ASTBlock::BLK_ASYNCFOR) {
                pyc_output << " ";
                print_src(blk.cast<ASTIterBlock>()->index(), mod, pyc_output);
                pyc_output << " in ";
                print_src(blk.cast<ASTIterBlock>()->iter(), mod, pyc_output);
            } else if (blk->blktype() == ASTBlock::BLK_EXCEPT &&
                    blk.cast<ASTCondBlock>()->cond() != NULL) {
                pyc_output << " ";
                print_src(blk.cast<ASTCondBlock>()->cond(), mod, pyc_output);
                PycRef<ASTName> alias = normalize_except_block(blk).alias;
                if (alias != nullptr) {
                    pyc_output << " as ";
                    print_src(alias.cast<ASTNode>(), mod, pyc_output);
                }
            } else if (blk->blktype() == ASTBlock::BLK_WITH) {
                pyc_output << " ";
                print_src(blk.cast<ASTWithBlock>()->expr(), mod, pyc_output);
                PycRef<ASTNode> var = blk.try_cast<ASTWithBlock>()->var();
                if (var != NULL) {
                    pyc_output << " as ";
                    print_src(var, mod, pyc_output);
                }
            }
            pyc_output << ":\n";

            cur_indent++;
            print_block(blk, mod, pyc_output);
            cur_indent--;
        }
        break;
    case ASTNode::NODE_OBJECT:
        {
            PycRef<PycObject> obj = node.cast<ASTObject>()->object();
            if (obj.type() == PycObject::TYPE_CODE) {
                PycRef<PycCode> code = obj.cast<PycCode>();
                decompyle(code, mod, pyc_output);
            } else {
                print_const(pyc_output, obj, mod);
            }
        }
        break;
    case ASTNode::NODE_PRINT:
        {
            pyc_output << "print ";
            bool first = true;
            if (node.cast<ASTPrint>()->stream() != nullptr) {
                pyc_output << ">>";
                print_src(node.cast<ASTPrint>()->stream(), mod, pyc_output);
                first = false;
            }

            for (const auto& val : node.cast<ASTPrint>()->values()) {
                if (!first)
                    pyc_output << ", ";
                print_src(val, mod, pyc_output);
                first = false;
            }
            if (!node.cast<ASTPrint>()->eol())
                pyc_output << ",";
        }
        break;
    case ASTNode::NODE_RAISE:
        {
            PycRef<ASTRaise> raise = node.cast<ASTRaise>();
            pyc_output << "raise";
            const auto& params = raise->params();
            if (!params.empty()) {
                pyc_output << " ";
                if (mod->verCompare(3, 0) >= 0 && params.size() == 2) {
                    auto it = params.cbegin();
                    print_src(*it++, mod, pyc_output);
                    pyc_output << " from ";
                    print_src(*it, mod, pyc_output);
                } else {
                    bool first = true;
                    for (const auto& param : params) {
                        if (!first)
                            pyc_output << ", ";
                        print_src(param, mod, pyc_output);
                        first = false;
                    }
                }
            }
        }
        break;
    case ASTNode::NODE_RETURN:
        {
            PycRef<ASTReturn> ret = node.cast<ASTReturn>();
            PycRef<ASTNode> value = ret->value();
            if (!inLambda) {
                switch (ret->rettype()) {
                case ASTReturn::RETURN:
                    pyc_output << "return ";
                    break;
                case ASTReturn::YIELD:
                    pyc_output << "yield ";
                    break;
                case ASTReturn::YIELD_FROM:
                    if (value.type() == ASTNode::NODE_AWAITABLE) {
                        pyc_output << "await ";
                        value = value.cast<ASTAwaitable>()->expression();
                    } else {
                        pyc_output << "yield from ";
                    }
                    break;
                }
            }
            print_src(value, mod, pyc_output);
        }
        break;
    case ASTNode::NODE_SLICE:
        {
            PycRef<ASTSlice> slice = node.cast<ASTSlice>();

            if (slice->op() & ASTSlice::SLICE1) {
                print_src(slice->left(), mod, pyc_output);
            }
            pyc_output << ":";
            if (slice->op() & ASTSlice::SLICE2) {
                print_src(slice->right(), mod, pyc_output);
            }
        }
        break;
    case ASTNode::NODE_IMPORT:
        {
            PycRef<ASTImport> import = node.cast<ASTImport>();
            if (import->stores().size()) {
                ASTImport::list_t stores = import->stores();
                bool has_module_name = true;

                pyc_output << "from ";
                for (int i = 0; i < import->level(); ++i)
                    pyc_output << ".";
                if (import->name().type() == ASTNode::NODE_IMPORT) {
                    print_src(import->name().cast<ASTImport>()->name(), mod, pyc_output);
                } else {
                    if (import->name().type() == ASTNode::NODE_NAME
                            && strlen(import->name().cast<ASTName>()->name()->value()) == 0) {
                        has_module_name = false;
                    }
                    if (has_module_name) {
                        print_src(import->name(), mod, pyc_output);
                    }
                }
                if (!has_module_name && import->level() == 0) {
                    print_src(import->name(), mod, pyc_output);
                }
                pyc_output << " import ";

                if (stores.size() == 1) {
                    auto src = stores.front()->src();
                    auto dest = stores.front()->dest();
                    print_src(src, mod, pyc_output);

                    if (src.cast<ASTName>()->name()->value() != dest.cast<ASTName>()->name()->value()) {
                        pyc_output << " as ";
                        print_src(dest, mod, pyc_output);
                    }
                } else {
                    bool first = true;
                    for (const auto& st : stores) {
                        if (!first)
                            pyc_output << ", ";
                        print_src(st->src(), mod, pyc_output);
                        first = false;

                        if (st->src().cast<ASTName>()->name()->value() != st->dest().cast<ASTName>()->name()->value()) {
                            pyc_output << " as ";
                            print_src(st->dest(), mod, pyc_output);
                        }
                    }
                }
            } else {
                pyc_output << "import ";
                print_src(import->name(), mod, pyc_output);
            }
        }
        break;
    case ASTNode::NODE_FUNCTION:
        {
            /* Actual named functions are NODE_STORE with a name */
            pyc_output << "(lambda ";
            PycRef<ASTNode> code = node.cast<ASTFunction>()->code();
            PycRef<PycCode> code_src = code.cast<ASTObject>()->object().cast<PycCode>();
            ASTFunction::defarg_t defargs = node.cast<ASTFunction>()->defargs();
            ASTFunction::defarg_t kwdefargs = node.cast<ASTFunction>()->kwdefargs();
            auto da = defargs.cbegin();
            int narg = 0;
            for (int i=0; i<code_src->argCount(); i++) {
                if (narg)
                    pyc_output << ", ";
                pyc_output << code_src->getLocal(narg++)->value();
                if ((code_src->argCount() - i) <= (int)defargs.size()) {
                    pyc_output << " = ";
                    print_src(*da++, mod, pyc_output);
                }
            }
            int kwonly_start = code_src->argCount();
            int vararg_index = code_src->argCount() + code_src->kwOnlyArgCount();
            int varkw_index = vararg_index + ((code_src->flags() & PycCode::CO_VARARGS) ? 1 : 0);
            if (code_src->flags() & PycCode::CO_VARARGS) {
                if (narg)
                    pyc_output << ", ";
                pyc_output << "*" << code_src->getLocal(vararg_index)->value();
                narg++;
            } else if (code_src->kwOnlyArgCount() != 0) {
                pyc_output << (narg == 0 ? "*" : ", *");
            }
            da = kwdefargs.cbegin();
            if (code_src->kwOnlyArgCount() != 0) {
                for (int i = 0; i < code_src->kwOnlyArgCount(); i++) {
                    pyc_output << ", ";
                    pyc_output << code_src->getLocal(kwonly_start + i)->value();
                    narg++;
                    if ((code_src->kwOnlyArgCount() - i) <= (int)kwdefargs.size()) {
                        pyc_output << " = ";
                        print_src(*da++, mod, pyc_output);
                    }
                }
            }
            if (code_src->flags() & PycCode::CO_VARKEYWORDS) {
                if (narg)
                    pyc_output << ", ";
                pyc_output << "**" << code_src->getLocal(varkw_index)->value();
            }
            pyc_output << ": ";

            inLambda = true;
            print_src(code, mod, pyc_output);
            inLambda = false;

            pyc_output << ")";
        }
        break;
    case ASTNode::NODE_STORE:
        {
            PycRef<ASTNode> src = node.cast<ASTStore>()->src();
            PycRef<ASTNode> dest = node.cast<ASTStore>()->dest();
            PycRef<ASTClass> klass;
            std::list<PycRef<ASTNode>> decorators;
            if (extract_decorated_class(src, klass, decorators)) {
                print_class_definition(dest, klass, decorators, mod, pyc_output);
            } else if (src.type() == ASTNode::NODE_FUNCTION) {
                PycRef<ASTNode> code = src.cast<ASTFunction>()->code();
                PycRef<PycCode> code_src = code.cast<ASTObject>()->object().cast<PycCode>();
                bool isLambda = false;

                if (strcmp(code_src->name()->value(), "<lambda>") == 0) {
                    pyc_output << "\n";
                    start_line(cur_indent, pyc_output);
                    print_src(dest, mod, pyc_output);
                    pyc_output << " = lambda ";
                    isLambda = true;
                } else {
                    pyc_output << "\n";
                    start_line(cur_indent, pyc_output);
                    if (code_src->flags() & PycCode::CO_COROUTINE)
                        pyc_output << "async ";
                    pyc_output << "def ";
                    print_src(dest, mod, pyc_output);
                    pyc_output << "(";
                }

                ASTFunction::defarg_t defargs = src.cast<ASTFunction>()->defargs();
                ASTFunction::defarg_t kwdefargs = src.cast<ASTFunction>()->kwdefargs();
                auto da = defargs.cbegin();
                int narg = 0;
                for (int i = 0; i < code_src->argCount(); ++i) {
                    if (narg)
                        pyc_output << ", ";
                    pyc_output << code_src->getLocal(narg++)->value();
                    if ((code_src->argCount() - i) <= (int)defargs.size()) {
                        pyc_output << " = ";
                        print_src(*da++, mod, pyc_output);
                    }
                }
                int kwonly_start = code_src->argCount();
                int vararg_index = code_src->argCount() + code_src->kwOnlyArgCount();
                int varkw_index = vararg_index + ((code_src->flags() & PycCode::CO_VARARGS) ? 1 : 0);
                if (code_src->flags() & PycCode::CO_VARARGS) {
                    if (narg)
                        pyc_output << ", ";
                    pyc_output << "*" << code_src->getLocal(vararg_index)->value();
                    narg++;
                } else if (code_src->kwOnlyArgCount() != 0) {
                    pyc_output << (narg == 0 ? "*" : ", *");
                }
                da = kwdefargs.cbegin();
                if (code_src->kwOnlyArgCount() != 0) {
                    for (int i = 0; i < code_src->kwOnlyArgCount(); ++i) {
                        pyc_output << ", ";
                        pyc_output << code_src->getLocal(kwonly_start + i)->value();
                        narg++;
                        if ((code_src->kwOnlyArgCount() - i) <= (int)kwdefargs.size()) {
                            pyc_output << " = ";
                            print_src(*da++, mod, pyc_output);
                        }
                    }
                }
                if (code_src->flags() & PycCode::CO_VARKEYWORDS) {
                    if (narg)
                        pyc_output << ", ";
                    pyc_output << "**" << code_src->getLocal(varkw_index)->value();
                }

                if (isLambda) {
                    pyc_output << ": ";
                } else {
                    pyc_output << "):\n";
                    printDocstringAndGlobals = true;
                }

                bool preLambda = inLambda;
                inLambda |= isLambda;

                print_src(code, mod, pyc_output);

                inLambda = preLambda;
            } else if (src.type() == ASTNode::NODE_IMPORT) {
                PycRef<ASTImport> import = src.cast<ASTImport>();
                if (import->fromlist() != NULL) {
                    PycRef<PycObject> fromlist = import->fromlist().cast<ASTObject>()->object();
                    if (fromlist != Pyc_None) {
                        pyc_output << "from ";
                        if (import->name().type() == ASTNode::NODE_IMPORT)
                            print_src(import->name().cast<ASTImport>()->name(), mod, pyc_output);
                        else
                            print_src(import->name(), mod, pyc_output);
                        pyc_output << " import ";
                        if (fromlist.type() == PycObject::TYPE_TUPLE ||
                                fromlist.type() == PycObject::TYPE_SMALL_TUPLE) {
                            bool first = true;
                            for (const auto& val : fromlist.cast<PycTuple>()->values()) {
                                if (!first)
                                    pyc_output << ", ";
                                pyc_output << val.cast<PycString>()->value();
                                first = false;
                            }
                        } else {
                            pyc_output << fromlist.cast<PycString>()->value();
                        }
                    } else {
                        pyc_output << "import ";
                        print_src(import->name(), mod, pyc_output);
                    }
                } else {
                    pyc_output << "import ";
                    PycRef<ASTNode> import_name = import->name();
                    print_src(import_name, mod, pyc_output);
                    if (!is_default_dotted_import_binding(import, dest)
                            && !dest.cast<ASTName>()->name()->isEqual(import_name.cast<ASTName>()->name().cast<PycObject>())) {
                        pyc_output << " as ";
                        print_src(dest, mod, pyc_output);
                    }
                }
            } else if (src.type() == ASTNode::NODE_BINARY
                    && src.cast<ASTBinary>()->is_inplace()) {
                print_src(src, mod, pyc_output);
            } else {
                print_src(dest, mod, pyc_output);
                pyc_output << " = ";
                print_src(src, mod, pyc_output);
            }
        }
        break;
    case ASTNode::NODE_CHAINSTORE:
        {
            for (auto& dest : node.cast<ASTChainStore>()->nodes()) {
                print_src(dest, mod, pyc_output);
                pyc_output << " = ";
            }
            print_src(node.cast<ASTChainStore>()->src(), mod, pyc_output);
        }
        break;
    case ASTNode::NODE_SUBSCR:
        {
            print_src(node.cast<ASTSubscr>()->name(), mod, pyc_output);
            pyc_output << "[";
            print_src(node.cast<ASTSubscr>()->key(), mod, pyc_output);
            pyc_output << "]";
        }
        break;
    case ASTNode::NODE_CONVERT:
        {
            pyc_output << "`";
            print_src(node.cast<ASTConvert>()->name(), mod, pyc_output);
            pyc_output << "`";
        }
        break;
    case ASTNode::NODE_TUPLE:
        {
            PycRef<ASTTuple> tuple = node.cast<ASTTuple>();
            ASTTuple::value_t values = tuple->values();
            if (tuple->requireParens())
                pyc_output << "(";
            bool first = true;
            for (const auto& val : values) {
                if (!first)
                    pyc_output << ", ";
                print_src(val, mod, pyc_output);
                first = false;
            }
            if (values.size() == 1)
                pyc_output << ',';
            if (tuple->requireParens())
                pyc_output << ')';
        }
        break;
    case ASTNode::NODE_ANNOTATED_VAR:
        {
            PycRef<ASTAnnotatedVar> annotated_var = node.cast<ASTAnnotatedVar>();
            PycRef<ASTObject> name = annotated_var->name().cast<ASTObject>();
            PycRef<ASTNode> annotation = annotated_var->annotation();

            pyc_output << name->object().cast<PycString>()->value();
            pyc_output << ": ";
            print_src(annotation, mod, pyc_output);
        }
        break;
    case ASTNode::NODE_TERNARY:
        {
            /* parenthesis might be needed
             * 
             * when if-expr is part of numerical expression, ternary has the LOWEST precedence
             *     print(a + b if False else c)
             * output is c, not a+c (a+b is calculated first)
             * 
             * but, let's not add parenthesis - to keep the source as close to original as possible in most cases
             */
            PycRef<ASTTernary> ternary = node.cast<ASTTernary>();
            //pyc_output << "(";
            print_src(ternary->if_expr(), mod, pyc_output);
            const auto if_block = ternary->if_block().cast<ASTCondBlock>();
            pyc_output << " if ";
            if (if_block->negative())
                pyc_output << "not ";
            print_src(if_block->cond(), mod, pyc_output);
            pyc_output << " else ";
            print_src(ternary->else_expr(), mod, pyc_output);
            //pyc_output << ")";
        }
        break;
    default:
        pyc_output << "<NODE:" << node->type() << ">";
        fprintf(stderr, "Unsupported Node type: %d\n", node->type());
        cleanBuild = false;
        node_seen.erase((ASTNode *)node);
        return;
    }

    cleanBuild = true;
    node_seen.erase((ASTNode *)node);
}

bool print_docstring(PycRef<PycObject> obj, int indent, PycModule* mod,
                     std::ostream& pyc_output)
{
    // docstrings are translated from the bytecode __doc__ = 'string' to simply '''string'''
    auto doc = obj.try_cast<PycString>();
    if (doc != nullptr) {
        start_line(indent, pyc_output);
        doc->print(pyc_output, mod, true);
        pyc_output << "\n";
        return true;
    }
    return false;
}

static std::unordered_set<PycCode *> code_seen;

static bool is_name_node(const PycRef<ASTNode>& node, const char* name)
{
    return node != nullptr
        && node->type() == ASTNode::NODE_NAME
        && strcmp(node.cast<ASTName>()->name()->value(), name) == 0;
}

static bool is_classcell_cleanup_assignment(const PycRef<ASTNode>& node)
{
    if (node == nullptr)
        return false;

    PycRef<ASTStore> store = node.try_cast<ASTStore>();
    if (store != nullptr) {
        return is_name_node(store->src(), "__class__")
            && is_name_node(store->dest(), "__classcell__");
    }

    PycRef<ASTChainStore> chain = node.try_cast<ASTChainStore>();
    if (chain == nullptr || chain->nodes().size() != 1)
        return false;

    return is_name_node(chain->nodes().front(), "__classcell__")
        && is_name_node(chain->src(), "__class__");
}

static bool is_classcell_cleanup_store(const PycRef<ASTNode>& node)
{
    return is_classcell_cleanup_assignment(node);
}

static bool is_classcell_cleanup_return(const PycRef<ASTNode>& node)
{
    PycRef<ASTReturn> ret = node.try_cast<ASTReturn>();
    if (ret == nullptr)
        return false;

    return is_classcell_cleanup_assignment(ret->value());
}

void decompyle(PycRef<PycCode> code, PycModule* mod, std::ostream& pyc_output)
{
    if (code_seen.find((PycCode *)code) != code_seen.end()) {
        fputs("WARNING: Circular reference detected\n", stderr);
        return;
    }
    code_seen.insert((PycCode *)code);

    PycRef<ASTNode> source = BuildFromCode(code, mod);

    PycRef<ASTNodeList> clean = source.cast<ASTNodeList>();
    if (cleanBuild) {
        // The Python compiler adds some stuff that we don't really care
        // about, and would add extra code for re-compilation anyway.
        // We strip these lines out here, and then add a "pass" statement
        // if the cleaned up code is empty
        if (clean->nodes().front().type() == ASTNode::NODE_STORE) {
            PycRef<ASTStore> store = clean->nodes().front().cast<ASTStore>();
            if (store->src().type() == ASTNode::NODE_NAME
                    && store->dest().type() == ASTNode::NODE_NAME) {
                PycRef<ASTName> src = store->src().cast<ASTName>();
                PycRef<ASTName> dest = store->dest().cast<ASTName>();
                if (src->name()->isEqual("__name__")
                        && dest->name()->isEqual("__module__")) {
                    // __module__ = __name__
                    // Automatically added by Python 2.2.1 and later
                    clean->removeFirst();
                }
            }
        }
        if (clean->nodes().front().type() == ASTNode::NODE_STORE) {
            PycRef<ASTStore> store = clean->nodes().front().cast<ASTStore>();
            if (store->src().type() == ASTNode::NODE_OBJECT
                    && store->dest().type() == ASTNode::NODE_NAME) {
                PycRef<ASTObject> src = store->src().cast<ASTObject>();
                PycRef<PycString> srcString = src->object().try_cast<PycString>();
                PycRef<ASTName> dest = store->dest().cast<ASTName>();
                if (dest->name()->isEqual("__qualname__")) {
                    // __qualname__ = '<Class Name>'
                    // Automatically added by Python 3.3 and later
                    clean->removeFirst();
                }
            }
        }

        // Class and module docstrings may only appear at the beginning of their source
        if (printClassDocstring && clean->nodes().front().type() == ASTNode::NODE_STORE) {
            PycRef<ASTStore> store = clean->nodes().front().cast<ASTStore>();
            if (store->dest().type() == ASTNode::NODE_NAME &&
                    store->dest().cast<ASTName>()->name()->isEqual("__doc__") &&
                    store->src().type() == ASTNode::NODE_OBJECT) {
                if (print_docstring(store->src().cast<ASTObject>()->object(),
                        cur_indent + (code->name()->isEqual("<module>") ? 0 : 1), mod, pyc_output))
                    clean->removeFirst();
            }
        }
        while (clean->nodes().size() > 0) {
            PycRef<ASTNode> last = clean->nodes().back();
            if (is_classcell_cleanup_store(last) || is_classcell_cleanup_return(last)) {
                clean->removeLast();
                continue;
            }

            PycRef<ASTReturn> ret = last.try_cast<ASTReturn>();
            if (ret != nullptr) {
                PycRef<ASTObject> retObj = ret->value().try_cast<ASTObject>();
                if (ret->value() == NULL || ret->value().type() == ASTNode::NODE_LOCALS ||
                        (retObj && retObj->object().type() == PycObject::TYPE_NONE)) {
                    clean->removeLast();  // Always an extraneous return statement
                    continue;
                }
            }
            break;
        }
    }
    if (printClassDocstring)
        printClassDocstring = false;
    // This is outside the clean check so a source block will always
    // be compilable, even if decompylation failed.
    if (code->name() != nullptr && code->name()->isEqual("<lambda>"))
        rewrite_lambda_blocks(clean);
    if (clean->nodes().size() == 0 && !code.isIdent(mod->code())) {
        if (code->name() != nullptr && code->name()->isEqual("<lambda>"))
            clean->append(new ASTObject(Pyc_None));
        else
            clean->append(new ASTKeyword(ASTKeyword::KW_PASS));
    }

    bool part1clean = cleanBuild;

    if (printDocstringAndGlobals) {
        if (code->consts()->size())
            print_docstring(code->getConst(0), cur_indent + 1, mod, pyc_output);

        PycCode::globals_t globs = code->getGlobals();
        if (globs.size()) {
            start_line(cur_indent + 1, pyc_output);
            pyc_output << "global ";
            bool first = true;
            for (const auto& glob : globs) {
                if (!first)
                    pyc_output << ", ";
                pyc_output << glob->value();
                first = false;
            }
            pyc_output << "\n";
        }
        printDocstringAndGlobals = false;
    }

    print_src(source, mod, pyc_output);

    if (!cleanBuild || !part1clean) {
        start_line(cur_indent, pyc_output);
        pyc_output << "# WARNING: Decompyle incomplete\n";
    }

    code_seen.erase((PycCode *)code);
}
