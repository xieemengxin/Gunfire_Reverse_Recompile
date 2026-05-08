# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DeviceTurret/LuWuSeekingAttack.pyc
# RelativePath: clientlogic/cl_betreedata/DeviceTurret/LuWuSeekingAttack.pyc
# Source Generated with Decompyle++
# File: LuWuSeekingAttack.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.GetLockEnemyHeightDis(oAgent) > 6


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.ChooseHateTarget(oAgent.GetData('HateMethod'), oAgent.GetConfig('HitRange'), oAgent)


def Func2(oAgent):
    return cl_betree.servantagent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.servantagent.CAgent.IsPerformUseArea(False, oAgent) == True

data = {
    'Name': 'LuWuSeekingAttack',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 17,
    'Node': [
        {
            'ID': 66,
            'Class': 'IfElse',
            'Node': [
                {
                    'ID': 54,
                    'Class': 'Condition',
                    'Method': (Func0, ()) },
                {
                    'ID': 50,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 61,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.ChooseOwnerAroundPos, (8, 12, 10, 30)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 52,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.MoveToPos, (2,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 45,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 31,
                            'Class': 'Action',
                            'Method': (Func1, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 6,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.ChooseAttack, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 57,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 0,
                            'ChildFinishPolicy': 1,
                            'Node': [
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
                                            'ID': 56,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.CatchLockEnemy, (5, 6)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 58,
                                    'Class': 'And',
                                    'Node': [
                                        {
                                            'ID': 59,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) },
                                        {
                                            'ID': 60,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) }] }] },
                        {
                            'ID': 35,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.FaceLockEnemy, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 36,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 67,
                                'Class': 'Precondition',
                                'Method': (cl_betree.servantagent.CAgent.StopMoving, ()),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' },),
                            'Method': (cl_betree.servantagent.CAgent.Attack, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 37,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.UpdateInAdvance, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
