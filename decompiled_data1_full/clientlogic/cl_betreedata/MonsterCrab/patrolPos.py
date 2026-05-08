# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterCrab/patrolPos.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterCrab/patrolPos.pyc
# Source Generated with Decompyle++
# File: patrolPos.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'patrolPos',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 17,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'IsWarning', 'false')),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetPatrolPos, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 9,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceCrossPath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMPatrol, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 6,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 7,
                        'Class': 'Effector',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 3,
                        'Flag': 'effector' },),
                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 8,
                    'Class': 'WaitFrame',
                    'Frames': 150 }] }] }
