# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Servant/ServantHold.pyc
# RelativePath: clientlogic/cl_betreedata/Servant/ServantHold.pyc
# Source Generated with Decompyle++
# File: ServantHold.pyc (Python 3.6)

import cl_betree.servantagent
data = {
    'Name': 'ServantHold',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 33,
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
                    'ID': 8,
                    'Class': 'WaitFrame',
                    'Frames': 75 },
                {
                    'ID': 24,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.ChooseHateTarget, (1, 0)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
