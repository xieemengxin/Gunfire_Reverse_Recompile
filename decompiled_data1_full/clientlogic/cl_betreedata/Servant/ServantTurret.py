# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Servant/ServantTurret.pyc
# RelativePath: clientlogic/cl_betreedata/Servant/ServantTurret.pyc
# Source Generated with Decompyle++
# File: ServantTurret.pyc (Python 3.6)

import cl_betree.servantagent
data = {
    'Name': 'ServantTurret',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 13,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 6,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.ChooseSeeEnemy, (1, 40)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.FaceLockEnemy, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.ChoosePF, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.Attack, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 7,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.UpdateInAdvance, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
