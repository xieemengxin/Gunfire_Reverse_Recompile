# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Pet/RemotePetMoveFsm.pyc
# RelativePath: clientlogic/cl_betreedata/Pet/RemotePetMoveFsm.pyc
# Source Generated with Decompyle++
# File: RemotePetMoveFsm.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.NeedToRescue(oAgent) == 1


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.IsEnterFight(oAgent) == True


def Func2(oAgent):
    return cl_betree.servantagent.CAgent.NeedToRescue(oAgent) == 1


def Func3(oAgent):
    return cl_betree.servantagent.CAgent.IsEnterFight(oAgent) == False


def Func4(oAgent):
    return cl_betree.servantagent.CAgent.NeedToRescue(oAgent) == 1


def Func5(oAgent):
    return cl_betree.servantagent.CAgent.IsEnterFight(oAgent) == True


def Func6(oAgent):
    return cl_betree.servantagent.CAgent.NeedToRescue(oAgent) == 2


def Func7(oAgent):
    return cl_betree.servantagent.CAgent.IsEnterFight(oAgent) == True


def Func8(oAgent):
    return cl_betree.servantagent.CAgent.IsEnterFight(oAgent) == False

data = {
    'Name': 'RemotePetMoveFsm',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': True,
    'Ver': 50,
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
                        'TargetFSMNodeID': 9 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 4,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 18,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 14,
                        'TransitionPhase': 1 }, {
                        'ID': 19,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 5,
                        'TransitionPhase': 1 }, {
                        'ID': 12,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Pet.RemotePatrol' },
                {
                    'ID': 5,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 20,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 14,
                        'TransitionPhase': 1 }, {
                        'ID': 21,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 4,
                        'TransitionPhase': 4 }, {
                        'ID': 22,
                        'Class': 'Effector',
                        'Method': (cl_betree.servantagent.CAgent.SetFightStatus, (1,)),
                        'Phase': 1,
                        'Flag': 'effector' }),
                    'ReferenceBehavior': 'Pet.RemoteMoveAttack' },
                {
                    'ID': 9,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 15,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 14,
                        'TransitionPhase': 1 }, {
                        'ID': 16,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 5,
                        'TransitionPhase': 1 }, {
                        'ID': 17,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 1,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 4 }),
                    'ReferenceBehavior': 'Pet.MeleePetInit' },
                {
                    'ID': 14,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 26,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 23,
                        'TransitionPhase': 1 },),
                    'ReferenceBehavior': 'Pet.PetRescue' },
                {
                    'ID': 23,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 24,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 5,
                        'TransitionPhase': 1 }, {
                        'ID': 25,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 4,
                        'TransitionPhase': 4 }),
                    'Method': None,
                    'IsEndState': False }] }] }
