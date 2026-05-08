# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterLargeFar/LargeFarGuerrillaAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterLargeFar/LargeFarGuerrillaAttack.pyc
# Source Generated with Decompyle++
# File: LargeFarGuerrillaAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 100, oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 20


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True

data = {
    'Name': 'LargeFarGuerrillaAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 148,
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
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (50, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
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
                                    'ID': 38,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 62,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 63,
                                    'Class': 'Condition',
                                    'Method': (Func2, ()) }] },
                        {
                            'ID': 64,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 65,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 72,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 76,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) },
                                                {
                                                    'ID': 77,
                                                    'Class': 'Action',
                                                    'Method': (Func4, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 78,
                                                    'Class': 'Action',
                                                    'Method': (Func5, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 67,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 68,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 69,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 73,
                                                    'Class': 'Action',
                                                    'Attachment': ({
                                                        'ID': 74,
                                                        'Class': 'Precondition',
                                                        'Method': (cl_betree.monsteragent.CAgent.TryReChooseHateFlankPos, (3, 6, 8, 0, 45)),
                                                        'Phase': 1,
                                                        'Flag': 'precondition',
                                                        'BinaryOperator': 'And' },),
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 75,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 79,
                                                            'Class': 'And',
                                                            'Node': [
                                                                {
                                                                    'ID': 81,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func6, ()) },
                                                                {
                                                                    'ID': 82,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func7, ()) }] },
                                                        {
                                                            'ID': 80,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] }] }] },
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
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (50, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 33,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
