# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Pet/CombatMoveAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Pet/CombatMoveAttack.pyc
# Source Generated with Decompyle++
# File: CombatMoveAttack.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.ChooseHateTarget(3, 0, oAgent) == 1


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.IsPerformUseArea(True, oAgent) == True


def Func2(oAgent):
    return cl_betree.servantagent.CAgent.GetLockEnemyHeightDis(oAgent) <= 3.5


def Func3(oAgent):
    return cl_betree.servantagent.CAgent.IsLockEnemyPosAccessible(oAgent) == False


def Func4(oAgent):
    return cl_betree.servantagent.CAgent.GetLockEnemyHeightDis(oAgent) < 3


def Func5(oAgent):
    return cl_betree.servantagent.CAgent.ChooseLockTargetNearestSpace(True, oAgent) == 1


def Func6(oAgent):
    return cl_betree.servantagent.CAgent.IsPerformUseArea(True, oAgent) == True


def Func7(oAgent):
    return cl_betree.servantagent.CAgent.GetChoosePF(oAgent) == oAgent.GetData('MoveUsePerform')


def Func8(oAgent):
    return cl_betree.servantagent.CAgent.CheckLockAlive(oAgent) == True

data = {
    'Name': 'CombatMoveAttack',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 165,
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
                    'ID': 119,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 120,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 121,
                            'Class': 'Noop' },
                        {
                            'ID': 122,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 0,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 123,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ChooseHateTarget, (3, 0)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 124,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 125,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.ChooseOwnerAroundPos, (3, 10, 0, 60)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 126,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 127,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.MoveToPos, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] }] },
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
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 100,
                                    'Class': 'Condition',
                                    'Method': (Func2, ()) }] },
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
                                            'Method': (Func3, ()) },
                                        {
                                            'ID': 115,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 116,
                                                    'Class': 'Condition',
                                                    'Method': (Func4, ()) },
                                                {
                                                    'ID': 128,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 129,
                                                            'Class': 'Condition',
                                                            'Method': (Func5, ()) },
                                                        {
                                                            'ID': 130,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.servantagent.CAgent.MoveToPos, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 131,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.servantagent.CAgent.MoveToLockEnemy, (15,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 132,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 133,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.servantagent.CAgent.ChooseOwnerAroundPos, (3, 10, 0, 60)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 134,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 135,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.servantagent.CAgent.MoveToPos, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] },
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
                                    'Method': (Func6, ()) }] }] },
                {
                    'ID': 7,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 179,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.StopMoving, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 164,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 165,
                            'Class': 'Condition',
                            'Method': (Func7, ()) },
                        {
                            'ID': 169,
                            'Class': 'Parallel',
                            'FailurePolicy': 0,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 170,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 172,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 173,
                                                    'Class': 'Condition',
                                                    'Method': (Func8, ()) },
                                                {
                                                    'ID': 174,
                                                    'Class': 'Noop' },
                                                {
                                                    'ID': 175,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 176,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.servantagent.CAgent.ChooseHateTarget, (3, 0)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 177,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.servantagent.CAgent.TurnToLockEnemy, (10, 1)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 178,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.servantagent.CAgent.MoveToLockEnemy, (5,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] },
                                {
                                    'ID': 171,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.Attack, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 167,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.Attack, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 107,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.UpdateInAdvance, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
