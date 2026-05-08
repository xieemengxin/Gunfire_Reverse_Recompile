# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/farNododgefsm.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/farNododgefsm.pyc
# Source Generated with Decompyle++
# File: farNododgefsm.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10

data = {
    'Name': 'farNododgefsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 19,
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
                    'ID': 10,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 18,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 19 },),
                    'ReferenceBehavior': 'DemoScene.farattackmsg' },
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
                    'ID': 19,
                    'Class': 'ReferenceBehavior',
                    'ReferenceBehavior': 'DemoScene.farbackattack' }] }] }
