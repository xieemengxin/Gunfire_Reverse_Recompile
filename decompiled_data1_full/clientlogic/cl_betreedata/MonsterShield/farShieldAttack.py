# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterShield/farShieldAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterShield/farShieldAttack.pyc
# Source Generated with Decompyle++
# File: farShieldAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, oAgent.GetConfig('IntervalTime'), oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.HasToStartGuerrilla(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func6(oAgent):
    return oAgent.GetConfig('GuerrillaInterval')


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True

data = {
    'Name': 'farShieldAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 138,
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
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 19,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 29,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 5,
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
                                            'ID': 8,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 8,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                                'Phase': 1,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 28,
                                            'Class': 'Condition',
                                            'Method': (Func0, ()) },
                                        {
                                            'ID': 9,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 11,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 27,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 7,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 12,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) },
                                                {
                                                    'ID': 13,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 15,
                                                            'Class': 'Action',
                                                            'Method': (Func3, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 20,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 1,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 21,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 22,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 23,
                                                                            'Class': 'And',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 25,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func4, ()) },
                                                                                {
                                                                                    'ID': 26,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func5, ()) }] },
                                                                        {
                                                                            'ID': 24,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] }] },
                                                {
                                                    'ID': 14,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 0,
                                                    'SuccessPolicy': 1,
                                                    'ExitPolicy': 0,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 17,
                                                            'Class': 'WaitFrame',
                                                            'Frames': (Func6, ()) },
                                                        {
                                                            'ID': 18,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.KeepMoving, (3,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] }] },
                        {
                            'ID': 30,
                            'Class': 'Condition',
                            'Method': (Func7, ()) }] }] }] }
