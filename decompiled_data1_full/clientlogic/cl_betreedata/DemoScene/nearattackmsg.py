# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/nearattackmsg.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/nearattackmsg.pyc
# Source Generated with Decompyle++
# File: nearattackmsg.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return oAgent.GetConfig('ShowCatchAni') == True

data = {
    'Name': 'nearattackmsg',
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
                    'ID': 19,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 20,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 21,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'false')),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 22,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'true')),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 23,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 24,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 25,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 1,
                            'ExitPolicy': 0,
                            'ChildFinishPolicy': 0,
                            'Node': [
                                {
                                    'ID': 27,
                                    'Class': 'WaitFrame',
                                    'Frames': 18 },
                                {
                                    'ID': 28,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 29,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 30,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetDirToLockEnemy, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 31,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (1, 'Guard', 'true')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 32,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FaceDir, (True,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 26,
                            'Class': 'Noop' }] },
                {
                    'ID': 8,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusAttack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
