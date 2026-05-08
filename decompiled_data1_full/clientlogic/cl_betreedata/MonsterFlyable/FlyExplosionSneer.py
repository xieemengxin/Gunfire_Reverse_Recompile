# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFlyable/FlyExplosionSneer.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFlyable/FlyExplosionSneer.pyc
# Source Generated with Decompyle++
# File: FlyExplosionSneer.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckArriveShowPos(oAgent) == False


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToFlyLockEnemy(oAgent.GetData('CurPerformUseDis'), 2, 4, oAgent)


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'FlyExplosionSneer',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 9,
    'Node': [
        {
            'ID': 10,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 11,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 12,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 13,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 14,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseShowPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 15,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 16,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 22,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FlyToPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 21,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.AddState, (8094, 0)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 24,
                            'Class': 'Noop' }] },
                {
                    'ID': 25,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 26,
                            'Class': 'Condition',
                            'Method': (Func1, ()) },
                        {
                            'ID': 27,
                            'Class': 'Sequence',
                            'Attachment': ({
                                'ID': 28,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' },),
                            'Node': [
                                {
                                    'ID': 29,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.StandUp, (24,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 30,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseAttack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 31,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 32,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 33,
                                    'Class': 'Action',
                                    'Method': (Func2, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 34,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 1,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 35,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) },
                                        {
                                            'ID': 37,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToFlyLockEnemy, (5, 2, 4)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 38,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 39,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 40,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.RemoveState, (20039,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
