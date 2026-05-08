# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Common/SurvivalAreamoveAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Common/SurvivalAreamoveAttack.pyc
# Source Generated with Decompyle++
# File: SurvivalAreamoveAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 60


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == False


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 50


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), 85, 95, oAgent)


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 50


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func6(oAgent):
    return oAgent.GetConfig('HideAttackStandingTime')


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == True


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetFirstRangedArrivePosDis(oAgent) >= 4


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(8046, oAgent) == False


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, oAgent.GetConfig('IntervalTime'), oAgent) == True


def Func15(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func16(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func17(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == False


def Func18(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(8092, oAgent) == False

data = {
    'Name': 'SurvivalAreamoveAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 145,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.RemoveState, (8092,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 5,
                            'Class': 'Or',
                            'Node': [
                                {
                                    'ID': 8,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 9,
                                    'Class': 'And',
                                    'Node': [
                                        {
                                            'ID': 16,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 17,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) }] }] },
                        {
                            'ID': 6,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 10,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 18,
                                            'Class': 'Action',
                                            'Method': (Func3, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 19,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 20,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 11,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 21,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 22,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 30,
                                                    'Class': 'Condition',
                                                    'Method': (Func4, ()) },
                                                {
                                                    'ID': 31,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] },
                        {
                            'ID': 7,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 12,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 0,
                                    'SuccessPolicy': 1,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 23,
                                            'Class': 'SelectorProbability',
                                            'RandomGenerator': None,
                                            'Node': [
                                                {
                                                    'ID': 32,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 25,
                                                    'Node': [
                                                        {
                                                            'ID': 39,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 47,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 48,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangeHidePosAndAttPos, (1, 10)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 49,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 50,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 0,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 0,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 64,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 65,
                                                                            'Class': 'WaitFrame',
                                                                            'Frames': 75 }] },
                                                                {
                                                                    'ID': 51,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 52,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 66,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func5, ()) },
                                                                        {
                                                                            'ID': 67,
                                                                            'Class': 'WaitFrame',
                                                                            'Frames': (Func6, ()) }] },
                                                                {
                                                                    'ID': 53,
                                                                    'Class': 'IfElse',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 68,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func7, ()) },
                                                                        {
                                                                            'ID': 69,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 80,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHorizontalPos, (2, 3)),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 81,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] },
                                                                        {
                                                                            'ID': 70,
                                                                            'Class': 'Noop' }] }] }] },
                                                {
                                                    'ID': 33,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 50,
                                                    'Node': [
                                                        {
                                                            'ID': 40,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 54,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedAreaPos, (25, 20, 8)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 55,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 71,
                                                                            'Class': 'IfElse',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 82,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func8, ()) },
                                                                                {
                                                                                    'ID': 83,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 85,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 86,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 87,
                                                                                            'Class': 'Parallel',
                                                                                            'FailurePolicy': 1,
                                                                                            'SuccessPolicy': 0,
                                                                                            'ExitPolicy': 1,
                                                                                            'ChildFinishPolicy': 1,
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 93,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None },
                                                                                                {
                                                                                                    'ID': 94,
                                                                                                    'Class': 'Sequence',
                                                                                                    'Node': [
                                                                                                        {
                                                                                                            'ID': 97,
                                                                                                            'Class': 'And',
                                                                                                            'Node': [
                                                                                                                {
                                                                                                                    'ID': 101,
                                                                                                                    'Class': 'Condition',
                                                                                                                    'Method': (Func9, ()) },
                                                                                                                {
                                                                                                                    'ID': 102,
                                                                                                                    'Class': 'Condition',
                                                                                                                    'Method': (Func10, ()) }] },
                                                                                                        {
                                                                                                            'ID': 98,
                                                                                                            'Class': 'Action',
                                                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                                            'ResultOption': 0,
                                                                                                            'ResultFunctor': None }] }] },
                                                                                        {
                                                                                            'ID': 88,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None }] },
                                                                                {
                                                                                    'ID': 84,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 89,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 90,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 91,
                                                                                            'Class': 'Parallel',
                                                                                            'FailurePolicy': 1,
                                                                                            'SuccessPolicy': 0,
                                                                                            'ExitPolicy': 1,
                                                                                            'ChildFinishPolicy': 1,
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 95,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None },
                                                                                                {
                                                                                                    'ID': 96,
                                                                                                    'Class': 'Sequence',
                                                                                                    'Node': [
                                                                                                        {
                                                                                                            'ID': 99,
                                                                                                            'Class': 'And',
                                                                                                            'Node': [
                                                                                                                {
                                                                                                                    'ID': 103,
                                                                                                                    'Class': 'Condition',
                                                                                                                    'Method': (Func11, ()) },
                                                                                                                {
                                                                                                                    'ID': 104,
                                                                                                                    'Class': 'Condition',
                                                                                                                    'Method': (Func12, ()) }] },
                                                                                                        {
                                                                                                            'ID': 100,
                                                                                                            'Class': 'Action',
                                                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                                            'ResultOption': 0,
                                                                                                            'ResultFunctor': None }] }] },
                                                                                        {
                                                                                            'ID': 92,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None }] }] },
                                                                        {
                                                                            'ID': 72,
                                                                            'Class': 'WaitFrame',
                                                                            'Frames': 75 }] }] }] }] },
                                        {
                                            'ID': 24,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 34,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 41,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 42,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 43,
                                                                'Class': 'Precondition',
                                                                'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                                                'Phase': 1,
                                                                'Flag': 'precondition',
                                                                'BinaryOperator': 'And' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 44,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 56,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func13, ()) },
                                                                {
                                                                    'ID': 57,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 73,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func14, ()) },
                                                                        {
                                                                            'ID': 74,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.AddState, (8046, 0)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] },
                                                                {
                                                                    'ID': 58,
                                                                    'Class': 'DecoratorAlwaysSuccess',
                                                                    'DecorateWhenChildEnds': False }] },
                                                        {
                                                            'ID': 45,
                                                            'Class': 'And',
                                                            'Node': [
                                                                {
                                                                    'ID': 59,
                                                                    'Class': 'And',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 75,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func15, ()) },
                                                                        {
                                                                            'ID': 76,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func16, ()) }] },
                                                                {
                                                                    'ID': 60,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func17, ()) }] }] },
                                                {
                                                    'ID': 35,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 46,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 61,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func18, ()) },
                                                                {
                                                                    'ID': 62,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 77,
                                                                            'Class': 'WaitFrame',
                                                                            'Frames': 125 },
                                                                        {
                                                                            'ID': 78,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.AddState, (8092, 0)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 79,
                                                                            'Class': 'DecoratorAlwaysFailure',
                                                                            'DecorateWhenChildEnds': False }] },
                                                                {
                                                                    'ID': 63,
                                                                    'Class': 'DecoratorAlwaysFailure',
                                                                    'DecorateWhenChildEnds': False }] }] }] }] },
                                {
                                    'ID': 13,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.RemoveState, (8046,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 14,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 26,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 105,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                'Phase': 1,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 27,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] }] }] }] }
