# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossLuoHou/bossLuoHouAttack2.pyc
# RelativePath: clientlogic/cl_betreedata/BossLuoHou/bossLuoHouAttack2.pyc
# Source Generated with Decompyle++
# File: bossLuoHouAttack2.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'bossLuoHouAttack2',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 18,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 17,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (50, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 16,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 23,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StateTransition, (8087,)),
                        'Phase': 2,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
