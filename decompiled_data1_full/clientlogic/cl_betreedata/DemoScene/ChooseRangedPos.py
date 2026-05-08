# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/ChooseRangedPos.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/ChooseRangedPos.pyc
# Source Generated with Decompyle++
# File: ChooseRangedPos.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'ChooseRangedPos',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 37,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 60,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 61,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 62,
                            'Class': 'Noop' },
                        {
                            'ID': 63,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 58,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (10, 4, 7, 75, 105)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 59,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
