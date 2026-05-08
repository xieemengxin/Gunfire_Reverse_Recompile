# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFlyable/FlyToShowPos.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFlyable/FlyToShowPos.pyc
# Source Generated with Decompyle++
# File: FlyToShowPos.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckArriveShowPos(oAgent) == False

data = {
    'Name': 'FlyToShowPos',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 24,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 28,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetCustomData, ('ScriptCtrlFlyToPos', 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 2,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 3,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 15,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 6,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseShowPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 10,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 0,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 0,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 22,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 24,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 26,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 9,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FlyToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 19,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 12,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 500 },
                                                {
                                                    'ID': 21,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FlashToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 27,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.AddState, (8094, 0)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 18,
                            'Class': 'Noop' }] }] }] }
