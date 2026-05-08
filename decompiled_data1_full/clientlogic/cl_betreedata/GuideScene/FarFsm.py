# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/GuideScene/FarFsm.pyc
# RelativePath: clientlogic/cl_betreedata/GuideScene/FarFsm.pyc
# Source Generated with Decompyle++
# File: FarFsm.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'

data = {
    'Name': 'FarFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 40,
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
                        'TargetFSMNodeID': 50 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 42,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 43,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 53,
                        'TransitionPhase': 1 }, {
                        'ID': 44,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 45,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 46,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 47 },),
                    'ReferenceBehavior': 'Common.moveToShowPos' },
                {
                    'ID': 47,
                    'Class': 'ReferenceBehavior',
                    'ReferenceBehavior': 'GuideScene.farAreamoveAttack' },
                {
                    'ID': 50,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 51,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 42,
                        'TransitionPhase': 4 }, {
                        'ID': 52,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 42,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'GuideScene.patrolmsg' },
                {
                    'ID': 53,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 54,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 45 }, {
                        'ID': 55,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.farAttackmsg' }] }] }
