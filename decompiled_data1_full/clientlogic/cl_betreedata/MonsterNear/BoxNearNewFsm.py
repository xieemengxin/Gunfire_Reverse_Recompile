# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterNear/BoxNearNewFsm.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterNear/BoxNearNewFsm.pyc
# Source Generated with Decompyle++
# File: BoxNearNewFsm.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(8050, oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(8050, oAgent) == True

data = {
    'Name': 'BoxNearNewFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 35,
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
                        'TargetFSMNodeID': 21 }, {
                        'ID': 20,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 18,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'Common.nearAttackmsg' },
                {
                    'ID': 18,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 19,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 14 },),
                    'ReferenceBehavior': 'MonsterNear.BoxNearClear' },
                {
                    'ID': 21,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 22,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 18,
                        'TransitionPhase': 1 },),
                    'ReferenceBehavior': 'MonsterNear.BoxNearRunNew' }] }] }
