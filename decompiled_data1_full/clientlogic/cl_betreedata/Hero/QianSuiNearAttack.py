# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Hero/QianSuiNearAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Hero/QianSuiNearAttack.pyc
# Source Generated with Decompyle++
# File: QianSuiNearAttack.pyc (Python 3.6)

import cl_betree.heroagent

def Func0(oAgent):
    return cl_betree.heroagent.CAgent.IsUsingCareerPF(oAgent) == True


def Func1(oAgent):
    return cl_betree.heroagent.CAgent.IsUsingCareerPF(oAgent) == True


def Func2(oAgent):
    return cl_betree.heroagent.CAgent.CanUseCareerPF(oAgent) == True


def Func3(oAgent):
    return cl_betree.heroagent.CAgent.CheckCanSeeLock(oAgent) == True


def Func4(oAgent):
    return cl_betree.heroagent.CAgent.CanUseThrowPF(oAgent) == True


def Func5(oAgent):
    return cl_betree.heroagent.CAgent.GetLockEnemyDis(oAgent) <= 7


def Func6(oAgent):
    return cl_betree.heroagent.CAgent.GetLockEnemyDis(oAgent) >= 12

data = {
    'Name': 'QianSuiNearAttack',
    'ID': 0,
    'AgentType': 'cl_betree.heroagent',
    'IsFSM': False,
    'Ver': 124,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.heroagent.CAgent.ChooseTarget, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 5,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 36,
                            'Class': 'Parallel',
                            'FailurePolicy': 0,
                            'SuccessPolicy': 1,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 37,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 6,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 11,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.FaceTarget, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 10,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.MoveToLockEnemy, (3,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 12,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.CancelShield, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 15,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 19,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 49,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.ChooseTarget, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 47,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.FaceTarget, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 26,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 31,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) },
                                                {
                                                    'ID': 32,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.UseCareerPF, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 38,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 51,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 39,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func3, ()) },
                                                                {
                                                                    'ID': 52,
                                                                    'Class': 'Noop' },
                                                                {
                                                                    'ID': 53,
                                                                    'Class': 'DecoratorAlwaysFailure',
                                                                    'DecorateWhenChildEnds': False,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 54,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.heroagent.CAgent.CancelLockTarget, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] },
                                                        {
                                                            'ID': 56,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 60,
                                                                    'Class': 'And',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 57,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func4, ()) },
                                                                        {
                                                                            'ID': 59,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func5, ()) }] },
                                                                {
                                                                    'ID': 61,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.heroagent.CAgent.UseThrowPF, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 33,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.heroagent.CAgent.Attack, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 55,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.heroagent.CAgent.CancelLockTarget, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] },
                                {
                                    'ID': 50,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 41,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 42,
                                                    'Class': 'Condition',
                                                    'Method': (Func6, ()) },
                                                {
                                                    'ID': 43,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.MoveToLockEnemy, (10,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 44,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 45,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.heroagent.CAgent.ChooseEnemyAroundPos, (10, 15, 0)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 46,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.heroagent.CAgent.MoveToPos, (2,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] }] }] }] }] }
