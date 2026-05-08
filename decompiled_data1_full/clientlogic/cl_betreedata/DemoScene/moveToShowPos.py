# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/moveToShowPos.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/moveToShowPos.pyc
# Source Generated with Decompyle++
# File: moveToShowPos.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'moveToShowPos',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 10,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseShowPos, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 5,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 6,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'false')),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 7,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'true')),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
