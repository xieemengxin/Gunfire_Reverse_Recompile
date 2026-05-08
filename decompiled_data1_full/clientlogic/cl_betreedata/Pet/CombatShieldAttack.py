# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Pet/CombatShieldAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Pet/CombatShieldAttack.pyc
# Source Generated with Decompyle++
# File: CombatShieldAttack.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.IsPerformUseArea(True, oAgent) == True


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.GetLockEnemyHeightDis(oAgent) <= 3.5


def Func2(oAgent):
    return cl_betree.servantagent.CAgent.IsLockEnemyPosAccessible(oAgent) == False


def Func3(oAgent):
    return cl_betree.servantagent.CAgent.GetLockEnemyDis(oAgent) <= 20

data = {
    'Name': 'CombatShieldAttack',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 98,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 113,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.SetActionSM, (2,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 114,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.SetFightStatus, (2,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 28,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.ChooseHateTarget, (1, 0)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 45,
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
                                    'ID': 99,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ChooseHateTarget, (1, 0)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 46,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ChoosePF, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 96,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 100,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) }] },
                        {
                            'ID': 73,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 12,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 71,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 72,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) },
                                        {
                                            'ID': 101,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 0,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 103,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) },
                                                {
                                                    'ID': 115,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.MoveToLockEnemy, (10,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 112,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.MoveToLockEnemy, (2,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 111,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ChoosePF, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 7,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 40,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.servantagent.CAgent.Attack, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 107,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.UpdateInAdvance, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
