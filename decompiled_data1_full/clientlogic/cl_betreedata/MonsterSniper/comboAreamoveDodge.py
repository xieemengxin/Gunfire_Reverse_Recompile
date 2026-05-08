# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterSniper/comboAreamoveDodge.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterSniper/comboAreamoveDodge.pyc
# Source Generated with Decompyle++
# File: comboAreamoveDodge.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 15

data = {
    'Name': 'comboAreamoveDodge',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 33,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 12,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 13,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 14,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (5, 7, 80, 100)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 15,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (5, 7, 85, 105)),
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
