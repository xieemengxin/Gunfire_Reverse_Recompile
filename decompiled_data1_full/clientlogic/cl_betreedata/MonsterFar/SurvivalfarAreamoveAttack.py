# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFar/SurvivalfarAreamoveAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFar/SurvivalfarAreamoveAttack.pyc
# Source Generated with Decompyle++
# File: SurvivalfarAreamoveAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 45


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == False


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 35


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), 85, 95, oAgent)


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 35


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


def Func19(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 8

data = {
    'Name': 'SurvivalfarAreamoveAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 132,
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
                    'ID': 516,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.RemoveState, (8092,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 456,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 471,
                            'Class': 'Or',
                            'Node': [
                                {
                                    'ID': 474,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 475,
                                    'Class': 'And',
                                    'Node': [
                                        {
                                            'ID': 472,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 457,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) }] }] },
                        {
                            'ID': 460,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 468,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 458,
                                            'Class': 'Action',
                                            'Method': (Func3, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 469,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 470,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 462,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 463,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 464,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 467,
                                                    'Class': 'Condition',
                                                    'Method': (Func4, ()) },
                                                {
                                                    'ID': 466,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] },
                        {
                            'ID': 461,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 318,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 0,
                                    'SuccessPolicy': 1,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 193,
                                            'Class': 'SelectorProbability',
                                            'RandomGenerator': None,
                                            'Node': [
                                                {
                                                    'ID': 195,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 25,
                                                    'Node': [
                                                        {
                                                            'ID': 476,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 477,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 478,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangeHidePosAndAttPos, (1, 10)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 479,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 505,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 0,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 0,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 480,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 506,
                                                                            'Class': 'WaitFrame',
                                                                            'Frames': 125 }] },
                                                                {
                                                                    'ID': 481,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 482,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 483,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func5, ()) },
                                                                        {
                                                                            'ID': 503,
                                                                            'Class': 'WaitFrame',
                                                                            'Frames': (Func6, ()) }] },
                                                                {
                                                                    'ID': 496,
                                                                    'Class': 'IfElse',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 498,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func7, ()) },
                                                                        {
                                                                            'ID': 499,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 501,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHorizontalPos, (2, 3)),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 502,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] },
                                                                        {
                                                                            'ID': 504,
                                                                            'Class': 'Noop' }] }] }] },
                                                {
                                                    'ID': 196,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 50,
                                                    'Node': [
                                                        {
                                                            'ID': 199,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 200,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedAreaPos, (10, 15, 8)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 517,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 291,
                                                                            'Class': 'IfElse',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 307,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func8, ()) },
                                                                                {
                                                                                    'ID': 308,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 310,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 311,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 415,
                                                                                            'Class': 'Parallel',
                                                                                            'FailurePolicy': 1,
                                                                                            'SuccessPolicy': 0,
                                                                                            'ExitPolicy': 1,
                                                                                            'ChildFinishPolicy': 1,
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 430,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None },
                                                                                                {
                                                                                                    'ID': 431,
                                                                                                    'Class': 'Sequence',
                                                                                                    'Node': [
                                                                                                        {
                                                                                                            'ID': 448,
                                                                                                            'Class': 'And',
                                                                                                            'Node': [
                                                                                                                {
                                                                                                                    'ID': 452,
                                                                                                                    'Class': 'Condition',
                                                                                                                    'Method': (Func9, ()) },
                                                                                                                {
                                                                                                                    'ID': 453,
                                                                                                                    'Class': 'Condition',
                                                                                                                    'Method': (Func10, ()) }] },
                                                                                                        {
                                                                                                            'ID': 449,
                                                                                                            'Class': 'Action',
                                                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                                            'ResultOption': 0,
                                                                                                            'ResultFunctor': None }] }] },
                                                                                        {
                                                                                            'ID': 312,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None }] },
                                                                                {
                                                                                    'ID': 309,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 313,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 314,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 416,
                                                                                            'Class': 'Parallel',
                                                                                            'FailurePolicy': 1,
                                                                                            'SuccessPolicy': 0,
                                                                                            'ExitPolicy': 1,
                                                                                            'ChildFinishPolicy': 1,
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 432,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None },
                                                                                                {
                                                                                                    'ID': 433,
                                                                                                    'Class': 'Sequence',
                                                                                                    'Node': [
                                                                                                        {
                                                                                                            'ID': 450,
                                                                                                            'Class': 'And',
                                                                                                            'Node': [
                                                                                                                {
                                                                                                                    'ID': 454,
                                                                                                                    'Class': 'Condition',
                                                                                                                    'Method': (Func11, ()) },
                                                                                                                {
                                                                                                                    'ID': 455,
                                                                                                                    'Class': 'Condition',
                                                                                                                    'Method': (Func12, ()) }] },
                                                                                                        {
                                                                                                            'ID': 451,
                                                                                                            'Class': 'Action',
                                                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                                            'ResultOption': 0,
                                                                                                            'ResultFunctor': None }] }] },
                                                                                        {
                                                                                            'ID': 315,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None }] }] },
                                                                        {
                                                                            'ID': 518,
                                                                            'Class': 'WaitFrame',
                                                                            'Frames': 125 }] }] }] }] },
                                        {
                                            'ID': 507,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 319,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 429,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 320,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 398,
                                                                'Class': 'Precondition',
                                                                'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                                                'Phase': 1,
                                                                'Flag': 'precondition',
                                                                'BinaryOperator': 'And' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 442,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 445,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func13, ()) },
                                                                {
                                                                    'ID': 443,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 405,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func14, ()) },
                                                                        {
                                                                            'ID': 446,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.AddState, (8046, 0)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] },
                                                                {
                                                                    'ID': 444,
                                                                    'Class': 'DecoratorAlwaysSuccess',
                                                                    'DecorateWhenChildEnds': False }] },
                                                        {
                                                            'ID': 399,
                                                            'Class': 'And',
                                                            'Node': [
                                                                {
                                                                    'ID': 400,
                                                                    'Class': 'And',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 402,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func15, ()) },
                                                                        {
                                                                            'ID': 403,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func16, ()) }] },
                                                                {
                                                                    'ID': 401,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func17, ()) }] }] },
                                                {
                                                    'ID': 509,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 510,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 511,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func18, ()) },
                                                                {
                                                                    'ID': 513,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 508,
                                                                            'Class': 'WaitFrame',
                                                                            'Frames': 125 },
                                                                        {
                                                                            'ID': 514,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.AddState, (8092, 0)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 515,
                                                                            'Class': 'DecoratorAlwaysFailure',
                                                                            'DecorateWhenChildEnds': False }] },
                                                                {
                                                                    'ID': 512,
                                                                    'Class': 'DecoratorAlwaysFailure',
                                                                    'DecorateWhenChildEnds': False }] }] }] }] },
                                {
                                    'ID': 447,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.RemoveState, (8046,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 254,
                                    'Class': 'Sequence',
                                    'Attachment': ({
                                        'ID': 414,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Node': [
                                        {
                                            'ID': 412,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Squat, (50, 68)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 407,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 257,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 413,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.StandUp, (24,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 408,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 409,
                                                    'Class': 'Condition',
                                                    'Method': (Func19, ()) },
                                                {
                                                    'ID': 410,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 411,
                                                    'Class': 'Noop' }] }] }] }] }] }] }
