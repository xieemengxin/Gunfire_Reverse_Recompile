# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumFar/MediumFarGuerrillaAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumFar/MediumFarGuerrillaAttack.pyc
# Source Generated with Decompyle++
# File: MediumFarGuerrillaAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 4


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, oAgent.GetConfig('IntervalTime'), oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 30


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), 85, 95, oAgent)


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(30, oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), 85, 95, oAgent)


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetLastArrIdx(oAgent) == 0


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True

data = {
    'Name': 'MediumFarGuerrillaAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 113,
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
                    'ID': 36,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 37,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 38,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 66,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 67,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 68,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 69,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 755,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 70,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 735,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 39,
                            'Class': 'SelectorProbability',
                            'RandomGenerator': None,
                            'Node': [
                                {
                                    'ID': 40,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 40,
                                    'Node': [
                                        {
                                            'ID': 52,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 0,
                                            'SuccessPolicy': 1,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 756,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 53,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 55,
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
                                                                    'ID': 744,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func1, ()) },
                                                                {
                                                                    'ID': 63,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func2, ()) },
                                                                {
                                                                    'ID': 64,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func3, ()) },
                                                                {
                                                                    'ID': 754,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 57,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 54,
                                                            'Class': 'DecoratorAlwaysRunning',
                                                            'DecorateWhenChildEnds': False,
                                                            'Node': [
                                                                {
                                                                    'ID': 745,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 746,
                                                                            'Class': 'IfElse',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 751,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func4, ()) },
                                                                                {
                                                                                    'ID': 752,
                                                                                    'Class': 'Action',
                                                                                    'Method': (Func5, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 753,
                                                                                    'Class': 'Action',
                                                                                    'Method': (Func6, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] },
                                                                        {
                                                                            'ID': 758,
                                                                            'Class': 'Parallel',
                                                                            'FailurePolicy': 1,
                                                                            'SuccessPolicy': 0,
                                                                            'ExitPolicy': 1,
                                                                            'ChildFinishPolicy': 1,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 750,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 759,
                                                                                    'Class': 'DecoratorAlwaysRunning',
                                                                                    'DecorateWhenChildEnds': False,
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 760,
                                                                                            'Class': 'IfElse',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 761,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func7, ()) },
                                                                                                {
                                                                                                    'ID': 762,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (7, 9, 15, 30)),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None },
                                                                                                {
                                                                                                    'ID': 763,
                                                                                                    'Class': 'Noop' }] }] }] }] }] }] },
                                                {
                                                    'ID': 757,
                                                    'Class': 'Condition',
                                                    'Method': (Func8, ()) }] }] },
                                {
                                    'ID': 41,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 60,
                                    'Node': [
                                        {
                                            'ID': 736,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 737,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (4, 7, 85, 95)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 738,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 739,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (2,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 740,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 741,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 742,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 743,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] }] }] }] }
