# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFar/farGuerrillaFsm.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFar/farGuerrillaFsm.pyc
# Source Generated with Decompyle++
# File: farGuerrillaFsm.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return oAgent.GetConfig('GuerrillaAttack') == True


def Func1(oAgent):
    return oAgent.GetConfig('GuerrillaAttack') == False


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.NeedToDodge(oAgent) == 1


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.NeedToDodge(oAgent) == 1


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'

data = {
    'Name': 'farGuerrillaFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 51,
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
                        'TargetFSMNodeID': 53 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 37,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 38,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 67,
                        'TransitionPhase': 1 }, {
                        'ID': 40,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 68,
                        'TransitionPhase': 1 }),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 53,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 58,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 54,
                        'TransitionPhase': 4 }, {
                        'ID': 59,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 55,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 54,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 60,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 62,
                        'TransitionPhase': 1 }, {
                        'ID': 56,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 88,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolFace' },
                {
                    'ID': 55,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 61,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 62,
                        'TransitionPhase': 1 }, {
                        'ID': 57,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 89,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolPos' },
                {
                    'ID': 62,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 63,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 65 }, {
                        'ID': 64,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.farAttackmsg' },
                {
                    'ID': 65,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 66,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 37 },),
                    'ReferenceBehavior': 'Common.moveToShowPos' },
                {
                    'ID': 67,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 73,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 75,
                        'TransitionPhase': 1 }, {
                        'ID': 74,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 84,
                        'TransitionPhase': 1 }, {
                        'ID': 69,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'MonsterFar.farGuerrillaMoveAttack' },
                {
                    'ID': 68,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 72,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 84,
                        'TransitionPhase': 1 }, {
                        'ID': 81,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 76,
                        'TransitionPhase': 1 }, {
                        'ID': 70,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'MonsterFar.farGuerrillaStandAttack' },
                {
                    'ID': 75,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 79,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 67 }, {
                        'ID': 77,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.dodge' },
                {
                    'ID': 76,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 80,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 68 }, {
                        'ID': 78,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.dodge' },
                {
                    'ID': 84,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 85,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 86 }, {
                        'ID': 87,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 86,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 90,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 62,
                        'TransitionPhase': 1 }, {
                        'ID': 91,
                        'Class': 'Transition',
                        'Method': (Func11, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 54,
                        'TransitionPhase': 4 }, {
                        'ID': 92,
                        'Class': 'Transition',
                        'Method': (Func12, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 55,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolGoback' }] }] }
