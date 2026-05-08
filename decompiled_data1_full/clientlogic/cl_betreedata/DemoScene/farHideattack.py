# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/farHideattack.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/farHideattack.pyc
# Source Generated with Decompyle++
# File: farHideattack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == True


def Func2(oAgent):
    return oAgent.GetConfig('HideAttackStandingTime')

data = {
    'Name': 'farHideattack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 38,
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
                    'ID': 17,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetMoveStatusRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 32,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 43,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 38,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusAttack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 60,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 62,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 63,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 64,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 65,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 67,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHorizontalPos, (2, 3)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 68,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 69,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 70,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 71,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 72,
                            'Class': 'WaitFrame',
                            'Frames': (Func2, ()) }] }] }] }
