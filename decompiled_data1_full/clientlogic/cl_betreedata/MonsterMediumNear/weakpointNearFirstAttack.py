# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumNear/weakpointNearFirstAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumNear/weakpointNearFirstAttack.pyc
# Source Generated with Decompyle++
# File: weakpointNearFirstAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 12


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) < 17


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 8


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) < 12


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.ChoosePF(1, oAgent) == 1


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 8


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.ChoosePF(1, oAgent) == 1

data = {
    'Name': 'weakpointNearFirstAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 91,
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
                    'ID': 30,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
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
                                    'ID': 49,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 0,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 50,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 52,
                                                    'Class': 'Condition',
                                                    'Method': (Func0, ()) },
                                                {
                                                    'ID': 53,
                                                    'Class': 'Condition',
                                                    'Method': (Func1, ()) },
                                                {
                                                    'ID': 54,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) },
                                                {
                                                    'ID': 56,
                                                    'Class': 'SelectorProbability',
                                                    'RandomGenerator': None,
                                                    'Node': [
                                                        {
                                                            'ID': 58,
                                                            'Class': 'DecoratorWeight',
                                                            'DecorateWhenChildEnds': False,
                                                            'Weight': 30,
                                                            'Node': [
                                                                {
                                                                    'ID': 60,
                                                                    'Class': 'DecoratorAlwaysFailure',
                                                                    'DecorateWhenChildEnds': False }] },
                                                        {
                                                            'ID': 59,
                                                            'Class': 'DecoratorWeight',
                                                            'DecorateWhenChildEnds': False,
                                                            'Weight': 70,
                                                            'Node': [
                                                                {
                                                                    'ID': 61,
                                                                    'Class': 'DecoratorAlwaysSuccess',
                                                                    'DecorateWhenChildEnds': False }] }] }] },
                                        {
                                            'ID': 64,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 65,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) },
                                                {
                                                    'ID': 66,
                                                    'Class': 'Condition',
                                                    'Method': (Func4, ()) },
                                                {
                                                    'ID': 67,
                                                    'Class': 'Condition',
                                                    'Method': (Func5, ()) },
                                                {
                                                    'ID': 68,
                                                    'Class': 'SelectorProbability',
                                                    'RandomGenerator': None,
                                                    'Node': [
                                                        {
                                                            'ID': 69,
                                                            'Class': 'DecoratorWeight',
                                                            'DecorateWhenChildEnds': False,
                                                            'Weight': 35,
                                                            'Node': [
                                                                {
                                                                    'ID': 71,
                                                                    'Class': 'DecoratorAlwaysFailure',
                                                                    'DecorateWhenChildEnds': False }] },
                                                        {
                                                            'ID': 70,
                                                            'Class': 'DecoratorWeight',
                                                            'DecorateWhenChildEnds': False,
                                                            'Weight': 65,
                                                            'Node': [
                                                                {
                                                                    'ID': 72,
                                                                    'Class': 'DecoratorAlwaysSuccess',
                                                                    'DecorateWhenChildEnds': False }] }] }] }] },
                                {
                                    'ID': 62,
                                    'Class': 'Condition',
                                    'Method': (Func6, ()) },
                                {
                                    'ID': 48,
                                    'Class': 'WaitFrame',
                                    'Frames': 15 }] },
                        {
                            'ID': 33,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 1,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 34,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 35,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (4.5,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 73,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 74,
                                    'Class': 'WaitFrame',
                                    'Frames': 25 },
                                {
                                    'ID': 80,
                                    'Class': 'DecoratorLoopUntil',
                                    'DecorateWhenChildEnds': False,
                                    'Count': -1,
                                    'Until': True,
                                    'Node': [
                                        {
                                            'ID': 81,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 83,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (0,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 75,
                                                    'Class': 'Condition',
                                                    'Method': (Func7, ()) },
                                                {
                                                    'ID': 79,
                                                    'Class': 'Condition',
                                                    'Method': (Func8, ()) },
                                                {
                                                    'ID': 76,
                                                    'Class': 'Condition',
                                                    'Method': (Func9, ()) },
                                                {
                                                    'ID': 82,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 5 }] }] }] }] },
                {
                    'ID': 25,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 14,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 32,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 15,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 36,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UpdateInAdvance, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
