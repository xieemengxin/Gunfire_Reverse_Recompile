# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Pet/CombatAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Pet/CombatAttack.pyc
# Source Generated with Decompyle++
# File: CombatAttack.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.IsPerformUseArea(True, oAgent) == True


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.GetLockEnemyHeightDis(oAgent) <= 3.5


def Func2(oAgent):
    return cl_betree.servantagent.CAgent.IsLockEnemyPosAccessible(oAgent) == False


def Func3(oAgent):
    return cl_betree.servantagent.CAgent.GetLockEnemyHeightDis(oAgent) < 3


def Func4(oAgent):
    return cl_betree.servantagent.CAgent.ChooseLockTargetNearestSpace(True, oAgent) == 1


def Func5(oAgent):
    return cl_betree.servantagent.CAgent.IsPerformUseArea(True, oAgent) == True


def Func6(oAgent):
    return cl_betree.servantagent.CAgent.IsLockEnemyPosAccessible(oAgent) == True


def Func7(oAgent):
    return cl_betree.servantagent.CAgent.IsPerformUseArea(True, oAgent) == True

data = {
    'Name': 'CombatAttack',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 134,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 113,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.SetActionSM, (3,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 114,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.SetFightStatus, (2,)),
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
                                    'Method': (cl_betree.servantagent.CAgent.ChooseHateTarget, (3, 0)),
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
                                            'ID': 115,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 116,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) },
                                                {
                                                    'ID': 128,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 129,
                                                            'Class': 'Condition',
                                                            'Method': (Func4, ()) },
                                                        {
                                                            'ID': 150,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 0,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 151,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (1,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 152,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 153,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.servantagent.CAgent.ChoosePF, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 154,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func5, ()) }] }] },
                                                        {
                                                            'ID': 131,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.servantagent.CAgent.MoveToLockEnemy, (15,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 155,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 1,
                                                    'ExitPolicy': 0,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 156,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 157,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.servantagent.CAgent.ChooseOwnerAroundPos, (3, 10, 0, 60)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 158,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 159,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (1,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 160,
                                                                    'Class': 'WaitFrame',
                                                                    'Frames': 50 }] },
                                                        {
                                                            'ID': 161,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 162,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.servantagent.CAgent.ChooseHateTarget, (3, 0)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 163,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func6, ()) }] }] }] },
                                        {
                                            'ID': 149,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.MoveToLockEnemy, (2,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 111,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ChoosePF, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 136,
                                    'Class': 'Condition',
                                    'Method': (Func7, ()) }] }] },
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
