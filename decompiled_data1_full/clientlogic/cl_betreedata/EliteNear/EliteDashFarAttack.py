# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteNear/EliteDashFarAttack.pyc
# RelativePath: clientlogic/cl_betreedata/EliteNear/EliteDashFarAttack.pyc
# Source Generated with Decompyle++
# File: EliteDashFarAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetCustomData('MonsterDashChoosePFFlag', oAgent) == 1

data = {
    'Name': 'EliteDashFarAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 26,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 14,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 19,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 22,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 20,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 4,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 18,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 6,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 7,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 8,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 10,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetCustomData, ('MonsterDashChoosePFFlag', 0)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 9,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 13,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (31342,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] },
                        {
                            'ID': 23,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetCustomData, ('CanChoosePF', 1)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
