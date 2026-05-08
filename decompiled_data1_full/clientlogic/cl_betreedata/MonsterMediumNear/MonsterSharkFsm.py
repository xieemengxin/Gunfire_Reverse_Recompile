# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumNear/MonsterSharkFsm.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumNear/MonsterSharkFsm.pyc
# Source Generated with Decompyle++
# File: MonsterSharkFsm.pyc (Python 3.6)

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
    return cl_betree.monsteragent.CAgent.CheckHasState(33607, oAgent) == True


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetTotalHPPercent(oAgent) <= 50


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(33607, oAgent) == True


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 1


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func15(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func16(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(33607, oAgent) == True


def Func17(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func18(oAgent):
    return cl_betree.monsteragent.CAgent.GetTotalHPPercent(oAgent) > 50


def Func19(oAgent):
    return cl_betree.monsteragent.CAgent.GetTotalHPPercent(oAgent) <= 50


def Func20(oAgent):
    return cl_betree.monsteragent.CAgent.GetTotalHPPercent(oAgent) > 50

data = {
    'Name': 'MonsterSharkFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 111,
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
                        'TargetFSMNodeID': 38 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 38,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 41,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 39,
                        'TransitionPhase': 4 }, {
                        'ID': 42,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 40,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 39,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 44,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 47,
                        'TransitionPhase': 1 }, {
                        'ID': 43,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 121,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolFace' },
                {
                    'ID': 40,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 45,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 47,
                        'TransitionPhase': 1 }, {
                        'ID': 46,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 122,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolPos' },
                {
                    'ID': 47,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 49,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 58 }, {
                        'ID': 48,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 175,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.ResetCatchStartFrame, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.farAttackmsg' },
                {
                    'ID': 58,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 86,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 110 },),
                    'ReferenceBehavior': 'Common.moveToShowPos' },
                {
                    'ID': 110,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 111,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 117,
                        'TransitionPhase': 1 }, {
                        'ID': 139,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 141,
                        'TransitionPhase': 4 }, {
                        'ID': 168,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 126,
                        'TransitionPhase': 4 }, {
                        'ID': 169,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 145,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'MonsterMediumNear.MonsterSharkAttack' },
                {
                    'ID': 117,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 119,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 118 }, {
                        'ID': 120,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 118,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 123,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 47,
                        'TransitionPhase': 1 }, {
                        'ID': 124,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 39,
                        'TransitionPhase': 4 }, {
                        'ID': 125,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 40,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolGoback' },
                {
                    'ID': 126,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 160,
                        'Class': 'Transition',
                        'Method': (Func11, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 176,
                        'TransitionPhase': 4 }, {
                        'ID': 166,
                        'Class': 'Transition',
                        'Method': (Func12, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 141,
                        'TransitionPhase': 4 }, {
                        'ID': 167,
                        'Class': 'Transition',
                        'Method': (Func13, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 155,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'MonsterMediumNear.MonsterSharkChaseCatch' },
                {
                    'ID': 141,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 172,
                        'Class': 'Effector',
                        'Method': (cl_betree.monsteragent.CAgent.AddState, (33615, 500)),
                        'Phase': 3,
                        'Flag': 'effector' }, {
                        'ID': 173,
                        'Class': 'Transition',
                        'Method': (Func14, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 176,
                        'TransitionPhase': 4 }, {
                        'ID': 174,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 155 }),
                    'ReferenceBehavior': 'MonsterMediumNear.MonsterSharkChaseLowHPCatch' },
                {
                    'ID': 145,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 151,
                        'Class': 'Transition',
                        'Method': (Func15, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 117,
                        'TransitionPhase': 1 }, {
                        'ID': 153,
                        'Class': 'Transition',
                        'Method': (Func16, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 141,
                        'TransitionPhase': 4 }, {
                        'ID': 170,
                        'Class': 'Transition',
                        'Method': (Func17, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 126,
                        'TransitionPhase': 4 }, {
                        'ID': 171,
                        'Class': 'Transition',
                        'Method': (Func18, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 110,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'MonsterMediumNear.MonsterSharkLowHPAttack' },
                {
                    'ID': 155,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 156,
                        'Class': 'Transition',
                        'Method': (Func19, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 145,
                        'TransitionPhase': 4 }, {
                        'ID': 157,
                        'Class': 'Transition',
                        'Method': (Func20, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 110,
                        'TransitionPhase': 4 }),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 176,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 178,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 117 },),
                    'ReferenceBehavior': 'MonsterMediumNear.MonsterSharkSurface' }] }] }
