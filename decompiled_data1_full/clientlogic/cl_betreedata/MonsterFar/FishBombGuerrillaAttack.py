# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFar/FishBombGuerrillaAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFar/FishBombGuerrillaAttack.pyc
# Source Generated with Decompyle++
# File: FishBombGuerrillaAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 20651


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == False


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, oAgent.GetConfig('IntervalTime'), oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 12


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 12


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == False


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, oAgent.GetConfig('IntervalTime'), oAgent) == True


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func15(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func16(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == False


def Func17(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, oAgent.GetConfig('IntervalTime'), oAgent) == True


def Func18(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), 3, 5, 80, 100, oAgent)


def Func19(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func20(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True

data = {
    'Name': 'FishBombGuerrillaAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 11,
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
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 40,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 41,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 42,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 43,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 5,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 9,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 12,
                                                    'Class': 'And',
                                                    'Node': [
                                                        {
                                                            'ID': 15,
                                                            'Class': 'Condition',
                                                            'Method': (Func1, ()) },
                                                        {
                                                            'ID': 16,
                                                            'Class': 'Condition',
                                                            'Method': (Func2, ()) }] },
                                                {
                                                    'ID': 13,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) }] },
                                        {
                                            'ID': 10,
                                            'Class': 'DecoratorAlwaysRunning',
                                            'DecorateWhenChildEnds': False,
                                            'Node': [
                                                {
                                                    'ID': 14,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 17,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 18,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 19,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func4, ()) },
                                                                {
                                                                    'ID': 20,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 22,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (12, 3, 5, 150, 180)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 26,
                                                                            'Class': 'Parallel',
                                                                            'FailurePolicy': 1,
                                                                            'SuccessPolicy': 0,
                                                                            'ExitPolicy': 1,
                                                                            'ChildFinishPolicy': 1,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 28,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 29,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 32,
                                                                                            'Class': 'And',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 36,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func5, ()) },
                                                                                                {
                                                                                                    'ID': 37,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func6, ()) }] },
                                                                                        {
                                                                                            'ID': 33,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None }] }] }] },
                                                                {
                                                                    'ID': 21,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 24,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (18, 3, 5, 90, 120)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 27,
                                                                            'Class': 'Parallel',
                                                                            'FailurePolicy': 1,
                                                                            'SuccessPolicy': 0,
                                                                            'ExitPolicy': 1,
                                                                            'ChildFinishPolicy': 1,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 30,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 31,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 34,
                                                                                            'Class': 'And',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 38,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func7, ()) },
                                                                                                {
                                                                                                    'ID': 39,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func8, ()) }] },
                                                                                        {
                                                                                            'ID': 35,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None }] }] }] }] }] }] }] },
                                {
                                    'ID': 6,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 7,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 8,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 80,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 81,
                                    'Class': 'Condition',
                                    'Method': (Func9, ()) },
                                {
                                    'ID': 82,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 83,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 1,
                                            'ExitPolicy': 0,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 45,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 47,
                                                            'Class': 'And',
                                                            'Node': [
                                                                {
                                                                    'ID': 50,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func10, ()) },
                                                                {
                                                                    'ID': 51,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func11, ()) }] },
                                                        {
                                                            'ID': 48,
                                                            'Class': 'Condition',
                                                            'Method': (Func12, ()) }] },
                                                {
                                                    'ID': 55,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 57,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (1, 3, 5, 150, 180)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 61,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 1,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 77,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 75,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 84,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 63,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] },
                                                                {
                                                                    'ID': 64,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 67,
                                                                            'Class': 'And',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 71,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func13, ()) },
                                                                                {
                                                                                    'ID': 72,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func14, ()) }] },
                                                                        {
                                                                            'ID': 68,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] }] }] },
                                        {
                                            'ID': 91,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 92,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                'Phase': 1,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 76,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 44,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 85,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 86,
                                                    'Class': 'And',
                                                    'Node': [
                                                        {
                                                            'ID': 88,
                                                            'Class': 'Condition',
                                                            'Method': (Func15, ()) },
                                                        {
                                                            'ID': 89,
                                                            'Class': 'Condition',
                                                            'Method': (Func16, ()) }] },
                                                {
                                                    'ID': 87,
                                                    'Class': 'Condition',
                                                    'Method': (Func17, ()) },
                                                {
                                                    'ID': 90,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 46,
                                            'Class': 'DecoratorAlwaysRunning',
                                            'DecorateWhenChildEnds': False,
                                            'Node': [
                                                {
                                                    'ID': 56,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 59,
                                                            'Class': 'Action',
                                                            'Method': (Func18, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 4,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 62,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 1,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 78,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 79,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 65,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] },
                                                                {
                                                                    'ID': 66,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 69,
                                                                            'Class': 'And',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 73,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func19, ()) },
                                                                                {
                                                                                    'ID': 74,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func20, ()) }] },
                                                                        {
                                                                            'ID': 70,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] }] }] }] }] }] }] }] }
