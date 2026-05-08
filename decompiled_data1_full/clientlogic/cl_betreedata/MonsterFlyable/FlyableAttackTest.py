# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFlyable/FlyableAttackTest.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFlyable/FlyableAttackTest.pyc
# Source Generated with Decompyle++
# File: FlyableAttackTest.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, oAgent.GetConfig('IntervalTime'), oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == False


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedFlyPos(1, 0, 5, oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), -2, 2, oAgent)


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 5


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'FlyableAttackTest',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 57,
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
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 206,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 235,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 236,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 207,
                                    'Class': 'And',
                                    'Node': [
                                        {
                                            'ID': 239,
                                            'Class': 'And',
                                            'Node': [
                                                {
                                                    'ID': 245,
                                                    'Class': 'And',
                                                    'Node': [
                                                        {
                                                            'ID': 208,
                                                            'Class': 'Condition',
                                                            'Method': (Func0, ()) },
                                                        {
                                                            'ID': 237,
                                                            'Class': 'Condition',
                                                            'Method': (Func1, ()) }] },
                                                {
                                                    'ID': 211,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) }] },
                                        {
                                            'ID': 215,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) }] },
                                {
                                    'ID': 243,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 5,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 202,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                'Phase': 1,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 203,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 209,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 212,
                                            'Class': 'Action',
                                            'Method': (Func4, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 219,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 221,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 225,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 226,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 242,
                                                            'Class': 'Condition',
                                                            'Method': (Func5, ()) },
                                                        {
                                                            'ID': 247,
                                                            'Class': 'Condition',
                                                            'Method': (Func6, ()) },
                                                        {
                                                            'ID': 230,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] }] }] }] }] }
