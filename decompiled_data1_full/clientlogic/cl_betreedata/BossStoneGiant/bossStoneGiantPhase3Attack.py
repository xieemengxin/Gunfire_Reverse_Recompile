# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossStoneGiant/bossStoneGiantPhase3Attack.pyc
# RelativePath: clientlogic/cl_betreedata/BossStoneGiant/bossStoneGiantPhase3Attack.pyc
# Source Generated with Decompyle++
# File: bossStoneGiantPhase3Attack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLastSucceededPF(oAgent) == 39095

data = {
    'Name': 'bossStoneGiantPhase3Attack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 6,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (0,)),
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
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 6,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 14,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 15,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 16,
                            'Class': 'Noop' },
                        {
                            'ID': 17,
                            'Class': 'WaitFrame',
                            'Frames': 25 }] }] }] }
