# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteNear/EliteNearHide.pyc
# RelativePath: clientlogic/cl_betreedata/EliteNear/EliteNearHide.pyc
# Source Generated with Decompyle++
# File: EliteNearHide.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 4


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 200, oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 15


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == False


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangeHidePosAndAttPos(1, 10, oAgent) == 1


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 10

data = {
    'Name': 'EliteNearHide',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 68,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 55,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 56,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 86,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 144,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 146,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 147,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 148,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 124,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 87,
                                    'Class': 'Condition',
                                    'Method': (Func2, ()) },
                                {
                                    'ID': 89,
                                    'Class': 'Condition',
                                    'Method': (Func3, ()) },
                                {
                                    'ID': 100,
                                    'Class': 'Condition',
                                    'Method': (Func4, ()) },
                                {
                                    'ID': 125,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 90,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 83,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 1,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 84,
                                            'Class': 'Condition',
                                            'Method': (Func5, ()) },
                                        {
                                            'ID': 153,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 154,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseTargetAwayPos, (15, 90, 10, 0.5)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 155,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 156,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 157,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 158,
                                                                    'Class': 'And',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 160,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func6, ()) },
                                                                        {
                                                                            'ID': 161,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func7, ()) }] },
                                                                {
                                                                    'ID': 159,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] },
                                                {
                                                    'ID': 162,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 163,
                                                            'Class': 'Condition',
                                                            'Method': (Func8, ()) },
                                                        {
                                                            'ID': 164,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 165,
                                                            'Class': 'Noop' }] }] }] },
                                {
                                    'ID': 94,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 95,
                                            'Class': 'Condition',
                                            'Method': (Func9, ()) },
                                        {
                                            'ID': 126,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 91,
                                                    'Class': 'WaitFrame',
                                                    'Frames': (cl_betree.monsteragent.CAgent.GetRandom, (75, 125)) },
                                                {
                                                    'ID': 135,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 136,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 137,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 138,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.KeepMoving, (3,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] },
                                {
                                    'ID': 92,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 93,
                                            'Class': 'Condition',
                                            'Method': (Func10, ()) },
                                        {
                                            'ID': 96,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 97,
                                                    'Class': 'Condition',
                                                    'Method': (Func11, ()) },
                                                {
                                                    'ID': 123,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 101,
                                                    'Class': 'Noop' }] },
                                        {
                                            'ID': 102,
                                            'Class': 'Noop' }] }] }] },
                {
                    'ID': 149,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UpdateInAdvance, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
