# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Hero/FarStandAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Hero/FarStandAttack.pyc
# Source Generated with Decompyle++
# File: FarStandAttack.pyc (Python 3.6)

import cl_betree.heroagent
data = {
    'Name': 'FarStandAttack',
    'ID': 0,
    'AgentType': 'cl_betree.heroagent',
    'IsFSM': False,
    'Ver': 33,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 41,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 0,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 42,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 44,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.ChooseTarget, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 49,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.FaceTarget, (0,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 45,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 43,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 46,
                                    'Class': 'Action',
                                    'Method': (cl_betree.heroagent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 47,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 48,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.heroagent.CAgent.ChooseLeaderPos, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.heroagent.CAgent.MoveToPos, (6,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
