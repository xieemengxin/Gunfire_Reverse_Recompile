# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFar/guerrilla.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFar/guerrilla.pyc
# Source Generated with Decompyle++
# File: guerrilla.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)

data = {
    'Name': 'guerrilla',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 144,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (Func0, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 11,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
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
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 7,
                    'Class': 'WaitFrame',
                    'Frames': (cl_betree.monsteragent.CAgent.GetGuerrillaInterval, ()) }] }] }
