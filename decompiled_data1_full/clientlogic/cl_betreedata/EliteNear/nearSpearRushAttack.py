# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteNear/nearSpearRushAttack.pyc
# RelativePath: clientlogic/cl_betreedata/EliteNear/nearSpearRushAttack.pyc
# Source Generated with Decompyle++
# File: nearSpearRushAttack.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'nearSpearRushAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 97,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 14,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 16,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 18,
                    'Class': 'Parallel',
                    'Attachment': ({
                        'ID': 20,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'FailurePolicy': 0,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 15,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 21,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 22,
                                    'Class': 'WaitFrame',
                                    'Frames': 38 },
                                {
                                    'ID': 29,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 30,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 27,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 19,
                                                            'Class': 'DecoratorAlwaysRunning',
                                                            'DecorateWhenChildEnds': False,
                                                            'Node': [
                                                                {
                                                                    'ID': 24,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (4.5,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 25,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 129 }] },
                                                {
                                                    'ID': 26,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 28,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 10 }] }] }] }] }] }] }
