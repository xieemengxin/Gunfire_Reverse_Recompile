# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFar/handbombGuerrillaFsm.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFar/handbombGuerrillaFsm.pyc
# Source Generated with Decompyle++
# File: handbombGuerrillaFsm.pyc (Python 3.6)

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
    return cl_betree.monsteragent.CAgent.GetHateListCnt(oAgent) < 1


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CalCheckVal(oAgent) >= 10


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolface'


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetPatrol(oAgent) == 'patrolpos'

data = {
    'Name': 'handbombGuerrillaFsm',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': True,
    'Ver': 27,
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
                        'TargetFSMNodeID': 29 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 29,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 32,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 30,
                        'TransitionPhase': 4 }, {
                        'ID': 33,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 31,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 30,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 36,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 38,
                        'TransitionPhase': 1 }, {
                        'ID': 34,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 74,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolFace' },
                {
                    'ID': 31,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 37,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 38,
                        'TransitionPhase': 1 }, {
                        'ID': 35,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 75,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolPos' },
                {
                    'ID': 38,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 39,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 2,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 42 }, {
                        'ID': 40,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.TestUpdateAIRuningState, (3,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.farAttackmsg' },
                {
                    'ID': 41,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 44,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 67,
                        'TransitionPhase': 1 }, {
                        'ID': 55,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 50 }),
                    'ReferenceBehavior': 'MonsterFar.handbombGuerrillaAttack' },
                {
                    'ID': 42,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 43,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 50 },),
                    'ReferenceBehavior': 'Common.moveToShowPos' },
                {
                    'ID': 50,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 62,
                        'Class': 'FuzzyTransition',
                        'Method': (cl_betree.monsteragent.CAgent.FuzzyGrenadeGuerrilla, ()),
                        'Flag': 'transition',
                        'TargetFSMNodeID': 41 }, {
                        'ID': 63,
                        'Class': 'FuzzyTransition',
                        'Method': (cl_betree.monsteragent.CAgent.FuzzyGrenadeHide, ()),
                        'Flag': 'transition',
                        'TargetFSMNodeID': 59 }),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 59,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 61,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 64 },),
                    'ReferenceBehavior': 'MonsterFar.hide' },
                {
                    'ID': 64,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 65,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 67,
                        'TransitionPhase': 1 }, {
                        'ID': 66,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 50 }),
                    'ReferenceBehavior': 'MonsterFar.handbombHideAttack' },
                {
                    'ID': 67,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 69,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 68 }, {
                        'ID': 70,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Common.patrolmsg' },
                {
                    'ID': 68,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 71,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 38,
                        'TransitionPhase': 1 }, {
                        'ID': 72,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 30,
                        'TransitionPhase': 4 }, {
                        'ID': 73,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 31,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'Common.patrolGoback' }] }] }
