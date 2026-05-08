# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterSniper/combododge.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterSniper/combododge.pyc
# Source Generated with Decompyle++
# File: combododge.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 30

data = {
    'Name': 'combododge',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 31,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 8,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 9,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 7,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (8, 12, 75, 95)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 10,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (7, 10, 85, 150)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 6,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (2,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
