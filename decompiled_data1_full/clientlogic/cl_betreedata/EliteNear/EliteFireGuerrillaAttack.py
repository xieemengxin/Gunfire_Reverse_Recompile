# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteNear/EliteFireGuerrillaAttack.pyc
# RelativePath: clientlogic/cl_betreedata/EliteNear/EliteFireGuerrillaAttack.pyc
# Source Generated with Decompyle++
# File: EliteFireGuerrillaAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) > 12

data = {
    'Name': 'EliteFireGuerrillaAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 118,
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
                    'ID': 45,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 46,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 52,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 47,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 49,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 50,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 51,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (10,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 53,
                                    'Class': 'WaitFrame',
                                    'Frames': 500 }] },
                        {
                            'ID': 48,
                            'Class': 'Noop' }] },
                {
                    'ID': 37,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 54,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
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
