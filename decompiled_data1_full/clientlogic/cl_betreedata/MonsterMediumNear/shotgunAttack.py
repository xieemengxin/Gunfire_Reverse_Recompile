# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumNear/shotgunAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumNear/shotgunAttack.pyc
# Source Generated with Decompyle++
# File: shotgunAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 50, oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 15


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True

data = {
    'Name': 'shotgunAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 147,
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
                    'ID': 59,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 63,
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
                                    'ID': 34,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 36,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 43,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                                'Phase': 1,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 61,
                                            'Class': 'Condition',
                                            'Method': (Func0, ()) },
                                        {
                                            'ID': 62,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 37,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) },
                                        {
                                            'ID': 38,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) }] },
                                {
                                    'ID': 60,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 55,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 56,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 58,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (5,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] },
                        {
                            'ID': 64,
                            'Class': 'Condition',
                            'Method': (Func4, ()) }] },
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
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 33,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
