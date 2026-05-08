# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumNear/mediumNearAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumNear/mediumNearAttack.pyc
# Source Generated with Decompyle++
# File: mediumNearAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True

data = {
    'Name': 'mediumNearAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 40,
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
                    'ID': 33,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
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
                                            'ID': 25,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 10,
                                            'Class': 'Condition',
                                            'Method': (Func0, ()) },
                                        {
                                            'ID': 31,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) }] },
                                {
                                    'ID': 23,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 27,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 3,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 24,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (2,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] },
                        {
                            'ID': 34,
                            'Class': 'Condition',
                            'Method': (Func2, ()) }] },
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
                    'ResultFunctor': None }] }] }
