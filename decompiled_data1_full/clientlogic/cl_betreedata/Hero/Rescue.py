# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Hero/Rescue.pyc
# RelativePath: clientlogic/cl_betreedata/Hero/Rescue.pyc
# Source Generated with Decompyle++
# File: Rescue.pyc (Python 3.6)

import cl_betree.heroagent
data = {
    'Name': 'Rescue',
    'ID': 0,
    'AgentType': 'cl_betree.heroagent',
    'IsFSM': False,
    'Ver': 31,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 39,
                    'Class': 'Action',
                    'Method': (cl_betree.heroagent.CAgent.ChooseRescueNearbyPos, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 41,
                    'Class': 'Action',
                    'Method': (cl_betree.heroagent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 40,
                    'Class': 'Action',
                    'Method': (cl_betree.heroagent.CAgent.MoveToPos, (3,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 22,
                    'Class': 'Action',
                    'Method': (cl_betree.heroagent.CAgent.RescueTeammate, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
