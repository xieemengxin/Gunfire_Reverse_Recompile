# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Hero/BigCangJueAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Hero/BigCangJueAttack.pyc
# Source Generated with Decompyle++
# File: BigCangJueAttack.pyc (Python 3.6)

import cl_betree.heroagent

def Func0(oAgent):
    return cl_betree.heroagent.CAgent.IsUsingCareerPF(oAgent) == True


def Func1(oAgent):
    return cl_betree.heroagent.CAgent.CheckCangJuePerform(1, oAgent) == True


def Func2(oAgent):
    return cl_betree.heroagent.CAgent.CheckCangJuePerform(3, oAgent) == True


def Func3(oAgent):
    return cl_betree.heroagent.CAgent.CheckHasState(33855, oAgent) == True


def Func4(oAgent):
    return cl_betree.heroagent.CAgent.CheckCangJuePerform(2, oAgent) == True

data = {
    'Name': 'BigCangJueAttack',
    'ID': 0,
    'AgentType': 'cl_betree.heroagent',
    'IsFSM': False,
    'Ver': 149,
    'Node': [
        {
            'ID': 3,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 7,
                    'Class': 'Action',
                    'Method': (cl_betree.heroagent.CAgent.ChooseTarget, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 59,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 60,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 61,
                            'Class': 'Noop' },
                        {
                            'ID': 62,
                            'Class': 'Action',
                            'Method': (cl_betree.heroagent.CAgent.UseCareerPF, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 18,
                    'Class': 'Action',
                    'Method': (cl_betree.heroagent.CAgent.FaceTarget, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 8,
                    'Class': 'Action',
                    'Method': (cl_betree.heroagent.CAgent.ChooseCangJuePerformType, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 9,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 10,
                            'Class': 'Condition',
                            'Method': (Func1, ()) },
                        {
                            'ID': 13,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 14,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.MoveToLockEnemy, (3,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 15,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.SetCertainPFIndex, (1330, 0)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 16,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.UseCertainPF, (1330,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 19,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.SetCertainPFIndex, (1330, 1)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 20,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.UseCertainPF, (1330,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 21,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.SetCertainPFIndex, (1330, 1)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 22,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.UseCertainPF, (1330,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 53,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.SetCangJuePerformTypeCD, (1, 75)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 23,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 24,
                                    'Class': 'Condition',
                                    'Method': (Func2, ()) },
                                {
                                    'ID': 25,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 26,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.MoveToLockEnemy, (3,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 67,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.SetCertainPFIndex, (1336, 0)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 30,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.UseCertainPF, (1336,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 68,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.SetCertainPFIndex, (1336, 1)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 69,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.UseCertainPF, (1336,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 63,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 64,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) },
                                                {
                                                    'ID': 65,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 27,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.heroagent.CAgent.SetCertainPFIndex, (1336, 2)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 28,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.heroagent.CAgent.UseCertainPF, (1336,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 70,
                                                    'Class': 'Noop' }] },
                                        {
                                            'ID': 54,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.SetCangJuePerformTypeCD, (3, 75)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 31,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 32,
                                            'Class': 'Condition',
                                            'Method': (Func4, ()) },
                                        {
                                            'ID': 33,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 34,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.MoveToLockEnemy, (3,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 41,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 0,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 0,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 42,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 35,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.heroagent.CAgent.SetCertainPFIndex, (1330, 3)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 36,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.heroagent.CAgent.UseCertainPF, (1330,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 55,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.heroagent.CAgent.SetCangJuePerformTypeCD, (2, 100)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 43,
                                                            'Class': 'DecoratorAlwaysRunning',
                                                            'DecorateWhenChildEnds': False,
                                                            'Node': [
                                                                {
                                                                    'ID': 44,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.heroagent.CAgent.MoveToLockEnemy, (3,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] },
                                        {
                                            'ID': 37,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 38,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.MoveToLockEnemy, (3,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 52,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.AddState, (33711, 300)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 57,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 75 },
                                                {
                                                    'ID': 58,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.SetCangJuePerformTypeCD, (4, 250)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] }] }] }] }
