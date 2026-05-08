# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterWizard/SurvivalwizardAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterWizard/SurvivalwizardAttack.pyc
# Source Generated with Decompyle++
# File: SurvivalwizardAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 20


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 50


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), 20, 60, oAgent)


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func6(oAgent):
    return oAgent.GetConfig('HideAttackStandingTime')


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == True


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 32838

data = {
    'Name': 'SurvivalwizardAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 156,
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
                    'ID': 6,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 34,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 36,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 43,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 37,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 38,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) }] },
                        {
                            'ID': 71,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 76,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 55,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 67,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 68,
                                                            'Class': 'Condition',
                                                            'Method': (Func2, ()) },
                                                        {
                                                            'ID': 72,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 73,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func3, ()) },
                                                                {
                                                                    'ID': 74,
                                                                    'Class': 'Action',
                                                                    'Method': (Func4, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 78,
                                                                    'Class': 'SelectorProbability',
                                                                    'RandomGenerator': None,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 79,
                                                                            'Class': 'DecoratorWeight',
                                                                            'DecorateWhenChildEnds': False,
                                                                            'Weight': 25,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 81,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 82,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 83,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangeHidePosAndAttPos, (1, 10)),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 84,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None },
                                                                                        {
                                                                                            'ID': 85,
                                                                                            'Class': 'Parallel',
                                                                                            'FailurePolicy': 0,
                                                                                            'SuccessPolicy': 0,
                                                                                            'ExitPolicy': 1,
                                                                                            'ChildFinishPolicy': 0,
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 90,
                                                                                                    'Class': 'Action',
                                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                                    'ResultOption': 0,
                                                                                                    'ResultFunctor': None },
                                                                                                {
                                                                                                    'ID': 91,
                                                                                                    'Class': 'WaitFrame',
                                                                                                    'Frames': 125 }] },
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
                                                                                                    'ID': 92,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func5, ()) },
                                                                                                {
                                                                                                    'ID': 93,
                                                                                                    'Class': 'WaitFrame',
                                                                                                    'Frames': (Func6, ()) }] },
                                                                                        {
                                                                                            'ID': 89,
                                                                                            'Class': 'IfElse',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 97,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func7, ()) },
                                                                                                {
                                                                                                    'ID': 98,
                                                                                                    'Class': 'Sequence',
                                                                                                    'Node': [
                                                                                                        {
                                                                                                            'ID': 105,
                                                                                                            'Class': 'Action',
                                                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHorizontalPos, (2, 3)),
                                                                                                            'ResultOption': 0,
                                                                                                            'ResultFunctor': None },
                                                                                                        {
                                                                                                            'ID': 106,
                                                                                                            'Class': 'Action',
                                                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                                            'ResultOption': 0,
                                                                                                            'ResultFunctor': None }] },
                                                                                                {
                                                                                                    'ID': 99,
                                                                                                    'Class': 'Noop' }] },
                                                                                        {
                                                                                            'ID': 107,
                                                                                            'Class': 'DecoratorAlwaysFailure',
                                                                                            'DecorateWhenChildEnds': False }] }] },
                                                                        {
                                                                            'ID': 80,
                                                                            'Class': 'DecoratorWeight',
                                                                            'DecorateWhenChildEnds': False,
                                                                            'Weight': 50,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 75,
                                                                                    'Class': 'Action',
                                                                                    'Method': (Func8, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] }] }] },
                                                        {
                                                            'ID': 70,
                                                            'Class': 'Action',
                                                            'Method': (Func9, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 56,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 58,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 77,
                                            'Class': 'WaitFrame',
                                            'Frames': 125 }] }] }] },
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
