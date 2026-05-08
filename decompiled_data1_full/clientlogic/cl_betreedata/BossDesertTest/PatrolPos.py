# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossDesertTest/PatrolPos.pyc
# RelativePath: clientlogic/cl_betreedata/BossDesertTest/PatrolPos.pyc
# Source Generated with Decompyle++
# File: PatrolPos.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'PatrolPos',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 19,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetPatrolPos, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 11,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 10,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 6,
                    'Class': 'WaitFrame',
                    'Frames': 10 }] }] }
