# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossLuWu/bossLuWuFsm.pyc
# RelativePath: clientlogic/cl_betreedata/BossLuWu/bossLuWuFsm.pyc
# Source Generated with Decompyle++
# File: bossLuWuFsm.pyc (Python 3.6)

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
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39011


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39012


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39013


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39014


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39015


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39016


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'


def Func15(oAgent):
    return cl_betree.monsteragent.CAgent.GetLiveHeroCnt(oAgent) < 1


def Func16(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 1


def Func17(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func18(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func19(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func20(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 1


def Func21(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func22(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func23(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func24(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 1


def Func25(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func26(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func27(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func28(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func29(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39011


def Func30(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39012


def Func31(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39013


def Func32(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39014


def Func33(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39015


def Func34(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39016


def Func35(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func36(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39011


def Func37(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39012


def Func38(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39013


def Func39(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39014


def Func40(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39015


def Func41(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 39016

data = {
    'Name': 'bossLuWuFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 54,
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
                        'TargetFSMNodeID': 42 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 42,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 43,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 45,
                        'TransitionPhase': 4 }, {
                        'ID': 44,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 46,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 45,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 49,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 51,
                        'TransitionPhase': 1 }, {
                        'ID': 47,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 67,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolFace' },
                {
                    'ID': 46,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 50,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 51,
                        'TransitionPhase': 1 }, {
                        'ID': 48,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 68,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolPos' },
                {
                    'ID': 51,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 52,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 54 }, {
                        'ID': 53,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossLuWu.bossLuWuAttackmsg' },
                {
                    'ID': 54,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 55,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 56 },),
                    'ReferenceBehavior': 'Common.moveToShowPos' },
                {
                    'ID': 56,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 57,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 61,
                        'TransitionPhase': 1 }, {
                        'ID': 92,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 86,
                        'TransitionPhase': 1 }, {
                        'ID': 93,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 72,
                        'TransitionPhase': 2 }, {
                        'ID': 96,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 72,
                        'TransitionPhase': 2 }, {
                        'ID': 99,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 73,
                        'TransitionPhase': 2 }, {
                        'ID': 102,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 75,
                        'TransitionPhase': 2 }, {
                        'ID': 114,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 73,
                        'TransitionPhase': 2 }, {
                        'ID': 127,
                        'Class': 'Transition',
                        'Method': (Func11, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 73,
                        'TransitionPhase': 2 }),
                    'ReferenceBehavior': 'BossLuWu.bossLuWuAttack' },
                {
                    'ID': 60,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 63,
                        'Class': 'Transition',
                        'Method': (Func12, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 51,
                        'TransitionPhase': 1 }, {
                        'ID': 64,
                        'Class': 'Transition',
                        'Method': (Func13, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 45,
                        'TransitionPhase': 4 }, {
                        'ID': 65,
                        'Class': 'Transition',
                        'Method': (Func14, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 46,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolGoback' },
                {
                    'ID': 61,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 62,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 60 }, {
                        'ID': 66,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 72,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 80,
                        'Class': 'Transition',
                        'Method': (Func15, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 61,
                        'TransitionPhase': 1 }, {
                        'ID': 118,
                        'Class': 'Transition',
                        'Method': (Func16, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 56,
                        'TransitionPhase': 4 }, {
                        'ID': 119,
                        'Class': 'Transition',
                        'Method': (Func17, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 86,
                        'TransitionPhase': 4 }, {
                        'ID': 120,
                        'Class': 'Transition',
                        'Method': (Func18, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 87,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'BossLuWu.bossLuWuFarAttack' },
                {
                    'ID': 73,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 81,
                        'Class': 'Transition',
                        'Method': (Func19, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 61,
                        'TransitionPhase': 1 }, {
                        'ID': 121,
                        'Class': 'Transition',
                        'Method': (Func20, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 56,
                        'TransitionPhase': 4 }, {
                        'ID': 123,
                        'Class': 'Transition',
                        'Method': (Func21, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 86,
                        'TransitionPhase': 4 }, {
                        'ID': 125,
                        'Class': 'Transition',
                        'Method': (Func22, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 87,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'BossLuWu.bossLuWuNearAttack' },
                {
                    'ID': 75,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 82,
                        'Class': 'Transition',
                        'Method': (Func23, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 61,
                        'TransitionPhase': 1 }, {
                        'ID': 122,
                        'Class': 'Transition',
                        'Method': (Func24, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 56,
                        'TransitionPhase': 4 }, {
                        'ID': 124,
                        'Class': 'Transition',
                        'Method': (Func25, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 86,
                        'TransitionPhase': 4 }, {
                        'ID': 126,
                        'Class': 'Transition',
                        'Method': (Func26, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 87,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'BossLuWu.bossLuWuSummon' },
                {
                    'ID': 86,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 89,
                        'Class': 'Transition',
                        'Method': (Func27, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 61,
                        'TransitionPhase': 1 }, {
                        'ID': 90,
                        'Class': 'Transition',
                        'Method': (Func28, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 87,
                        'TransitionPhase': 1 }, {
                        'ID': 94,
                        'Class': 'Transition',
                        'Method': (Func29, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 72,
                        'TransitionPhase': 2 }, {
                        'ID': 97,
                        'Class': 'Transition',
                        'Method': (Func30, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 72,
                        'TransitionPhase': 2 }, {
                        'ID': 100,
                        'Class': 'Transition',
                        'Method': (Func31, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 73,
                        'TransitionPhase': 2 }, {
                        'ID': 103,
                        'Class': 'Transition',
                        'Method': (Func32, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 75,
                        'TransitionPhase': 2 }, {
                        'ID': 115,
                        'Class': 'Transition',
                        'Method': (Func33, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 73,
                        'TransitionPhase': 2 }, {
                        'ID': 128,
                        'Class': 'Transition',
                        'Method': (Func34, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 73,
                        'TransitionPhase': 2 }),
                    'ReferenceBehavior': 'BossLuWu.bossLuWuPhase2' },
                {
                    'ID': 87,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 91,
                        'Class': 'Transition',
                        'Method': (Func35, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 61,
                        'TransitionPhase': 1 }, {
                        'ID': 95,
                        'Class': 'Transition',
                        'Method': (Func36, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 72,
                        'TransitionPhase': 2 }, {
                        'ID': 98,
                        'Class': 'Transition',
                        'Method': (Func37, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 72,
                        'TransitionPhase': 2 }, {
                        'ID': 101,
                        'Class': 'Transition',
                        'Method': (Func38, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 73,
                        'TransitionPhase': 2 }, {
                        'ID': 104,
                        'Class': 'Transition',
                        'Method': (Func39, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 75,
                        'TransitionPhase': 2 }, {
                        'ID': 116,
                        'Class': 'Transition',
                        'Method': (Func40, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 73,
                        'TransitionPhase': 2 }, {
                        'ID': 129,
                        'Class': 'Transition',
                        'Method': (Func41, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 73,
                        'TransitionPhase': 2 }),
                    'ReferenceBehavior': 'BossLuWu.bossLuWuPhase3' }] }] }
