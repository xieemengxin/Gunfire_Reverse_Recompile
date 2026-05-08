# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteNear/EliteDashAttackAfter.pyc
# RelativePath: clientlogic/cl_betreedata/EliteNear/EliteDashAttackAfter.pyc
# Source Generated with Decompyle++
# File: EliteDashAttackAfter.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockNavMeshRayCast(5, oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) > 7


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 5

data = {
    'Name': 'EliteDashAttackAfter',
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
                    'ID': 21,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 48,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 29,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 30,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 56,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 58,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 31,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 20,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 43,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                'Phase': 1,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 3,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 4,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) },
                                                {
                                                    'ID': 5,
                                                    'Class': 'SelectorProbability',
                                                    'RandomGenerator': None,
                                                    'Node': [
                                                        {
                                                            'ID': 6,
                                                            'Class': 'DecoratorWeight',
                                                            'DecorateWhenChildEnds': False,
                                                            'Weight': 20,
                                                            'Node': [
                                                                {
                                                                    'ID': 9,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 33,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetCustomData, ('MonsterDashChoosePFFlag', 1)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 66,
                                                                            'Class': 'Parallel',
                                                                            'FailurePolicy': 0,
                                                                            'SuccessPolicy': 0,
                                                                            'ExitPolicy': 0,
                                                                            'ChildFinishPolicy': 1,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 78,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (40, 1)),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 67,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 68,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseEnemyPos, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 69,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 70,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None }] },
                                                                                {
                                                                                    'ID': 71,
                                                                                    'Class': 'WaitFrame',
                                                                                    'Frames': 12 }] },
                                                                        {
                                                                            'ID': 8,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (31343,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] },
                                                        {
                                                            'ID': 7,
                                                            'Class': 'DecoratorWeight',
                                                            'DecorateWhenChildEnds': False,
                                                            'Weight': 80,
                                                            'Node': [
                                                                {
                                                                    'ID': 35,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetCustomData, ('DashAfterMove', 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] },
                                                {
                                                    'ID': 16,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 34,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetCustomData, ('MonsterDashChoosePFFlag', 1)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 50,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 0,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 0,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 79,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (40, 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 51,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 49,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseEnemyPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 53,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 55,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] },
                                                                {
                                                                    'ID': 52,
                                                                    'Class': 'WaitFrame',
                                                                    'Frames': 12 }] },
                                                        {
                                                            'ID': 18,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (31341,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] },
                                {
                                    'ID': 59,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 60,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (8, 1, 2, 70, 110)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 72,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 77,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 63,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 0,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 75,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 74,
                                                            'Class': 'Condition',
                                                            'Method': (Func3, ()) },
                                                        {
                                                            'ID': 76,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (31341,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 65,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 64,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 75 }] }] }] },
                        {
                            'ID': 32,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetCustomData, ('CanChoosePF', 1)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
