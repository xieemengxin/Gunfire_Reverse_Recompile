# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteFar/EliteSniperAttack.pyc
# RelativePath: clientlogic/cl_betreedata/EliteFar/EliteSniperAttack.pyc
# Source Generated with Decompyle++
# File: EliteSniperAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 4


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 30


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), 85, 95, oAgent)


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 15


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), 90, 150, oAgent)


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(15, oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), 85, 95, oAgent)


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 20


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), 45, 90, oAgent)


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 15


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), 85, 95, oAgent)


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(15, oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), 85, 95, oAgent)


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.GetFirstRangedArrivePosDis(oAgent) >= 4


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func15(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func16(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func17(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func18(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 31643


def Func19(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True

data = {
    'Name': 'EliteSniperAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 357,
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
                    'ID': 635,
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
                            'ID': 805,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 850,
                                    'Class': 'WaitFrame',
                                    'Frames': (cl_betree.monsteragent.CAgent.GetGapRandomNum, (10, 66, 7)) },
                                {
                                    'ID': 807,
                                    'Class': 'DecoratorLoopUntil',
                                    'DecorateWhenChildEnds': False,
                                    'Count': -1,
                                    'Until': True,
                                    'Node': [
                                        {
                                            'ID': 817,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 852,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 827,
                                                    'Class': 'Condition',
                                                    'Method': (Func0, ()) },
                                                {
                                                    'ID': 828,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 5 }] }] }] },
                        {
                            'ID': 851,
                            'Class': 'Condition',
                            'Method': (Func1, ()) },
                        {
                            'ID': 581,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 795,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 796,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) },
                                        {
                                            'ID': 653,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 661,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) },
                                                {
                                                    'ID': 662,
                                                    'Class': 'Action',
                                                    'Method': (Func4, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 791,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 792,
                                                            'Class': 'Condition',
                                                            'Method': (Func5, ()) },
                                                        {
                                                            'ID': 793,
                                                            'Class': 'Action',
                                                            'Method': (Func6, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 794,
                                                            'Class': 'Action',
                                                            'Method': (Func7, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] },
                                        {
                                            'ID': 797,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 798,
                                                    'Class': 'Condition',
                                                    'Method': (Func8, ()) },
                                                {
                                                    'ID': 799,
                                                    'Class': 'Action',
                                                    'Method': (Func9, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 800,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 801,
                                                            'Class': 'Condition',
                                                            'Method': (Func10, ()) },
                                                        {
                                                            'ID': 802,
                                                            'Class': 'Action',
                                                            'Method': (Func11, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 803,
                                                            'Class': 'Action',
                                                            'Method': (Func12, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] },
                                {
                                    'ID': 657,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 658,
                                            'Class': 'Condition',
                                            'Method': (Func13, ()) },
                                        {
                                            'ID': 659,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 664,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 665,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 666,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 686,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 687,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 690,
                                                                    'Class': 'And',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 703,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func14, ()) },
                                                                        {
                                                                            'ID': 704,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func15, ()) }] },
                                                                {
                                                                    'ID': 691,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] },
                                        {
                                            'ID': 660,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 667,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 668,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 669,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 688,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 689,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 692,
                                                                    'Class': 'And',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 705,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func16, ()) },
                                                                        {
                                                                            'ID': 706,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func17, ()) }] },
                                                                {
                                                                    'ID': 693,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] }] },
                                {
                                    'ID': 804,
                                    'Class': 'DecoratorAlwaysFailure',
                                    'DecorateWhenChildEnds': False }] }] },
                {
                    'ID': 364,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 789,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 638,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 709,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' },),
                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 730,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 729,
                                    'Class': 'Condition',
                                    'Method': (Func18, ()) },
                                {
                                    'ID': 718,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 732,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 0,
                                    'SuccessPolicy': 1,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 848,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 0,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 733,
                                                    'Class': 'DecoratorAlwaysRunning',
                                                    'DecorateWhenChildEnds': False,
                                                    'Node': [
                                                        {
                                                            'ID': 735,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 736,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 737,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHorizontalPos, (4, 5)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 738,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] },
                                                {
                                                    'ID': 734,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 849,
                                            'Class': 'Condition',
                                            'Method': (Func19, ()) }] }] }] }] }] }
