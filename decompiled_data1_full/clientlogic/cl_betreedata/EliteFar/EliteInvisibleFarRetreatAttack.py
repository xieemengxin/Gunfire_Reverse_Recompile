# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteFar/EliteInvisibleFarRetreatAttack.pyc
# RelativePath: clientlogic/cl_betreedata/EliteFar/EliteInvisibleFarRetreatAttack.pyc
# Source Generated with Decompyle++
# File: EliteInvisibleFarRetreatAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 4


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 50, oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 4

data = {
    'Name': 'EliteInvisibleFarRetreatAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 7,
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
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 6,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 7,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 9,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 10,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 11,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 8,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 41,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 0,
                                    'SuccessPolicy': 1,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 12,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 17,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 19,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 20,
                                                                'Class': 'Precondition',
                                                                'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                                                'Phase': 1,
                                                                'Flag': 'precondition',
                                                                'BinaryOperator': 'And' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 21,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 1,
                                                            'ExitPolicy': 1,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 22,
                                                                    'Class': 'And',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 24,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func1, ()) },
                                                                        {
                                                                            'ID': 25,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func2, ()) }] },
                                                                {
                                                                    'ID': 23,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func3, ()) }] }] },
                                                {
                                                    'ID': 18,
                                                    'Class': 'DecoratorAlwaysRunning',
                                                    'DecorateWhenChildEnds': False,
                                                    'Node': [
                                                        {
                                                            'ID': 26,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 27,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (5, 3, 7, 150, 180)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 34,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 35,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 36,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 37,
                                                                                    'Class': 'And',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 39,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func4, ()) },
                                                                                        {
                                                                                            'ID': 40,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func5, ()) }] },
                                                                                {
                                                                                    'ID': 38,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] }] }] }] }] },
                                        {
                                            'ID': 42,
                                            'Class': 'Condition',
                                            'Method': (Func6, ()) }] },
                                {
                                    'ID': 13,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 14,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 15,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 16,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 29,
                                            'Class': 'Condition',
                                            'Method': (Func7, ()) },
                                        {
                                            'ID': 30,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 32,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (31243,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 33,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 31,
                                            'Class': 'Noop' }] }] }] }] }] }
