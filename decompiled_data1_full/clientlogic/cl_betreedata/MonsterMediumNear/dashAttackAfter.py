# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumNear/dashAttackAfter.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumNear/dashAttackAfter.pyc
# Source Generated with Decompyle++
# File: dashAttackAfter.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockNavMeshRayCast(5, oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) > 7


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 5


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 5

data = {
    'Name': 'dashAttackAfter',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 60,
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
                    'ID': 19,
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
                            'ID': 31,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 35,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 36,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 37,
                                            'Class': 'Noop' },
                                        {
                                            'ID': 38,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 39,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 40,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 41,
                                                    'Class': 'Action',
                                                    'Method': (Func2, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 48,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 49,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) },
                                        {
                                            'ID': 45,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 20,
                                                    'Class': 'Action',
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
                                                            'Method': (Func4, ()) },
                                                        {
                                                            'ID': 55,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 0,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 11,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 13,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseEnemyPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 12,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 92,
                                                                            'Class': 'Parallel',
                                                                            'FailurePolicy': 1,
                                                                            'SuccessPolicy': 0,
                                                                            'ExitPolicy': 0,
                                                                            'ChildFinishPolicy': 1,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 14,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (50, 1)),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 15,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 93,
                                                                                    'Class': 'WaitFrame',
                                                                                    'Frames': 75 }] },
                                                                        {
                                                                            'ID': 24,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetCustomData, ('CanChoosePF', 1)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] },
                                                                {
                                                                    'ID': 56,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 57,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func5, ()) },
                                                                        {
                                                                            'ID': 58,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetCustomData, ('DashAfterChoosePFFlag', 1)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 59,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (0,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 60,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 61,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (21341,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] },
                                                        {
                                                            'ID': 16,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 34,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetCustomData, ('DashAfterChoosePFFlag', 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 70,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 96,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (0,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 71,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseEnemyPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 72,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 94,
                                                                            'Class': 'Parallel',
                                                                            'FailurePolicy': 1,
                                                                            'SuccessPolicy': 0,
                                                                            'ExitPolicy': 0,
                                                                            'ChildFinishPolicy': 1,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 73,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (40, 1)),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 84,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 68,
                                                                                    'Class': 'WaitFrame',
                                                                                    'Frames': 12 }] },
                                                                        {
                                                                            'ID': 95,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (21341,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] }] }] },
                                        {
                                            'ID': 50,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 51,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (8, 1, 2, 70, 110)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 52,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 53,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 86,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 0,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 54,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 90,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 75 },
                                                        {
                                                            'ID': 87,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 89,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func6, ()) },
                                                                {
                                                                    'ID': 91,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (21341,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] }] }] },
                        {
                            'ID': 32,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetCustomData, ('CanChoosePF', 1)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
