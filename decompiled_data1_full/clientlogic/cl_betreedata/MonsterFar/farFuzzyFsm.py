# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFar/farFuzzyFsm.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFar/farFuzzyFsm.pyc
# Source Generated with Decompyle++
# File: farFuzzyFsm.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.NeedToDodge(oAgent) == 1


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.NeedToDodge(oAgent) == 1


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.NeedToDodge(oAgent) == 1


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.NeedToDodge(oAgent) == 1


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'

data = {
    'Name': 'farFuzzyFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 49,
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
                        'TargetFSMNodeID': 38 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 38,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 41,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 39,
                        'TransitionPhase': 4 }, {
                        'ID': 42,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 40,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 39,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 44,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 47,
                        'TransitionPhase': 1 }, {
                        'ID': 43,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 110,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolFace' },
                {
                    'ID': 40,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 45,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 47,
                        'TransitionPhase': 1 }, {
                        'ID': 46,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 111,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolPos' },
                {
                    'ID': 47,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 49,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 58 }, {
                        'ID': 48,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.farAttackmsg' },
                {
                    'ID': 50,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 51,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 100,
                        'TransitionPhase': 1 }, {
                        'ID': 52,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 54,
                        'TransitionPhase': 1 }, {
                        'ID': 87,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 79 }),
                    'ReferenceBehavior': 'MonsterFar.farFuzzyChargeAttack' },
                {
                    'ID': 54,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 55,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 50 }, {
                        'ID': 56,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.dodge' },
                {
                    'ID': 58,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 86,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 79 },),
                    'ReferenceBehavior': 'Common.moveToShowPos' },
                {
                    'ID': 65,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 67,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 100,
                        'TransitionPhase': 1 }, {
                        'ID': 68,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 69,
                        'TransitionPhase': 1 }, {
                        'ID': 88,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 79 }),
                    'ReferenceBehavior': 'MonsterFar.farFuzzyGuerrillaAttack' },
                {
                    'ID': 69,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 71,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 65 }, {
                        'ID': 70,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.dodge' },
                {
                    'ID': 72,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 74,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 100,
                        'TransitionPhase': 1 }, {
                        'ID': 75,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 76,
                        'TransitionPhase': 1 }, {
                        'ID': 89,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 79 }),
                    'ReferenceBehavior': 'MonsterFar.farFuzzySquareGuerrillaAttack' },
                {
                    'ID': 76,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 78,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 72 }, {
                        'ID': 77,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.dodge' },
                {
                    'ID': 79,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 82,
                        'Class': 'FuzzyTransition',
                        'Method': (cl_betree.monsteragent.CAgent.FuzzyFarCharge, ()),
                        'Flag': 'transition',
                        'TargetFSMNodeID': 50 }, {
                        'ID': 84,
                        'Class': 'FuzzyTransition',
                        'Method': (cl_betree.monsteragent.CAgent.FuzzyFarGuerrilla, ()),
                        'Flag': 'transition',
                        'TargetFSMNodeID': 65 }, {
                        'ID': 85,
                        'Class': 'FuzzyTransition',
                        'Method': (cl_betree.monsteragent.CAgent.FuzzyFarSquareGuerrilla, ()),
                        'Flag': 'transition',
                        'TargetFSMNodeID': 72 }, {
                        'ID': 91,
                        'Class': 'FuzzyTransition',
                        'Method': (cl_betree.monsteragent.CAgent.FuzzyFarHide, ()),
                        'Flag': 'transition',
                        'TargetFSMNodeID': 98 }),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 90,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 92,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 100,
                        'TransitionPhase': 1 }, {
                        'ID': 93,
                        'Class': 'Transition',
                        'Method': (Func11, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 94,
                        'TransitionPhase': 1 }, {
                        'ID': 97,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 79 }),
                    'ReferenceBehavior': 'MonsterFar.farFuzzyHideAttack' },
                {
                    'ID': 94,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 96,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 90 }, {
                        'ID': 95,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.dodge' },
                {
                    'ID': 98,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 99,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 90 },),
                    'ReferenceBehavior': 'MonsterFar.hide' },
                {
                    'ID': 100,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 101,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 102 }, {
                        'ID': 109,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 102,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 106,
                        'Class': 'Transition',
                        'Method': (Func12, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 47,
                        'TransitionPhase': 1 }, {
                        'ID': 107,
                        'Class': 'Transition',
                        'Method': (Func13, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 39,
                        'TransitionPhase': 4 }, {
                        'ID': 108,
                        'Class': 'Transition',
                        'Method': (Func14, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 40,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolGoback' }] }] }
