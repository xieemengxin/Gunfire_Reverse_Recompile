# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteFar/EliteLargeFarGuerrillaPhase2.pyc
# RelativePath: clientlogic/cl_betreedata/EliteFar/EliteLargeFarGuerrillaPhase2.pyc
# Source Generated with Decompyle++
# File: EliteLargeFarGuerrillaPhase2.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 40


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 50, oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 15


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True

data = {
    'Name': 'EliteLargeFarGuerrillaPhase2',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 85,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 9,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 10,
                            'Class': 'Sequence',
                            'Node': [
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
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (35,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 11,
                            'Class': 'Noop' }] },
                {
                    'ID': 5,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 12,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 17,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 18,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 19,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 20,
                                    'Class': 'Condition',
                                    'Method': (Func2, ()) },
                                {
                                    'ID': 21,
                                    'Class': 'Condition',
                                    'Method': (Func3, ()) }] },
                        {
                            'ID': 22,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 24,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 25,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 37,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 38,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 39,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 44,
                                                            'Class': 'Condition',
                                                            'Method': (Func4, ()) },
                                                        {
                                                            'ID': 45,
                                                            'Class': 'Action',
                                                            'Method': (Func5, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 46,
                                                            'Class': 'Action',
                                                            'Method': (Func6, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 42,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 47,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 48,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 49,
                                                                    'Class': 'And',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 51,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func7, ()) },
                                                                        {
                                                                            'ID': 52,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func8, ()) }] },
                                                                {
                                                                    'ID': 50,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] }] }] }] }] }] }
