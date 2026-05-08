# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteNear/EliteMediumAttack.pyc
# RelativePath: clientlogic/cl_betreedata/EliteNear/EliteMediumAttack.pyc
# Source Generated with Decompyle++
# File: EliteMediumAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.IsLockEnemyPosRangeAccessible(3, oAgent) == False


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) != 31263

data = {
    'Name': 'EliteMediumAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 73,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 66,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 90,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 73,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 77,
                            'Class': 'Action',
                            'Method': (Func0, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 79,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 84,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 85,
                                    'Class': 'Condition',
                                    'Method': (Func2, ()) },
                                {
                                    'ID': 86,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (31264,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 92,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 91,
                                    'Class': 'WaitFrame',
                                    'Frames': 150 },
                                {
                                    'ID': 94,
                                    'Class': 'Condition',
                                    'Method': (Func3, ()) },
                                {
                                    'ID': 93,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (31262,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 11,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 14,
                            'Class': 'Condition',
                            'Method': (Func4, ()) },
                        {
                            'ID': 95,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 97,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' },),
                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 96,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 24,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
