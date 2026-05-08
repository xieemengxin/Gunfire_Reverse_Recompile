# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Hero/HeroPatrol.pyc
# RelativePath: clientlogic/cl_betreedata/Hero/HeroPatrol.pyc
# Source Generated with Decompyle++
# File: HeroPatrol.pyc (Python 3.6)

import cl_betree.heroagent

def Func0(oAgent):
    return cl_betree.heroagent.CAgent.GetLeaderDis(oAgent) >= 10


def Func1(oAgent):
    return cl_betree.heroagent.CAgent.CanUseShiftPF(oAgent) == True

data = {
    'Name': 'HeroPatrol',
    'ID': 0,
    'AgentType': 'cl_betree.heroagent',
    'IsFSM': False,
    'Ver': 50,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 54,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 55,
                            'Class': 'Action',
                            'Method': (cl_betree.heroagent.CAgent.ChooseTarget, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 67,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 56,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 58,
                                            'Class': 'Condition',
                                            'Method': (Func0, ()) },
                                        {
                                            'ID': 53,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 46,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.heroagent.CAgent.FacePath, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 76,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 0,
                                                    'SuccessPolicy': 1,
                                                    'ExitPolicy': 0,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 47,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 48,
                                                                'Class': 'Precondition',
                                                                'Method': (cl_betree.heroagent.CAgent.ChooseLeaderPos, ()),
                                                                'Phase': 1,
                                                                'Flag': 'precondition',
                                                                'BinaryOperator': 'And' },),
                                                            'Method': (cl_betree.heroagent.CAgent.MoveToPos, (6,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 68,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 69,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func1, ()) },
                                                                {
                                                                    'ID': 70,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.heroagent.CAgent.UseShiftPF, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 71,
                                                                    'Class': 'Noop' }] }] }] },
                                        {
                                            'ID': 59,
                                            'Class': 'SelectorProbability',
                                            'RandomGenerator': None,
                                            'Node': [
                                                {
                                                    'ID': 60,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 20,
                                                    'Node': [
                                                        {
                                                            'ID': 63,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 64,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.heroagent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 65,
                                                                    'Class': 'Action',
                                                                    'Attachment': ({
                                                                        'ID': 66,
                                                                        'Class': 'Precondition',
                                                                        'Method': (cl_betree.heroagent.CAgent.ChooseLeaderPos, ()),
                                                                        'Phase': 1,
                                                                        'Flag': 'precondition',
                                                                        'BinaryOperator': 'And' },),
                                                                    'Method': (cl_betree.heroagent.CAgent.MoveToPos, (6,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] },
                                                {
                                                    'ID': 61,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 80,
                                                    'Node': [
                                                        {
                                                            'ID': 62,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 25 }] }] }] }] }] }] }] }
