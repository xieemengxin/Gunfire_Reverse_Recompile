# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteNear/EliteDashNearAttack.pyc
# RelativePath: clientlogic/cl_betreedata/EliteNear/EliteDashNearAttack.pyc
# Source Generated with Decompyle++
# File: EliteDashNearAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetCustomData('MonsterDashChoosePFFlag', oAgent) == 1

data = {
    'Name': 'EliteDashNearAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 186,
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
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 24,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 26,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 25,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 8,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 23,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 18,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 2,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 16,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 17,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetCustomData, ('MonsterDashChoosePFFlag', 0)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 10,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 15,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (31342,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] },
                        {
                            'ID': 27,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetCustomData, ('CanChoosePF', 1)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
