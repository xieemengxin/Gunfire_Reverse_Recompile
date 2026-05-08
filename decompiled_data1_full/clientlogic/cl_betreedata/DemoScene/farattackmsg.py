# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/farattackmsg.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/farattackmsg.pyc
# Source Generated with Decompyle++
# File: farattackmsg.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return oAgent.GetConfig('ShowCatchAni') == True

data = {
    'Name': 'farattackmsg',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 30,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ClearAgentEvent, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.AddEventDamHateVal, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.AddEventDamDodgeVal, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.AddEventAttDodgeVal, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 20,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 21,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 24,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 1,
                            'ExitPolicy': 0,
                            'ChildFinishPolicy': 0,
                            'Node': [
                                {
                                    'ID': 25,
                                    'Class': 'WaitFrame',
                                    'Frames': 22 },
                                {
                                    'ID': 26,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 27,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 28,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetDirToLockEnemy, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 30,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (1, 'Guard', 'true')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 29,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FaceDir, (True,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 23,
                            'Class': 'Noop' }] },
                {
                    'ID': 15,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusAttack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 16,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 17,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 18,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'true')),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 19,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'false')),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
