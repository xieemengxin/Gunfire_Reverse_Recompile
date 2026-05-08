# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DeviceTurret/FollowAttack.pyc
# RelativePath: clientlogic/cl_betreedata/DeviceTurret/FollowAttack.pyc
# Source Generated with Decompyle++
# File: FollowAttack.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.CheckInHeroSight(30, oAgent) == True


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.GetHeroDis(oAgent) <= 12


def Func2(oAgent):
    return cl_betree.servantagent.CAgent.GetHeroDis(oAgent) >= 8


def Func3(oAgent):
    return cl_betree.servantagent.CAgent.CheckInHeroSight(40, oAgent) == False


def Func4(oAgent):
    return cl_betree.servantagent.CAgent.GetHeroDis(oAgent) > 15


def Func5(oAgent):
    return cl_betree.servantagent.CAgent.GetHeroDis(oAgent) < 5


def Func6(oAgent):
    return cl_betree.servantagent.CAgent.ChooseSeeEnemy(oAgent.GetData('HateMethod'), oAgent.GetConfig('HitRange'), oAgent) == 1


def Func7(oAgent):
    return cl_betree.servantagent.CAgent.CheckCanSeeLock(oAgent) == True


def Func8(oAgent):
    return cl_betree.servantagent.CAgent.IsPerformUseArea(False, oAgent) == True

data = {
    'Name': 'FollowAttack',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 104,
    'Node': [
        {
            'ID': 6,
            'Class': 'Parallel',
            'FailurePolicy': 1,
            'SuccessPolicy': 1,
            'ExitPolicy': 1,
            'ChildFinishPolicy': 1,
            'Node': [
                {
                    'ID': 66,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 50,
                            'Class': 'And',
                            'Node': [
                                {
                                    'ID': 27,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 51,
                                    'Class': 'And',
                                    'Node': [
                                        {
                                            'ID': 52,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 53,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) }] }] },
                        {
                            'ID': 54,
                            'Class': 'Parallel',
                            'FailurePolicy': 0,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 0,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 75,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 16,
                                            'Class': 'SelectorProbability',
                                            'RandomGenerator': None,
                                            'Node': [
                                                {
                                                    'ID': 17,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 10,
                                                    'Node': [
                                                        {
                                                            'ID': 20,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 200 }] },
                                                {
                                                    'ID': 18,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 10,
                                                    'Node': [
                                                        {
                                                            'ID': 21,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 400 }] },
                                                {
                                                    'ID': 19,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 10,
                                                    'Node': [
                                                        {
                                                            'ID': 22,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 600 }] }] },
                                        {
                                            'ID': 76,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.ChooseOwnerAroundPos, (8, 12, 10, 30)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 82,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.SetForceMoveSpeed, (300,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 77,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.MoveToPos, (2,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 55,
                                    'Class': 'Or',
                                    'Node': [
                                        {
                                            'ID': 57,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) },
                                        {
                                            'ID': 56,
                                            'Class': 'Or',
                                            'Node': [
                                                {
                                                    'ID': 58,
                                                    'Class': 'Condition',
                                                    'Method': (Func4, ()) },
                                                {
                                                    'ID': 59,
                                                    'Class': 'Condition',
                                                    'Method': (Func5, ()) }] }] }] },
                        {
                            'ID': 67,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 61,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ChooseOwnerAroundPos, (8, 12, 10, 30)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 78,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.SetForceMoveSpeed, (0,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 62,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 0,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 0,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 63,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.MoveToPos, (2,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 65,
                                            'Class': 'WaitFrame',
                                            'Frames': 10 }] }] }] },
                {
                    'ID': 39,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 43,
                            'Class': 'Condition',
                            'Method': (Func6, ()) },
                        {
                            'ID': 41,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 74,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.SetForceMoveSpeed, (0,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 71,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.FaceLockEnemy, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 42,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ChooseAttack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 44,
                                    'Class': 'And',
                                    'Node': [
                                        {
                                            'ID': 34,
                                            'Class': 'Condition',
                                            'Method': (Func7, ()) },
                                        {
                                            'ID': 45,
                                            'Class': 'Condition',
                                            'Method': (Func8, ()) }] },
                                {
                                    'ID': 3,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.Attack, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 9,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.UpdateInAdvance, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 70,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
