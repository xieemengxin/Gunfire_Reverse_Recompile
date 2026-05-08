# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossDemon/bossDemonFsm.pyc
# RelativePath: clientlogic/cl_betreedata/BossDemon/bossDemonFsm.pyc
# Source Generated with Decompyle++
# File: bossDemonFsm.pyc (Python 3.6)

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
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 6


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.StateTransition(7994, oAgent) == 2


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 1


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 4


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 5


def Func15(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func16(oAgent):
    return cl_betree.monsteragent.CAgent.StateTransition(7994, oAgent) == 2


def Func17(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func18(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func19(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 4


def Func20(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 5


def Func21(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func22(oAgent):
    return cl_betree.monsteragent.CAgent.StateTransition(7994, oAgent) == 2


def Func23(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func24(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 4


def Func25(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 5


def Func26(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func27(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 4


def Func28(oAgent):
    return cl_betree.monsteragent.CAgent.StateTransition(7994, oAgent) == 2


def Func29(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 1


def Func30(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func31(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func32(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 5


def Func33(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func34(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 5


def Func35(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 6


def Func36(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func37(oAgent):
    return cl_betree.monsteragent.CAgent.StateTransition(7994, oAgent) == 2


def Func38(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 1


def Func39(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func40(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func41(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 4


def Func42(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 5


def Func43(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 1


def Func44(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func45(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func46(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 6


def Func47(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func48(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 6

data = {
    'Name': 'bossDemonFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 50,
    'Node': [
        {
            'ID': 1,
            'Class': 'FSM',
            'InitialID': 89,
            'Node': [
                {
                    'ID': 4,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 8,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 6,
                        'TransitionPhase': 4 }, {
                        'ID': 9,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 7,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 6,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 15,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 14,
                        'TransitionPhase': 1 }, {
                        'ID': 10,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 12,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolFace' },
                {
                    'ID': 7,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 16,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 14,
                        'TransitionPhase': 1 }, {
                        'ID': 11,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 13,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolPos' },
                {
                    'ID': 14,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 104,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 93,
                        'TransitionPhase': 4 }, {
                        'ID': 105,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 67 }, {
                        'ID': 18,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.farAttackmsg' },
                {
                    'ID': 23,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 25,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 26 }, {
                        'ID': 24,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 91,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.RemoveState, (7994,)),
                        'Phase': 3,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 92,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.HaltPerform, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 103,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Teleport', 'False')),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 26,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 27,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 14,
                        'TransitionPhase': 1 }, {
                        'ID': 28,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 6,
                        'TransitionPhase': 4 }, {
                        'ID': 29,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 7,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolGoback' },
                {
                    'ID': 30,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 32,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 23,
                        'TransitionPhase': 4 }, {
                        'ID': 38,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 36,
                        'TransitionPhase': 1 }, {
                        'ID': 40,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 93,
                        'TransitionPhase': 4 }, {
                        'ID': 42,
                        'Class': 'Transition',
                        'Method': (Func11, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 31,
                        'TransitionPhase': 4 }, {
                        'ID': 45,
                        'Class': 'Transition',
                        'Method': (Func12, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 34,
                        'TransitionPhase': 4 }, {
                        'ID': 83,
                        'Class': 'Transition',
                        'Method': (Func13, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 51,
                        'TransitionPhase': 4 }, {
                        'ID': 87,
                        'Class': 'Transition',
                        'Method': (Func14, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 54,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'BossDemon.bossDemonPhase1' },
                {
                    'ID': 31,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 33,
                        'Class': 'Transition',
                        'Method': (Func15, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 23,
                        'TransitionPhase': 4 }, {
                        'ID': 39,
                        'Class': 'Transition',
                        'Method': (Func16, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 36,
                        'TransitionPhase': 1 }, {
                        'ID': 43,
                        'Class': 'Transition',
                        'Method': (Func17, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 93,
                        'TransitionPhase': 4 }, {
                        'ID': 47,
                        'Class': 'Transition',
                        'Method': (Func18, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 34,
                        'TransitionPhase': 4 }, {
                        'ID': 84,
                        'Class': 'Transition',
                        'Method': (Func19, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 51,
                        'TransitionPhase': 4 }, {
                        'ID': 88,
                        'Class': 'Transition',
                        'Method': (Func20, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 54,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'BossDemon.bossDemonPhase2' },
                {
                    'ID': 34,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 35,
                        'Class': 'Transition',
                        'Method': (Func21, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 23,
                        'TransitionPhase': 4 }, {
                        'ID': 58,
                        'Class': 'Transition',
                        'Method': (Func22, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 36,
                        'TransitionPhase': 1 }, {
                        'ID': 59,
                        'Class': 'Transition',
                        'Method': (Func23, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 93,
                        'TransitionPhase': 4 }, {
                        'ID': 60,
                        'Class': 'Transition',
                        'Method': (Func24, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 51,
                        'TransitionPhase': 4 }, {
                        'ID': 61,
                        'Class': 'Transition',
                        'Method': (Func25, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 54,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'BossDemon.bossDemonPhase3' },
                {
                    'ID': 36,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 37,
                        'Class': 'Transition',
                        'Method': (Func26, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 23,
                        'TransitionPhase': 1 }, {
                        'ID': 76,
                        'Class': 'Transition',
                        'Method': (Func27, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 51,
                        'TransitionPhase': 4 }, {
                        'ID': 78,
                        'Class': 'Transition',
                        'Method': (Func28, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 36,
                        'TransitionPhase': 1 }, {
                        'ID': 79,
                        'Class': 'Transition',
                        'Method': (Func29, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 30,
                        'TransitionPhase': 4 }, {
                        'ID': 80,
                        'Class': 'Transition',
                        'Method': (Func30, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 31,
                        'TransitionPhase': 4 }, {
                        'ID': 81,
                        'Class': 'Transition',
                        'Method': (Func31, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 34,
                        'TransitionPhase': 4 }, {
                        'ID': 82,
                        'Class': 'Transition',
                        'Method': (Func32, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 54,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'BossDemon.bossDemonCharge' },
                {
                    'ID': 51,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 52,
                        'Class': 'Transition',
                        'Method': (Func33, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 23,
                        'TransitionPhase': 4 }, {
                        'ID': 55,
                        'Class': 'Transition',
                        'Method': (Func34, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 54,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'BossDemon.bossDemonPhase4' },
                {
                    'ID': 54,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 99,
                        'Class': 'Transition',
                        'Method': (Func35, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 98,
                        'TransitionPhase': 1 }, {
                        'ID': 74,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.HaltPerform, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossDemon.bossDemonPhase5' },
                {
                    'ID': 67,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 68,
                        'Class': 'Transition',
                        'Method': (Func36, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 23,
                        'TransitionPhase': 4 }, {
                        'ID': 69,
                        'Class': 'Transition',
                        'Method': (Func37, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 36,
                        'TransitionPhase': 1 }, {
                        'ID': 70,
                        'Class': 'Transition',
                        'Method': (Func38, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 30,
                        'TransitionPhase': 4 }, {
                        'ID': 71,
                        'Class': 'Transition',
                        'Method': (Func39, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 31,
                        'TransitionPhase': 4 }, {
                        'ID': 72,
                        'Class': 'Transition',
                        'Method': (Func40, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 34,
                        'TransitionPhase': 4 }, {
                        'ID': 85,
                        'Class': 'Transition',
                        'Method': (Func41, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 51,
                        'TransitionPhase': 4 }, {
                        'ID': 86,
                        'Class': 'Transition',
                        'Method': (Func42, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 54,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'BossDemon.bossDemonShowAttack' },
                {
                    'ID': 89,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 90,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 4 },),
                    'ReferenceBehavior': 'BossDemon.bossDemonAppear' },
                {
                    'ID': 93,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 95,
                        'Class': 'Transition',
                        'Method': (Func43, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 30,
                        'TransitionPhase': 1 }, {
                        'ID': 96,
                        'Class': 'Transition',
                        'Method': (Func44, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 31,
                        'TransitionPhase': 1 }, {
                        'ID': 97,
                        'Class': 'Transition',
                        'Method': (Func45, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 34,
                        'TransitionPhase': 1 }, {
                        'ID': 100,
                        'Class': 'Transition',
                        'Method': (Func46, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 98,
                        'TransitionPhase': 1 }, {
                        'ID': 106,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Teleport', 'False')),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossDemon.bossDemonMedium' },
                {
                    'ID': 98,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 101,
                        'Class': 'Transition',
                        'Method': (Func47, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 23,
                        'TransitionPhase': 4 }, {
                        'ID': 102,
                        'Class': 'Transition',
                        'Method': (Func48, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 93,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'BossDemon.bossDemonPhase6' }] }] }
