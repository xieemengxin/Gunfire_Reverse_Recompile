# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossTornado/bossTornadoFlash.pyc
# RelativePath: clientlogic/cl_betreedata/BossTornado/bossTornadoFlash.pyc
# Source Generated with Decompyle++
# File: bossTornadoFlash.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(7957, oAgent) == True

data = {
    'Name': 'bossTornadoFlash',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 10,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 16,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 17,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 18,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39161,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 19,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39160,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
