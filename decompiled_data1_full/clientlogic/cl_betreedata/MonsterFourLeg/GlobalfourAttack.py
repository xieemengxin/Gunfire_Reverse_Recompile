# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFourLeg/GlobalfourAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFourLeg/GlobalfourAttack.pyc
# Source Generated with Decompyle++
# File: GlobalfourAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckInLockEnemySight(60, 30, 0, oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 13


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == False


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.HasToStartGuerrilla(oAgent) == True


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetFirstRangedArrivePosDis(oAgent) >= 6


def Func8(oAgent):
    return oAgent.GetConfig('GuerrillaInterval')


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 6

data = {
    'Name': 'GlobalfourAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 239,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 98,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseNearestHateTarget, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 397,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 509,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 510,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 262,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 359,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 502,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 503,
                                                    'Class': 'Condition',
                                                    'Method': (Func1, ()) },
                                                {
                                                    'ID': 263,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (20212,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 504,
                                                    'Class': 'SelectorProbability',
                                                    'RandomGenerator': None,
                                                    'Node': [
                                                        {
                                                            'ID': 505,
                                                            'Class': 'DecoratorWeight',
                                                            'DecorateWhenChildEnds': False,
                                                            'Weight': 20,
                                                            'Node': [
                                                                {
                                                                    'ID': 507,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (20212,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 506,
                                                            'Class': 'DecoratorWeight',
                                                            'DecorateWhenChildEnds': False,
                                                            'Weight': 20,
                                                            'Node': [
                                                                {
                                                                    'ID': 508,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (20211,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] },
                                        {
                                            'ID': 394,
                                            'Class': 'And',
                                            'Node': [
                                                {
                                                    'ID': 360,
                                                    'Class': 'And',
                                                    'Node': [
                                                        {
                                                            'ID': 361,
                                                            'Class': 'Condition',
                                                            'Method': (Func2, ()) },
                                                        {
                                                            'ID': 362,
                                                            'Class': 'Condition',
                                                            'Method': (Func3, ()) }] },
                                                {
                                                    'ID': 393,
                                                    'Class': 'Condition',
                                                    'Method': (Func4, ()) }] }] },
                                {
                                    'ID': 450,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 451,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 452,
                                                    'Class': 'Condition',
                                                    'Method': (Func5, ()) },
                                                {
                                                    'ID': 453,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 455,
                                                            'Class': 'Action',
                                                            'Method': (Func6, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 470,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 471,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func7, ()) },
                                                                {
                                                                    'ID': 497,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 498,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 500,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 501,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] },
                                                                {
                                                                    'ID': 493,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 494,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (4, 5, 60, 180)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 495,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (2,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 496,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] }] },
                                                {
                                                    'ID': 454,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 0,
                                                    'SuccessPolicy': 1,
                                                    'ExitPolicy': 0,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 465,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 466,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 467,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHorizontalPos, (4, 5)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 468,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 469,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 457,
                                                            'Class': 'WaitFrame',
                                                            'Frames': (Func8, ()) }] }] }] }] },
                        {
                            'ID': 511,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 512,
                                    'Class': 'SelectorProbability',
                                    'RandomGenerator': None,
                                    'Node': [
                                        {
                                            'ID': 513,
                                            'Class': 'DecoratorWeight',
                                            'DecorateWhenChildEnds': False,
                                            'Weight': 20,
                                            'Node': [
                                                {
                                                    'ID': 516,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 20 }] },
                                        {
                                            'ID': 514,
                                            'Class': 'DecoratorWeight',
                                            'DecorateWhenChildEnds': False,
                                            'Weight': 10,
                                            'Node': [
                                                {
                                                    'ID': 515,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 517,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (20212,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 518,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 0,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 519,
                                                                    'Class': 'And',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 522,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func9, ()) },
                                                                        {
                                                                            'ID': 523,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func10, ()) }] },
                                                                {
                                                                    'ID': 524,
                                                                    'Class': 'DecoratorAlwaysRunning',
                                                                    'DecorateWhenChildEnds': False,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 525,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 526,
                                                                                    'Class': 'Action',
                                                                                    'Method': (Func11, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 527,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 528,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 530,
                                                                                    'Class': 'Parallel',
                                                                                    'FailurePolicy': 1,
                                                                                    'SuccessPolicy': 0,
                                                                                    'ExitPolicy': 1,
                                                                                    'ChildFinishPolicy': 1,
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 531,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 532,
                                                                                            'Class': 'Sequence',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 533,
                                                                                                    'Class': 'And',
                                                                                                    'Node': [
                                                                                                        {
                                                                                                            'ID': 535,
                                                                                                            'Class': 'Condition',
                                                                                                            'Method': (Func12, ()) },
                                                                                                        {
                                                                                                            'ID': 536,
                                                                                                            'Class': 'Condition',
                                                                                                            'Method': (Func13, ()) }] },
                                                                                                {
                                                                                                    'ID': 534,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None }] }] }] }] }] }] }] }] }] }] },
                {
                    'ID': 364,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 406,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 407,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' },),
                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 367,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 432,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 433,
                                    'Class': 'Condition',
                                    'Method': (Func14, ()) },
                                {
                                    'ID': 442,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 443,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 444,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 448,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (5, 3, 5, 170, 180)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 446,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 447,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 435,
                                    'Class': 'Noop' }] }] }] }] }
