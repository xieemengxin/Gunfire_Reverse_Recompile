# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumNear/dashNearAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumNear/dashNearAttack.pyc
# Source Generated with Decompyle++
# File: dashNearAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetCustomData('DashAfterChoosePFFlag', oAgent) == 1


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetCatchFrame(oAgent) >= 75


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 21341

data = {
    'Name': 'dashNearAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 162,
    'Node': [
        {
            'ID': 3,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 19,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 7,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 18,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 2,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 16,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 17,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetCustomData, ('DashAfterChoosePFFlag', 0)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 8,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 21,
                                        'Class': 'Effector',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'effector' },),
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 10,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 13,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ResetCatchStartFrame, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 24,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 25,
                                            'Class': 'Action',
                                            'Method': (Func1, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 26,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 27,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) },
                                                {
                                                    'ID': 28,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (21342,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 29,
                                                    'Class': 'False' }] }] },
                                {
                                    'ID': 31,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 32,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) },
                                        {
                                            'ID': 23,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 33,
                                            'Class': 'False' }] },
                                {
                                    'ID': 15,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (21342,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
