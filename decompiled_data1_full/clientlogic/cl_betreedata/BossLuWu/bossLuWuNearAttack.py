# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossLuWu/bossLuWuNearAttack.pyc
# RelativePath: clientlogic/cl_betreedata/BossLuWu/bossLuWuNearAttack.pyc
# Source Generated with Decompyle++
# File: bossLuWuNearAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.IsLockEnemyPosRangeAccessible(1.5, oAgent) == False

data = {
    'Name': 'bossLuWuNearAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 161,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 189,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 203,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 204,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 206,
                            'Class': 'Noop' },
                        {
                            'ID': 194,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 205,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 188,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 195,
                                            'Class': 'Action',
                                            'Method': (Func1, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 196,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 198,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) },
                                        {
                                            'ID': 199,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) },
                                        {
                                            'ID': 200,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39011,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 202,
                                    'Class': 'WaitFrame',
                                    'Frames': 250 }] }] },
                {
                    'ID': 193,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 201,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 124,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
