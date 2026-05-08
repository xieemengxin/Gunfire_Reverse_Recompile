# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFar/farCoverFsm.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFar/farCoverFsm.pyc
# Source Generated with Decompyle++
# File: farCoverFsm.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetCoveredPos(oAgent) == 1


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.HasToStartGuerrilla(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'

data = {
    'Name': 'farCoverFsm',
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
                        'TargetFSMNodeID': 69 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 51,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 52,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 94,
                        'TransitionPhase': 1 }, {
                        'ID': 66,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 55 }),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 55,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 57,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 91,
                        'TransitionPhase': 1 }, {
                        'ID': 64,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 87 }),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 69,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 72,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 70,
                        'TransitionPhase': 4 }, {
                        'ID': 73,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 71,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 70,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 77,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 78,
                        'TransitionPhase': 1 }, {
                        'ID': 74,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 105,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolFace' },
                {
                    'ID': 71,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 76,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 78,
                        'TransitionPhase': 1 }, {
                        'ID': 75,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 106,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolPos' },
                {
                    'ID': 78,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 79,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 97 }, {
                        'ID': 80,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.farAttackmsg' },
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
                        'TargetFSMNodeID': 100,
                        'TransitionPhase': 1 }, {
                        'ID': 84,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 51 }, {
                        'ID': 82,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'MonsterFar.farCoverAttack' },
                {
                    'ID': 87,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 88,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 81 }, {
                        'ID': 89,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 3,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 91 }, {
                        'ID': 90,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'MonsterFar.hide' },
                {
                    'ID': 91,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 93,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 81 }, {
                        'ID': 92,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'MonsterFar.guerrilla' },
                {
                    'ID': 94,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 96,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 81 }, {
                        'ID': 95,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'MonsterFar.cover' },
                {
                    'ID': 97,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 98,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 81 },),
                    'ReferenceBehavior': 'Common.moveToShowPos' },
                {
                    'ID': 99,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 102,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 78,
                        'TransitionPhase': 1 }, {
                        'ID': 103,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 70,
                        'TransitionPhase': 4 }, {
                        'ID': 104,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 71,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolGoback' },
                {
                    'ID': 100,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 101,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 99 }, {
                        'ID': 107,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolmsg' }] }] }
