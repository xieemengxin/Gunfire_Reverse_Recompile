# m1logic4 Opcode Review

Date: 2026-03-28

Scope:
- IDB: `reverse_bin/m1logic4.dll.i64`
- Anchors:
  - `_PyEval_EvalFrameDefault` at `0x1800AE0A0`
  - `r_object` at `0x180103420`

## Confirmed From IDA

1. `case 118` is not a normal opcode handler.
   - Entry: `0x1800AE886`
   - Behavior: combines bytes and dispatches based on the next opcode byte.
   - This matches our current `marker/ext` handling in `decode_custom_stream()`.
   - Current map entry `118 -> 144` should be treated as marker semantics, not as an independently emitted decoded opcode.

2. `case 253` is `COMPARE_OP`.
   - Entry: `0x1800AEC4D`
   - Calls `sub_1800B52D0`.
   - `sub_1800B52D0` implements rich-compare plus `in / not in / is / is not / exception match`.
   - Current map entry `253 -> 107` is consistent.

3. `case 197` and `case 240` match `POP_JUMP_IF_FALSE / POP_JUMP_IF_TRUE`.
   - `case 2` (`UNARY_NOT`) proves:
     - `qword_18087BCE0` is `Py_True`
     - `qword_18087BD00` is `Py_False`
   - `case 197` compares TOS against `Py_True` first, and jumps on the `Py_False` path.
   - `case 240` compares TOS against `Py_False` first, and jumps on the `Py_True` path.
   - Current map entries:
     - `197 -> 114`
     - `240 -> 115`
     are consistent.

4. `cases 113 / 169 / 219` share the unpack handler and are broadly consistent with the current map.
   - Shared entry: `0x1800B0AB9`
   - Handler builds a temporary list via `PyList_New` + `listextend`.
   - If opcode byte is `0xDB` (`219`), it keeps the list result.
   - Otherwise it converts the temporary list to tuple via `PyList_AsTuple`.
   - This supports:
     - `219 -> 149` (`BUILD_LIST_UNPACK`)
     - `113 -> 152` (`BUILD_TUPLE_UNPACK`)
     - `169 -> 158` (`BUILD_TUPLE_UNPACK_WITH_CALL`)

5. Low-sample items inspected in IDA are consistent with the current map.
   - `159 -> 98`
     - `case 159` calls `PyDict_DelItem` on `[frame+0x30]`.
     - This matches `DELETE_GLOBAL`.
   - `215 -> 150`
     - `case 215` creates a dict and repeatedly merges stack sources into it.
     - This matches `BUILD_MAP_UNPACK`.
   - `222 -> 138`
     - `case 222` clears cell contents.
     - This matches `DELETE_DEREF`.
   - `224 -> 148`
     - `case 224` loads from class-deref style storage.
     - This matches `LOAD_CLASSDEREF`.

6. `r_object(TYPE_CODE)` in `tools/gunfire_pyc_convert.py` is consistent with IDA.
   - Important detail:
     - `sub_180103300` is not an integer reader.
     - It is the ref/index reservation helper for marshal refs.
   - After that helper, the code-object path performs six integer reads via `sub_180102F40` before the first `r_object()`:
     - `argcount`
     - `kwonlyargcount`
     - `nlocals`
     - `stacksize`
     - `flags`
     - `custom_split`
   - Then it reads the object fields:
     - `co_code`
     - `co_consts`
     - `co_names`
     - `co_varnames`
     - `co_freevars`
     - `co_cellvars`
     - `co_filename`
     - `co_name`
     - `firstlineno`
     - `lnotab`
   - So the current parser shape is still correct.

## Important Mismatch

1. `custom opcode 24` is currently mapped wrong in our tools.
   - Current map:
     - `tools/opcode_map.json`: `24 -> 15`
     - `tools/gunfire_pyc_convert.py`: `mapping[24] = 15`
   - IDA evidence:
     - `case 24` entry at `0x1800AF538`
     - Calls wrapper at `0x180069C70`
   - Critical nuance:
     - The imported wrapper names around `0x180069C00 ~ 0x180069CE0` are misleading.
     - They appear to be shifted by BinDiff/symbol propagation.
   - Actual semantics from wrapper internals and error strings:
     - `0x180069C00` named `PyNumber_Positive`
       - really reports `bad operand type for unary -`
       - actual semantic: unary negative
     - `0x180069C70` named `PyNumber_Invert`
       - really reports `bad operand type for unary +`
       - actual semantic: unary positive
     - `0x180069CE0` named `PyNumber_Absolute`
       - really reports `bad operand type for unary ~`
       - actual semantic: unary invert
     - `0x180069D50` named `PySequence_Size`
       - really reports `bad operand type for abs()`
       - actual semantic: absolute wrapper
   - Therefore:
     - `case 24` is `UNARY_POSITIVE`
     - correct mapping should be `24 -> 10`

2. `custom opcode 73` is currently correct in the map, but only after correcting for the misleading wrapper name.
   - `case 73` entry at `0x1800AF5EB`
   - Calls wrapper at `0x180069CE0`
   - Although the imported name is `PyNumber_Absolute`, the wrapper's own error string is for unary `~`.
   - Therefore:
     - `case 73` is `UNARY_INVERT`
     - current map `73 -> 15` is correct

3. `custom opcode 44` is also consistent after correcting for the wrapper-name issue.
   - `case 44` entry at `0x1800AF575`
   - Calls wrapper at `0x180069C00`
   - Wrapper reports unary `-`
   - Therefore:
     - `case 44` is `UNARY_NEGATIVE`
     - current map `44 -> 11` is correct

## Manual Follow-Up In IDA (Completed)

1. The misleading unary wrappers were corrected in IDA.
   - `0x180069C00` -> actual unary negative wrapper
   - `0x180069C70` -> actual unary positive wrapper
   - `0x180069CE0` -> actual unary invert wrapper
   - `0x180069D50` -> actual absolute wrapper

2. The converter was updated to match the confirmed VM behavior.
   - `tools/opcode_map.json`
     - `24` changed from `15` to `10`
   - `tools/gunfire_pyc_convert.py`
     - hardcoded confirmation updated to `mapping[24] = 10`

3. A focused stdlib/sample diff was re-run after fixing `24`.
   - `operator.pos`
   - `numbers.Real.real`
   - `ast.literal_eval` unary cases
   - Result:
     - unary behavior is now correct
     - the only remaining structural question is the `197/240` short-circuit jump family

## Short Verdict

- `r_object` and the current convert flow are broadly correct.
- `opcode_map.json` is mostly in good shape.
- The concrete bug confirmed from IDA is:
  - `24` should be `UNARY_POSITIVE (10)`, not `UNARY_INVERT (15)`.
- The strongest source of confusion was not the dispatcher itself, but the misnamed unary number wrappers imported into IDA.

## Validation After Fixing `24`

1. `24 -> 10` fixed the real unary bug.
   - Updated:
     - `tools/opcode_map.json`
     - `tools/gunfire_pyc_convert.py`
   - Runtime sanity checks on converted stdlib samples now match expectations:
     - `operator.pos(5) == 5`
     - `operator.neg(5) == -5`
     - `operator.invert(3) == -4`
     - `ast.literal_eval("+1") == 1`
     - `ast.literal_eval("-1") == -1`

2. `operator.pyc` and `numbers.pyc` fully match Python 3.6 `-OO` reference bytecode after the fix.
   - Reference build: local `pyenv` Python `3.6.15`, `optimize=2`
   - Result:
     - `StableLib/operator.pyc`: exact logical instruction match
     - `StableLib/numbers.pyc`: exact logical instruction match

3. `StableLib/ast.pyc` still has one structural diff in `literal_eval._convert`.
   - Converted code uses:
     - `POP_JUMP_IF_FALSE`
   - CPython `3.6.15 -OO` reference uses:
     - `JUMP_IF_FALSE_OR_POP`
   - The concrete site is the short-circuit test:
     - `if isinstance(node, UnaryOp) and isinstance(node.op, (UAdd, USub)):`

## Open Question: `197/240` vs `111/112`

1. IDA says `197` and `240` are still pop-style jumps.
   - `case 197` enters `LABEL_160`
   - `case 240` enters `LABEL_167`
   - In both handlers the value is popped first:
     - `v97 = (__int64 *)*--v22;`
   - This is consistent with:
     - `197 -> POP_JUMP_IF_FALSE (114)`
     - `240 -> POP_JUMP_IF_TRUE (115)`
   - It is not consistent with:
     - `JUMP_IF_FALSE_OR_POP (111)`
     - `JUMP_IF_TRUE_OR_POP (112)`
     because those must preserve TOS on one branch.

2. Even so, paired stdlib comparison still finds a small number of CPython sites where the reference bytecode uses `111/112`.
   - Counts from `extracted_data2` vs local Python `3.6.15 -OO` reference:
     - `custom 197 -> std 111`: `73` sites
     - `custom 240 -> std 112`: `1` site
   - Representative examples:
     - `ast.pyc:_convert`
     - `distutils/dir_util.pyc:copy_tree`
     - `distutils/cygwinccompiler.pyc:link`
     - `distutils/sysconfig.pyc:<module>`
     - `distutils/sysconfig.pyc:get_config_vars`
     - `distutils/_msvccompiler.pyc:_find_vcvarsall`

3. Current interpretation:
   - This does not currently look like a bad `opcode_map` entry.
   - It looks more like the custom compiler/VM collapses some CPython short-circuit forms into `POP_JUMP_*` bytecode when the expression is only used as a condition.
   - That would explain why:
     - IDA shows real pop semantics in the VM
     - converted code runs correctly
     - but a few modules still differ from stock CPython bytecode shape

## Manual Confirmation Targets

1. Confirm there is no separate custom opcode implementing real `JUMP_IF_FALSE_OR_POP`.
   - Good anchors:
     - `ast.pyc:_convert`
     - `distutils/dir_util.pyc:copy_tree`
     - `distutils/cygwinccompiler.pyc:link`
   - In each case, verify the custom bytecode is only used in `if A and B` / `if A or B` style condition chains, not value-producing boolean expressions.

2. Confirm there is no separate custom opcode implementing real `JUMP_IF_TRUE_OR_POP`.
   - Anchor:
     - `distutils/_msvccompiler.pyc:_find_vcvarsall`

3. If later evidence shows the VM really distinguishes `111/112`, then `197/240` must stay mapped to `114/115` and we will need to identify the missing custom opcode(s) separately.
   - As of this review, no such opcode is confirmed.

## Post-Pass Normalization Status

1. Added a conservative post-pass in `tools/gunfire_pyc_convert.py` to make converted bytecode closer to stock CPython 3.6 layout.
   - Confirmed updates:
     - `24 -> 10` remains fixed
     - short-circuit chains are only rewritten to `*_OR_POP` in selected patterns
     - forward unconditional jumps are only rewritten when doing so avoids large absolute jump encodings

2. Current stock-reference comparison against local Python `3.6.15 -OO` build:
   - `numbers.pyc`: exact logical instruction match
   - `dir_util.pyc`: exact logical instruction match
   - `sysconfig.pyc`: only one real structural mismatch left
   - `ast.pyc`: one confirmed structural mismatch left
   - `operator.pyc`: decompiles cleanly; pairwise bytecode compare has false positives because nested helper code objects reuse the same `co_name`

3. `uncompyle6` validation status:
   - Decompilation succeeds for:
     - `StableLib/distutils/dir_util.pyc`
     - `StableLib/distutils/sysconfig.pyc`
     - `StableLib/ast.pyc`
     - `StableLib/operator.pyc`
     - `StableLib/numbers.pyc`
   - Local test environment:
     - `uncompyle6 3.8.0`
     - `xdis 6.0.5`
     - `spark-parser 1.8.9`
     - Python `3.6.15`

## Remaining Manual Checks

1. `ast.pyc:literal_eval._convert`
   - One confirmed short-circuit shape diff remains:
     - current converted code:
       - `POP_JUMP_IF_FALSE`
     - stock `3.6.15 -OO`:
       - `JUMP_IF_FALSE_OR_POP`
   - Concrete site:
     - `if isinstance(node, UnaryOp) and isinstance(node.op, (UAdd, USub)):`
   - This does not block `uncompyle6`, but it is still the cleanest remaining stock-shape mismatch in `ast.pyc`.

2. `sysconfig.pyc:parse_makefile`
   - Remaining difference is not an opcode-map bug.
   - Current converted output jumps directly to the final join point, while stock CPython uses a small forward-jump trampoline.
   - `uncompyle6` decompiles this file successfully, so this is low priority unless exact byte-for-byte stock shape is required.

3. Duplicate `co_name` note
   - Some nested code objects in `ast.pyc` and `operator.pyc` reuse names like `<genexpr>` or `func`.
   - Simple compare-by-name can report false positives there.
   - For those cases, compare by parent path / const index rather than `co_name` alone.
