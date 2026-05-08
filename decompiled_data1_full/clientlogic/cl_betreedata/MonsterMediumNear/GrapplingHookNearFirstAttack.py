# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumNear/GrapplingHookNearFirstAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumNear/GrapplingHookNearFirstAttack.pyc
# Source Generated with Decompyle++
# File: GrapplingHookNearFirstAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 17

data = {
    'Name': 'GrapplingHookNearFirstAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 95,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 30,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 84,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 79,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 83,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetPhase, (2,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 85,
                            'Class': 'Parallel',
                            'FailurePolicy': 0,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 0,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 86,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 0,
                                    'SuccessPolicy': 1,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 87,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 88,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (4.5,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 25,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 14,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 32,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 15,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 36,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UpdateInAdvance, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
