# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFar/FishBombGuerrillaFsm.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFar/FishBombGuerrillaFsm.pyc
# Source Generated with Decompyle++
# File: FishBombGuerrillaFsm.pyc (Python 3.6)

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
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'

data = {
    'Name': 'FishBombGuerrillaFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 8,
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
                        'ID': 3,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 1,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 4 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 4,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 5,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 7,
                        'TransitionPhase': 4 }, {
                        'ID': 6,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 11,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 7,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 10,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 15,
                        'TransitionPhase': 1 }, {
                        'ID': 8,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 9,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolFace' },
                {
                    'ID': 11,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 14,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 15,
                        'TransitionPhase': 1 }, {
                        'ID': 12,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 13,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolPos' },
                {
                    'ID': 15,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 17,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 18 }, {
                        'ID': 16,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.farAttackmsg' },
                {
                    'ID': 18,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 19,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 20 },),
                    'ReferenceBehavior': 'Common.moveToShowPos' },
                {
                    'ID': 20,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 21,
                        'Class': 'FuzzyTransition',
                        'Method': (cl_betree.monsteragent.CAgent.FuzzyGrenadeGuerrilla, ()),
                        'Flag': 'transition',
                        'TargetFSMNodeID': 23 }, {
                        'ID': 22,
                        'Class': 'FuzzyTransition',
                        'Method': (cl_betree.monsteragent.CAgent.FuzzyGrenadeHide, ()),
                        'Flag': 'transition',
                        'TargetFSMNodeID': 24 }),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 23,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 29,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 35,
                        'TransitionPhase': 1 }, {
                        'ID': 30,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 32,
                        'TransitionPhase': 1 }, {
                        'ID': 31,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 20 }),
                    'ReferenceBehavior': 'MonsterFar.FishBombGuerrillaAttack' },
                {
                    'ID': 24,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 25,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 26 },),
                    'ReferenceBehavior': 'MonsterFar.hide' },
                {
                    'ID': 26,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 27,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 35,
                        'TransitionPhase': 1 }, {
                        'ID': 28,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 20 }),
                    'ReferenceBehavior': 'MonsterFar.handbombHideAttack' },
                {
                    'ID': 32,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 34,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 20 }, {
                        'ID': 33,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.dodge' },
                {
                    'ID': 35,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 36,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 38 }, {
                        'ID': 37,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 38,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 39,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 15,
                        'TransitionPhase': 1 }, {
                        'ID': 40,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 7,
                        'TransitionPhase': 4 }, {
                        'ID': 41,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 11,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolGoback' }] }] }
