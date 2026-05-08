# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteNear/EliteDashNearFsm.pyc
# RelativePath: clientlogic/cl_betreedata/EliteNear/EliteDashNearFsm.pyc
# Source Generated with Decompyle++
# File: EliteDashNearFsm.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 31342


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetCustomData('MonsterDashChoosePFFlag', oAgent) == 0


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetCustomData('CanChoosePF', oAgent) == 1


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 31341


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 31342


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 31343


def Func15(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func16(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 31342


def Func17(oAgent):
    return cl_betree.monsteragent.CAgent.GetCustomData('MonsterDashChoosePFFlag', oAgent) == 0


def Func18(oAgent):
    return cl_betree.monsteragent.CAgent.GetCustomData('CanChoosePF', oAgent) == 1


def Func19(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func20(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 31341


def Func21(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 31343


def Func22(oAgent):
    return cl_betree.monsteragent.CAgent.GetCustomData('DashAfterMove', oAgent) == 1


def Func23(oAgent):
    return cl_betree.monsteragent.CAgent.GetCustomData('CanChoosePF', oAgent) == 1


def Func24(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func25(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 31341


def Func26(oAgent):
    return cl_betree.monsteragent.CAgent.GetCustomData('CanChoosePF', oAgent) == 1

data = {
    'Name': 'EliteDashNearFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 56,
    'Node': [
        {
            'ID': 1,
            'Class': 'FSM',
            'InitialID': 2,
            'Node': [
                {
                    'ID': 2,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 9,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 1,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 34 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 34,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 35,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 37,
                        'TransitionPhase': 4 }, {
                        'ID': 36,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 38,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 37,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 39,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 43,
                        'TransitionPhase': 1 }, {
                        'ID': 42,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 69,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolFace' },
                {
                    'ID': 38,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 40,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 43,
                        'TransitionPhase': 1 }, {
                        'ID': 41,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 70,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolPos' },
                {
                    'ID': 43,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 44,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 54 }, {
                        'ID': 45,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.nearAttackmsg' },
                {
                    'ID': 54,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 55,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 71 },),
                    'ReferenceBehavior': 'Common.moveToShowPos' },
                {
                    'ID': 59,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 85,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 63,
                        'TransitionPhase': 1 }, {
                        'ID': 93,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 90,
                        'TransitionPhase': 2 }, {
                        'ID': 100,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 71,
                        'TransitionPhase': 2 }, {
                        'ID': 104,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 71,
                        'TransitionPhase': 2 }, {
                        'ID': 117,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 3,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 71 }),
                    'ReferenceBehavior': 'EliteNear.EliteDashFarAttack' },
                {
                    'ID': 62,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 65,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 43,
                        'TransitionPhase': 1 }, {
                        'ID': 66,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 37,
                        'TransitionPhase': 4 }, {
                        'ID': 67,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 38,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolGoback' },
                {
                    'ID': 63,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 64,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 62 }, {
                        'ID': 68,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 71,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 73,
                        'Class': 'Transition',
                        'Method': (Func11, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 63,
                        'TransitionPhase': 1 }, {
                        'ID': 77,
                        'Class': 'Transition',
                        'Method': (Func12, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 72,
                        'TransitionPhase': 2 }, {
                        'ID': 78,
                        'Class': 'Transition',
                        'Method': (Func13, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 90,
                        'TransitionPhase': 2 }, {
                        'ID': 79,
                        'Class': 'Transition',
                        'Method': (Func14, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 59,
                        'TransitionPhase': 2 }),
                    'ReferenceBehavior': 'EliteNear.EliteDashMoveChoosePF' },
                {
                    'ID': 72,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 87,
                        'Class': 'Transition',
                        'Method': (Func15, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 63,
                        'TransitionPhase': 1 }, {
                        'ID': 95,
                        'Class': 'Transition',
                        'Method': (Func16, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 90,
                        'TransitionPhase': 2 }, {
                        'ID': 101,
                        'Class': 'Transition',
                        'Method': (Func17, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 71,
                        'TransitionPhase': 2 }, {
                        'ID': 105,
                        'Class': 'Transition',
                        'Method': (Func18, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 71,
                        'TransitionPhase': 2 }, {
                        'ID': 116,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 3,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 71 }),
                    'ReferenceBehavior': 'EliteNear.EliteDashNearAttack' },
                {
                    'ID': 90,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 97,
                        'Class': 'Transition',
                        'Method': (Func19, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 63,
                        'TransitionPhase': 1 }, {
                        'ID': 98,
                        'Class': 'Transition',
                        'Method': (Func20, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 72,
                        'TransitionPhase': 2 }, {
                        'ID': 99,
                        'Class': 'Transition',
                        'Method': (Func21, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 59,
                        'TransitionPhase': 2 }, {
                        'ID': 113,
                        'Class': 'Transition',
                        'Method': (Func22, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 106,
                        'TransitionPhase': 2 }, {
                        'ID': 114,
                        'Class': 'Transition',
                        'Method': (Func23, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 71,
                        'TransitionPhase': 2 }, {
                        'ID': 115,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 3,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 71 }),
                    'ReferenceBehavior': 'EliteNear.EliteDashAttackAfter' },
                {
                    'ID': 106,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 107,
                        'Class': 'Transition',
                        'Method': (Func24, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 63,
                        'TransitionPhase': 1 }, {
                        'ID': 108,
                        'Class': 'Transition',
                        'Method': (Func25, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 72,
                        'TransitionPhase': 2 }, {
                        'ID': 109,
                        'Class': 'Transition',
                        'Method': (Func26, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 71,
                        'TransitionPhase': 2 }, {
                        'ID': 110,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 3,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 71 }),
                    'ReferenceBehavior': 'EliteNear.EliteDashAfterMove' }] }] }
