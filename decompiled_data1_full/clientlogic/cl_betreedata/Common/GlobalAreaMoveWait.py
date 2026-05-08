# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Common/GlobalAreaMoveWait.pyc
# RelativePath: clientlogic/cl_betreedata/Common/GlobalAreaMoveWait.pyc
# Source Generated with Decompyle++
# File: GlobalAreaMoveWait.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 15


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckInLockEnemySight(60, 25, 0, oAgent) == False


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CheckInLockEnemySight(60, 30, 0, oAgent) == False


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= oAgent.GetConfig('FightMaxDis')

data = {
    'Name': 'GlobalAreaMoveWait',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 9,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseNearestHateTarget, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 32,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 0,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 5,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 15,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 7,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 22,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseEnemyPos, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 23,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 24,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 25,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 37,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 38,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 39,
                                                            'Class': 'And',
                                                            'Node': [
                                                                {
                                                                    'ID': 41,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func1, ()) },
                                                                {
                                                                    'ID': 42,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func2, ()) }] },
                                                        {
                                                            'ID': 40,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] }] },
                                {
                                    'ID': 8,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 13,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 0,
                                            'SuccessPolicy': 1,
                                            'ExitPolicy': 0,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 14,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) },
                                                {
                                                    'ID': 16,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 19,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangeHidePosAndAttPos, (1, 10)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 17,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 18,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 4,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 20,
                                                                'Class': 'Effector',
                                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                'Phase': 1,
                                                                'Flag': 'effector' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 21,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 100 }] }] }] }] },
                        {
                            'ID': 33,
                            'Class': 'And',
                            'Node': [
                                {
                                    'ID': 34,
                                    'Class': 'Condition',
                                    'Method': (Func4, ()) },
                                {
                                    'ID': 36,
                                    'Class': 'Condition',
                                    'Method': (Func5, ()) }] }] }] }] }
