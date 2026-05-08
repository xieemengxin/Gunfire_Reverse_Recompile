# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/SpiderMove.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/SpiderMove.pyc
# Source Generated with Decompyle++
# File: SpiderMove.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 15

data = {
    'Name': 'SpiderMove',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 3,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusAttack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 12,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'DecoratorAlwaysRunning',
                    'DecorateWhenChildEnds': False,
                    'Node': [
                        {
                            'ID': 6,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 7,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 8,
                                            'Class': 'Condition',
                                            'Method': (Func0, ()) },
                                        {
                                            'ID': 9,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (5, 10, 1, 75)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 10,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (12, 6, 10, 120, 180)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 11,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
