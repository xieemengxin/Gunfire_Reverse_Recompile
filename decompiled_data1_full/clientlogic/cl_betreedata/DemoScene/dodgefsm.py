# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/dodgefsm.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/dodgefsm.pyc
# Source Generated with Decompyle++
# File: dodgefsm.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.NeedToDodge(oAgent) == 1

data = {
    'Name': 'dodgefsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 14,
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
                        'TargetFSMNodeID': 12 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 6,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 15,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 16 },),
                    'ReferenceBehavior': 'DemoScene.dodge' },
                {
                    'ID': 10,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 18,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 16 },),
                    'ReferenceBehavior': 'DemoScene.attackmsg' },
                {
                    'ID': 12,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 13,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 10,
                        'TransitionPhase': 1 },),
                    'ReferenceBehavior': 'DemoScene.patrolmsg' },
                {
                    'ID': 16,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 17,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 6,
                        'TransitionPhase': 1 },),
                    'ReferenceBehavior': 'DemoScene.stand' }] }] }
