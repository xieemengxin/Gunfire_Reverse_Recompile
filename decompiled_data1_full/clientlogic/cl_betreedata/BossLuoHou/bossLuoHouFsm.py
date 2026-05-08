# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossLuoHou/bossLuoHouFsm.pyc
# RelativePath: clientlogic/cl_betreedata/BossLuoHou/bossLuoHouFsm.pyc
# Source Generated with Decompyle++
# File: bossLuoHouFsm.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(8085, oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.StateTransition(8086, oAgent) == 2


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(8087, oAgent) == True


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(8085, oAgent) == True


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.StateTransition(8087, oAgent) == 2


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(8114, oAgent) == True


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(8085, oAgent) == True


def Func15(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func16(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func17(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(8086, oAgent) == True


def Func18(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(8087, oAgent) == True


def Func19(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 1


def Func20(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 2


def Func21(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func22(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func23(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1

data = {
    'Name': 'bossLuoHouFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 83,
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
                        'TargetFSMNodeID': 62 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 62,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 63,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 64 },),
                    'ReferenceBehavior': 'BossLuoHou.bossLuoHouAppear' },
                {
                    'ID': 64,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 65,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 93 },),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 72,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 80,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 81,
                        'TransitionPhase': 4 }, {
                        'ID': 98,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 97,
                        'TransitionPhase': 1 }, {
                        'ID': 105,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 75,
                        'TransitionPhase': 1 }, {
                        'ID': 108,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 76,
                        'TransitionPhase': 4 }, {
                        'ID': 109,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 78,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'BossLuoHou.bossLuoHouAttack' },
                {
                    'ID': 74,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 79,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 72 },),
                    'ReferenceBehavior': 'Common.farAttackmsg' },
                {
                    'ID': 75,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 117,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 77,
                        'TransitionPhase': 4 }, {
                        'ID': 118,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 81,
                        'TransitionPhase': 4 }, {
                        'ID': 119,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 76 }),
                    'ReferenceBehavior': 'BossLuoHou.bossLuoHouState2' },
                {
                    'ID': 76,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 84,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 81,
                        'TransitionPhase': 4 }, {
                        'ID': 102,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 97,
                        'TransitionPhase': 1 }, {
                        'ID': 107,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 77,
                        'TransitionPhase': 4 }, {
                        'ID': 110,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 78,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'BossLuoHou.bossLuoHouAttack2' },
                {
                    'ID': 77,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 86,
                        'Class': 'Transition',
                        'Method': (Func11, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 81,
                        'TransitionPhase': 4 }, {
                        'ID': 92,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 78 }),
                    'ReferenceBehavior': 'BossLuoHou.bossLuoHouState3' },
                {
                    'ID': 78,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 87,
                        'Class': 'Transition',
                        'Method': (Func12, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 81,
                        'TransitionPhase': 4 }, {
                        'ID': 120,
                        'Class': 'Transition',
                        'Method': (Func13, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 121,
                        'TransitionPhase': 1 }, {
                        'ID': 124,
                        'Class': 'Transition',
                        'Method': (Func14, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 97,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'BossLuoHou.bossLuoHouAttack3' },
                {
                    'ID': 81,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 95,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 82 },),
                    'ReferenceBehavior': 'BossLuoHou.bossLuoHoupatrolmsg' },
                {
                    'ID': 82,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 96,
                        'Class': 'Transition',
                        'Method': (Func15, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 74,
                        'TransitionPhase': 1 },),
                    'ReferenceBehavior': 'BossLuoHou.bossLuoHoupatrolmsg2' },
                {
                    'ID': 93,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 94,
                        'Class': 'Transition',
                        'Method': (Func16, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 74,
                        'TransitionPhase': 1 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 97,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 111,
                        'Class': 'Transition',
                        'Method': (Func17, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 75,
                        'TransitionPhase': 4 }, {
                        'ID': 112,
                        'Class': 'Transition',
                        'Method': (Func18, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 77,
                        'TransitionPhase': 4 }, {
                        'ID': 113,
                        'Class': 'Transition',
                        'Method': (Func19, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 72,
                        'TransitionPhase': 4 }, {
                        'ID': 114,
                        'Class': 'Transition',
                        'Method': (Func20, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 76,
                        'TransitionPhase': 4 }, {
                        'ID': 115,
                        'Class': 'Transition',
                        'Method': (Func21, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 78,
                        'TransitionPhase': 4 }, {
                        'ID': 116,
                        'Class': 'Transition',
                        'Method': (Func22, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 81,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'BossLuoHou.bossLuoHouBreakHand' },
                {
                    'ID': 121,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 122,
                        'Class': 'Transition',
                        'Method': (Func23, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 81,
                        'TransitionPhase': 4 }, {
                        'ID': 123,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 78 }),
                    'ReferenceBehavior': 'BossLuoHou.bossLuoHouState4' }] }] }
