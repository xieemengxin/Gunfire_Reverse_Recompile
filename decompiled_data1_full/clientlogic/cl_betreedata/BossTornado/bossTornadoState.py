# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossTornado/bossTornadoState.pyc
# RelativePath: clientlogic/cl_betreedata/BossTornado/bossTornadoState.pyc
# Source Generated with Decompyle++
# File: bossTornadoState.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'bossTornadoState',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 5,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39153,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.RemoveState, (8116,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
