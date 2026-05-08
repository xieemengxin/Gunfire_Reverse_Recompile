# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumNear/dashNearFsm.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumNear/dashNearFsm.pyc
# Source Generated with Decompyle++
# File: dashNearFsm.pyc (Python 3.6)

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
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 21341


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 21342


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 21341


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.GetCustomData('CanChoosePF', oAgent) == 1


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 21342


def Func15(oAgent):
    return cl_betree.monsteragent.CAgent.GetCustomData('DashAfterChoosePFFlag', oAgent) == 0

data = {
    'Name': 'dashNearFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 32,
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
                        'TargetFSMNodeID': 59 },),
                    'ReferenceBehavior': 'Common.moveToShowPos' },
                {
                    'ID': 59,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 60,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 63,
                        'TransitionPhase': 1 }, {
                        'ID': 76,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 74,
                        'TransitionPhase': 1 }, {
                        'ID': 77,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 71,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'MonsterMediumNear.dashMoveChoosePF' },
                {
                    'ID': 62,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 65,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 43,
                        'TransitionPhase': 1 }, {
                        'ID': 66,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 37,
                        'TransitionPhase': 4 }, {
                        'ID': 67,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
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
                        'ID': 72,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 63,
                        'TransitionPhase': 1 }, {
                        'ID': 75,
                        'Class': 'Transition',
                        'Method': (Func11, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 74,
                        'TransitionPhase': 1 }, {
                        'ID': 79,
                        'Class': 'Transition',
                        'Method': (Func12, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 59,
                        'TransitionPhase': 2 }, {
                        'ID': 80,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 3,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 59 }),
                    'ReferenceBehavior': 'MonsterMediumNear.dashAttackAfter' },
                {
                    'ID': 74,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 78,
                        'Class': 'Transition',
                        'Method': (Func13, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 63,
                        'TransitionPhase': 1 }, {
                        'ID': 81,
                        'Class': 'Transition',
                        'Method': (Func14, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 71,
                        'TransitionPhase': 1 }, {
                        'ID': 82,
                        'Class': 'Transition',
                        'Method': (Func15, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 59,
                        'TransitionPhase': 2 }),
                    'ReferenceBehavior': 'MonsterMediumNear.dashNearAttack' }] }] }
