# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DeviceTurret/Attack.pyc
# RelativePath: clientlogic/cl_betreedata/DeviceTurret/Attack.pyc
# Source Generated with Decompyle++
# File: Attack.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.ChooseSeeEnemy(oAgent.GetData('HateMethod'), oAgent.GetConfig('HitRange'), oAgent)


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'Attack',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 35,
    'Node': [
        {
            'ID': 6,
            'Class': 'Parallel',
            'FailurePolicy': 1,
            'SuccessPolicy': 1,
            'ExitPolicy': 0,
            'ChildFinishPolicy': 1,
            'Node': [
                {
                    'ID': 15,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.FlashToPos, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 1,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 8,
                            'Class': 'Action',
                            'Method': (Func0, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 2,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.ChooseAttack, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 18,
                            'Class': 'Condition',
                            'Method': (Func1, ()) },
                        {
                            'ID': 11,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.FaceLockEnemy, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 3,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.Attack, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 9,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.UpdateInAdvance, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
