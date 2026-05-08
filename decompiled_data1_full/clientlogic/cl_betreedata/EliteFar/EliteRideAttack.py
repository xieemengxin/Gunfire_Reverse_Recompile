# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteFar/EliteRideAttack.pyc
# RelativePath: clientlogic/cl_betreedata/EliteFar/EliteRideAttack.pyc
# Source Generated with Decompyle++
# File: EliteRideAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 4


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 5


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= oAgent.GetData('CurPerformUseDis')


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 33814


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 21


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 21


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True

data = {
    'Name': 'EliteRideAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 37,
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
                    'ID': 3,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 137,
                            'Class': 'And',
                            'Node': [
                                {
                                    'ID': 5,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 138,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) }] },
                        {
                            'ID': 57,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 58,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 62,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 135,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 64,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 90,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 91,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 92,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) },
                                                {
                                                    'ID': 93,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 141,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 0,
                                            'SuccessPolicy': 1,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 99,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 102,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 98,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 100,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func3, ()) },
                                                                {
                                                                    'ID': 139,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func4, ()) }] },
                                                        {
                                                            'ID': 140,
                                                            'Class': 'DecoratorAlwaysRunning',
                                                            'DecorateWhenChildEnds': False,
                                                            'Node': [
                                                                {
                                                                    'ID': 136,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (5,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] },
                                                {
                                                    'ID': 142,
                                                    'Class': 'Condition',
                                                    'Method': (Func5, ()) }] }] }] }] },
                {
                    'ID': 129,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 134,
                            'Class': 'Condition',
                            'Method': (Func6, ()) },
                        {
                            'ID': 103,
                            'Class': 'Parallel',
                            'FailurePolicy': 0,
                            'SuccessPolicy': 1,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 145,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 104,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 105,
                                            'Class': 'DecoratorAlwaysRunning',
                                            'DecorateWhenChildEnds': False,
                                            'Node': [
                                                {
                                                    'ID': 106,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 107,
                                                            'Class': 'Condition',
                                                            'Method': (Func7, ()) },
                                                        {
                                                            'ID': 108,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 110,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 111,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 112,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (15,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 109,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 113,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 143,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 0,
                                                                    'SuccessPolicy': 1,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 114,
                                                                            'Class': 'Parallel',
                                                                            'FailurePolicy': 1,
                                                                            'SuccessPolicy': 0,
                                                                            'ExitPolicy': 1,
                                                                            'ChildFinishPolicy': 1,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 115,
                                                                                    'Class': 'DecoratorAlwaysRunning',
                                                                                    'DecorateWhenChildEnds': False,
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 117,
                                                                                            'Class': 'Sequence',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 120,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (14, 16, 0, 20)),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None },
                                                                                                {
                                                                                                    'ID': 121,
                                                                                                    'Class': 'Parallel',
                                                                                                    'FailurePolicy': 1,
                                                                                                    'SuccessPolicy': 0,
                                                                                                    'ExitPolicy': 1,
                                                                                                    'ChildFinishPolicy': 1,
                                                                                                    'Node': [
                                                                                                        {
                                                                                                            'ID': 122,
                                                                                                            'Class': 'Action',
                                                                                                            'Attachment': ({
                                                                                                                'ID': 123,
                                                                                                                'Class': 'Precondition',
                                                                                                                'Method': (cl_betree.monsteragent.CAgent.TryReChooseHateFlankPos, (3, 14, 16, 0, 20)),
                                                                                                                'Phase': 1,
                                                                                                                'Flag': 'precondition',
                                                                                                                'BinaryOperator': 'And' },),
                                                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                                            'ResultOption': 0,
                                                                                                            'ResultFunctor': None },
                                                                                                        {
                                                                                                            'ID': 124,
                                                                                                            'Class': 'Sequence',
                                                                                                            'Node': [
                                                                                                                {
                                                                                                                    'ID': 125,
                                                                                                                    'Class': 'And',
                                                                                                                    'Node': [
                                                                                                                        {
                                                                                                                            'ID': 127,
                                                                                                                            'Class': 'Condition',
                                                                                                                            'Method': (Func8, ()) },
                                                                                                                        {
                                                                                                                            'ID': 128,
                                                                                                                            'Class': 'Condition',
                                                                                                                            'Method': (Func9, ()) }] },
                                                                                                                {
                                                                                                                    'ID': 126,
                                                                                                                    'Class': 'Action',
                                                                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                                                    'ResultOption': 0,
                                                                                                                    'ResultFunctor': None }] }] }] }] },
                                                                                {
                                                                                    'ID': 116,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 118,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 119,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func10, ()) }] }] },
                                                                        {
                                                                            'ID': 144,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func11, ()) }] }] }] }] }] },
                                {
                                    'ID': 146,
                                    'Class': 'Condition',
                                    'Method': (Func12, ()) }] },
                        {
                            'ID': 130,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 131,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 133,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 132,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UpdateInAdvance, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
