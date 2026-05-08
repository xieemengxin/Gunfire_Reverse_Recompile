# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumFar/MediumFarFuzzyChargeAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumFar/MediumFarFuzzyChargeAttack.pyc
# Source Generated with Decompyle++
# File: MediumFarFuzzyChargeAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, oAgent.GetConfig('IntervalTime'), oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 5


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 5


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True

data = {
    'Name': 'MediumFarFuzzyChargeAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 100,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Attachment': ({
                'ID': 35,
                'Class': 'Effector',
                'Method': (cl_betree.monsteragent.CAgent.SetFightLogicType, (1,)),
                'Phase': 1,
                'Flag': 'effector' }, {
                'ID': 34,
                'Class': 'Precondition',
                'Method': (cl_betree.monsteragent.CAgent.SetFightLogicType, (2,)),
                'Phase': 1,
                'Flag': 'precondition',
                'BinaryOperator': 'And' }),
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
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 693,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 759,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 4,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 7,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 5,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 32,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                                'Phase': 1,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 758,
                                            'Class': 'Or',
                                            'Node': [
                                                {
                                                    'ID': 553,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 1,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 430,
                                                            'Class': 'And',
                                                            'Node': [
                                                                {
                                                                    'ID': 431,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func0, ()) },
                                                                {
                                                                    'ID': 432,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func1, ()) }] },
                                                        {
                                                            'ID': 462,
                                                            'Class': 'Condition',
                                                            'Method': (Func2, ()) }] },
                                                {
                                                    'ID': 757,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) }] }] },
                                {
                                    'ID': 30,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 656,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 658,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 662,
                                                            'Class': 'Condition',
                                                            'Method': (Func4, ()) },
                                                        {
                                                            'ID': 715,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 712,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (8, 2, 5, 165, 180)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 717,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 742,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 735,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 736,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 737,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 747,
                                                                                    'Class': 'And',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 753,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func5, ()) },
                                                                                        {
                                                                                            'ID': 754,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func6, ()) }] },
                                                                                {
                                                                                    'ID': 748,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] }] }] },
                                                        {
                                                            'ID': 716,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 711,
                                                                    'Class': 'Action',
                                                                    'Method': (Func7, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 718,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 743,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 728,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 729,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 730,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 749,
                                                                                    'Class': 'And',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 755,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func8, ()) },
                                                                                        {
                                                                                            'ID': 756,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func9, ()) }] },
                                                                                {
                                                                                    'ID': 750,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] }] }] }] }] }] }] },
                        {
                            'ID': 760,
                            'Class': 'Condition',
                            'Method': (Func10, ()) }] },
                {
                    'ID': 713,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 714,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 692,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 624,
                    'Class': 'SelectorProbability',
                    'RandomGenerator': None,
                    'Node': [
                        {
                            'ID': 625,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 50,
                            'Node': [
                                {
                                    'ID': 694,
                                    'Class': 'Noop' }] },
                        {
                            'ID': 626,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 50,
                            'Node': [
                                {
                                    'ID': 628,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 631,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (4, 7, 85, 95)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 632,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 633,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (2,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 634,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] }] }] }] }
