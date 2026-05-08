# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Hero/HeroRescue.pyc
# RelativePath: clientlogic/cl_betreedata/Hero/HeroRescue.pyc
# Source Generated with Decompyle++
# File: HeroRescue.pyc (Python 3.6)

import cl_betree.heroagent

def Func0(oAgent):
    return cl_betree.heroagent.CAgent.CheckSpecialKey(4096, oAgent) == True


def Func1(oAgent):
    return cl_betree.heroagent.CAgent.CheckRescueTargetCanSee(oAgent) == True


def Func2(oAgent):
    return cl_betree.heroagent.CAgent.CheckToRescueTargetDis(4, oAgent) == True


def Func3(oAgent):
    return cl_betree.heroagent.CAgent.CanUseShiftPF(oAgent) == True

data = {
    'Name': 'HeroRescue',
    'ID': 0,
    'AgentType': 'cl_betree.heroagent',
    'IsFSM': False,
    'Ver': 92,
    'Node': [
        {
            'ID': 42,
            'Class': 'Parallel',
            'FailurePolicy': 0,
            'SuccessPolicy': 1,
            'ExitPolicy': 0,
            'ChildFinishPolicy': 1,
            'Node': [
                {
                    'ID': 43,
                    'Class': 'Action',
                    'Method': (cl_betree.heroagent.CAgent.NeedToRescue, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 1,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 62,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 0,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 67,
                                    'Class': 'Or',
                                    'Node': [
                                        {
                                            'ID': 71,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 69,
                                                    'Class': 'And',
                                                    'Node': [
                                                        {
                                                            'ID': 68,
                                                            'Class': 'Condition',
                                                            'Method': (Func0, ()) },
                                                        {
                                                            'ID': 70,
                                                            'Class': 'Condition',
                                                            'Method': (Func1, ()) }] },
                                                {
                                                    'ID': 72,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 12 }] },
                                        {
                                            'ID': 65,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) }] },
                                {
                                    'ID': 55,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 41,
                                            'Class': 'Action',
                                            'Method': (cl_betree.heroagent.CAgent.FacePath, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 73,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 0,
                                            'SuccessPolicy': 1,
                                            'ExitPolicy': 0,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 74,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 75,
                                                            'Class': 'Condition',
                                                            'Method': (Func3, ()) },
                                                        {
                                                            'ID': 76,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.heroagent.CAgent.UseShiftPF, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 77,
                                                            'Class': 'Noop' }] },
                                                {
                                                    'ID': 40,
                                                    'Class': 'Action',
                                                    'Attachment': ({
                                                        'ID': 66,
                                                        'Class': 'Precondition',
                                                        'Method': (cl_betree.heroagent.CAgent.ChooseRescueTargetPos, (4,)),
                                                        'Phase': 2,
                                                        'Flag': 'precondition',
                                                        'BinaryOperator': 'And' },),
                                                    'Method': (cl_betree.heroagent.CAgent.MoveToPos, (3,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] },
                        {
                            'ID': 48,
                            'Class': 'Action',
                            'Method': (cl_betree.heroagent.CAgent.StopMoving, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 22,
                            'Class': 'Action',
                            'Method': (cl_betree.heroagent.CAgent.RescueTeammate, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
