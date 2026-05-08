# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossSeaMonster/bossSeaMonsterpatrolmove.pyc
# RelativePath: clientlogic/cl_betreedata/BossSeaMonster/bossSeaMonsterpatrolmove.pyc
# Source Generated with Decompyle++
# File: bossSeaMonsterpatrolmove.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'bossSeaMonsterpatrolmove',
    'ID': 0,
    'AgentType': '',
    'IsFSM': False,
    'Ver': 3,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusDefault, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 6,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.HaltPerform, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 9,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.AbsoluteArcMove, (60, 10, 60, 250)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
