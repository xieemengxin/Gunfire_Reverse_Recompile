# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterNear/nearMonkeyAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterNear/nearMonkeyAttack.pyc
# Source Generated with Decompyle++
# File: nearMonkeyAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 3


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 12


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 3


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 50, oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 10


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 20893


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 3


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetLastSucceededPF(oAgent) == 20891


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.GetLastSucceededPF(oAgent) == 20892


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 1.5


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 2

data = {
    'Name': 'nearMonkeyAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 142,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 146,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 78,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 82,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 101,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 102,
                                            'Class': 'Condition',
                                            'Method': (Func0, ()) },
                                        {
                                            'ID': 119,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 136,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 0,
                                            'SuccessPolicy': 1,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 147,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 141,
                                                            'Class': 'DecoratorAlwaysRunning',
                                                            'DecorateWhenChildEnds': False,
                                                            'Node': [
                                                                {
                                                                    'ID': 105,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (3,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 137,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 138,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func1, ()) },
                                                                {
                                                                    'ID': 140,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (7.8, 8.2, 10, 25)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 139,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 104,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 142,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func2, ()) },
                                                                {
                                                                    'ID': 107,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 109,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 144,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 1,
                                                            'ExitPolicy': 0,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 94,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func3, ()) },
                                                                {
                                                                    'ID': 90,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 145,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func4, ()) },
                                                                        {
                                                                            'ID': 89,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 96,
                                                                            'Class': 'IfElse',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 97,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func5, ()) },
                                                                                {
                                                                                    'ID': 99,
                                                                                    'Class': 'Noop' },
                                                                                {
                                                                                    'ID': 98,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] }] }] }] },
                                                {
                                                    'ID': 148,
                                                    'Class': 'Condition',
                                                    'Method': (Func6, ()) }] }] }] },
                        {
                            'ID': 77,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 79,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 114,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 131,
                                    'Class': 'Condition',
                                    'Method': (Func7, ()) },
                                {
                                    'ID': 120,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 116,
                                            'Class': 'Or',
                                            'Node': [
                                                {
                                                    'ID': 115,
                                                    'Class': 'Condition',
                                                    'Method': (Func8, ()) },
                                                {
                                                    'ID': 117,
                                                    'Class': 'Condition',
                                                    'Method': (Func9, ()) }] },
                                        {
                                            'ID': 124,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 129,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 121,
                                                            'Class': 'Condition',
                                                            'Method': (Func10, ()) },
                                                        {
                                                            'ID': 122,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (1, 1.5, 125, 180)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 132,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 133,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func11, ()) },
                                                                {
                                                                    'ID': 134,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (1, 1.2, 75, 130)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 135,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (1, 1.5, 70, 80)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] },
                                                {
                                                    'ID': 125,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 126,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (20897,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 127,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 123,
                                            'Class': 'Noop' }] },
                                {
                                    'ID': 128,
                                    'Class': 'Noop' }] },
                        {
                            'ID': 100,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.UpdateInAdvance, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
