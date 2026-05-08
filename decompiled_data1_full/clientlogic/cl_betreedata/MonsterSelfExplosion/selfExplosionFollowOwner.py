# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterSelfExplosion/selfExplosionFollowOwner.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterSelfExplosion/selfExplosionFollowOwner.pyc
# Source Generated with Decompyle++
# File: selfExplosionFollowOwner.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'selfExplosionFollowOwner',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 36,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 11,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 8,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 9,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.GetMonsterOwnerPos, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 10,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
