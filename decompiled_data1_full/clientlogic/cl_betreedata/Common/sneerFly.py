# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Common/sneerFly.pyc
# RelativePath: clientlogic/cl_betreedata/Common/sneerFly.pyc
# Source Generated with Decompyle++
# File: sneerFly.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToFlyLockEnemy(oAgent.GetData('CurPerformUseDis'), 2, 4, oAgent)


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'sneerFly',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 4,
    'Node': [
        {
            'ID': 16,
            'Class': 'IfElse',
            'Node': [
                {
                    'ID': 17,
                    'Class': 'Condition',
                    'Method': (Func0, ()) },
                {
                    'ID': 1,
                    'Class': 'Sequence',
                    'Attachment': ({
                        'ID': 2,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Node': [
                        {
                            'ID': 3,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.StandUp, (24,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 5,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseAttack, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 6,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 7,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 8,
                            'Class': 'Action',
                            'Method': (Func1, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 9,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 13,
                                    'Class': 'Condition',
                                    'Method': (Func2, ()) },
                                {
                                    'ID': 14,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 15,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToFlyLockEnemy, (5, 2, 4)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 10,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 11,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' },),
                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 12,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 18,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.RemoveState, (20039,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
