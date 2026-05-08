# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteNear/EliteNearMoveAttack.pyc
# RelativePath: clientlogic/cl_betreedata/EliteNear/EliteNearMoveAttack.pyc
# Source Generated with Decompyle++
# File: EliteNearMoveAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 4


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 8


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckChooseMovingCastPF(oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 4


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True

data = {
    'Name': 'EliteNearMoveAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 163,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 55,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 56,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 107,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 108,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 109,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.LimitChoosePFDistance, (0, 12)),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' },),
                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 110,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 111,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (5,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 57,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 58,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 112,
                            'Class': 'Noop' },
                        {
                            'ID': 60,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 63,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 65,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 66,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 0,
                                            'SuccessPolicy': 1,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 64,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 68,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 69,
                                                            'Class': 'Action',
                                                            'Method': (Func2, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 71,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) }] },
                                        {
                                            'ID': 67,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 0,
                                            'SuccessPolicy': 1,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 83,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 86,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 113,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 114,
                                                                'Class': 'Precondition',
                                                                'Method': (cl_betree.monsteragent.CAgent.TryReChooseHateFlankPos, (3, 6, 10, 15, 45)),
                                                                'Phase': 1,
                                                                'Flag': 'precondition',
                                                                'BinaryOperator': 'And' },),
                                                            'Method': (Func4, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 73,
                                                    'Class': 'Condition',
                                                    'Method': (Func5, ()) }] }] }] }] },
                {
                    'ID': 90,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 91,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 92,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 93,
                            'Class': 'Condition',
                            'Method': (Func6, ()) },
                        {
                            'ID': 94,
                            'Class': 'Parallel',
                            'FailurePolicy': 0,
                            'SuccessPolicy': 1,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 96,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 0,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 98,
                                            'Class': 'DecoratorAlwaysRunning',
                                            'DecorateWhenChildEnds': False,
                                            'Node': [
                                                {
                                                    'ID': 100,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 102,
                                                            'Class': 'Condition',
                                                            'Method': (Func7, ()) },
                                                        {
                                                            'ID': 103,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 104,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 105,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 106,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (3,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] },
                                        {
                                            'ID': 99,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 101,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 97,
                                    'Class': 'Condition',
                                    'Method': (Func8, ()) }] },
                        {
                            'ID': 95,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
