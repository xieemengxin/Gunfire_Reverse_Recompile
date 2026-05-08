# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Spare/SparePatrol.pyc
# RelativePath: clientlogic/cl_betreedata/Spare/SparePatrol.pyc
# Source Generated with Decompyle++
# File: SparePatrol.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.GetHeroDis(oAgent) > 12

data = {
    'Name': 'SparePatrol',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 36,
    'Node': [
        {
            'ID': 18,
            'Class': 'Parallel',
            'FailurePolicy': 1,
            'SuccessPolicy': 0,
            'ExitPolicy': 1,
            'ChildFinishPolicy': 1,
            'Node': [
                {
                    'ID': 25,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 19,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 26,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.SetForceMoveSpeed, (0,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 28,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.MoveToHeroPos, (3,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 22,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 13,
                            'Class': 'SelectorProbability',
                            'RandomGenerator': None,
                            'Node': [
                                {
                                    'ID': 14,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 10,
                                    'Node': [
                                        {
                                            'ID': 8,
                                            'Class': 'WaitFrame',
                                            'Frames': 75 }] },
                                {
                                    'ID': 15,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 10,
                                    'Node': [
                                        {
                                            'ID': 16,
                                            'Class': 'WaitFrame',
                                            'Frames': 100 }] },
                                {
                                    'ID': 20,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 10,
                                    'Node': [
                                        {
                                            'ID': 21,
                                            'Class': 'WaitFrame',
                                            'Frames': 125 }] }] },
                        {
                            'ID': 23,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.SetForceMoveSpeed, (200,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 11,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.MoveToHeroPos, (3,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
