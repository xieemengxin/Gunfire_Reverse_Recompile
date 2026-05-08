# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossStoneGiant/bossStoneGiantPhase3.pyc
# RelativePath: clientlogic/cl_betreedata/BossStoneGiant/bossStoneGiantPhase3.pyc
# Source Generated with Decompyle++
# File: bossStoneGiantPhase3.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLastSucceededPF(oAgent) == 39095

data = {
    'Name': 'bossStoneGiantPhase3',
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
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFaceMapCenterDir, (-10, -1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceDir, (True,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 10,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 11,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 12,
                            'Class': 'Noop' },
                        {
                            'ID': 13,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 5,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39095,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 6,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 9,
                                    'Class': 'WaitFrame',
                                    'Frames': 15 }] }] }] }] }
