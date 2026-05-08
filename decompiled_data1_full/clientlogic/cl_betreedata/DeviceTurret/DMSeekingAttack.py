# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DeviceTurret/DMSeekingAttack.pyc
# RelativePath: clientlogic/cl_betreedata/DeviceTurret/DMSeekingAttack.pyc
# Source Generated with Decompyle++
# File: DMSeekingAttack.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.ChooseHateTarget(oAgent.GetConfig('HitRange'), 0, oAgent)


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.LockEnemyIsBoss(oAgent) == True


def Func2(oAgent):
    return cl_betree.servantagent.CAgent.CheckLockTargetSID(3905, oAgent) == True

data = {
    'Name': 'DMSeekingAttack',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 3,
    'Node': [
        {
            'ID': 45,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 31,
                    'Class': 'Action',
                    'Method': (Func0, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 6,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.ChooseAttack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 8,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 9,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 10,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 46,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 50,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 47,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 48,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) },
                                                {
                                                    'ID': 51,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.GetTargetOffsetPos, (0, 0, -24.5, True, True)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 53,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.GetTargetOffsetPos, (0, 0, -16.3, True, True)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 52,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.MoveToPos, (0.5,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 13,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.MoveToLockEnemy, (3,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 35,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 36,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.Attack, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 37,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.UpdateInAdvance, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
