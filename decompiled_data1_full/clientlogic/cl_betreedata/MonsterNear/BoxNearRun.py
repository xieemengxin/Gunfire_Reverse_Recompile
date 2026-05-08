# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterNear/BoxNearRun.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterNear/BoxNearRun.pyc
# Source Generated with Decompyle++
# File: BoxNearRun.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'BoxNearRun',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 204,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseTargetAwayPos, (20, 90, 10, 0.5)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 6,
                    'Class': 'WaitFrame',
                    'Frames': 25 }] }] }
