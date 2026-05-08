# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterNear/MonsterElectricGuerrillaAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterNear/MonsterElectricGuerrillaAttack.pyc
# Source Generated with Decompyle++
# File: MonsterElectricGuerrillaAttack.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'MonsterElectricGuerrillaAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 109,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Attachment': ({
                'ID': 35,
                'Class': 'Effector',
                'Method': (cl_betree.monsteragent.CAgent.SetFightLogicType, (1,)),
                'Phase': 1,
                'Flag': 'effector' }, {
                'ID': 34,
                'Class': 'Precondition',
                'Method': (cl_betree.monsteragent.CAgent.SetFightLogicType, (2,)),
                'Phase': 1,
                'Flag': 'precondition',
                'BinaryOperator': 'And' }),
            'Node': [
                {
                    'ID': 36,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 37,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (50, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 38,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 39,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 44,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.KeepMoving, (3,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 41,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
