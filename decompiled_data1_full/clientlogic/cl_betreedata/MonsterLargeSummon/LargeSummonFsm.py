# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterLargeSummon/LargeSummonFsm.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterLargeSummon/LargeSummonFsm.pyc
# Source Generated with Decompyle++
# File: LargeSummonFsm.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(7115, oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 24011


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 24013


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(7115, oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(7115, oAgent) == True


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(7115, oAgent) == True

data = {
    'Name': 'LargeSummonFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 79,
    'Node': [
        {
            'ID': 1,
            'Class': 'FSM',
            'InitialID': 82,
            'Node': [
                {
                    'ID': 40,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 45,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 47,
                        'TransitionPhase': 4 }, {
                        'ID': 95,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 94 }, {
                        'ID': 46,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 74,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'MonsterLargeSummon.MoveToStartPos' },
                {
                    'ID': 47,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 49,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 118 }, {
                        'ID': 48,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.farAttackmsg' },
                {
                    'ID': 69,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 70,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 91,
                        'TransitionPhase': 4 }, {
                        'ID': 89,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 78,
                        'TransitionPhase': 4 }, {
                        'ID': 105,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 108,
                        'TransitionPhase': 2 }, {
                        'ID': 106,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 107,
                        'TransitionPhase': 2 }, {
                        'ID': 112,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 3,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 87 }),
                    'ReferenceBehavior': 'MonsterLargeSummon.LargeSummonAttack' },
                {
                    'ID': 78,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 79,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 91,
                        'TransitionPhase': 4 }, {
                        'ID': 80,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 69 }),
                    'ReferenceBehavior': 'MonsterLargeSummon.LargeSummonChangePhase' },
                {
                    'ID': 82,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 83,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 1,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 84 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 84,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 85,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 40 },),
                    'ReferenceBehavior': 'MonsterLargeSummon.LargeSummonBorn' },
                {
                    'ID': 87,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 88,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 69 }, {
                        'ID': 113,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 78,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'MonsterLargeSummon.LargeSummonMove' },
                {
                    'ID': 91,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 93,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 100 }, {
                        'ID': 92,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'MonsterLargeSummon.LargeSummonBorn' },
                {
                    'ID': 94,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 96,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 47,
                        'TransitionPhase': 1 }, {
                        'ID': 97,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 100 }),
                    'ReferenceBehavior': 'MonsterLargeSummon.Stay' },
                {
                    'ID': 100,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 103,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 47,
                        'TransitionPhase': 4 }, {
                        'ID': 104,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 94 }, {
                        'ID': 101,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 102,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'MonsterLargeSummon.LargeSummonPatrol' },
                {
                    'ID': 107,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 115,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 78,
                        'TransitionPhase': 4 }, {
                        'ID': 116,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 3,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 87 }, {
                        'ID': 117,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 69 }),
                    'ReferenceBehavior': 'MonsterLargeSummon.LargeSummonHeal' },
                {
                    'ID': 108,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 109,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 69 }, {
                        'ID': 114,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 78,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'MonsterLargeSummon.LargeSummonFarAttack' },
                {
                    'ID': 118,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 119,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 69 },),
                    'ReferenceBehavior': 'MonsterLargeSummon.LargeSummonFirstHeal' }] }] }
