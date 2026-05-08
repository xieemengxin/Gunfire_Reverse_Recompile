# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Common/GlobalApplyToken.pyc
# RelativePath: clientlogic/cl_betreedata/Common/GlobalApplyToken.pyc
# Source Generated with Decompyle++
# File: GlobalApplyToken.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.ApplyOccupyAttackToken(oAgent) == True

data = {
    'Name': 'GlobalApplyToken',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 5,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 4,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 3,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 5,
                            'Class': 'DecoratorAlwaysSuccess',
                            'DecorateWhenChildEnds': False },
                        {
                            'ID': 6,
                            'Class': 'DecoratorAlwaysFailure',
                            'DecorateWhenChildEnds': False }] }] }] }
