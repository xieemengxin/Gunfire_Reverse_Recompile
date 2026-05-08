# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteNear/nearSpearEliteFsm.pyc
# RelativePath: clientlogic/cl_betreedata/EliteNear/nearSpearEliteFsm.pyc
# Source Generated with Decompyle++
# File: nearSpearEliteFsm.pyc (Python 3.6)

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
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 30831


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 30832


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 30833


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 30834


def Func15(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 30835


def Func16(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func17(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 30831


def Func18(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 30832


def Func19(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 30833


def Func20(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 30834


def Func21(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 30835


def Func22(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1

data = {
    'Name': 'nearSpearEliteFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 33,
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
                        'ID': 66,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 43,
                        'TransitionPhase': 4 }, {
                        'ID': 67,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 37,
                        'TransitionPhase': 4 }, {
                        'ID': 68,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
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
                        'Method': (Func3, ()),
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
                        'ID': 57,
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
                        'Method': (Func4, ()),
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
                        'ID': 58,
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
                        'ID': 63,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 43,
                        'TransitionPhase': 1 }, {
                        'ID': 64,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 37,
                        'TransitionPhase': 4 }, {
                        'ID': 65,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 38,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolGoback' },
                {
                    'ID': 60,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 62,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 59 }, {
                        'ID': 61,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 69,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 70,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 60,
                        'TransitionPhase': 1 }, {
                        'ID': 77,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 71 }),
                    'ReferenceBehavior': 'EliteNear.nearSpearAttack' },
                {
                    'ID': 71,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 73,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 60,
                        'TransitionPhase': 1 }, {
                        'ID': 75,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 72,
                        'TransitionPhase': 1 }, {
                        'ID': 80,
                        'Class': 'Transition',
                        'Method': (Func11, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 69,
                        'TransitionPhase': 2 }, {
                        'ID': 81,
                        'Class': 'Transition',
                        'Method': (Func12, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 69,
                        'TransitionPhase': 2 }, {
                        'ID': 82,
                        'Class': 'Transition',
                        'Method': (Func13, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 69,
                        'TransitionPhase': 2 }, {
                        'ID': 83,
                        'Class': 'Transition',
                        'Method': (Func14, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 69,
                        'TransitionPhase': 2 }, {
                        'ID': 84,
                        'Class': 'Transition',
                        'Method': (Func15, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 79,
                        'TransitionPhase': 2 }),
                    'ReferenceBehavior': 'EliteNear.nearSpearPhase1' },
                {
                    'ID': 72,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 74,
                        'Class': 'Transition',
                        'Method': (Func16, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 60,
                        'TransitionPhase': 1 }, {
                        'ID': 85,
                        'Class': 'Transition',
                        'Method': (Func17, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 69,
                        'TransitionPhase': 2 }, {
                        'ID': 86,
                        'Class': 'Transition',
                        'Method': (Func18, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 69,
                        'TransitionPhase': 2 }, {
                        'ID': 87,
                        'Class': 'Transition',
                        'Method': (Func19, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 69,
                        'TransitionPhase': 2 }, {
                        'ID': 88,
                        'Class': 'Transition',
                        'Method': (Func20, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 69,
                        'TransitionPhase': 2 }, {
                        'ID': 89,
                        'Class': 'Transition',
                        'Method': (Func21, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 79,
                        'TransitionPhase': 2 }),
                    'ReferenceBehavior': 'EliteNear.nearSpearPhase2' },
                {
                    'ID': 79,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 90,
                        'Class': 'Transition',
                        'Method': (Func22, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 60,
                        'TransitionPhase': 1 }, {
                        'ID': 91,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 71 }),
                    'ReferenceBehavior': 'EliteNear.nearSpearRushAttack' }] }] }
