# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Servant/ServantAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Servant/ServantAttack.pyc
# Source Generated with Decompyle++
# File: ServantAttack.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.IsPerformUseArea(False, oAgent) == True


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.GetChoosePF(oAgent) == 7150


def Func2(oAgent):
    return cl_betree.servantagent.CAgent.GetChoosePF(oAgent) == 7143


def Func3(oAgent):
    return cl_betree.servantagent.CAgent.GetLockEnemyHeightDis(oAgent) <= 3.5


def Func4(oAgent):
    return cl_betree.servantagent.CAgent.IsLockEnemyPosAccessible(oAgent) == False


def Func5(oAgent):
    return cl_betree.servantagent.CAgent.GetLockEnemyDis(oAgent) < 20


def Func6(oAgent):
    return cl_betree.servantagent.CAgent.GetLockEnemyHeightDis(oAgent) > 1.5

data = {
    'Name': 'ServantAttack',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 84,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
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
                                    'ID': 94,
                                    'Class': 'Or',
                                    'Node': [
                                        {
                                            'ID': 98,
                                            'Class': 'Or',
                                            'Node': [
                                                {
                                                    'ID': 97,
                                                    'Class': 'Condition',
                                                    'Method': (Func1, ()) },
                                                {
                                                    'ID': 95,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) }] },
                                        {
                                            'ID': 93,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) }] }] },
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
                                            'Method': (Func4, ()) },
                                        {
                                            'ID': 81,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 84,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 61,
                                                            'Class': 'Condition',
                                                            'Method': (Func5, ()) },
                                                        {
                                                            'ID': 85,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 63,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.servantagent.CAgent.ChooseEnemyAroundPos, (3, 5, 0)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 86,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (0,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] },
                                                {
                                                    'ID': 82,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 83,
                                                            'Class': 'Condition',
                                                            'Method': (Func6, ()) },
                                                        {
                                                            'ID': 87,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.servantagent.CAgent.ChooseTargetAwayPos, (20, 180, 10)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 48,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.servantagent.CAgent.ChooseRangedPos, (10, 3, 5, 0, 45)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 67,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (0,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 89,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.MoveToLockEnemy, (2,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 90,
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
                    'ID': 39,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.UpdateInAdvance, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
