# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterSelfExplosion/poisonExplosionAttackmsg.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterSelfExplosion/poisonExplosionAttackmsg.pyc
# Source Generated with Decompyle++
# File: poisonExplosionAttackmsg.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'poisonExplosionAttackmsg',
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
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.AddAttackEvents, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 9,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.AddState, (7050, 0)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 8,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusAttack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
