# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossDesert/bossDesertFsm.pyc
# RelativePath: clientlogic/cl_betreedata/BossDesert/bossDesertFsm.pyc
# Source Generated with Decompyle++
# File: bossDesertFsm.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetNextState('qianxing', oAgent) == 1


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetNextState('zuanchu', oAgent) == 1


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetNextState('zuanchu', oAgent) == 2


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetNextState('zuanchu', oAgent) == 3


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetNextState('qianxing', oAgent) == 1


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.GetNextState('zuanchu', oAgent) == 1


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.GetNextState('zuanchu', oAgent) == 2


def Func15(oAgent):
    return cl_betree.monsteragent.CAgent.GetNextState('zuanchu', oAgent) == 3

data = {
    'Name': 'bossDesertFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 105,
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
                        'TargetFSMNodeID': 124 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 58,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 59,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 110 },),
                    'ReferenceBehavior': 'BossDesert.Goback' },
                {
                    'ID': 63,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 132,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 129,
                        'TransitionPhase': 4 }, {
                        'ID': 139,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 120,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'BossDesert.HeadAttack' },
                {
                    'ID': 66,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 80,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 58,
                        'TransitionPhase': 1 }, {
                        'ID': 102,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 88,
                        'TransitionPhase': 1 }, {
                        'ID': 103,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 91,
                        'TransitionPhase': 1 }, {
                        'ID': 104,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 75,
                        'TransitionPhase': 1 }, {
                        'ID': 148,
                        'Class': 'Effector',
                        'Method': (cl_betree.monsteragent.CAgent.SetPyFlag, (16, 0)),
                        'Phase': 3,
                        'Flag': 'effector' }, {
                        'ID': 147,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.SetPyFlag, (16, 1)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossDesert.Swimming' },
                {
                    'ID': 75,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 76,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 140 },),
                    'ReferenceBehavior': 'BossDesert.SwimmingAttack' },
                {
                    'ID': 81,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 83,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 130,
                        'TransitionPhase': 4 }, {
                        'ID': 105,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 121,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'BossDesert.TailAttack' },
                {
                    'ID': 88,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 90,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 129,
                        'TransitionPhase': 4 }, {
                        'ID': 138,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 63 }, {
                        'ID': 151,
                        'Class': 'Effector',
                        'Method': (cl_betree.monsteragent.CAgent.HateAllPlayer, ()),
                        'Phase': 2,
                        'Flag': 'effector' }),
                    'ReferenceBehavior': 'BossDesert.HeadAppear' },
                {
                    'ID': 91,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 93,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 130,
                        'TransitionPhase': 4 }, {
                        'ID': 131,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 81 }, {
                        'ID': 150,
                        'Class': 'Effector',
                        'Method': (cl_betree.monsteragent.CAgent.HateAllPlayer, ()),
                        'Phase': 2,
                        'Flag': 'effector' }),
                    'ReferenceBehavior': 'BossDesert.TailAppear' },
                {
                    'ID': 106,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 107,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 145 }, {
                        'ID': 114,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossDesert.Attackmsg' },
                {
                    'ID': 108,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 112,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 135,
                        'TransitionPhase': 1 },),
                    'ReferenceBehavior': 'BossDesert.PatrolPos' },
                {
                    'ID': 110,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 111,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 108 }, {
                        'ID': 113,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossDesert.Patrolmsg' },
                {
                    'ID': 117,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 128,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 126 }, {
                        'ID': 118,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossDesert.Patrolmsg' },
                {
                    'ID': 120,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 123,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 66 },),
                    'ReferenceBehavior': 'BossDesert.HeadDive' },
                {
                    'ID': 121,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 122,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 66 },),
                    'ReferenceBehavior': 'BossDesert.TailDive' },
                {
                    'ID': 124,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 125,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 117 },),
                    'ReferenceBehavior': 'BossDesert.Born' },
                {
                    'ID': 126,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 127,
                        'Class': 'Transition',
                        'Method': (Func11, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 106,
                        'TransitionPhase': 1 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 129,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 133,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 110 },),
                    'ReferenceBehavior': 'BossDesert.HeadGobackDive' },
                {
                    'ID': 130,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 134,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 110 },),
                    'ReferenceBehavior': 'BossDesert.TailGobackDive' },
                {
                    'ID': 135,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 137,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 66 }, {
                        'ID': 136,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossDesert.Attackmsg' },
                {
                    'ID': 140,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 141,
                        'Class': 'Transition',
                        'Method': (Func12, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 58,
                        'TransitionPhase': 1 }, {
                        'ID': 142,
                        'Class': 'Transition',
                        'Method': (Func13, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 88,
                        'TransitionPhase': 1 }, {
                        'ID': 143,
                        'Class': 'Transition',
                        'Method': (Func14, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 91,
                        'TransitionPhase': 1 }, {
                        'ID': 144,
                        'Class': 'Transition',
                        'Method': (Func15, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 75,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'BossDesert.SwimmingAttackEnd' },
                {
                    'ID': 145,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 146,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 63 },),
                    'ReferenceBehavior': 'BossDesert.ShowAttack' }] }] }
