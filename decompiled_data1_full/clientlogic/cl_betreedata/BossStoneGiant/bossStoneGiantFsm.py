# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossStoneGiant/bossStoneGiantFsm.pyc
# RelativePath: clientlogic/cl_betreedata/BossStoneGiant/bossStoneGiantFsm.pyc
# Source Generated with Decompyle++
# File: bossStoneGiantFsm.pyc (Python 3.6)

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
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 4


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 4


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 4


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10

data = {
    'Name': 'bossStoneGiantFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 103,
    'Node': [
        {
            'ID': 1,
            'Class': 'FSM',
            'InitialID': 63,
            'Node': [
                {
                    'ID': 63,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 64,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 1,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 89 },),
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
                        'TargetFSMNodeID': 73 },),
                    'ReferenceBehavior': 'Common.farAttackmsg' },
                {
                    'ID': 70,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 71,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 67,
                        'TransitionPhase': 1 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 73,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 94,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 91,
                        'TransitionPhase': 4 }, {
                        'ID': 104,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 75,
                        'TransitionPhase': 4 }, {
                        'ID': 105,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 79,
                        'TransitionPhase': 4 }, {
                        'ID': 106,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 83,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'BossStoneGiant.bossStoneGiantAttack' },
                {
                    'ID': 75,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 77,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 76 }, {
                        'ID': 97,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 91,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'BossStoneGiant.bossStoneGiantPhase2' },
                {
                    'ID': 76,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 78,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 83,
                        'TransitionPhase': 4 }, {
                        'ID': 86,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 79,
                        'TransitionPhase': 4 }, {
                        'ID': 95,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 91,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'BossStoneGiant.bossStoneGiantPhase2Attack' },
                {
                    'ID': 79,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 80,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 81 }, {
                        'ID': 96,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 91,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'BossStoneGiant.bossStoneGiantPhase3' },
                {
                    'ID': 81,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 82,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 83,
                        'TransitionPhase': 4 }, {
                        'ID': 98,
                        'Class': 'Transition',
                        'Method': (Func11, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 91,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'BossStoneGiant.bossStoneGiantPhase3Attack' },
                {
                    'ID': 83,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 87,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 88 }, {
                        'ID': 99,
                        'Class': 'Transition',
                        'Method': (Func12, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 91,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'BossStoneGiant.bossStoneGiantPhase4' },
                {
                    'ID': 88,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 107,
                        'Class': 'Transition',
                        'Method': (Func13, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 91,
                        'TransitionPhase': 4 },),
                    'ReferenceBehavior': 'BossStoneGiant.bossStoneGiantAttack' },
                {
                    'ID': 89,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 90,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 65 },),
                    'ReferenceBehavior': 'BossStoneGiant.bossStoneGiantAppear' },
                {
                    'ID': 91,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 101,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 100 },),
                    'ReferenceBehavior': 'BossStoneGiant.bossStoneGiantpatrolmsg' },
                {
                    'ID': 93,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 103,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 73 },),
                    'ReferenceBehavior': 'Common.farAttackmsg' },
                {
                    'ID': 100,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 102,
                        'Class': 'Transition',
                        'Method': (Func14, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 93,
                        'TransitionPhase': 4 },),
                    'ReferenceBehavior': 'BossStoneGiant.bossStoneGiantpatolmove' }] }] }
