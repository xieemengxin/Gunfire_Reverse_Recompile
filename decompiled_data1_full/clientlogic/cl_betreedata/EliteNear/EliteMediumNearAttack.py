# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteNear/EliteMediumNearAttack.pyc
# RelativePath: clientlogic/cl_betreedata/EliteNear/EliteMediumNearAttack.pyc
# Source Generated with Decompyle++
# File: EliteMediumNearAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 4


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 75, oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) != 31263


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.IsLockEnemyPosRangeAccessible(1.5, oAgent) == False


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'EliteMediumNearAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 54,
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
                    'ID': 66,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 4,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 5,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 7,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 8,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 9,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 6,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 10,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 12,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 17,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 18,
                                                    'Class': 'Condition',
                                                    'Method': (Func1, ()) },
                                                {
                                                    'ID': 19,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) }] },
                                        {
                                            'ID': 67,
                                            'Class': 'DecoratorAlwaysRunning',
                                            'DecorateWhenChildEnds': False,
                                            'Node': [
                                                {
                                                    'ID': 68,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 69,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 70,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (2,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] },
                                {
                                    'ID': 11,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 14,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) },
                                        {
                                            'ID': 15,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 22,
                                                    'Class': 'Action',
                                                    'Attachment': ({
                                                        'ID': 23,
                                                        'Class': 'Precondition',
                                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                        'Phase': 1,
                                                        'Flag': 'precondition',
                                                        'BinaryOperator': 'And' },),
                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 24,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 71,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 72,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 90,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 73,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 77,
                                                            'Class': 'Action',
                                                            'Method': (Func4, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 79,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 84,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func5, ()) },
                                                                {
                                                                    'ID': 85,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func6, ()) },
                                                                {
                                                                    'ID': 86,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (31263,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 92,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 91,
                                                                    'Class': 'WaitFrame',
                                                                    'Frames': 250 },
                                                                {
                                                                    'ID': 94,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func7, ()) },
                                                                {
                                                                    'ID': 93,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (31262,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] },
                                                {
                                                    'ID': 74,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 75,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] }] }] }] }
