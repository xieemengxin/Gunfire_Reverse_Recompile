# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Hero/HeroNearAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Hero/HeroNearAttack.pyc
# Source Generated with Decompyle++
# File: HeroNearAttack.pyc (Python 3.6)

import cl_betree.heroagent

def Func0(oAgent):
    return cl_betree.heroagent.CAgent.CanUseCareerPF(oAgent) == True


def Func1(oAgent):
    return cl_betree.heroagent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.heroagent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.heroagent.CAgent.CanUseThrowPF(oAgent) == True


def Func4(oAgent):
    return cl_betree.heroagent.CAgent.GetLockEnemyDis(oAgent) <= 7


def Func5(oAgent):
    return cl_betree.heroagent.CAgent.GetLockEnemyDis(oAgent) >= 12

data = {
    'Name': 'HeroNearAttack',
    'ID': 0,
    'AgentType': 'cl_betree.heroagent',
    'IsFSM': False,
    'Ver': 110,
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
                            'ID': 90,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 99,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 102,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 100,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.MoveToLockEnemy, (8,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 110,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 93,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 111,
                                            'Class': 'Noop' },
                                        {
                                            'ID': 112,
                                            'Class': 'DecoratorAlwaysFailure',
                                            'DecorateWhenChildEnds': False,
                                            'Node': [
                                                {
                                                    'ID': 113,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.CancelLockTarget, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 107,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.FaceTarget, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 94,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 101,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.heroagent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.heroagent.CAgent.UseCareerPF, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 87,
                            'Class': 'Parallel',
                            'FailurePolicy': 0,
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
                                            'ID': 114,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 106,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) },
                                                {
                                                    'ID': 115,
                                                    'Class': 'Noop' },
                                                {
                                                    'ID': 116,
                                                    'Class': 'DecoratorAlwaysFailure',
                                                    'DecorateWhenChildEnds': False,
                                                    'Node': [
                                                        {
                                                            'ID': 117,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.heroagent.CAgent.CancelLockTarget, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] },
                                        {
                                            'ID': 119,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 120,
                                                    'Class': 'And',
                                                    'Node': [
                                                        {
                                                            'ID': 121,
                                                            'Class': 'Condition',
                                                            'Method': (Func3, ()) },
                                                        {
                                                            'ID': 122,
                                                            'Class': 'Condition',
                                                            'Method': (Func4, ()) }] },
                                                {
                                                    'ID': 123,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.UseThrowPF, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 124,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.Attack, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 118,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.CancelLockTarget, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 109,
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
