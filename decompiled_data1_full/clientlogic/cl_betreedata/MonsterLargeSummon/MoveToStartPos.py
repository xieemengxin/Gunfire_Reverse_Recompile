# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterLargeSummon/MoveToStartPos.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterLargeSummon/MoveToStartPos.pyc
# Source Generated with Decompyle++
# File: MoveToStartPos.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'MoveToStartPos',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 16,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 6,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.CurveFlyToPos, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
