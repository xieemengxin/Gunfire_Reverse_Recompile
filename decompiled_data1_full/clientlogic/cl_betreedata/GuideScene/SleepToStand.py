# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/GuideScene/SleepToStand.pyc
# RelativePath: clientlogic/cl_betreedata/GuideScene/SleepToStand.pyc
# Source Generated with Decompyle++
# File: SleepToStand.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'SleepToStand',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 39,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sleep', 'false')),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'WaitFrame',
                    'Frames': 125 },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.RemoveState, (7059,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
