# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossDesert/ShowAttack.pyc
# RelativePath: clientlogic/cl_betreedata/BossDesert/ShowAttack.pyc
# Source Generated with Decompyle++
# File: ShowAttack.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'ShowAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 133,
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
                    'ID': 149,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 150,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 151,
                    'Class': 'WaitFrame',
                    'Frames': 10 }] }] }
