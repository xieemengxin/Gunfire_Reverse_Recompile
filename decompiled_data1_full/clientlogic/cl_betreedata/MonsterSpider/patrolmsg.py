# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterSpider/patrolmsg.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterSpider/patrolmsg.pyc
# Source Generated with Decompyle++
# File: patrolmsg.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'patrolmsg',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 11,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 20,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ClearCheckVal, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.AddPatrolEvents, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 22,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.BornAction, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 21,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMPatrol, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
