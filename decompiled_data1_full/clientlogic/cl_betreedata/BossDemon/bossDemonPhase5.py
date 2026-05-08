# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossDemon/bossDemonPhase5.pyc
# RelativePath: clientlogic/cl_betreedata/BossDemon/bossDemonPhase5.pyc
# Source Generated with Decompyle++
# File: bossDemonPhase5.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'bossDemonPhase5',
    'ID': 0,
    'AgentType': '',
    'IsFSM': False,
    'Ver': 11,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 6,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 0,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 7,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 8,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 13,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 14,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.HateAllPlayer, ()),
                                        'Phase': 3,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateHero, (0,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 9,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39248,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 10,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 11,
                                    'Class': 'WaitFrame',
                                    'Frames': 40000 }] }] }] }] }
