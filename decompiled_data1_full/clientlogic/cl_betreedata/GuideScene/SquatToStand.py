# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/GuideScene/SquatToStand.pyc
# RelativePath: clientlogic/cl_betreedata/GuideScene/SquatToStand.pyc
# Source Generated with Decompyle++
# File: SquatToStand.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'SquatToStand',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 40,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Squat', 'false')),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'WaitFrame',
                    'Frames': 100 },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.RemoveState, (7059,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
