# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterSniper/GlobalSniperAreaMove.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterSniper/GlobalSniperAreaMove.pyc
# Source Generated with Decompyle++
# File: GlobalSniperAreaMove.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 30


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= oAgent.GetConfig('FightMinDis')


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckInLockEnemySight(60, 30, 0, oAgent) == True

data = {
    'Name': 'GlobalSniperAreaMove',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 26,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 41,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 0,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 2,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 7,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseNearestHateTarget, (10,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 6,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 49,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 50,
                                                    'Class': 'Condition',
                                                    'Method': (Func0, ()) },
                                                {
                                                    'ID': 51,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedAreaPos, (5, 20, 5)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 52,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 53,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (10, 20, 30, 90)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 54,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 55,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 57,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 1,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 58,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 59,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 60,
                                                                            'Class': 'And',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 62,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func1, ()) },
                                                                                {
                                                                                    'ID': 63,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func2, ()) }] },
                                                                        {
                                                                            'ID': 61,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] },
                                                        {
                                                            'ID': 56,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangedAreaPos, (5, 20, 10)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] },
                                        {
                                            'ID': 32,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 33,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 34,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 0,
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
                                                                    'ID': 38,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func3, ()) },
                                                                {
                                                                    'ID': 39,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func4, ()) }] },
                                                        {
                                                            'ID': 40,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] }] },
                        {
                            'ID': 42,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 43,
                                    'Class': 'Condition',
                                    'Method': (Func5, ()) },
                                {
                                    'ID': 44,
                                    'Class': 'Condition',
                                    'Method': (Func6, ()) },
                                {
                                    'ID': 45,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseShotPF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 46,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ForceOccupyAttackToken, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 47,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 48,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ReleaseAttackToken, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
