# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Servant/ServantSeaAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Servant/ServantSeaAttack.pyc
# Source Generated with Decompyle++
# File: ServantSeaAttack.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.LockEnemyIsBoss(oAgent) == True

data = {
    'Name': 'ServantSeaAttack',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 101,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 46,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 0,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 47,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.ChooseEnemyBySceneObj, (True, '', True)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 48,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 54,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 51,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ChooseOwnerAroundPos, (6, 10, 0, 180)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 50,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 59,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 58,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 60,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 57,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ChoosePFByMonsterSkill, (4.5,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 56,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.FaceSkillEndPos, (1080,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 61,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 62,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ChoosePF, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 63,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.FaceLockEnemy, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
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
