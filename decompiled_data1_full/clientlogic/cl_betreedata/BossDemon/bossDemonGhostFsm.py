# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossDemon/bossDemonGhostFsm.pyc
# RelativePath: clientlogic/cl_betreedata/BossDemon/bossDemonGhostFsm.pyc
# Source Generated with Decompyle++
# File: bossDemonGhostFsm.pyc (Python 3.6)

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
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1

data = {
    'Name': 'bossDemonGhostFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 4,
    'Node': [
        {
            'ID': 1,
            'Class': 'FSM',
            'InitialID': 4,
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
                        'ID': 114,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 115 }, {
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
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 14,
                        'TransitionPhase': 1 }, {
                        'ID': 28,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 6,
                        'TransitionPhase': 4 }, {
                        'ID': 29,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 7,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolGoback' },
                {
                    'ID': 93,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 120,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 115 }, {
                        'ID': 106,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Teleport', 'False')),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossDemon.bossDemonMedium' },
                {
                    'ID': 115,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 116,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 23,
                        'TransitionPhase': 4 }, {
                        'ID': 119,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 93 }),
                    'ReferenceBehavior': 'BossDemon.bossDemonGhostAttack' }] }] }
