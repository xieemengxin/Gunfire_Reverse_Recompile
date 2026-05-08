# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFlyable/FlyableIllusion.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFlyable/FlyableIllusion.pyc
# Source Generated with Decompyle++
# File: FlyableIllusion.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckArriveShowPos(oAgent) == False


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetCustomData('ScriptCtrlFlyToPos', oAgent) == 1


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.ChoosePsychTarget(30, oAgent) == 1


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'FlyableIllusion',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 7,
    'Node': [
        {
            'ID': 10,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 11,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 12,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 13,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 14,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseShowPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 15,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 16,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 17,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 18,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 22,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FlyToPos, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 20,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 21,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.AddState, (8094, 0)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 1,
                            'Class': 'Parallel',
                            'FailurePolicy': 0,
                            'SuccessPolicy': 1,
                            'ExitPolicy': 0,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 2,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 3,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) },
                                        {
                                            'ID': 4,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (20432,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 5,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (0, 0)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 9,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) },
                                        {
                                            'ID': 6,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 7,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 8,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToFlyLockEnemy, (6, 5, 10)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] }] }] }] }
