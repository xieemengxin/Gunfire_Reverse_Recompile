# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterLargeFar/LaserFarAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterLargeFar/LaserFarAttack.pyc
# Source Generated with Decompyle++
# File: LaserFarAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckInSigntLock(120, 0, oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 40


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckInSigntLock(120, 0, oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, oAgent.GetConfig('IntervalTime'), oAgent) == True


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 15


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('LockTargetDis'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.CheckInSigntLock(120, 0, oAgent) == True

data = {
    'Name': 'LaserFarAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 222,
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
                    'ID': 634,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 635,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 620,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 621,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 622,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 624,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 625,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 626,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (35,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 631,
                                    'Class': 'Noop' }] },
                        {
                            'ID': 636,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 638,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 639,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 637,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.TurningMoveToLockTarget, (120,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 629,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
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
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 641,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) },
                                        {
                                            'ID': 38,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) },
                                        {
                                            'ID': 628,
                                            'Class': 'Condition',
                                            'Method': (Func4, ()) }] },
                                {
                                    'ID': 60,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 597,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 616,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 617,
                                                            'Class': 'Condition',
                                                            'Method': (Func5, ()) },
                                                        {
                                                            'ID': 618,
                                                            'Class': 'Action',
                                                            'Method': (Func6, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 619,
                                                            'Class': 'Action',
                                                            'Method': (Func7, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 608,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 644,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetDirToLockEnemy, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 607,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FaceDir, (True,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 599,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 600,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 606,
                                                                'Class': 'Precondition',
                                                                'Method': (cl_betree.monsteragent.CAgent.TryReChooseHateFlankPos, (3, 6, 8, 0, 45)),
                                                                'Phase': 1,
                                                                'Flag': 'precondition',
                                                                'BinaryOperator': 'And' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 601,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 612,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func8, ()) },
                                                                {
                                                                    'ID': 610,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] }] }] },
                        {
                            'ID': 630,
                            'Class': 'Condition',
                            'Method': (Func9, ()) },
                        {
                            'ID': 643,
                            'Class': 'Condition',
                            'Method': (Func10, ()) }] },
                {
                    'ID': 646,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetDirToLockEnemy, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 647,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 652,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.FaceDir, (True,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 33,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
