# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumNear/MonsterSharkSurface.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumNear/MonsterSharkSurface.pyc
# Source Generated with Decompyle++
# File: MonsterSharkSurface.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(33586, oAgent) == True

data = {
    'Name': 'MonsterSharkSurface',
    'ID': 0,
    'AgentType': '',
    'IsFSM': False,
    'Ver': 92,
    'Node': [
        {
            'ID': 234,
            'Class': 'IfElse',
            'Node': [
                {
                    'ID': 235,
                    'Class': 'Condition',
                    'Method': (Func0, ()) },
                {
                    'ID': 1,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 237,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.RemoveState, (33586,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 238,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.UseCertainPFToPos, (21338, 0, 0, 0)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 236,
                    'Class': 'Noop' }] }] }
