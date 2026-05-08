# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteFar/WizardEliteGuerrila.pyc
# RelativePath: clientlogic/cl_betreedata/EliteFar/WizardEliteGuerrila.pyc
# Source Generated with Decompyle++
# File: WizardEliteGuerrila.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 45, oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 60, oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 5


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 32814


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 32815


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 10


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 32811


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 32815


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 32814


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 32814


def Func13(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 32815


def Func14(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'WizardEliteGuerrila',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 27,
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
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 0)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 104,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 105,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 80,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 81,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 82,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 83,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (10, 5, 15, 150, 180)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 84,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 69,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 106,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 71,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 107,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 108,
                                                    'Class': 'And',
                                                    'Node': [
                                                        {
                                                            'ID': 109,
                                                            'Class': 'Condition',
                                                            'Method': (Func1, ()) },
                                                        {
                                                            'ID': 110,
                                                            'Class': 'Condition',
                                                            'Method': (Func2, ()) }] },
                                                {
                                                    'ID': 111,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 78,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] }] },
                {
                    'ID': 5,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 6,
                            'Class': 'Condition',
                            'Method': (Func3, ()) },
                        {
                            'ID': 7,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 8,
                                    'Class': 'Condition',
                                    'Method': (Func4, ()) },
                                {
                                    'ID': 9,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 10,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 11,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                'Phase': 1,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 0)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 12,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 13,
                                                'Class': 'Effector',
                                                'Method': (cl_betree.monsteragent.CAgent.UseMovePosAsSkillEnd, ()),
                                                'Phase': 1,
                                                'Flag': 'effector' },),
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (15, 18, 10, 45)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 14,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 15,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 16,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 17,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                'Phase': 1,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 0)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 85,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 86,
                                                    'Class': 'Condition',
                                                    'Method': (Func5, ()) },
                                                {
                                                    'ID': 18,
                                                    'Class': 'Action',
                                                    'Attachment': ({
                                                        'ID': 19,
                                                        'Class': 'Effector',
                                                        'Method': (cl_betree.monsteragent.CAgent.UseMovePosAsSkillEnd, ()),
                                                        'Phase': 1,
                                                        'Flag': 'effector' },),
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (18, 20, 0, 75)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 99,
                                                    'Class': 'Noop' }] },
                                        {
                                            'ID': 20,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 21,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 22,
                                    'Class': 'Condition',
                                    'Method': (Func6, ()) },
                                {
                                    'ID': 23,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 24,
                                            'Class': 'Condition',
                                            'Method': (Func7, ()) },
                                        {
                                            'ID': 25,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 112,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 0,
                                                    'SuccessPolicy': 1,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 41,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 1,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 42,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func8, ()) },
                                                                {
                                                                    'ID': 43,
                                                                    'Class': 'DecoratorAlwaysRunning',
                                                                    'DecorateWhenChildEnds': False,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 44,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 45,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (20, 4, 7, 75, 105)),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 46,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 47,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 48,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] }] }] },
                                                        {
                                                            'ID': 113,
                                                            'Class': 'Condition',
                                                            'Method': (Func9, ()) }] },
                                                {
                                                    'ID': 49,
                                                    'Class': 'Action',
                                                    'Attachment': ({
                                                        'ID': 50,
                                                        'Class': 'Precondition',
                                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                        'Phase': 1,
                                                        'Flag': 'precondition',
                                                        'BinaryOperator': 'And' },),
                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 0)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 51,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 26,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 27,
                                                    'Class': 'Action',
                                                    'Attachment': ({
                                                        'ID': 28,
                                                        'Class': 'Precondition',
                                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                        'Phase': 1,
                                                        'Flag': 'precondition',
                                                        'BinaryOperator': 'And' },),
                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 0)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 92,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 93,
                                                            'Class': 'Condition',
                                                            'Method': (Func10, ()) },
                                                        {
                                                            'ID': 29,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 30,
                                                                'Class': 'Effector',
                                                                'Method': (cl_betree.monsteragent.CAgent.UseMovePosAsSkillEnd, ()),
                                                                'Phase': 1,
                                                                'Flag': 'effector' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (18, 20, 0, 75)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 94,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 95,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func11, ()) },
                                                                {
                                                                    'ID': 96,
                                                                    'Class': 'Action',
                                                                    'Attachment': ({
                                                                        'ID': 97,
                                                                        'Class': 'Effector',
                                                                        'Method': (cl_betree.monsteragent.CAgent.UseMovePosAsSkillEnd, ()),
                                                                        'Phase': 1,
                                                                        'Flag': 'effector' },),
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (18, 20, 10, 45)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 98,
                                                                    'Class': 'Noop' }] }] },
                                                {
                                                    'ID': 31,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 32,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 33,
                                            'Class': 'Condition',
                                            'Method': (Func12, ()) },
                                        {
                                            'ID': 34,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 35,
                                                    'Class': 'Action',
                                                    'Attachment': ({
                                                        'ID': 36,
                                                        'Class': 'Precondition',
                                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                        'Phase': 1,
                                                        'Flag': 'precondition',
                                                        'BinaryOperator': 'And' },),
                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 0)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 37,
                                                    'Class': 'Action',
                                                    'Attachment': ({
                                                        'ID': 38,
                                                        'Class': 'Effector',
                                                        'Method': (cl_betree.monsteragent.CAgent.UseMovePosAsSkillEnd, ()),
                                                        'Phase': 1,
                                                        'Flag': 'effector' },),
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (18, 25, 10, 45)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 39,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 40,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 100,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 101,
                                                            'Class': 'Condition',
                                                            'Method': (Func13, ()) },
                                                        {
                                                            'ID': 102,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 103,
                                                                'Class': 'Effector',
                                                                'Method': (cl_betree.monsteragent.CAgent.UseMovePosAsSkillEnd, ()),
                                                                'Phase': 1,
                                                                'Flag': 'effector' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (15, 18, 0, 75)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 52,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 1,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 53,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func14, ()) },
                                                                {
                                                                    'ID': 54,
                                                                    'Class': 'DecoratorAlwaysRunning',
                                                                    'DecorateWhenChildEnds': False,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 55,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 56,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (20, 4, 7, 75, 105)),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 57,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 58,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 59,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] }] }] }] },
                                                {
                                                    'ID': 60,
                                                    'Class': 'Action',
                                                    'Attachment': ({
                                                        'ID': 61,
                                                        'Class': 'Precondition',
                                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                        'Phase': 1,
                                                        'Flag': 'precondition',
                                                        'BinaryOperator': 'And' },),
                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 0)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 62,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] }] }] }] }
