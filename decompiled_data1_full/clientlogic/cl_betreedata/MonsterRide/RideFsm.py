# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterRide/RideFsm.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterRide/RideFsm.pyc
# Source Generated with Decompyle++
# File: RideFsm.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 23812


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 23811


def Func15(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func16(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func17(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func18(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func19(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func20(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func21(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func22(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func23(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1

data = {
    'Name': 'RideFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 18,
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
                        'ID': 3,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 1,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 4 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 4,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 5,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 16,
                        'TransitionPhase': 4 }, {
                        'ID': 6,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 8,
                        'TransitionPhase': 4 }, {
                        'ID': 7,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 9,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 8,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 12,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 16,
                        'TransitionPhase': 1 }, {
                        'ID': 10,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 11,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolFace' },
                {
                    'ID': 9,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 15,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 16,
                        'TransitionPhase': 1 }, {
                        'ID': 13,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 14,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolPos' },
                {
                    'ID': 16,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 18,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 19 }, {
                        'ID': 17,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.nearAttackmsg' },
                {
                    'ID': 19,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 64,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 36,
                        'TransitionPhase': 1 }, {
                        'ID': 65,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 39,
                        'TransitionPhase': 1 }, {
                        'ID': 66,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 44 }),
                    'ReferenceBehavior': 'Common.moveToShowPos' },
                {
                    'ID': 29,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 31,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 32 }, {
                        'ID': 30,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 32,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 33,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 16,
                        'TransitionPhase': 1 }, {
                        'ID': 34,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 8,
                        'TransitionPhase': 4 }, {
                        'ID': 35,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 9,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolGoback' },
                {
                    'ID': 36,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 38,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 60 }, {
                        'ID': 37,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.HaltPerform, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 42,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'MonsterRide.RideKnightDie' },
                {
                    'ID': 39,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 41,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 68 }, {
                        'ID': 40,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.HaltPerform, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 43,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'MonsterRide.RideMountDie' },
                {
                    'ID': 44,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 45,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 29,
                        'TransitionPhase': 1 }, {
                        'ID': 46,
                        'Class': 'Transition',
                        'Method': (Func11, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 36,
                        'TransitionPhase': 1 }, {
                        'ID': 47,
                        'Class': 'Transition',
                        'Method': (Func12, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 39,
                        'TransitionPhase': 1 }, {
                        'ID': 48,
                        'Class': 'Transition',
                        'Method': (Func13, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 50,
                        'TransitionPhase': 4 }, {
                        'ID': 57,
                        'Class': 'Transition',
                        'Method': (Func14, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 49,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'MonsterRide.RideAttack' },
                {
                    'ID': 49,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 54,
                        'Class': 'Transition',
                        'Method': (Func15, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 29,
                        'TransitionPhase': 1 }, {
                        'ID': 55,
                        'Class': 'Transition',
                        'Method': (Func16, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 36,
                        'TransitionPhase': 1 }, {
                        'ID': 56,
                        'Class': 'Transition',
                        'Method': (Func17, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 39,
                        'TransitionPhase': 1 }, {
                        'ID': 59,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 44 }),
                    'ReferenceBehavior': 'MonsterRide.RideFireAttack' },
                {
                    'ID': 50,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 51,
                        'Class': 'Transition',
                        'Method': (Func18, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 29,
                        'TransitionPhase': 1 }, {
                        'ID': 52,
                        'Class': 'Transition',
                        'Method': (Func19, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 36,
                        'TransitionPhase': 1 }, {
                        'ID': 53,
                        'Class': 'Transition',
                        'Method': (Func20, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 39,
                        'TransitionPhase': 1 }, {
                        'ID': 58,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 44 }),
                    'ReferenceBehavior': 'MonsterRide.RideNearAttack' },
                {
                    'ID': 60,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 61,
                        'Class': 'Transition',
                        'Method': (Func21, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 29,
                        'TransitionPhase': 1 }, {
                        'ID': 67,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.SetChooseCrazyTargetNoHate, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'MonsterRide.MountAttack' },
                {
                    'ID': 62,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 63,
                        'Class': 'Transition',
                        'Method': (Func22, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 29,
                        'TransitionPhase': 1 },),
                    'ReferenceBehavior': 'MonsterRide.KnightAttack' },
                {
                    'ID': 68,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 70,
                        'Class': 'Transition',
                        'Method': (Func23, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 29,
                        'TransitionPhase': 1 }, {
                        'ID': 71,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 62 }),
                    'ReferenceBehavior': 'MonsterRide.RideKnightRun' }] }] }
