# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Common/goback.pyc
# RelativePath: clientlogic/cl_betreedata/Common/goback.pyc
# Source Generated with Decompyle++
# File: goback.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'goback',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 11,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 13,
                    'Class': 'WaitFrame',
                    'Frames': 12 },
                {
                    'ID': 2,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 0,
                    'Node': [
                        {
                            'ID': 3,
                            'Class': 'WaitFrame',
                            'Frames': 50 },
                        {
                            'ID': 4,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 422,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'IsSquat', '0')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 423,
                                    'Class': 'WaitFrame',
                                    'Frames': 6 },
                                {
                                    'ID': 5,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusDefault, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 14,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMPatrol, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 7,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.NextPatrolPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 8,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 9,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
