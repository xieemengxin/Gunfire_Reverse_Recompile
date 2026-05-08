# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterRide/RideFireAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterRide/RideFireAttack.pyc
# Source Generated with Decompyle++
# File: RideFireAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 21


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 16


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 21


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 25, oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 18


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True

data = {
    'Name': 'RideFireAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 315,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 50,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 3,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 13,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 14,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 15,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 8,
                                                    'Class': 'Condition',
                                                    'Method': (Func0, ()) },
                                                {
                                                    'ID': 5,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 9,
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
                                                            'ID': 12,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToSlopeLockEnemy, (15, 20)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 33,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 19,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 24,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 25,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func1, ()) },
                                                                {
                                                                    'ID': 34,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 49,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToSlopeLockEnemy, (15, 20)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 36,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 37,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 38,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func2, ()) }] }] },
                                                                {
                                                                    'ID': 39,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 48,
                                                                            'Class': 'DecoratorAlwaysRunning',
                                                                            'DecorateWhenChildEnds': False,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 44,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 47,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func3, ()) },
                                                                                        {
                                                                                            'ID': 45,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.KeepMoving, (3,)),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None }] }] },
                                                                        {
                                                                            'ID': 41,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 42,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 43,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func4, ()) }] }] }] }] }] }] }] },
                        {
                            'ID': 51,
                            'Class': 'Condition',
                            'Method': (Func5, ()) }] }] }] }
