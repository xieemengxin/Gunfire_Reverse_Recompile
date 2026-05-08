# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterNear/nearSwordAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterNear/nearSwordAttack.pyc
# Source Generated with Decompyle++
# File: nearSwordAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 3


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, oAgent.GetConfig('IntervalTime'), oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 3

data = {
    'Name': 'nearSwordAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 97,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 5,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 6,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 8,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 582,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 636,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 9,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 7,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 639,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 0,
                                    'SuccessPolicy': 1,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 10,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 12,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 18,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 593,
                                                            'Class': 'Condition',
                                                            'Method': (Func1, ()) }] },
                                                {
                                                    'ID': 595,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 573,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 13,
                                                            'Class': 'DecoratorAlwaysRunning',
                                                            'DecorateWhenChildEnds': False,
                                                            'Node': [
                                                                {
                                                                    'ID': 20,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 21,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (8, 12, 15, 30)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 571,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 572,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 574,
                                                                                    'Class': 'Parallel',
                                                                                    'FailurePolicy': 1,
                                                                                    'SuccessPolicy': 0,
                                                                                    'ExitPolicy': 1,
                                                                                    'ChildFinishPolicy': 1,
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 575,
                                                                                            'Class': 'Action',
                                                                                            'Attachment': ({
                                                                                                'ID': 596,
                                                                                                'Class': 'Precondition',
                                                                                                'Method': (cl_betree.monsteragent.CAgent.TryReChooseHateFlankPos, (3, 8, 12, 15, 30)),
                                                                                                'Phase': 1,
                                                                                                'Flag': 'precondition',
                                                                                                'BinaryOperator': 'And' },),
                                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 576,
                                                                                            'Class': 'Sequence',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 583,
                                                                                                    'Class': 'And',
                                                                                                    'Node': [
                                                                                                        {
                                                                                                            'ID': 588,
                                                                                                            'Class': 'Condition',
                                                                                                            'Method': (Func2, ()) },
                                                                                                        {
                                                                                                            'ID': 589,
                                                                                                            'Class': 'Condition',
                                                                                                            'Method': (Func3, ()) }] },
                                                                                                {
                                                                                                    'ID': 584,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None }] }] }] }] }] }] }] },
                                        {
                                            'ID': 640,
                                            'Class': 'Condition',
                                            'Method': (Func4, ()) }] },
                                {
                                    'ID': 11,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 581,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 637,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 0,
                                            'SuccessPolicy': 1,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 608,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 609,
                                                            'Class': 'Action',
                                                            'Method': (Func5, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 610,
                                                            'Class': 'DecoratorAlwaysRunning',
                                                            'DecorateWhenChildEnds': False,
                                                            'Node': [
                                                                {
                                                                    'ID': 611,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 612,
                                                                            'Class': 'WaitFrame',
                                                                            'Frames': 5 },
                                                                        {
                                                                            'ID': 613,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] }] },
                                                {
                                                    'ID': 638,
                                                    'Class': 'Condition',
                                                    'Method': (Func6, ()) }] },
                                        {
                                            'ID': 630,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 631,
                                                    'Class': 'Condition',
                                                    'Method': (Func7, ()) },
                                                {
                                                    'ID': 632,
                                                    'Class': 'Noop' },
                                                {
                                                    'ID': 614,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 1,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 616,
                                                            'Class': 'Condition',
                                                            'Method': (Func8, ()) },
                                                        {
                                                            'ID': 618,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 619,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (4, 6, 60, 75)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 620,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 621,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 622,
                                                                            'Class': 'Parallel',
                                                                            'FailurePolicy': 1,
                                                                            'SuccessPolicy': 0,
                                                                            'ExitPolicy': 1,
                                                                            'ChildFinishPolicy': 1,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 623,
                                                                                    'Class': 'Action',
                                                                                    'Attachment': ({
                                                                                        'ID': 624,
                                                                                        'Class': 'Precondition',
                                                                                        'Method': (cl_betree.monsteragent.CAgent.TryReChooseHateFlankPos, (3, 8, 12, 15, 30)),
                                                                                        'Phase': 1,
                                                                                        'Flag': 'precondition',
                                                                                        'BinaryOperator': 'And' },),
                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 625,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 626,
                                                                                            'Class': 'And',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 628,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func9, ()) },
                                                                                                {
                                                                                                    'ID': 629,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func10, ()) }] },
                                                                                        {
                                                                                            'ID': 627,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None }] }] }] }] }] }] },
                                        {
                                            'ID': 16,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 635,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                'Phase': 1,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 634,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 597,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 598,
                                                    'Class': 'Condition',
                                                    'Method': (Func11, ()) },
                                                {
                                                    'ID': 604,
                                                    'Class': 'SelectorProbability',
                                                    'RandomGenerator': None,
                                                    'Node': [
                                                        {
                                                            'ID': 605,
                                                            'Class': 'DecoratorWeight',
                                                            'DecorateWhenChildEnds': False,
                                                            'Weight': 50,
                                                            'Node': [
                                                                {
                                                                    'ID': 599,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 600,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (20872,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 601,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 602,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] },
                                                        {
                                                            'ID': 606,
                                                            'Class': 'DecoratorWeight',
                                                            'DecorateWhenChildEnds': False,
                                                            'Weight': 50,
                                                            'Node': [
                                                                {
                                                                    'ID': 607,
                                                                    'Class': 'Noop' }] }] },
                                                {
                                                    'ID': 603,
                                                    'Class': 'Noop' }] }] },
                                {
                                    'ID': 591,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 587,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (3, 4, 170, 180)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 590,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (2,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 592,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] }] }] }] }
