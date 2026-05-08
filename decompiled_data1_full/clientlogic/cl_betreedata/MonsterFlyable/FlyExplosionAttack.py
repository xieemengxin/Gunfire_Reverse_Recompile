# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFlyable/FlyExplosionAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFlyable/FlyExplosionAttack.pyc
# Source Generated with Decompyle++
# File: FlyExplosionAttack.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'FlyExplosionAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 207,
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
                    'ID': 311,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 288,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 307,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ZigFlyToLockTarget, (18, 2, 30, 2, 4)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 313,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (22253,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 314,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 315,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 304,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetPhase, (2,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
