# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumFar/InvisibleFarRetreatAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumFar/InvisibleFarRetreatAttack.pyc
# Source Generated with Decompyle++
# File: InvisibleFarRetreatAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 4


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, oAgent.GetConfig('IntervalTime'), oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 4

data = {
    'Name': 'InvisibleFarRetreatAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 110,
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
                    'ID': 693,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 730,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 731,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 732,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 733,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 734,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 735,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 736,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 759,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 0,
                                    'SuccessPolicy': 1,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 737,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 738,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 740,
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
                                                            'ID': 741,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 1,
                                                            'ExitPolicy': 1,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 744,
                                                                    'Class': 'And',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 748,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func1, ()) },
                                                                        {
                                                                            'ID': 749,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func2, ()) }] },
                                                                {
                                                                    'ID': 745,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func3, ()) }] }] },
                                                {
                                                    'ID': 739,
                                                    'Class': 'DecoratorAlwaysRunning',
                                                    'DecorateWhenChildEnds': False,
                                                    'Node': [
                                                        {
                                                            'ID': 743,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 746,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (5, 3, 7, 150, 180)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 747,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] },
                                        {
                                            'ID': 760,
                                            'Class': 'Condition',
                                            'Method': (Func4, ()) }] },
                                {
                                    'ID': 751,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 752,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 742,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 756,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 755,
                                            'Class': 'Condition',
                                            'Method': (Func5, ()) },
                                        {
                                            'ID': 757,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 753,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (21423,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 754,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 758,
                                            'Class': 'Noop' }] }] }] }] }] }
