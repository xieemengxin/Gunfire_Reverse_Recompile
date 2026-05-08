# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFar/GlobalThrowMove.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFar/GlobalThrowMove.pyc
# Source Generated with Decompyle++
# File: GlobalThrowMove.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= oAgent.GetConfig('FightMaxDis')


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CheckInLockEnemySight(60, 30, 0, oAgent) == True


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= oAgent.GetConfig('FightMinDis')


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CheckInLockEnemySight(60, 30, 0, oAgent) == True

data = {
    'Name': 'GlobalThrowMove',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 28,
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
                            'ID': 25,
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
                                            'ID': 20,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 0,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 21,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 22,
                                                            'Class': 'And',
                                                            'Node': [
                                                                {
                                                                    'ID': 23,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func0, ()) },
                                                                {
                                                                    'ID': 24,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func1, ()) }] }] },
                                                {
                                                    'ID': 5,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 9,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (15, 20, 60, 120)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 8,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 10,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 11,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 0,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 12,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 13,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 14,
                                                                            'Class': 'And',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 15,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func2, ()) },
                                                                                {
                                                                                    'ID': 16,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func3, ()) }] },
                                                                        {
                                                                            'ID': 17,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] }] }] }] },
                                {
                                    'ID': 27,
                                    'Class': 'And',
                                    'Node': [
                                        {
                                            'ID': 26,
                                            'Class': 'Condition',
                                            'Method': (Func4, ()) },
                                        {
                                            'ID': 28,
                                            'Class': 'Condition',
                                            'Method': (Func5, ()) }] }] },
                        {
                            'ID': 42,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 43,
                                    'Class': 'Condition',
                                    'Method': (Func6, ()) },
                                {
                                    'ID': 44,
                                    'Class': 'Condition',
                                    'Method': (Func7, ()) },
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
                                    'ID': 49,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 50,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (30, 1)),
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
