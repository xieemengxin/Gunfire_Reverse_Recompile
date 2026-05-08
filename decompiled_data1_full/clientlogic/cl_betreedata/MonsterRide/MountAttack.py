# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterRide/MountAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterRide/MountAttack.pyc
# Source Generated with Decompyle++
# File: MountAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseCrazyTarget(15, 50, 16, oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseCrazyTarget(15, 500, 16, oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 150, oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) > 5


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 5


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToSlopeLockEnemy(oAgent.GetData('CurPerformUseDis'), 20, oAgent)


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 200, oAgent) == True


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= oAgent.GetData('CurPerformUseDis')


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'MountAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 76,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 85,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 21,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 62,
                            'Class': 'SelectorProbability',
                            'RandomGenerator': None,
                            'Node': [
                                {
                                    'ID': 63,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 75,
                                    'Node': [
                                        {
                                            'ID': 22,
                                            'Class': 'Condition',
                                            'Method': (Func0, ()) }] },
                                {
                                    'ID': 65,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 25,
                                    'Node': [
                                        {
                                            'ID': 67,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) }] }] },
                        {
                            'ID': 45,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 59,
                                    'Class': 'SelectorProbability',
                                    'RandomGenerator': None,
                                    'Node': [
                                        {
                                            'ID': 60,
                                            'Class': 'DecoratorWeight',
                                            'DecorateWhenChildEnds': False,
                                            'Weight': 50,
                                            'Node': [
                                                {
                                                    'ID': 46,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (23814,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 61,
                                            'Class': 'DecoratorWeight',
                                            'DecorateWhenChildEnds': False,
                                            'Weight': 50,
                                            'Node': [
                                                {
                                                    'ID': 56,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (23819,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 71,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 72,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 74,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 80,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 86,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (5,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 75,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) }] },
                                        {
                                            'ID': 73,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 76,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) },
                                                {
                                                    'ID': 77,
                                                    'Class': 'Noop' },
                                                {
                                                    'ID': 78,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 82,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 83,
                                                                'Class': 'Precondition',
                                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                'Phase': 1,
                                                                'Flag': 'precondition',
                                                                'BinaryOperator': 'And' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 84,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] }] },
                        {
                            'ID': 24,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 34,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 27,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 28,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 35,
                                            'Class': 'Condition',
                                            'Method': (Func4, ()) },
                                        {
                                            'ID': 101,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 102,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 29,
                                                    'Class': 'Action',
                                                    'Attachment': ({
                                                        'ID': 30,
                                                        'Class': 'Precondition',
                                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                        'Phase': 1,
                                                        'Flag': 'precondition',
                                                        'BinaryOperator': 'And' },),
                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 49,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 87,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 88,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 90,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 95,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 103,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 39,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 1,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 42,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func5, ()) },
                                                                        {
                                                                            'ID': 53,
                                                                            'Class': 'Action',
                                                                            'Method': (Func6, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] },
                                                        {
                                                            'ID': 91,
                                                            'Class': 'Condition',
                                                            'Method': (Func7, ()) }] },
                                                {
                                                    'ID': 89,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 105,
                                                            'Class': 'And',
                                                            'Node': [
                                                                {
                                                                    'ID': 92,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func8, ()) },
                                                                {
                                                                    'ID': 106,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func9, ()) }] },
                                                        {
                                                            'ID': 94,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 97,
                                                                    'Class': 'Action',
                                                                    'Attachment': ({
                                                                        'ID': 98,
                                                                        'Class': 'Precondition',
                                                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                        'Phase': 1,
                                                                        'Flag': 'precondition',
                                                                        'BinaryOperator': 'And' },),
                                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 99,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 93,
                                                            'Class': 'Noop' }] }] }] }] }] },
                {
                    'ID': 54,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UpdateInAdvance, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
