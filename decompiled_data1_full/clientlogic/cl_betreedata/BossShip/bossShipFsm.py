# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossShip/bossShipFsm.pyc
# RelativePath: clientlogic/cl_betreedata/BossShip/bossShipFsm.pyc
# Source Generated with Decompyle++
# File: bossShipFsm.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10

data = {
    'Name': 'bossShipFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 83,
    'Node': [
        {
            'ID': 1,
            'Class': 'FSM',
            'InitialID': 63,
            'Node': [
                {
                    'ID': 62,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 86,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 87,
                        'TransitionPhase': 4 },),
                    'ReferenceBehavior': 'BossShip.bossShipAttack' },
                {
                    'ID': 63,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 64,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 1,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 65 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 65,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 72,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 70 },),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 67,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 68,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 81 },),
                    'ReferenceBehavior': 'Common.farAttackmsg' },
                {
                    'ID': 70,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 71,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 67,
                        'TransitionPhase': 1 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 81,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 83,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 62 }, {
                        'ID': 85,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossShip.bossShipSummon' },
                {
                    'ID': 87,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 90,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 88 },),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 88,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 89,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 91,
                        'TransitionPhase': 1 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 91,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 92,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 62 },),
                    'ReferenceBehavior': 'Common.farAttackmsg' }] }] }
