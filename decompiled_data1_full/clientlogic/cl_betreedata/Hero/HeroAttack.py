# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Hero/HeroAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Hero/HeroAttack.pyc
# Source Generated with Decompyle++
# File: HeroAttack.pyc (Python 3.6)

import cl_betree.heroagent

def Func0(oAgent):
    return cl_betree.heroagent.CAgent.GetLeaderDis(oAgent) <= 10


def Func1(oAgent):
    return cl_betree.heroagent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.heroagent.CAgent.CanUseCareerPF(oAgent) == True


def Func3(oAgent):
    return cl_betree.heroagent.CAgent.CanUseThrowPF(oAgent) == True


def Func4(oAgent):
    return cl_betree.heroagent.CAgent.GetLeaderDis(oAgent) <= 10


def Func5(oAgent):
    return cl_betree.heroagent.CAgent.GetLeaderDis(oAgent) >= 10

data = {
    'Name': 'HeroAttack',
    'ID': 0,
    'AgentType': 'cl_betree.heroagent',
    'IsFSM': False,
    'Ver': 103,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 50,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 51,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 62,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.ChooseTarget, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 54,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.FaceTarget, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 79,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 111,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 80,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 112,
                                            'Class': 'Noop' },
                                        {
                                            'ID': 113,
                                            'Class': 'DecoratorAlwaysFailure',
                                            'DecorateWhenChildEnds': False,
                                            'Node': [
                                                {
                                                    'ID': 114,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.CancelLockTarget, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 104,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 105,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) },
                                        {
                                            'ID': 106,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.UseCareerPF, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 118,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 119,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) },
                                                {
                                                    'ID': 120,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.UseThrowPF, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 121,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.Attack, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 117,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.CancelLockTarget, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 82,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 89,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 90,
                                            'Class': 'Condition',
                                            'Method': (Func4, ()) },
                                        {
                                            'ID': 93,
                                            'Class': 'SelectorProbability',
                                            'RandomGenerator': None,
                                            'Node': [
                                                {
                                                    'ID': 94,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 25,
                                                    'Node': [
                                                        {
                                                            'ID': 96,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 50 }] },
                                                {
                                                    'ID': 95,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 25,
                                                    'Node': [
                                                        {
                                                            'ID': 100,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 25 }] },
                                                {
                                                    'ID': 98,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 50,
                                                    'Node': [
                                                        {
                                                            'ID': 101,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 102,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.heroagent.CAgent.ChooseEnemyAroundPos, (10, 15, 0)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 115,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 0,
                                                                    'SuccessPolicy': 1,
                                                                    'ExitPolicy': 0,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 103,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.heroagent.CAgent.MoveToPos, (2,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 116,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func5, ()) }] }] }] }] },
                                        {
                                            'ID': 67,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 68,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.ChooseLeaderPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 69,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.MoveToPos, (2,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] }] }] }] }
