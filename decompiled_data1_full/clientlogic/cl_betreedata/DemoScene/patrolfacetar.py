# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/patrolfacetar.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/patrolfacetar.pyc
# Source Generated with Decompyle++
# File: patrolfacetar.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'patrolfacetar',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 9,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 7,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 6,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.KeepMoving, (5,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
