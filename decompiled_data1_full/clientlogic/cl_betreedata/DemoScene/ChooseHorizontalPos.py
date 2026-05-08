# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/ChooseHorizontalPos.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/ChooseHorizontalPos.pyc
# Source Generated with Decompyle++
# File: ChooseHorizontalPos.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == True

data = {
    'Name': 'ChooseHorizontalPos',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 34,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 63,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 64,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 66,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 61,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHorizontalPos, (2, 3)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 62,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 65,
                            'Class': 'Noop' }] }] }] }
