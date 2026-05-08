# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DeviceTurret/SeekingAttack.pyc
# RelativePath: clientlogic/cl_betreedata/DeviceTurret/SeekingAttack.pyc
# Source Generated with Decompyle++
# File: SeekingAttack.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.ChooseHateTarget(1, oAgent.GetConfig('HitRange'), oAgent)


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.IsPerformUseArea(False, oAgent) == True


def Func2(oAgent):
    return cl_betree.servantagent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.servantagent.CAgent.IsLockEnemyPosAccessible(oAgent) == True

data = {
    'Name': 'SeekingAttack',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 47,
    'Node': [
        {
            'ID': 44,
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
                    'ID': 41,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 0,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 40,
                            'Class': 'And',
                            'Node': [
                                {
                                    'ID': 7,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 30,
                                    'Class': 'Condition',
                                    'Method': (Func2, ()) }] },
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
                                            'ID': 11,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) },
                                        {
                                            'ID': 13,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.MoveToLockEnemy, (5,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 12,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 18,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.ChooseLockTargetNearestSpace, (False,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 17,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (5,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] }] },
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
                        'ID': 45,
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
                    'ResultFunctor': None }] }] }
