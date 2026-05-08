# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossLuoHou/bossLuoHouState1.pyc
# RelativePath: clientlogic/cl_betreedata/BossLuoHou/bossLuoHouState1.pyc
# Source Generated with Decompyle++
# File: bossLuoHouState1.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'bossLuoHouState1',
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
                    'ID': 8,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.HaltPerform, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (1, 'S1toS2', '')),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 2,
                    'Class': 'WaitFrame',
                    'Frames': 150 },
                {
                    'ID': 4,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 5,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetFaceDir, (0, 1)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 6,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.FaceDir, (True,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 7,
                            'Class': 'WaitFrame',
                            'Frames': 25 }] }] }] }
