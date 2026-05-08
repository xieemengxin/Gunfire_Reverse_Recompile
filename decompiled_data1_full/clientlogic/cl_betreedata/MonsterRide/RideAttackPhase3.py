# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterRide/RideAttackPhase3.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterRide/RideAttackPhase3.pyc
# Source Generated with Decompyle++
# File: RideAttackPhase3.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.ChoosePF(1, oAgent) == 1


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), 4, 6, 60, 120, oAgent)


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.ChoosePF(1, oAgent) == 1


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 30


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), 2, 3, 150, 180, oAgent)


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), 2, 3, 0, 45, oAgent)

data = {
    'Name': 'RideAttackPhase3',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 6,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 31,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 32,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 65,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 66,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 67,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 33,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 34,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 69,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 36,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 37,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 38,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) },
                                                {
                                                    'ID': 39,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 52,
                                                            'Class': 'Action',
                                                            'Method': (Func3, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 46,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 53,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 42,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 54,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 0,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 62,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 63,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 64,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] },
                                                                {
                                                                    'ID': 56,
                                                                    'Class': 'DecoratorAlwaysRunning',
                                                                    'DecorateWhenChildEnds': False,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 57,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 58,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 59,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.KeepMoving, (4,)),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] }] }] }] },
                                                {
                                                    'ID': 47,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 0,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 60,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 61,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 40,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 48,
                                                            'Class': 'DecoratorAlwaysRunning',
                                                            'DecorateWhenChildEnds': False,
                                                            'Node': [
                                                                {
                                                                    'ID': 49,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 50,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 51,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.KeepMoving, (4,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] }] }] },
                                        {
                                            'ID': 70,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 71,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (6, 8, 15, 30)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 72,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 73,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 74,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 76,
                                                    'Class': 'Condition',
                                                    'Method': (Func4, ()) },
                                                {
                                                    'ID': 77,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 0,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 78,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 80,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 81,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 79,
                                                            'Class': 'DecoratorAlwaysRunning',
                                                            'DecorateWhenChildEnds': False,
                                                            'Node': [
                                                                {
                                                                    'ID': 82,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 83,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 84,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.KeepMoving, (4,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] }] }] }] }] },
                        {
                            'ID': 95,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 86,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 87,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 91,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 0,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 92,
                                            'Class': 'Condition',
                                            'Method': (Func5, ()) },
                                        {
                                            'ID': 93,
                                            'Class': 'DecoratorAlwaysRunning',
                                            'DecorateWhenChildEnds': False,
                                            'Node': [
                                                {
                                                    'ID': 68,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 96,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 97,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func6, ()) },
                                                                {
                                                                    'ID': 85,
                                                                    'Class': 'Action',
                                                                    'Method': (Func7, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 98,
                                                                    'Class': 'Action',
                                                                    'Method': (Func8, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 89,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] }] }] },
                {
                    'ID': 94,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
