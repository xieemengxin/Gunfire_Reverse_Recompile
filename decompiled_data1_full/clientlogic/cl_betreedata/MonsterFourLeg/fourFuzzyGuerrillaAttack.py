# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFourLeg/fourFuzzyGuerrillaAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFourLeg/fourFuzzyGuerrillaAttack.pyc
# Source Generated with Decompyle++
# File: fourFuzzyGuerrillaAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, oAgent.GetConfig('IntervalTime'), oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 4


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 30


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(30, oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), 85, 95, oAgent)


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 20


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), 85, 95, oAgent)


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True

data = {
    'Name': 'fourFuzzyGuerrillaAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 56,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Attachment': ({
                'ID': 42,
                'Class': 'Precondition',
                'Method': (cl_betree.monsteragent.CAgent.SetFightLogicType, (4,)),
                'Phase': 1,
                'Flag': 'precondition',
                'BinaryOperator': 'And' },),
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 155,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 44,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 45,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 49,
                                            'Class': 'Condition',
                                            'Method': (Func0, ()) },
                                        {
                                            'ID': 50,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 48,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 47,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 55,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) },
                                        {
                                            'ID': 81,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) },
                                        {
                                            'ID': 56,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 68,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 82,
                                            'Class': 'SelectorProbability',
                                            'RandomGenerator': None,
                                            'Node': [
                                                {
                                                    'ID': 83,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 70,
                                                    'Node': [
                                                        {
                                                            'ID': 126,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 148,
                                                                    'Class': 'IfElse',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 149,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func4, ()) },
                                                                        {
                                                                            'ID': 150,
                                                                            'Class': 'Action',
                                                                            'Method': (Func5, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 151,
                                                                            'Class': 'IfElse',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 152,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func6, ()) },
                                                                                {
                                                                                    'ID': 153,
                                                                                    'Class': 'Action',
                                                                                    'Method': (Func7, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 154,
                                                                                    'Class': 'Action',
                                                                                    'Method': (Func8, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] }] },
                                                                {
                                                                    'ID': 142,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 143,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 135,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 136,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 137,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 144,
                                                                                    'Class': 'And',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 146,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func9, ()) },
                                                                                        {
                                                                                            'ID': 147,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func10, ()) }] },
                                                                                {
                                                                                    'ID': 145,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] }] }] }] },
                                                {
                                                    'ID': 85,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 30,
                                                    'Node': [
                                                        {
                                                            'ID': 120,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 121,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (3, 5, 85, 95)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 122,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 123,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (2,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 124,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] }] }] },
                        {
                            'ID': 156,
                            'Class': 'Condition',
                            'Method': (Func11, ()) }] },
                {
                    'ID': 118,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 119,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 51,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
