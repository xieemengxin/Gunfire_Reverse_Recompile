# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/stand.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/stand.pyc
# Source Generated with Decompyle++
# File: stand.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'stand',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 26,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 8,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 9,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetDirToLockEnemy, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 10,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceDir, (True,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 11,
                    'Class': 'WaitFrame',
                    'Frames': 45 }] }] }
