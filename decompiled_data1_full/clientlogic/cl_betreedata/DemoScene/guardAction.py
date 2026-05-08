# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/guardAction.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/guardAction.pyc
# Source Generated with Decompyle++
# File: guardAction.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'guardAction',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 14,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseGuardPos, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.PlayGuardAct, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 9,
                    'Class': 'WaitFrame',
                    'Frames': (cl_betree.monsteragent.CAgent.GetGuardWaitTime, ()) },
                {
                    'ID': 17,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceDir, (True,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 19,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusAttack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 18,
                    'Class': 'WaitFrame',
                    'Frames': 12 },
                {
                    'ID': 14,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ClearCheckVal, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 20,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusDefault, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
