# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/fourfsm.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/fourfsm.pyc
# Source Generated with Decompyle++
# File: fourfsm.pyc (Python 3.6)

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
    return cl_betree.monsteragent.CAgent.NeedToDodge(oAgent) == 1

data = {
    'Name': 'fourfsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 11,
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
                        'TargetFSMNodeID': 4 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 4,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 7,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 5,
                        'TransitionPhase': 1 }, {
                        'ID': 8,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 6,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'DemoScene.patrolmsg' },
                {
                    'ID': 5,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 11,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 14,
                        'TransitionPhase': 1 }, {
                        'ID': 21,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'DemoScene.patrolface' },
                {
                    'ID': 6,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 12,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 14,
                        'TransitionPhase': 1 }, {
                        'ID': 22,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'DemoScene.patrolpos' },
                {
                    'ID': 14,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 19,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 18 }, {
                        'ID': 33,
                        'Class': 'Precondition',
                        'Attachment': ({
                            'ID': 34,
                            'Class': 'Precondition',
                            'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                            'Phase': 1,
                            'Flag': 'precondition',
                            'BinaryOperator': 'And' },),
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 35,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'DemoScene.farattackmsg' },
                {
                    'ID': 18,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 20,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 25,
                        'TransitionPhase': 1 }, {
                        'ID': 28,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 27,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'DemoScene.fourattack' },
                {
                    'ID': 25,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 26,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 4 },),
                    'ReferenceBehavior': 'DemoScene.goback' },
                {
                    'ID': 27,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 29,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 18 }, {
                        'ID': 32,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'DemoScene.dodge' }] }] }
