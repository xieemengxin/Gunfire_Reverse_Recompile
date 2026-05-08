# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFar/GlobalThrowAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFar/GlobalThrowAttack.pyc
# Source Generated with Decompyle++
# File: GlobalThrowAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckInLockEnemySight(90, 30, 0, oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == False


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckInLockEnemySight(60, 30, 0, oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == False


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.GetArrivePosDis(oAgent) >= 25


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.CheckInLockEnemySight(60, 30, 0, oAgent) == True


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True

data = {
    'Name': 'GlobalThrowAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 170,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseNearestHateTarget, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 406,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 562,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 563,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 254,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 591,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 0,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 576,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 606,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 593,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 0,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 318,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 1,
                                                            'ExitPolicy': 1,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 609,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 0,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
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
                                                                                            'Method': (Func1, ()) },
                                                                                        {
                                                                                            'ID': 403,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func2, ()) }] },
                                                                                {
                                                                                    'ID': 401,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func3, ()) }] },
                                                                        {
                                                                            'ID': 610,
                                                                            'Class': 'WaitFrame',
                                                                            'Frames': 50 }] },
                                                                {
                                                                    'ID': 518,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 519,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseEnemyPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 523,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
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
                                                                                    'ID': 538,
                                                                                    'Class': 'Parallel',
                                                                                    'FailurePolicy': 1,
                                                                                    'SuccessPolicy': 0,
                                                                                    'ExitPolicy': 1,
                                                                                    'ChildFinishPolicy': 1,
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 539,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 540,
                                                                                            'Class': 'Sequence',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 543,
                                                                                                    'Class': 'And',
                                                                                                    'Node': [
                                                                                                        {
                                                                                                            'ID': 547,
                                                                                                            'Class': 'Condition',
                                                                                                            'Method': (Func4, ()) },
                                                                                                        {
                                                                                                            'ID': 548,
                                                                                                            'Class': 'Condition',
                                                                                                            'Method': (Func5, ()) }] },
                                                                                                {
                                                                                                    'ID': 544,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None }] }] },
                                                                                {
                                                                                    'ID': 530,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] }] }] },
                                                        {
                                                            'ID': 607,
                                                            'Class': 'And',
                                                            'Node': [
                                                                {
                                                                    'ID': 594,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func6, ()) },
                                                                {
                                                                    'ID': 608,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func7, ()) }] }] },
                                                {
                                                    'ID': 577,
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
                                                    'ID': 578,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 602,
                                            'Class': 'Condition',
                                            'Method': (Func8, ()) },
                                        {
                                            'ID': 573,
                                            'Class': 'Condition',
                                            'Method': (Func9, ()) }] }] },
                        {
                            'ID': 564,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 565,
                                    'Class': 'SelectorProbability',
                                    'RandomGenerator': None,
                                    'Node': [
                                        {
                                            'ID': 567,
                                            'Class': 'DecoratorWeight',
                                            'DecorateWhenChildEnds': False,
                                            'Weight': 20,
                                            'Node': [
                                                {
                                                    'ID': 626,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 20 }] },
                                        {
                                            'ID': 568,
                                            'Class': 'DecoratorWeight',
                                            'DecorateWhenChildEnds': False,
                                            'Weight': 10,
                                            'Node': [
                                                {
                                                    'ID': 580,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 581,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 596,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 0,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 598,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func10, ()) },
                                                                {
                                                                    'ID': 625,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 620,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (4, 10, 30, 90)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 627,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 628,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 629,
                                                                            'Class': 'Parallel',
                                                                            'FailurePolicy': 1,
                                                                            'SuccessPolicy': 0,
                                                                            'ExitPolicy': 1,
                                                                            'ChildFinishPolicy': 1,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 630,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 631,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 632,
                                                                                            'Class': 'And',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 634,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func11, ()) },
                                                                                                {
                                                                                                    'ID': 635,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func12, ()) }] },
                                                                                        {
                                                                                            'ID': 633,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None }] }] }] }] },
                                                        {
                                                            'ID': 603,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 605,
                                                                'Class': 'Precondition',
                                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                'Phase': 1,
                                                                'Flag': 'precondition',
                                                                'BinaryOperator': 'And' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 604,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] }] }] }] }] }
