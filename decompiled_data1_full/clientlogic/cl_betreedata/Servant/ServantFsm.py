# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Servant/ServantFsm.pyc
# RelativePath: clientlogic/cl_betreedata/Servant/ServantFsm.pyc
# Source Generated with Decompyle++
# File: ServantFsm.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.NeedToRescue(oAgent) == 1


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.IsHeroCtrlUsePF(oAgent) == 1


def Func2(oAgent):
    return cl_betree.servantagent.CAgent.IsEnterFight(oAgent) == True


def Func3(oAgent):
    return cl_betree.servantagent.CAgent.NeedToRescue(oAgent) == 1


def Func4(oAgent):
    return cl_betree.servantagent.CAgent.IsHeroCtrlUsePF(oAgent) == 1


def Func5(oAgent):
    return cl_betree.servantagent.CAgent.IsEnterFight(oAgent) == False


def Func6(oAgent):
    return cl_betree.servantagent.CAgent.NeedToRescue(oAgent) == 1


def Func7(oAgent):
    return cl_betree.servantagent.CAgent.IsHeroCtrlUsePF(oAgent) == 1


def Func8(oAgent):
    return cl_betree.servantagent.CAgent.IsEnterFight(oAgent) == False


def Func9(oAgent):
    return cl_betree.servantagent.CAgent.NeedToRescue(oAgent) == 2


def Func10(oAgent):
    return cl_betree.servantagent.CAgent.NeedToRescue(oAgent) == 1


def Func11(oAgent):
    return cl_betree.servantagent.CAgent.GetPhase(oAgent) == 2


def Func12(oAgent):
    return cl_betree.servantagent.CAgent.NeedToRescue(oAgent) == 1


def Func13(oAgent):
    return cl_betree.servantagent.CAgent.IsHeroCtrlUsePF(oAgent) == 1


def Func14(oAgent):
    return cl_betree.servantagent.CAgent.IsEnterFight(oAgent) == True


def Func15(oAgent):
    return cl_betree.servantagent.CAgent.GetPhase(oAgent) == 1


def Func16(oAgent):
    return cl_betree.servantagent.CAgent.GetPhase(oAgent) == 2


def Func17(oAgent):
    return cl_betree.servantagent.CAgent.NeedToRescue(oAgent) == 2


def Func18(oAgent):
    return cl_betree.servantagent.CAgent.IsHeroCtrlUsePF(oAgent) == 1


def Func19(oAgent):
    return cl_betree.servantagent.CAgent.IsEnterFight(oAgent) == True


def Func20(oAgent):
    return cl_betree.servantagent.CAgent.IsEnterFight(oAgent) == False


def Func21(oAgent):
    return cl_betree.servantagent.CAgent.IsHeroCtrlUsePF(oAgent) == 1


def Func22(oAgent):
    return cl_betree.servantagent.CAgent.IsEnterFight(oAgent) == True


def Func23(oAgent):
    return cl_betree.servantagent.CAgent.IsEnterFight(oAgent) == False


def Func24(oAgent):
    return cl_betree.servantagent.CAgent.NeedToRescue(oAgent) == 1


def Func25(oAgent):
    return cl_betree.servantagent.CAgent.IsHeroCtrlUsePF(oAgent) == 1


def Func26(oAgent):
    return cl_betree.servantagent.CAgent.IsEnterFight(oAgent) == True

data = {
    'Name': 'ServantFsm',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': True,
    'Ver': 43,
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
                        'ID': 25,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 26,
                        'TransitionPhase': 1 }, {
                        'ID': 46,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 37,
                        'TransitionPhase': 1 }, {
                        'ID': 48,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 5,
                        'TransitionPhase': 1 }, {
                        'ID': 60,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 61,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.HaltPerform, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 63,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.UpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Servant.ServantPatrol' },
                {
                    'ID': 5,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 29,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 26,
                        'TransitionPhase': 1 }, {
                        'ID': 49,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 37,
                        'TransitionPhase': 1 }, {
                        'ID': 111,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 127,
                        'TransitionPhase': 4 }, {
                        'ID': 123,
                        'Class': 'Effector',
                        'Method': (cl_betree.servantagent.CAgent.SendFightStatusMessage, (1, False)),
                        'Phase': 3,
                        'Flag': 'effector' }, {
                        'ID': 21,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 24,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.HaltPerform, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 64,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.UpdateAIRuningState, (2,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 122,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.SendFightStatusMessage, (1, True)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Servant.ServantAttack' },
                {
                    'ID': 11,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 30,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 84,
                        'TransitionPhase': 1 }, {
                        'ID': 50,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 37,
                        'TransitionPhase': 1 }, {
                        'ID': 112,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 68,
                        'TransitionPhase': 4 }, {
                        'ID': 125,
                        'Class': 'Effector',
                        'Method': (cl_betree.servantagent.CAgent.SendFightStatusMessage, (2, False)),
                        'Phase': 3,
                        'Flag': 'effector' }, {
                        'ID': 12,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 19,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.HaltPerform, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 67,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.UpdateAIRuningState, (2,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 124,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.SendFightStatusMessage, (2, True)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Servant.ServantTurret' },
                {
                    'ID': 26,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 104,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 100,
                        'TransitionPhase': 1 }, {
                        'ID': 35,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 65,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.UpdateAIRuningState, (2,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 75,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Servant.ServantRescue' },
                {
                    'ID': 37,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 96,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 76,
                        'TransitionPhase': 4 }, {
                        'ID': 97,
                        'Class': 'Transition',
                        'Method': (Func11, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 108,
                        'TransitionPhase': 4 }, {
                        'ID': 118,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 100 }, {
                        'ID': 38,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 62,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.HaltPerform, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 66,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.UpdateAIRuningState, (2,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Servant.ServantOperate' },
                {
                    'ID': 68,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 69,
                        'Class': 'Transition',
                        'Method': (Func12, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 84,
                        'TransitionPhase': 1 }, {
                        'ID': 70,
                        'Class': 'Transition',
                        'Method': (Func13, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 37,
                        'TransitionPhase': 1 }, {
                        'ID': 73,
                        'Class': 'Transition',
                        'Method': (Func14, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 11,
                        'TransitionPhase': 1 }, {
                        'ID': 74,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.UpdateAIRuningState, (1,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Servant.ServantPhase2Patrol' },
                {
                    'ID': 76,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 77,
                        'Class': 'Transition',
                        'Method': (Func15, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 26,
                        'TransitionPhase': 1 }, {
                        'ID': 78,
                        'Class': 'Transition',
                        'Method': (Func16, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 84,
                        'TransitionPhase': 1 }),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 79,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 88,
                        'Class': 'Transition',
                        'Method': (Func17, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 85,
                        'TransitionPhase': 1 }, {
                        'ID': 80,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 81,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.UpdateAIRuningState, (2,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 82,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 126,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.ClearArrivePos, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Servant.ServantRescue' },
                {
                    'ID': 84,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 86,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 79 },),
                    'ReferenceBehavior': 'Servant.ServantChangePhase' },
                {
                    'ID': 85,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 114,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 108 }, {
                        'ID': 95,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'Servant.ServantChangePhase' },
                {
                    'ID': 100,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 101,
                        'Class': 'Transition',
                        'Method': (Func18, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 37,
                        'TransitionPhase': 1 }, {
                        'ID': 116,
                        'Class': 'Transition',
                        'Method': (Func19, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 5,
                        'TransitionPhase': 1 }, {
                        'ID': 117,
                        'Class': 'Transition',
                        'Method': (Func20, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 127,
                        'TransitionPhase': 1 }, {
                        'ID': 105,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 108,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 119,
                        'Class': 'Transition',
                        'Method': (Func21, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 37,
                        'TransitionPhase': 1 }, {
                        'ID': 120,
                        'Class': 'Transition',
                        'Method': (Func22, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 11,
                        'TransitionPhase': 1 }, {
                        'ID': 121,
                        'Class': 'Transition',
                        'Method': (Func23, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 68,
                        'TransitionPhase': 1 }),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 127,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 128,
                        'Class': 'Transition',
                        'Method': (Func24, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 26,
                        'TransitionPhase': 1 }, {
                        'ID': 129,
                        'Class': 'Transition',
                        'Method': (Func25, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 37,
                        'TransitionPhase': 1 }, {
                        'ID': 131,
                        'Class': 'Transition',
                        'Method': (Func26, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 5,
                        'TransitionPhase': 1 }, {
                        'ID': 133,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 4 }),
                    'ReferenceBehavior': 'Servant.ServantHold' }] }] }
