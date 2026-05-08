# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossDesertTest/bossDesertFsm.pyc
# RelativePath: clientlogic/cl_betreedata/BossDesertTest/bossDesertFsm.pyc
# Source Generated with Decompyle++
# File: bossDesertFsm.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetNextState('qianxing', oAgent) == 1


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetNextState('zuanchu', oAgent) == 1


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetNextState('zuanchu', oAgent) == 2


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetNextState('zuanchu', oAgent) == 3


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.GetNextState('qianxing', oAgent) == 1

data = {
    'Name': 'bossDesertFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 98,
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
                        'TargetFSMNodeID': 140 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 126,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 127,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 145,
                        'TransitionPhase': 1 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 140,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 141,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 142 },),
                    'ReferenceBehavior': 'BossDesertTest.Born' },
                {
                    'ID': 142,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 144,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 126 }, {
                        'ID': 143,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossDesertTest.Patrolmsg' },
                {
                    'ID': 145,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 147,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 160 }, {
                        'ID': 146,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossDesertTest.Attackmsg' },
                {
                    'ID': 148,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 149,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 150 },),
                    'ReferenceBehavior': 'BossDesertTest.Goback' },
                {
                    'ID': 150,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 151,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 153 }, {
                        'ID': 152,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossDesertTest.Patrolmsg' },
                {
                    'ID': 153,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 154,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 155,
                        'TransitionPhase': 1 },),
                    'ReferenceBehavior': 'BossDesertTest.PatrolPos' },
                {
                    'ID': 155,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 156,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 168 }, {
                        'ID': 157,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'BossDesertTest.Attackmsg' },
                {
                    'ID': 158,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 159,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 168 },),
                    'ReferenceBehavior': 'BossDesertTest.HeadDive' },
                {
                    'ID': 160,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 161,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 166,
                        'TransitionPhase': 4 }, {
                        'ID': 162,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 158,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'BossDesertTest.HeadAttack' },
                {
                    'ID': 163,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 164,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 166,
                        'TransitionPhase': 4 }, {
                        'ID': 165,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 160 }),
                    'ReferenceBehavior': 'BossDesertTest.HeadAppear' },
                {
                    'ID': 166,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 167,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 150 },),
                    'ReferenceBehavior': 'BossDesertTest.HeadGobackDive' },
                {
                    'ID': 168,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 169,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 148,
                        'TransitionPhase': 1 }, {
                        'ID': 170,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 163,
                        'TransitionPhase': 1 }, {
                        'ID': 171,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 177,
                        'TransitionPhase': 1 }, {
                        'ID': 172,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 173,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'BossDesertTest.Swimming' },
                {
                    'ID': 173,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 174,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 168 },),
                    'ReferenceBehavior': 'BossDesertTest.SwimmingAttack' },
                {
                    'ID': 175,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 176,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 150 },),
                    'ReferenceBehavior': 'BossDesertTest.TailGobackDive' },
                {
                    'ID': 177,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 178,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 175,
                        'TransitionPhase': 4 }, {
                        'ID': 179,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 180 }),
                    'ReferenceBehavior': 'BossDesertTest.TailAppear' },
                {
                    'ID': 180,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 181,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 175,
                        'TransitionPhase': 4 }, {
                        'ID': 182,
                        'Class': 'Transition',
                        'Method': (Func11, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 183,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'BossDesertTest.TailAttack' },
                {
                    'ID': 183,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 184,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 168 },),
                    'ReferenceBehavior': 'BossDesertTest.TailDive' }] }] }
