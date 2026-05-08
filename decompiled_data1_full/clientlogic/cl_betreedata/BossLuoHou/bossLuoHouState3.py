# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossLuoHou/bossLuoHouState3.pyc
# RelativePath: clientlogic/cl_betreedata/BossLuoHou/bossLuoHouState3.pyc
# Source Generated with Decompyle++
# File: bossLuoHouState3.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == False

data = {
    'Name': 'bossLuoHouState3',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 28,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 11,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 12,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 10,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 13,
                            'Class': 'Noop' }] },
                {
                    'ID': 9,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.HaltPerform, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39122,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 6,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.RemoveState, (8087,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 14,
                    'Class': 'Selector',
                    'Node': [
                        {
                            'ID': 15,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39027,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 16,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39030,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 17,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
