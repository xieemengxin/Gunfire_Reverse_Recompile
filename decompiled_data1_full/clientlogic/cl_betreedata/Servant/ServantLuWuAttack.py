# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Servant/ServantLuWuAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Servant/ServantLuWuAttack.pyc
# Source Generated with Decompyle++
# File: ServantLuWuAttack.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.GetLockEnemyHeightDis(oAgent) > 6


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'ServantLuWuAttack',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 72,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 28,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.ChooseHateTarget, (1, 0)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 45,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 46,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.ChoosePF, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 59,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 58,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 60,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 61,
                                            'Class': 'Condition',
                                            'Method': (Func0, ()) },
                                        {
                                            'ID': 72,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 65,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.ChooseCertainPF, (7143,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 71,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 64,
                                                            'Class': 'Condition',
                                                            'Method': (Func1, ()) },
                                                        {
                                                            'ID': 66,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 69,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.servantagent.CAgent.ChooseOwnerAroundPos, (6, 10, 0, 180)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 70,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (1,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] },
                                        {
                                            'ID': 63,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 67,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.CatchLockEnemy, (4, 6)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 68,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.ChoosePF, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] }] },
                {
                    'ID': 7,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 40,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.servantagent.CAgent.Attack, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 39,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.UpdateInAdvance, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
