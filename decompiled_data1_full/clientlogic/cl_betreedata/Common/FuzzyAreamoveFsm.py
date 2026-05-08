# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Common/FuzzyAreamoveFsm.pyc
# RelativePath: clientlogic/cl_betreedata/Common/FuzzyAreamoveFsm.pyc
# Source Generated with Decompyle++
# File: FuzzyAreamoveFsm.pyc (Python 3.6)

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


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.NeedToDodge(oAgent) == 1


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.NeedToDodge(oAgent) == 1

data = {
    'Name': 'FuzzyAreamoveFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 28,
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
                        'TargetFSMNodeID': 36 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 36,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 39,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 37,
                        'TransitionPhase': 4 }, {
                        'ID': 40,
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
                        'ID': 43,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 45,
                        'TransitionPhase': 1 }, {
                        'ID': 41,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 81,
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
                        'ID': 44,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 45,
                        'TransitionPhase': 1 }, {
                        'ID': 42,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 82,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolPos' },
                {
                    'ID': 45,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 46,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 48 }, {
                        'ID': 47,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.farAttackmsg' },
                {
                    'ID': 48,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 49,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 58 },),
                    'ReferenceBehavior': 'Common.moveToShowPos' },
                {
                    'ID': 54,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 56,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 88 }, {
                        'ID': 55,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.dodge' },
                {
                    'ID': 58,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 86,
                        'Class': 'FuzzyTransition',
                        'Method': (cl_betree.monsteragent.CAgent.FuzzyOverallGuerrilla, ()),
                        'Flag': 'transition',
                        'TargetFSMNodeID': 88 }, {
                        'ID': 87,
                        'Class': 'FuzzyTransition',
                        'Method': (cl_betree.monsteragent.CAgent.FuzzyOverallAwait, ()),
                        'Flag': 'transition',
                        'TargetFSMNodeID': 89 }, {
                        'ID': 61,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.SetFightLogicType, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 73,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 75,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 89 }, {
                        'ID': 74,
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
                        'ID': 79,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 77 }, {
                        'ID': 78,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.SetFightLogicType, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 80,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 77,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 83,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 45,
                        'TransitionPhase': 1 }, {
                        'ID': 84,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 37,
                        'TransitionPhase': 4 }, {
                        'ID': 85,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 38,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolGoback' },
                {
                    'ID': 88,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 92,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 76,
                        'TransitionPhase': 1 }, {
                        'ID': 93,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 54,
                        'TransitionPhase': 1 }, {
                        'ID': 94,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 58 }, {
                        'ID': 90,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.SetFightLogicType, (4,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.FuzzyAreamoveAttack' },
                {
                    'ID': 89,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 95,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 76,
                        'TransitionPhase': 1 }, {
                        'ID': 96,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 73,
                        'TransitionPhase': 1 }, {
                        'ID': 97,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 58 }, {
                        'ID': 91,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.SetFightLogicType, (5,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.FuzzyAreamoveAwait' }] }] }
