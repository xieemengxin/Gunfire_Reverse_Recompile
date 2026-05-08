# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFlyable/FlyExplosionRushAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFlyable/FlyExplosionRushAttack.pyc
# Source Generated with Decompyle++
# File: FlyExplosionRushAttack.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'FlyExplosionRushAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 193,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 271,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseNearestHateTarget, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 302,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 206,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 311,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.MoveToFlyLockEnemy, (4, 0, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 280,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
