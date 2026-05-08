# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/bossattackmsg.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/bossattackmsg.pyc
# Source Generated with Decompyle++
# File: bossattackmsg.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'bossattackmsg',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 34,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ClearAgentEvent, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.AddEventDamHateVal, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.AddEventDamDodgeVal, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.AddEventAttDodgeVal, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 15,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusAttack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 30,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.AddState, (1042, 0)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 16,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 17,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 18,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'true')),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 19,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'false')),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
