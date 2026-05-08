# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFar/cover.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFar/cover.pyc
# Source Generated with Decompyle++
# File: cover.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'cover',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 38,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 3,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 5,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 6,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.GetCoveredPos, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 7,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 8,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 4,
                            'Class': 'WaitFrame',
                            'Frames': 50 }] }] }] }
