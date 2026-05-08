# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterNear/BoxNearAlert.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterNear/BoxNearAlert.pyc
# Source Generated with Decompyle++
# File: BoxNearAlert.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 20


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(8104, oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 20


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 10


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(8104, oAgent) == True


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 10


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'BoxNearAlert',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 12,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseNearestHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 4,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 5,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 7,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 45,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 46,
                                            'Class': 'WaitFrame',
                                            'Frames': 25 },
                                        {
                                            'ID': 47,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.AddState, (8104, 500)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 19,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 28,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 29,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) },
                                                {
                                                    'ID': 20,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.RemoveState, (8104,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 30,
                                                    'Class': 'Noop' }] },
                                        {
                                            'ID': 10,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 0,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 12,
                                                    'Class': 'DecoratorAlwaysRunning',
                                                    'DecorateWhenChildEnds': False,
                                                    'Node': [
                                                        {
                                                            'ID': 13,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 15,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (12, 10, 15, 75, 105)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 16,
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
                                                                    'ID': 17,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] },
                                                {
                                                    'ID': 21,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 50 },
                                                {
                                                    'ID': 22,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) }] }] }] },
                        {
                            'ID': 6,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 8,
                                    'Class': 'Condition',
                                    'Method': (Func4, ()) },
                                {
                                    'ID': 48,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 49,
                                            'Class': 'WaitFrame',
                                            'Frames': 25 },
                                        {
                                            'ID': 50,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.AddState, (8104, 500)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 25,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 31,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 32,
                                                    'Class': 'Condition',
                                                    'Method': (Func5, ()) },
                                                {
                                                    'ID': 26,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.RemoveState, (8104,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 33,
                                                    'Class': 'Noop' }] },
                                        {
                                            'ID': 34,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 0,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 35,
                                                    'Class': 'DecoratorAlwaysRunning',
                                                    'DecorateWhenChildEnds': False,
                                                    'Node': [
                                                        {
                                                            'ID': 36,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 37,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (12, 10, 15, 75, 105)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 38,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 39,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 40,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] },
                                                {
                                                    'ID': 41,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 50 },
                                                {
                                                    'ID': 42,
                                                    'Class': 'Or',
                                                    'Node': [
                                                        {
                                                            'ID': 43,
                                                            'Class': 'Condition',
                                                            'Method': (Func6, ()) },
                                                        {
                                                            'ID': 44,
                                                            'Class': 'Condition',
                                                            'Method': (Func7, ()) }] }] }] }] }] }] }] }
