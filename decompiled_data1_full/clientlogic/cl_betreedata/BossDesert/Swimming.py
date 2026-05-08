# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossDesert/Swimming.pyc
# RelativePath: clientlogic/cl_betreedata/BossDesert/Swimming.pyc
# Source Generated with Decompyle++
# File: Swimming.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return oAgent.GetConfig('GuerrillaInterval')


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsGroupAllDie(3, oAgent) == True

data = {
    'Name': 'Swimming',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 144,
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
                    'ID': 151,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 6,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusAttack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 156,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 164,
                            'Class': 'WaitFrame',
                            'Frames': (Func0, ()) },
                        {
                            'ID': 166,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 165,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 167,
                                    'Class': 'WaitFrame',
                                    'Frames': 15 }] }] },
                {
                    'ID': 157,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 159,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChoosePosFarAwayFromEnemy, (18,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 161,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.FlashToPos, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 155,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.CheckStateChange, ('zuanchu',)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
