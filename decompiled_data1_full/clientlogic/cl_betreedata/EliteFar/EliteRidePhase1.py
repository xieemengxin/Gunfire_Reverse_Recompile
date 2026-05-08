# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteFar/EliteRidePhase1.pyc
# RelativePath: clientlogic/cl_betreedata/EliteFar/EliteRidePhase1.pyc
# Source Generated with Decompyle++
# File: EliteRidePhase1.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 4


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.ChoosePF(1, oAgent) == 1


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 33812


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 20


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 20


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), 16, 20, 10, 30, oAgent)


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 12


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), 12, 15, 45, 75, oAgent)

data = {
    'Name': 'EliteRidePhase1',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 3,
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
                    'ID': 61,
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
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 6,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 7,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 16,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 8,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 9,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 10,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 11,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (0, 0)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 12,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (33812,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 13,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 14,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.AddState, (7117, 100)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 15,
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
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 19,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) },
                                        {
                                            'ID': 20,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 21,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) },
                                                {
                                                    'ID': 22,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 23,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 58,
                                                                'Class': 'Precondition',
                                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                'Phase': 1,
                                                                'Flag': 'precondition',
                                                                'BinaryOperator': 'And' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 24,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 25,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 29,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 27,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 26,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (18,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 59,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 60,
                                                                'Class': 'Precondition',
                                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                'Phase': 1,
                                                                'Flag': 'precondition',
                                                                'BinaryOperator': 'And' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 28,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] },
                                        {
                                            'ID': 30,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 31,
                                                    'Class': 'Condition',
                                                    'Method': (Func4, ()) },
                                                {
                                                    'ID': 32,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 33,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 34,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 35,
                                                            'Class': 'Action',
                                                            'Method': (Func5, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 36,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 37,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 57,
                                                                'Class': 'Precondition',
                                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                'Phase': 1,
                                                                'Flag': 'precondition',
                                                                'BinaryOperator': 'And' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 38,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 39,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 40,
                                                            'Class': 'Condition',
                                                            'Method': (Func6, ()) },
                                                        {
                                                            'ID': 41,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 42,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 45,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 0,
                                                                    'SuccessPolicy': 1,
                                                                    'ExitPolicy': 0,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 46,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 44,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHorizontalPos, (3, 5)),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 43,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 47,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] },
                                                                        {
                                                                            'ID': 48,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] },
                                                        {
                                                            'ID': 49,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 50,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 51,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 52,
                                                                    'Class': 'Action',
                                                                    'Method': (Func7, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 53,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 54,
                                                                    'Class': 'Action',
                                                                    'Attachment': ({
                                                                        'ID': 56,
                                                                        'Class': 'Precondition',
                                                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                        'Phase': 1,
                                                                        'Flag': 'precondition',
                                                                        'BinaryOperator': 'And' },),
                                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 55,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] }] }] }] }] }] }
