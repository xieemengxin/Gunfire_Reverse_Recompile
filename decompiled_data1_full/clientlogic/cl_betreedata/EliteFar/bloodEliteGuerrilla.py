# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteFar/bloodEliteGuerrilla.pyc
# RelativePath: clientlogic/cl_betreedata/EliteFar/bloodEliteGuerrilla.pyc
# Source Generated with Decompyle++
# File: bloodEliteGuerrilla.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 8


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsLockEnemyPosRangeAccessible(1.5, oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 75, oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.IsLockEnemyPosRangeAccessible(1.5, oAgent) == False


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 20


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 20


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True

data = {
    'Name': 'bloodEliteGuerrilla',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 84,
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
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 31,
                            'Class': 'And',
                            'Node': [
                                {
                                    'ID': 32,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 33,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) }] },
                        {
                            'ID': 7,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 8,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 9,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 11,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) },
                                        {
                                            'ID': 30,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 26,
                                                    'Class': 'And',
                                                    'Node': [
                                                        {
                                                            'ID': 27,
                                                            'Class': 'Condition',
                                                            'Method': (Func3, ()) },
                                                        {
                                                            'ID': 28,
                                                            'Class': 'Condition',
                                                            'Method': (Func4, ()) }] },
                                                {
                                                    'ID': 29,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (32831,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 34,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 35,
                                                            'Class': 'Condition',
                                                            'Method': (Func5, ()) },
                                                        {
                                                            'ID': 36,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 37,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (32837,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 40,
                                                                    'Class': 'Action',
                                                                    'Attachment': ({
                                                                        'ID': 41,
                                                                        'Class': 'Precondition',
                                                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                        'Phase': 1,
                                                                        'Flag': 'precondition',
                                                                        'BinaryOperator': 'And' },),
                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 42,
                                                                    'Class': 'Action',
                                                                    'Attachment': ({
                                                                        'ID': 43,
                                                                        'Class': 'Effector',
                                                                        'Method': (cl_betree.monsteragent.CAgent.UseMovePosAsSkillEnd, ()),
                                                                        'Phase': 1,
                                                                        'Flag': 'effector' },),
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (15, 19, 0, 45)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 38,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 39,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] },
                                {
                                    'ID': 10,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 44,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 45,
                                                    'Class': 'Condition',
                                                    'Method': (Func6, ()) },
                                                {
                                                    'ID': 46,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 47,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (32837,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 48,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 51,
                                                                'Class': 'Precondition',
                                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                'Phase': 1,
                                                                'Flag': 'precondition',
                                                                'BinaryOperator': 'And' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 49,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 52,
                                                                'Class': 'Effector',
                                                                'Method': (cl_betree.monsteragent.CAgent.UseMovePosAsSkillEnd, ()),
                                                                'Phase': 1,
                                                                'Flag': 'effector' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (15, 19, 0, 45)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 50,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 53,
                                                    'Class': 'Noop' }] },
                                        {
                                            'ID': 13,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (10, 5, 15, 150, 180)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 14,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 15,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 16,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 18,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 19,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 20,
                                                            'Class': 'And',
                                                            'Node': [
                                                                {
                                                                    'ID': 22,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func7, ()) },
                                                                {
                                                                    'ID': 23,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func8, ()) }] },
                                                        {
                                                            'ID': 21,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] },
                                        {
                                            'ID': 24,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] }] }] }] }
