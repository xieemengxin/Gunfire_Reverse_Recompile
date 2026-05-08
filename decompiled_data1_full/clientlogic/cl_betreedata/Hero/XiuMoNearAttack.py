# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Hero/XiuMoNearAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Hero/XiuMoNearAttack.pyc
# Source Generated with Decompyle++
# File: XiuMoNearAttack.pyc (Python 3.6)

import cl_betree.heroagent

def Func0(oAgent):
    return cl_betree.heroagent.CAgent.CanUseCareerPF(oAgent) == True


def Func1(oAgent):
    return cl_betree.heroagent.CAgent.GetLockEnemyDis(oAgent) >= 5


def Func2(oAgent):
    return cl_betree.heroagent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.heroagent.CAgent.CanUseThrowPF(oAgent) == True


def Func4(oAgent):
    return cl_betree.heroagent.CAgent.GetLockEnemyDis(oAgent) <= 15


def Func5(oAgent):
    return cl_betree.heroagent.CAgent.GetLockEnemyDis(oAgent) >= 12

data = {
    'Name': 'XiuMoNearAttack',
    'ID': 0,
    'AgentType': 'cl_betree.heroagent',
    'IsFSM': False,
    'Ver': 121,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 98,
                    'Class': 'Action',
                    'Method': (cl_betree.heroagent.CAgent.ChooseTarget, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 89,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 118,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 126,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 128,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.ChooseTarget, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 129,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.FaceTarget, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 130,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 0,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 127,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.UseCareerPF, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 131,
                                            'Class': 'DecoratorAlwaysRunning',
                                            'DecorateWhenChildEnds': False,
                                            'Node': [
                                                {
                                                    'ID': 132,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 133,
                                                            'Class': 'Condition',
                                                            'Method': (Func1, ()) },
                                                        {
                                                            'ID': 134,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.heroagent.CAgent.MoveToLockEnemy, (4,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 135,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 136,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.heroagent.CAgent.ChooseEnemyAroundPos, (4, 8, 2)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 137,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.heroagent.CAgent.MoveToPos, (2,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] }] }] },
                        {
                            'ID': 87,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 103,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 104,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.ChooseTarget, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 108,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.FaceTarget, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 138,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 106,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) },
                                                {
                                                    'ID': 139,
                                                    'Class': 'Noop' },
                                                {
                                                    'ID': 140,
                                                    'Class': 'DecoratorAlwaysFailure',
                                                    'DecorateWhenChildEnds': False,
                                                    'Node': [
                                                        {
                                                            'ID': 141,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.heroagent.CAgent.CancelLockTarget, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] },
                                        {
                                            'ID': 143,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 144,
                                                    'Class': 'And',
                                                    'Node': [
                                                        {
                                                            'ID': 145,
                                                            'Class': 'Condition',
                                                            'Method': (Func3, ()) },
                                                        {
                                                            'ID': 146,
                                                            'Class': 'Condition',
                                                            'Method': (Func4, ()) }] },
                                                {
                                                    'ID': 147,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.UseThrowPF, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 96,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.Attack, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 142,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.CancelLockTarget, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 117,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 82,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 83,
                                                    'Class': 'Condition',
                                                    'Method': (Func5, ()) },
                                                {
                                                    'ID': 81,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.MoveToLockEnemy, (10,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 84,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 85,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.heroagent.CAgent.ChooseEnemyAroundPos, (10, 15, 0)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 86,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.heroagent.CAgent.MoveToPos, (2,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] }] }] }] }] }
