# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumNear/shotgunGuerrillaAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumNear/shotgunGuerrillaAttack.pyc
# Source Generated with Decompyle++
# File: shotgunGuerrillaAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, oAgent.GetConfig('IntervalTime'), oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 15


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 15


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetConfig('RangedPosR'), oAgent)


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True

data = {
    'Name': 'shotgunGuerrillaAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 148,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (50, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 70,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 6,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 63,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 64,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 65,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                                'Phase': 1,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 66,
                                            'Class': 'Condition',
                                            'Method': (Func0, ()) },
                                        {
                                            'ID': 67,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 68,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) },
                                        {
                                            'ID': 69,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) }] },
                                {
                                    'ID': 35,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 44,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 45,
                                                    'Class': 'Condition',
                                                    'Method': (Func4, ()) },
                                                {
                                                    'ID': 58,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 59,
                                                            'Class': 'Action',
                                                            'Method': (Func5, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 62,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 60,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 61,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 50,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 55,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 56,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 57,
                                                            'Class': 'Action',
                                                            'Method': (Func6, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] }] },
                        {
                            'ID': 71,
                            'Class': 'Condition',
                            'Method': (Func7, ()) }] },
                {
                    'ID': 9,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 32,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (50, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 33,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
