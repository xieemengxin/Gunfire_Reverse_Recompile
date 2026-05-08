# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFar/farGuerrillaStandAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFar/farGuerrillaStandAttack.pyc
# Source Generated with Decompyle++
# File: farGuerrillaStandAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == False


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(0, 100, oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.HasToStartGuerrilla(oAgent) == True


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetFirstRangedArrivePosDis(oAgent) >= 6


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 8

data = {
    'Name': 'farGuerrillaStandAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 226,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 98,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 430,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 262,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 359,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 263,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 398,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 394,
                                    'Class': 'And',
                                    'Node': [
                                        {
                                            'ID': 360,
                                            'Class': 'And',
                                            'Node': [
                                                {
                                                    'ID': 361,
                                                    'Class': 'Condition',
                                                    'Method': (Func0, ()) },
                                                {
                                                    'ID': 362,
                                                    'Class': 'Condition',
                                                    'Method': (Func1, ()) }] },
                                        {
                                            'ID': 393,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) }] },
                                {
                                    'ID': 405,
                                    'Class': 'Condition',
                                    'Method': (Func3, ()) }] },
                        {
                            'ID': 264,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 269,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 270,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 271,
                                                    'Class': 'Condition',
                                                    'Method': (Func4, ()) },
                                                {
                                                    'ID': 407,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 408,
                                                            'Class': 'Action',
                                                            'Method': (Func5, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 409,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 420,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func6, ()) },
                                                                {
                                                                    'ID': 421,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 423,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 424,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 436,
                                                                            'Class': 'Parallel',
                                                                            'FailurePolicy': 1,
                                                                            'SuccessPolicy': 0,
                                                                            'ExitPolicy': 1,
                                                                            'ChildFinishPolicy': 1,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 446,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 447,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 452,
                                                                                            'Class': 'And',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 458,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func7, ()) },
                                                                                                {
                                                                                                    'ID': 459,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func8, ()) }] },
                                                                                        {
                                                                                            'ID': 453,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None }] }] }] },
                                                                {
                                                                    'ID': 422,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 426,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 427,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 443,
                                                                            'Class': 'Parallel',
                                                                            'FailurePolicy': 1,
                                                                            'SuccessPolicy': 0,
                                                                            'ExitPolicy': 1,
                                                                            'ChildFinishPolicy': 1,
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 444,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None },
                                                                                {
                                                                                    'ID': 445,
                                                                                    'Class': 'Sequence',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 450,
                                                                                            'Class': 'And',
                                                                                            'Node': [
                                                                                                {
                                                                                                    'ID': 456,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func9, ()) },
                                                                                                {
                                                                                                    'ID': 457,
                                                                                                    'Class': 'Condition',
                                                                                                    'Method': (Func10, ()) }] },
                                                                                        {
                                                                                            'ID': 451,
                                                                                            'Class': 'Action',
                                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                            'ResultOption': 0,
                                                                                            'ResultFunctor': None }] }] }] }] }] },
                                                {
                                                    'ID': 404,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 399,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 401,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 396,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 1,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 397,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.KeepMoving, (3,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 268,
                                                                    'Class': 'WaitFrame',
                                                                    'Frames': (cl_betree.monsteragent.CAgent.GetGuerrillaInterval, ()) }] }] }] }] }] }] },
                {
                    'ID': 364,
                    'Class': 'Sequence',
                    'Attachment': ({
                        'ID': 462,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Node': [
                        {
                            'ID': 431,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 460,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.Squat, (50, 68)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 367,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 461,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.StandUp, (24,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 432,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 433,
                                    'Class': 'Condition',
                                    'Method': (Func11, ()) },
                                {
                                    'ID': 434,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 435,
                                    'Class': 'Noop' }] }] }] }] }
