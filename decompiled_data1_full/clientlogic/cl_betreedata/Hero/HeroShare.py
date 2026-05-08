# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Hero/HeroShare.pyc
# RelativePath: clientlogic/cl_betreedata/Hero/HeroShare.pyc
# Source Generated with Decompyle++
# File: HeroShare.pyc (Python 3.6)

import cl_betree.heroagent

def Func0(oAgent):
    return cl_betree.heroagent.CAgent.CheckHideDoorObstacle(oAgent) == True

data = {
    'Name': 'HeroShare',
    'ID': 0,
    'AgentType': 'cl_betree.heroagent',
    'IsFSM': False,
    'Ver': 94,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Attachment': ({
                'ID': 101,
                'Class': 'Effector',
                'Method': (cl_betree.heroagent.CAgent.CancelLockTarget, ()),
                'Phase': 3,
                'Flag': 'effector' },),
            'Node': [
                {
                    'ID': 86,
                    'Class': 'Action',
                    'Method': (cl_betree.heroagent.CAgent.LockShareItem, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 76,
                    'Class': 'Action',
                    'Method': (cl_betree.heroagent.CAgent.FaceTarget, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 69,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 70,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 71,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 74,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 88,
                                        'Class': 'Effector',
                                        'Method': (cl_betree.heroagent.CAgent.RestoreCurWeaponAccuracyRate, (1,)),
                                        'Phase': 1,
                                        'Flag': 'effector' }, {
                                        'ID': 87,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.heroagent.CAgent.SetCurWeaponAccuracyRate, (100, 1)),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' }),
                                    'Method': (cl_betree.heroagent.CAgent.AttackOnce, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 79,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.GetHideDoorNpc, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 78,
                            'Class': 'Noop' }] },
                {
                    'ID': 67,
                    'Class': 'Action',
                    'Method': (cl_betree.heroagent.CAgent.AdddShareItemSignal, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
