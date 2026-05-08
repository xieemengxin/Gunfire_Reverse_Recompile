# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumNear/dashMoveChoosePF.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumNear/dashMoveChoosePF.pyc
# Source Generated with Decompyle++
# File: dashMoveChoosePF.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, oAgent.GetConfig('IntervalTime'), oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 20


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 12


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 8


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), 1, 2, 85, 95, oAgent)


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True

data = {
    'Name': 'dashMoveChoosePF',
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
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 43,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 90,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 22,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 26,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 25,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 99,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.LimitChoosePFDistance, (0, 20)),
                                                'Phase': 1,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 40,
                                            'Class': 'Condition',
                                            'Method': (Func0, ()) },
                                        {
                                            'ID': 10,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) }] },
                                {
                                    'ID': 23,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 61,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 68,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) },
                                                {
                                                    'ID': 74,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 75,
                                                            'Class': 'Condition',
                                                            'Method': (Func3, ()) },
                                                        {
                                                            'ID': 92,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 94,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func4, ()) },
                                                                {
                                                                    'ID': 132,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 133,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 134,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 135,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (5,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] },
                                                                {
                                                                    'ID': 95,
                                                                    'Class': 'SelectorProbability',
                                                                    'RandomGenerator': None,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 96,
                                                                            'Class': 'DecoratorWeight',
                                                                            'DecorateWhenChildEnds': False,
                                                                            'Weight': 50,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 62,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 63,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (13, 1, 2, 85, 95)),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 64,
                                                                                            'Class': 'Sequence',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 65,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None },
                                                                                                {
                                                                                                    'ID': 66,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None },
                                                                                                {
                                                                                                    'ID': 67,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None }] }] }] },
                                                                        {
                                                                            'ID': 97,
                                                                            'Class': 'DecoratorWeight',
                                                                            'DecorateWhenChildEnds': False,
                                                                            'Weight': 50,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 131,
                                                                                    'Class': 'Noop' }] }] }] },
                                                        {
                                                            'ID': 125,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 126,
                                                                    'Class': 'Action',
                                                                    'Method': (Func5, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 127,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 128,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 129,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 130,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] }] },
                                                {
                                                    'ID': 76,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 77,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 78,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 79,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (15,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] }] },
                        {
                            'ID': 91,
                            'Class': 'Condition',
                            'Method': (Func6, ()) }] }] }] }
