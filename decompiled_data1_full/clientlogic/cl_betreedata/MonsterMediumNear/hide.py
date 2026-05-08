# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumNear/hide.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumNear/hide.pyc
# Source Generated with Decompyle++
# File: hide.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangeHidePosAndAttPos(1, oAgent.GetConfig('HideR'), oAgent)


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return oAgent.GetConfig('HideTime')


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'hide',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 44,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 26,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 27,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 25,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 14,
                            'Class': 'Action',
                            'Method': (Func0, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 29,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 8,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 31,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 12,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 13,
                            'Class': 'Condition',
                            'Method': (Func1, ()) },
                        {
                            'ID': 9,
                            'Class': 'WaitFrame',
                            'Frames': (Func2, ()) }] },
                {
                    'ID': 16,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 15,
                            'Class': 'Condition',
                            'Method': (Func3, ()) },
                        {
                            'ID': 17,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 22,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetAttackPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 18,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 10,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetAttackPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 32,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 30,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 11,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
