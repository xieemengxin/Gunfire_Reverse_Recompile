# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumFar/SurvivalMediumFarAreamoveAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumFar/SurvivalMediumFarAreamoveAttack.pyc
# Source Generated with Decompyle++
# File: SurvivalMediumFarAreamoveAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(8046, oAgent) == False


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 50, oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == False


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetFirstRangedArrivePosDis(oAgent) <= 5


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True

data = {
    'Name': 'SurvivalMediumFarAreamoveAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 17,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
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
                            'ID': 6,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 11,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 77,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 78,
                                            'Class': 'Condition',
                                            'Method': (Func0, ()) },
                                        {
                                            'ID': 79,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 13,
                                                    'Class': 'Condition',
                                                    'Method': (Func1, ()) },
                                                {
                                                    'ID': 82,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.AddState, (8046, 0)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 80,
                                            'Class': 'DecoratorAlwaysSuccess',
                                            'DecorateWhenChildEnds': False }] },
                                {
                                    'ID': 12,
                                    'Class': 'And',
                                    'Node': [
                                        {
                                            'ID': 15,
                                            'Class': 'And',
                                            'Node': [
                                                {
                                                    'ID': 19,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) },
                                                {
                                                    'ID': 20,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) }] },
                                        {
                                            'ID': 16,
                                            'Class': 'Condition',
                                            'Method': (Func4, ()) }] }] },
                        {
                            'ID': 84,
                            'Class': 'DecoratorAlwaysFailure',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 43,
                                    'Class': 'SelectorProbability',
                                    'RandomGenerator': None,
                                    'Node': [
                                        {
                                            'ID': 44,
                                            'Class': 'DecoratorWeight',
                                            'DecorateWhenChildEnds': False,
                                            'Weight': 20,
                                            'Node': [
                                                {
                                                    'ID': 71,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 86,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (10, 1)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 72,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 74,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 1,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 75,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.KeepMoving, (3,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 76,
                                                                    'Class': 'WaitFrame',
                                                                    'Frames': 25 }] }] }] },
                                        {
                                            'ID': 45,
                                            'Class': 'DecoratorWeight',
                                            'DecorateWhenChildEnds': False,
                                            'Weight': 80,
                                            'Node': [
                                                {
                                                    'ID': 46,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 47,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangedAreaPos, (6, 10, '')),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 48,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 49,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func5, ()) },
                                                                {
                                                                    'ID': 50,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 85,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (10, 1)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 52,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 54,
                                                                            'Class': 'Parallel',
                                                                            'FailurePolicy': 1,
                                                                            'SuccessPolicy': 0,
                                                                            'ExitPolicy': 1,
                                                                            'ChildFinishPolicy': 1,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 59,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 60,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 63,
                                                                                            'Class': 'And',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 67,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func6, ()) },
                                                                                                {
                                                                                                    'ID': 68,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func7, ()) }] },
                                                                                        {
                                                                                            'ID': 64,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None }] }] }] },
                                                                {
                                                                    'ID': 51,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 56,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 55,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 57,
                                                                            'Class': 'Parallel',
                                                                            'FailurePolicy': 1,
                                                                            'SuccessPolicy': 0,
                                                                            'ExitPolicy': 1,
                                                                            'ChildFinishPolicy': 1,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 61,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 62,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 65,
                                                                                            'Class': 'And',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 69,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func8, ()) },
                                                                                                {
                                                                                                    'ID': 70,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func9, ()) }] },
                                                                                        {
                                                                                            'ID': 66,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None }] }] }] }] }] }] }] }] }] },
                {
                    'ID': 83,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.RemoveState, (8046,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 8,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 9,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' },),
                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 10,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
