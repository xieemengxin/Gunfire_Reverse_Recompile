# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Servant/ServantDMAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Servant/ServantDMAttack.pyc
# Source Generated with Decompyle++
# File: ServantDMAttack.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.LockEnemyIsBoss(oAgent) == True


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.CheckLockTargetSID(3905, oAgent) == True

data = {
    'Name': 'ServantDMAttack',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 28,
    'Node': [
        {
            'ID': 2,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 25,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.HateAllMonster, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 1,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.ChooseHateTarget, (1, 0)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 23,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 12,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 11,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 17,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 18,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 4,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 8,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 3,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.GetTargetOffsetPos, (0, 0, -24.5, True, True)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 13,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (0.5,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 5,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.ChoosePFByArgs, (25,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 20,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 22,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 19,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.GetTargetOffsetPos, (0, 0, -16.3, True, True)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 24,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (0.5,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 21,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.ChoosePFByArgs, (15,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 15,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 16,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ChoosePF, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 14,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.MoveToLockEnemy, (4,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 26,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.StopMoving, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 7,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.FaceLockEnemy, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 10,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.Attack, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 27,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.UpdateInAdvance, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
