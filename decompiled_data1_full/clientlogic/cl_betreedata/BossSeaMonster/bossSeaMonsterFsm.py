# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossSeaMonster/bossSeaMonsterFsm.pyc
# RelativePath: clientlogic/cl_betreedata/BossSeaMonster/bossSeaMonsterFsm.pyc
# Source Generated with Decompyle++
# File: bossSeaMonsterFsm.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 1


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10

data = {
    'Name': 'bossSeaMonsterFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 30,
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
                        'ID': 4,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 1,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 3 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 3,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 6,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 5 },),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 5,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 7,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 8,
                        'TransitionPhase': 1 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 8,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 9,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 17 },),
                    'ReferenceBehavior': 'Common.farAttackmsg' },
                {
                    'ID': 10,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 29,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 32,
                        'TransitionPhase': 4 }, {
                        'ID': 30,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 14,
                        'TransitionPhase': 4 }, {
                        'ID': 31,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 16,
                        'TransitionPhase': 4 }, {
                        'ID': 39,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossSeaMonster.bossSeaMonsterPhase1' },
                {
                    'ID': 14,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 27,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 32,
                        'TransitionPhase': 4 }, {
                        'ID': 28,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 16,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'BossSeaMonster.bossSeaMonsterPhase2' },
                {
                    'ID': 16,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 26,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 32,
                        'TransitionPhase': 4 },),
                    'ReferenceBehavior': 'BossSeaMonster.bossSeaMonsterPhase3' },
                {
                    'ID': 17,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 40,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 32,
                        'TransitionPhase': 4 }, {
                        'ID': 41,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 10,
                        'TransitionPhase': 4 }, {
                        'ID': 42,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 14,
                        'TransitionPhase': 4 }, {
                        'ID': 43,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 16,
                        'TransitionPhase': 4 }, {
                        'ID': 18,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossSeaMonster.bossSeaMonsterShow' },
                {
                    'ID': 32,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 34,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 45 }, {
                        'ID': 33,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossSeaMonster.bossSeaMonsterpatrolmsg' },
                {
                    'ID': 35,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 36,
                        'Class': 'Transition',
                        'Method': (Func11, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 37,
                        'TransitionPhase': 4 },),
                    'ReferenceBehavior': 'BossSeaMonster.bossSeaMonsterpatrolmove' },
                {
                    'ID': 37,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 38,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 10 }, {
                        'ID': 44,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.farAttackmsg' },
                {
                    'ID': 45,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 47,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 3,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 35 }, {
                        'ID': 48,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossSeaMonster.bossNotTargetAtt' }] }] }
