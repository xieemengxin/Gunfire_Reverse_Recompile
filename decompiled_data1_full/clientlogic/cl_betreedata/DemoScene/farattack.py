# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/farattack.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/farattack.pyc
# Source Generated with Decompyle++
# File: farattack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == True

data = {
    'Name': 'farattack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 9,
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
                    'ID': 6,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 8,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 11,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 10,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 12,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 13,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHorizontalPos, (2, 3)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 15,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 14,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 16,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
