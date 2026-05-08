# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/guardpatrol.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/guardpatrol.pyc
# Source Generated with Decompyle++
# File: guardpatrol.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'guardpatrol',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 19,
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
                    'ID': 16,
                    'Class': 'WaitFrame',
                    'Frames': (cl_betree.monsteragent.CAgent.GetGuardWaitTime, ()) },
                {
                    'ID': 17,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceDir, (True,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 9,
                    'Class': 'WaitFrame',
                    'Frames': 4 },
                {
                    'ID': 10,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetMoveStatusWalk, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 15,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 12,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 13,
                    'Class': 'WaitFrame',
                    'Frames': 30 },
                {
                    'ID': 14,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ClearCheckVal, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
