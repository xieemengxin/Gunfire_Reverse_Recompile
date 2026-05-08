# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DeviceTurret/Fsm.pyc
# RelativePath: clientlogic/cl_betreedata/DeviceTurret/Fsm.pyc
# Source Generated with Decompyle++
# File: Fsm.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return oAgent.GetData('FollowMoveStatus') == 0


def Func1(oAgent):
    return oAgent.GetData('FollowMoveStatus') == 1


def Func2(oAgent):
    return cl_betree.servantagent.CAgent.CheckHasState(33150, oAgent) == True


def Func3(oAgent):
    return oAgent.GetData('FollowMoveStatus') == 1


def Func4(oAgent):
    return cl_betree.servantagent.CAgent.CheckHasState(33150, oAgent) == False


def Func5(oAgent):
    return oAgent.GetData('TransferPos') != None


def Func6(oAgent):
    return cl_betree.servantagent.CAgent.CheckSceneHasFightMonster(oAgent.GetConfig('HitRange'), oAgent) == False


def Func7(oAgent):
    return cl_betree.servantagent.CAgent.CheckHasState(33150, oAgent) == False


def Func8(oAgent):
    return cl_betree.servantagent.CAgent.CheckHasState(33150, oAgent) == True


def Func9(oAgent):
    return oAgent.GetData('FollowMoveStatus') == 1


def Func10(oAgent):
    return cl_betree.servantagent.CAgent.CheckHasState(33150, oAgent) == False


def Func11(oAgent):
    return oAgent.GetData('TransferPos') != None


def Func12(oAgent):
    return cl_betree.servantagent.CAgent.CheckSceneHasFightMonster(oAgent.GetConfig('HitRange'), oAgent) == True

data = {
    'Name': 'Fsm',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': True,
    'Ver': 38,
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
                        'TargetFSMNodeID': 11 },),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 7,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 29,
                        'Class': 'Transition',
                        'Method': (Func0, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 47,
                        'TransitionPhase': 1 }, {
                        'ID': 69,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.ChooseOwnerAroundPos, (8, 12, 10, 30)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 70,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.MoveToPos, (2,)),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'DeviceTurret.FollowAttack' },
                {
                    'ID': 11,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 23,
                        'Class': 'Transition',
                        'Method': (Func1, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 7,
                        'TransitionPhase': 1 }, {
                        'ID': 50,
                        'Class': 'Transition',
                        'Method': (Func2, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 15,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'DeviceTurret.Attack' },
                {
                    'ID': 15,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 39,
                        'Class': 'Transition',
                        'Method': (Func3, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 7,
                        'TransitionPhase': 1 }, {
                        'ID': 51,
                        'Class': 'Transition',
                        'Method': (Func4, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 11,
                        'TransitionPhase': 1 }, {
                        'ID': 55,
                        'Class': 'Transition',
                        'Method': (Func5, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 53,
                        'TransitionPhase': 1 }, {
                        'ID': 62,
                        'Class': 'Transition',
                        'Method': (Func6, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 59,
                        'TransitionPhase': 4 }),
                    'ReferenceBehavior': 'DeviceTurret.SeekingAttack' },
                {
                    'ID': 47,
                    'Class': 'State',
                    'Attachment': ({
                        'ID': 49,
                        'Class': 'Transition',
                        'Method': (Func7, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 11,
                        'TransitionPhase': 1 }, {
                        'ID': 52,
                        'Class': 'Transition',
                        'Method': (Func8, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 15,
                        'TransitionPhase': 1 }),
                    'Method': None,
                    'IsEndState': False },
                {
                    'ID': 53,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 56,
                        'Class': 'AlwaysTransition',
                        'TransitionPhase': 4,
                        'Flag': 'transition',
                        'TargetFSMNodeID': 15 }, {
                        'ID': 57,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 58,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.HaltPerform, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'ReferenceBehavior': 'DeviceTurret.Flash' },
                {
                    'ID': 59,
                    'Class': 'ReferenceBehavior',
                    'Attachment': ({
                        'ID': 63,
                        'Class': 'Transition',
                        'Method': (Func9, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 7,
                        'TransitionPhase': 1 }, {
                        'ID': 65,
                        'Class': 'Transition',
                        'Method': (Func10, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 11,
                        'TransitionPhase': 1 }, {
                        'ID': 66,
                        'Class': 'Transition',
                        'Method': (Func11, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 53,
                        'TransitionPhase': 1 }, {
                        'ID': 68,
                        'Class': 'Transition',
                        'Method': (Func12, ()),
                        'Phase': 1,
                        'Flag': 'transition',
                        'BinaryOperator': 'And',
                        'EffectorsFunc': [],
                        'TargetFSMNodeID': 15,
                        'TransitionPhase': 1 }),
                    'ReferenceBehavior': 'DeviceTurret.FollowNoAttack' }] }] }
