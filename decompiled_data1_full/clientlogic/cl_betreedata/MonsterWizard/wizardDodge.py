# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterWizard/wizardDodge.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterWizard/wizardDodge.pyc
# Source Generated with Decompyle++
# File: wizardDodge.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'wizardDodge',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 32,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 9,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.HaltPerform, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 6,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 13,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 14,
                        'Class': 'Effector',
                        'Method': (cl_betree.monsteragent.CAgent.UseMovePosAsSkillEnd, ()),
                        'Phase': 1,
                        'Flag': 'effector' },),
                    'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (6, 10, 150, 180)),
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
                    'ResultFunctor': None },
                {
                    'ID': 8,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.RemoveState, (7089,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
