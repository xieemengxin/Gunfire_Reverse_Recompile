# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Hero/QianSuiNearFsm.pyc
# RelativePath: clientlogic/cl_betreedata/Hero/QianSuiNearFsm.pyc
# Source Generated with Decompyle++
# File: QianSuiNearFsm.pyc (Python 3.6)

import cl_betree.heroagent

def Func0(oAgent):
    return cl_betree.heroagent.CAgent.NeedToRescue(oAgent) == 1


def Func1(oAgent):
    return cl_betree.heroagent.CAgent.ChooseTarget(oAgent) == 2


def Func2(oAgent):
    return cl_betree.heroagent.CAgent.NeedToRescue(oAgent) == 1


def Func3(oAgent):
    return cl_betree.heroagent.CAgent.SearchNearShareItem(12, 3, oAgent) == 1


def Func4(oAgent):
    return cl_betree.heroagent.CAgent.ChooseTarget(oAgent) == 1


def Func5(oAgent):
    return cl_betree.heroagent.CAgent.NeedToRescue(oAgent) != 1


def Func6(oAgent):
    return cl_betree.heroagent.CAgent.NeedToRescue(oAgent) == 1


def Func7(oAgent):
    return cl_betree.heroagent.CAgent.ChooseTarget(oAgent) == 1

data = {
    'Name': 'QianSuiNearFsm',
    'ID': 0,
    'AgentType': 'cl_betree.heroagent',
    'IsFSM': True,
    'Ver': 88,
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
                        'TargetFSMNodeID': 55 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 54,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 57,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 56,
                        'TransitionPhase': 1 }, {
                        'ID': 65,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 55,
                        'TransitionPhase': 1 }, {
                        'ID': 79,
                        'Class': 'Precondition',
                        'Method': (cl_betree.heroagent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Hero.QianSuiNearAttack' },
                {
                    'ID': 55,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 63,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 56,
                        'TransitionPhase': 1 }, {
                        'ID': 68,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 67,
                        'TransitionPhase': 1 }, {
                        'ID': 80,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 54,
                        'TransitionPhase': 1 }, {
                        'ID': 73,
                        'Class': 'Precondition',
                        'Method': (cl_betree.heroagent.CAgent.HaltPerform, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Hero.HeroPatrol' },
                {
                    'ID': 56,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 58,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 55,
                        'TransitionPhase': 4 }, {
                        'ID': 74,
                        'Class': 'Precondition',
                        'Method': (cl_betree.heroagent.CAgent.HaltPerform, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 81,
                        'Class': 'Precondition',
                        'Method': (cl_betree.heroagent.CAgent.ClearArrivePos, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Hero.HeroRescue' },
                {
                    'ID': 67,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 70,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 56,
                        'TransitionPhase': 1 }, {
                        'ID': 76,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 54,
                        'TransitionPhase': 1 }, {
                        'ID': 77,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 55 }, {
                        'ID': 75,
                        'Class': 'Precondition',
                        'Method': (cl_betree.heroagent.CAgent.HaltPerform, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Hero.HeroShare' }] }] }
