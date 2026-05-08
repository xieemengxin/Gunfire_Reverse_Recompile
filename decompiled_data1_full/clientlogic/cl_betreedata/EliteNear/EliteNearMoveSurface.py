# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteNear/EliteNearMoveSurface.pyc
# RelativePath: clientlogic/cl_betreedata/EliteNear/EliteNearMoveSurface.pyc
# Source Generated with Decompyle++
# File: EliteNearMoveSurface.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 3

data = {
    'Name': 'EliteNearMoveSurface',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 16,
    'Node': [
        {
            'ID': 12,
            'Class': 'IfElse',
            'Node': [
                {
                    'ID': 11,
                    'Class': 'Condition',
                    'Method': (Func0, ()) },
                {
                    'ID': 1,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 10,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.UseCertainPFToPos, (31840, 0, 0, 0)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 13,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetPhase, (4,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 14,
                    'Class': 'Noop' }] }] }
