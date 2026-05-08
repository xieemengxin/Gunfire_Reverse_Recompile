# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterNear/BoxNearWipeFsm.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterNear/BoxNearWipeFsm.pyc
# Source Generated with Decompyle++
# File: BoxNearWipeFsm.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(8104, oAgent) == False


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(8104, oAgent) == True

data = {
    'Name': 'BoxNearWipeFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 39,
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
                        'TargetFSMNodeID': 10 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 10,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 11,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 12 },),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 12,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 13,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 15,
                        'TransitionPhase': 1 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 15,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 16,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 25 },),
                    'ReferenceBehavior': 'Common.nearAttackmsg' },
                {
                    'ID': 17,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 24,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 25,
                        'TransitionPhase': 4 },),
                    'ReferenceBehavior': 'MonsterNear.BoxNearEscape' },
                {
                    'ID': 25,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 26,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 17,
                        'TransitionPhase': 4 },),
                    'ReferenceBehavior': 'MonsterNear.BoxNearAlert' }] }] }
