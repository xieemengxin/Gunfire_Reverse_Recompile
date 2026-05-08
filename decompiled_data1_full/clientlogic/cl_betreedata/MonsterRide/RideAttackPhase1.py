# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterRide/RideAttackPhase1.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterRide/RideAttackPhase1.pyc
# Source Generated with Decompyle++
# File: RideAttackPhase1.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) > 30


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 100, oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) > 30


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 25


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) > 20


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), 2, 4, 80, 100, oAgent)


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 25, oAgent) == True


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), 5, 8, 80, 100, oAgent)


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) > 4


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 4


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), 3, 5, 160, 180, oAgent)


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func15(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 50, oAgent) == True


def Func16(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), 5, 8, 160, 180, oAgent)


def Func17(oAgent):
    return cl_betree.monsteragent.CAgent.GetLastSucceededPF(oAgent) == 23812


def Func18(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), 2, 4, 170, 180, oAgent)


def Func19(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 50, oAgent) == True

data = {
    'Name': 'RideAttackPhase1',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 185,
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
                    'ID': 43,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 44,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 216,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 215,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 106,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 484,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 495,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 108,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (25,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 498,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) }] },
                                {
                                    'ID': 336,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 337,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) },
                                        {
                                            'ID': 338,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 228,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 227,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 229,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 232,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 555,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func3, ()) },
                                                                {
                                                                    'ID': 235,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (23811,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 239,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 233,
                                                            'Class': 'DecoratorAlwaysRunning',
                                                            'DecorateWhenChildEnds': False,
                                                            'Node': [
                                                                {
                                                                    'ID': 340,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (20,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] },
                                        {
                                            'ID': 339,
                                            'Class': 'Noop' }] }] },
                        {
                            'ID': 69,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 70,
                                    'Class': 'Condition',
                                    'Method': (Func4, ()) },
                                {
                                    'ID': 71,
                                    'Class': 'SelectorProbability',
                                    'RandomGenerator': None,
                                    'Node': [
                                        {
                                            'ID': 72,
                                            'Class': 'DecoratorWeight',
                                            'DecorateWhenChildEnds': False,
                                            'Weight': 50,
                                            'Node': [
                                                {
                                                    'ID': 342,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 360,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 361,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 355,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 1,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 350,
                                                                    'Class': 'DecoratorAlwaysRunning',
                                                                    'DecorateWhenChildEnds': False,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 351,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 352,
                                                                                    'Class': 'Action',
                                                                                    'Method': (Func5, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 435,
                                                                                    'Class': 'Parallel',
                                                                                    'FailurePolicy': 1,
                                                                                    'SuccessPolicy': 0,
                                                                                    'ExitPolicy': 1,
                                                                                    'ChildFinishPolicy': 1,
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 485,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 486,
                                                                                            'Class': 'Sequence',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 539,
                                                                                                    'Class': 'And',
                                                                                                    'Node': [
                                                                                                        {
                                                                                                            'ID': 548,
                                                                                                            'Class': 'Condition',
                                                                                                            'Method': (Func6, ()) },
                                                                                                        {
                                                                                                            'ID': 549,
                                                                                                            'Class': 'Condition',
                                                                                                            'Method': (Func7, ()) }] },
                                                                                                {
                                                                                                    'ID': 540,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None }] }] }] }] },
                                                                {
                                                                    'ID': 356,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 358,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func8, ()) },
                                                                        {
                                                                            'ID': 357,
                                                                            'Class': 'Action',
                                                                            'Attachment': ({
                                                                                'ID': 553,
                                                                                'Class': 'Precondition',
                                                                                'Method': (cl_betree.monsteragent.CAgent.LimitChoosePFDistance, (15, 0)),
                                                                                'Phase': 1,
                                                                                'Flag': 'precondition',
                                                                                'BinaryOperator': 'And' },),
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 359,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] }] }] },
                                        {
                                            'ID': 109,
                                            'Class': 'DecoratorWeight',
                                            'DecorateWhenChildEnds': False,
                                            'Weight': 50,
                                            'Node': [
                                                {
                                                    'ID': 362,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 365,
                                                            'Class': 'Action',
                                                            'Method': (Func9, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 364,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 367,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 366,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 370,
                                                            'Class': 'Parallel',
                                                            'Attachment': ({
                                                                'ID': 479,
                                                                'Class': 'Precondition',
                                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                'Phase': 1,
                                                                'Flag': 'precondition',
                                                                'BinaryOperator': 'And' },),
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 1,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 371,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 368,
                                                                            'Class': 'Action',
                                                                            'Attachment': ({
                                                                                'ID': 554,
                                                                                'Class': 'Precondition',
                                                                                'Method': (cl_betree.monsteragent.CAgent.LimitChoosePFDistance, (15, 0)),
                                                                                'Phase': 1,
                                                                                'Flag': 'precondition',
                                                                                'BinaryOperator': 'And' },),
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 369,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] },
                                                                {
                                                                    'ID': 480,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 496,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 497,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 483,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.KeepMoving, (4,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] }] }] }] },
                                {
                                    'ID': 379,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 383,
                                            'Class': 'Condition',
                                            'Method': (Func10, ()) },
                                        {
                                            'ID': 384,
                                            'Class': 'SelectorProbability',
                                            'RandomGenerator': None,
                                            'Node': [
                                                {
                                                    'ID': 401,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 10,
                                                    'Node': [
                                                        {
                                                            'ID': 430,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 433,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 446,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 442,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 454,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (3.5,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 443,
                                                                            'Class': 'WaitFrame',
                                                                            'Frames': 100 }] },
                                                                {
                                                                    'ID': 450,
                                                                    'Class': 'IfElse',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 451,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func11, ()) },
                                                                        {
                                                                            'ID': 452,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 445,
                                                                                    'Class': 'Action',
                                                                                    'Attachment': ({
                                                                                        'ID': 453,
                                                                                        'Class': 'Precondition',
                                                                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                        'Phase': 1,
                                                                                        'Flag': 'precondition',
                                                                                        'BinaryOperator': 'And' },),
                                                                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 447,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 448,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] },
                                                                        {
                                                                            'ID': 547,
                                                                            'Class': 'Noop' }] }] }] },
                                                {
                                                    'ID': 402,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 80,
                                                    'Node': [
                                                        {
                                                            'ID': 455,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 456,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 457,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 458,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 459,
                                                                            'Class': 'DecoratorAlwaysRunning',
                                                                            'DecorateWhenChildEnds': False,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 461,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 465,
                                                                                            'Class': 'Action',
                                                                                            'Method': (Func12, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 466,
                                                                                            'Class': 'Parallel',
                                                                                            'FailurePolicy': 1,
                                                                                            'SuccessPolicy': 0,
                                                                                            'ExitPolicy': 1,
                                                                                            'ChildFinishPolicy': 1,
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 467,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None },
                                                                                                {
                                                                                                    'ID': 468,
                                                                                                    'Class': 'Sequence',
                                                                                                    'Node': [
                                                                                                        {
                                                                                                            'ID': 491,
                                                                                                            'Class': 'And',
                                                                                                            'Node': [
                                                                                                                {
                                                                                                                    'ID': 543,
                                                                                                                    'Class': 'Condition',
                                                                                                                    'Method': (Func13, ()) },
                                                                                                                {
                                                                                                                    'ID': 544,
                                                                                                                    'Class': 'Condition',
                                                                                                                    'Method': (Func14, ()) }] },
                                                                                                        {
                                                                                                            'ID': 492,
                                                                                                            'Class': 'Action',
                                                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                                            'ResultOption': 0,
                                                                                                            'ResultFunctor': None }] }] }] }] },
                                                                        {
                                                                            'ID': 460,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 462,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func15, ()) },
                                                                                {
                                                                                    'ID': 463,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (23811,)),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 464,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] }] }] }] },
                                                {
                                                    'ID': 429,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 10,
                                                    'Node': [
                                                        {
                                                            'ID': 473,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 474,
                                                                    'Class': 'Action',
                                                                    'Method': (Func16, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 475,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 476,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 477,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] },
                                        {
                                            'ID': 504,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 505,
                                                    'Class': 'Condition',
                                                    'Method': (Func17, ()) },
                                                {
                                                    'ID': 506,
                                                    'Class': 'SelectorProbability',
                                                    'RandomGenerator': None,
                                                    'Node': [
                                                        {
                                                            'ID': 507,
                                                            'Class': 'DecoratorWeight',
                                                            'DecorateWhenChildEnds': False,
                                                            'Weight': 75,
                                                            'Node': [
                                                                {
                                                                    'ID': 509,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 511,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 512,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 513,
                                                                            'Class': 'Parallel',
                                                                            'FailurePolicy': 1,
                                                                            'SuccessPolicy': 0,
                                                                            'ExitPolicy': 1,
                                                                            'ChildFinishPolicy': 1,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 520,
                                                                                    'Class': 'DecoratorAlwaysRunning',
                                                                                    'DecorateWhenChildEnds': False,
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 524,
                                                                                            'Class': 'Sequence',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 533,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (Func18, ()),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None },
                                                                                                {
                                                                                                    'ID': 550,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None }] }] },
                                                                                {
                                                                                    'ID': 521,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 525,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func19, ()) },
                                                                                        {
                                                                                            'ID': 551,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (23811,)),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 552,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None }] }] }] }] },
                                                        {
                                                            'ID': 508,
                                                            'Class': 'DecoratorWeight',
                                                            'DecorateWhenChildEnds': False,
                                                            'Weight': 25,
                                                            'Node': [
                                                                {
                                                                    'ID': 510,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 514,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (23, 3, 5, 80, 100)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 515,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 516,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 517,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] }] },
                                                {
                                                    'ID': 499,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 500,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 501,
                                                                'Class': 'Precondition',
                                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                'Phase': 1,
                                                                'Flag': 'precondition',
                                                                'BinaryOperator': 'And' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 502,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 503,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] }] }] }] }] }
