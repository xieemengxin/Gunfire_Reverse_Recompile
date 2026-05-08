# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Hero/SmallCangJueAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Hero/SmallCangJueAttack.pyc
# Source Generated with Decompyle++
# File: SmallCangJueAttack.pyc (Python 3.6)

import cl_betree.heroagent

def Func0(oAgent):
    return cl_betree.heroagent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.heroagent.CAgent.CanUseThrowPF(oAgent) == True


def Func2(oAgent):
    return cl_betree.heroagent.CAgent.GetLockEnemyDis(oAgent) <= 15


def Func3(oAgent):
    return cl_betree.heroagent.CAgent.GetLockEnemyDis(oAgent) >= 12

data = {
    'Name': 'SmallCangJueAttack',
    'ID': 0,
    'AgentType': 'cl_betree.heroagent',
    'IsFSM': False,
    'Ver': 123,
    'Node': [
        {
            'ID': 1,
            'Class': 'Parallel',
            'FailurePolicy': 1,
            'SuccessPolicy': 0,
            'ExitPolicy': 1,
            'ChildFinishPolicy': 1,
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 4,
                            'Class': 'Action',
                            'Method': (cl_betree.heroagent.CAgent.ChooseTarget, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 5,
                            'Class': 'Action',
                            'Method': (cl_betree.heroagent.CAgent.FaceTarget, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 6,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 10,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 11,
                                    'Class': 'Noop' },
                                {
                                    'ID': 12,
                                    'Class': 'DecoratorAlwaysFailure',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 19,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.CancelLockTarget, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 7,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 13,
                                    'Class': 'And',
                                    'Node': [
                                        {
                                            'ID': 20,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 21,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) }] },
                                {
                                    'ID': 14,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.UseThrowPF, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 15,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 8,
                            'Class': 'Action',
                            'Method': (cl_betree.heroagent.CAgent.CancelLockTarget, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 3,
                    'Class': 'DecoratorAlwaysRunning',
                    'DecorateWhenChildEnds': False,
                    'Node': [
                        {
                            'ID': 9,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 16,
                                    'Class': 'Condition',
                                    'Method': (Func3, ()) },
                                {
                                    'ID': 17,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.MoveToLockEnemy, (10,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 18,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 22,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.ChooseEnemyAroundPos, (10, 15, 0)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 23,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.MoveToPos, (2,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] }] }] }] }
