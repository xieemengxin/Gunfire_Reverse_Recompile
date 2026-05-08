# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterLargeSummon/LargeSummonChangePhase.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterLargeSummon/LargeSummonChangePhase.pyc
# Source Generated with Decompyle++
# File: LargeSummonChangePhase.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'LargeSummonChangePhase',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 96,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 267,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseAreaConfigPos, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 219,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 266,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.RemoveState, (7115,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 268,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 0,
                    'Node': [
                        {
                            'ID': 225,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.FlyToPos, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 269,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 252,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (24011,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 265,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
