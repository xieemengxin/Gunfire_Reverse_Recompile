# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterSniper/snipeFuzzyAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterSniper/snipeFuzzyAttack.pyc
# Source Generated with Decompyle++
# File: snipeFuzzyAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, oAgent.GetConfig('IntervalTime'), oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 4


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.HasToStartGuerrilla(oAgent) == True


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == False


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 30


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), 85, 95, oAgent)


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(30, oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), 85, 95, oAgent)


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetFirstRangedArrivePosDis(oAgent) >= 4


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func15(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func16(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'snipeFuzzyAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 275,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 98,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 583,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 453,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 454,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 456,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 570,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 571,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 572,
                                    'Class': 'Condition',
                                    'Method': (Func2, ()) }] },
                        {
                            'ID': 632,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 633,
                                    'Class': 'Condition',
                                    'Method': (Func3, ()) },
                                {
                                    'ID': 634,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 636,
                                    'Class': 'DecoratorAlwaysFailure',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 635,
                                            'Class': 'Noop' }] }] },
                        {
                            'ID': 660,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 661,
                                    'Class': 'Or',
                                    'Node': [
                                        {
                                            'ID': 662,
                                            'Class': 'Condition',
                                            'Method': (Func4, ()) },
                                        {
                                            'ID': 663,
                                            'Class': 'Condition',
                                            'Method': (Func5, ()) }] },
                                {
                                    'ID': 666,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 667,
                                            'Class': 'Condition',
                                            'Method': (Func6, ()) },
                                        {
                                            'ID': 687,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 0,
                                            'SuccessPolicy': 1,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 631,
                                                    'Class': 'DecoratorAlwaysRunning',
                                                    'DecorateWhenChildEnds': False,
                                                    'Node': [
                                                        {
                                                            'ID': 588,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 605,
                                                                    'Class': 'IfElse',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 606,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func7, ()) },
                                                                        {
                                                                            'ID': 607,
                                                                            'Class': 'Action',
                                                                            'Method': (Func8, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 608,
                                                                            'Class': 'Action',
                                                                            'Method': (Func9, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] },
                                                                {
                                                                    'ID': 609,
                                                                    'Class': 'IfElse',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 639,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func10, ()) },
                                                                        {
                                                                            'ID': 640,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 642,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 643,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 644,
                                                                                    'Class': 'Parallel',
                                                                                    'FailurePolicy': 1,
                                                                                    'SuccessPolicy': 0,
                                                                                    'ExitPolicy': 1,
                                                                                    'ChildFinishPolicy': 1,
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 675,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 676,
                                                                                            'Class': 'Sequence',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 679,
                                                                                                    'Class': 'And',
                                                                                                    'Node': [
                                                                                                        {
                                                                                                            'ID': 683,
                                                                                                            'Class': 'Condition',
                                                                                                            'Method': (Func11, ()) },
                                                                                                        {
                                                                                                            'ID': 684,
                                                                                                            'Class': 'Condition',
                                                                                                            'Method': (Func12, ()) }] },
                                                                                                {
                                                                                                    'ID': 680,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None }] }] }] },
                                                                        {
                                                                            'ID': 641,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 645,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 646,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 647,
                                                                                    'Class': 'Parallel',
                                                                                    'FailurePolicy': 1,
                                                                                    'SuccessPolicy': 0,
                                                                                    'ExitPolicy': 1,
                                                                                    'ChildFinishPolicy': 1,
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 677,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 678,
                                                                                            'Class': 'Sequence',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 681,
                                                                                                    'Class': 'And',
                                                                                                    'Node': [
                                                                                                        {
                                                                                                            'ID': 685,
                                                                                                            'Class': 'Condition',
                                                                                                            'Method': (Func13, ()) },
                                                                                                        {
                                                                                                            'ID': 686,
                                                                                                            'Class': 'Condition',
                                                                                                            'Method': (Func14, ()) }] },
                                                                                                {
                                                                                                    'ID': 682,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None }] }] }] }] }] }] },
                                                {
                                                    'ID': 688,
                                                    'Class': 'Condition',
                                                    'Method': (Func15, ()) }] },
                                        {
                                            'ID': 668,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 669,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 670,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 672,
                                                    'Class': 'Parallel',
                                                    'Attachment': ({
                                                        'ID': 674,
                                                        'Class': 'Effector',
                                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                        'Phase': 1,
                                                        'Flag': 'effector' },),
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 671,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (5,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 673,
                                                            'Class': 'Condition',
                                                            'Method': (Func16, ()) }] }] }] },
                                {
                                    'ID': 587,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 589,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 590,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 664,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 594,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.KeepMoving, (3,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 665,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 50 }] }] }] }] },
                {
                    'ID': 388,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 579,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 582,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
