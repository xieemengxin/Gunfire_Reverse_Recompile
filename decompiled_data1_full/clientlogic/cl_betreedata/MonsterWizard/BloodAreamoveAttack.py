# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterWizard/BloodAreamoveAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterWizard/BloodAreamoveAttack.pyc
# Source Generated with Decompyle++
# File: BloodAreamoveAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == False


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


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


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 32838

data = {
    'Name': 'BloodAreamoveAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 153,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 59,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 71,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 72,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 74,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 114,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 75,
                                    'Class': 'And',
                                    'Node': [
                                        {
                                            'ID': 79,
                                            'Class': 'And',
                                            'Node': [
                                                {
                                                    'ID': 83,
                                                    'Class': 'Condition',
                                                    'Method': (Func0, ()) },
                                                {
                                                    'ID': 84,
                                                    'Class': 'Condition',
                                                    'Method': (Func1, ()) }] },
                                        {
                                            'ID': 80,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) }] }] },
                        {
                            'ID': 115,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 116,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 117,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 118,
                                    'Class': 'Condition',
                                    'Method': (Func3, ()) },
                                {
                                    'ID': 119,
                                    'Class': 'Condition',
                                    'Method': (Func4, ()) }] },
                        {
                            'ID': 73,
                            'Class': 'SelectorProbability',
                            'RandomGenerator': None,
                            'Node': [
                                {
                                    'ID': 77,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 20,
                                    'Node': [
                                        {
                                            'ID': 81,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 85,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 86,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 87,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 90,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.KeepMoving, (3,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 91,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 25 }] }] }] },
                                {
                                    'ID': 78,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 80,
                                    'Node': [
                                        {
                                            'ID': 82,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 88,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedAreaPos, (6, 10, '')),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 89,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 92,
                                                            'Class': 'Condition',
                                                            'Method': (Func5, ()) },
                                                        {
                                                            'ID': 93,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 95,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 96,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 97,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 102,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 103,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 106,
                                                                                    'Class': 'And',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 110,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func6, ()) },
                                                                                        {
                                                                                            'ID': 111,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func7, ()) }] },
                                                                                {
                                                                                    'ID': 107,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] }] }] },
                                                        {
                                                            'ID': 94,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 98,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 99,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 100,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 104,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 105,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 108,
                                                                                    'Class': 'And',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 112,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func8, ()) },
                                                                                        {
                                                                                            'ID': 113,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func9, ()) }] },
                                                                                {
                                                                                    'ID': 109,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] }] },
                                                                {
                                                                    'ID': 101,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] }] }] }] },
                {
                    'ID': 9,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 32,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 63,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 62,
                            'Class': 'Condition',
                            'Method': (Func10, ()) },
                        {
                            'ID': 60,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 66,
                                'Class': 'Effector',
                                'Method': (cl_betree.monsteragent.CAgent.UseMovePosAsSkillEnd, ()),
                                'Phase': 1,
                                'Flag': 'effector' },),
                            'Method': (cl_betree.monsteragent.CAgent.ChooseFriendAroundPos, (5, 10)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 64,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 65,
                                'Class': 'Effector',
                                'Method': (cl_betree.monsteragent.CAgent.UseMovePosAsSkillEnd, ()),
                                'Phase': 1,
                                'Flag': 'effector' },),
                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (5, 7, 0, 45)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 33,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
