# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossTornado/bossTornadoNearAttack.pyc
# RelativePath: clientlogic/cl_betreedata/BossTornado/bossTornadoNearAttack.pyc
# Source Generated with Decompyle++
# File: bossTornadoNearAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.IsLockEnemyPosRangeAccessible(1.5, oAgent) == False

data = {
    'Name': 'bossTornadoNearAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 4,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 8,
                            'Class': 'Action',
                            'Method': (Func0, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 9,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 11,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 12,
                                    'Class': 'Condition',
                                    'Method': (Func2, ()) },
                                {
                                    'ID': 13,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39155,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 10,
                            'Class': 'WaitFrame',
                            'Frames': 250 }] },
                {
                    'ID': 14,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 15,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 7,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
