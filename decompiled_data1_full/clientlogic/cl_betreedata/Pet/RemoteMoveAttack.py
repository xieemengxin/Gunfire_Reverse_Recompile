# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Pet/RemoteMoveAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Pet/RemoteMoveAttack.pyc
# Source Generated with Decompyle++
# File: RemoteMoveAttack.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.CalFrameOwnerOutSight(70, oAgent) > 75


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.ChoosePF(oAgent) == 1


def Func2(oAgent):
    return cl_betree.servantagent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.servantagent.CAgent.IsPerformUseArea('', oAgent) == True


def Func4(oAgent):
    return cl_betree.servantagent.CAgent.ChooseAttackTarget(oAgent.GetData('MinPerformUseDis'), True, oAgent) == 1


def Func5(oAgent):
    return cl_betree.servantagent.CAgent.IsLockEnemyPosAccessible(oAgent) == False


def Func6(oAgent):
    return cl_betree.servantagent.CAgent.ChooseLockTargetNearestSpace(False, oAgent) == 1


def Func7(oAgent):
    return cl_betree.servantagent.CAgent.GetOwnerToLockEnemyDis(oAgent) < oAgent.GetData('MinPerformUseDis')


def Func8(oAgent):
    return cl_betree.servantagent.CAgent.GetLockEnemyDis(oAgent) >= 7


def Func9(oAgent):
    return cl_betree.servantagent.CAgent.GetLockEnemyDis(oAgent) < 7


def Func10(oAgent):
    return cl_betree.servantagent.CAgent.ChooseAttackTarget(oAgent.GetData('MinPerformUseDis'), True, oAgent)


def Func11(oAgent):
    return cl_betree.servantagent.CAgent.IsPerformUseArea('', oAgent) == True

data = {
    'Name': 'RemoteMoveAttack',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 144,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 113,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.SetActionSM, (3,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 186,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.SetFightStatus, (2,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 239,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 240,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 250,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 251,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ChooseOwnerAroundPos, (0, 6, 10, 180)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 252,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.FlashToPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 253,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ClearTimeAtOwnerOutSight, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 254,
                            'Class': 'Noop' }] },
                {
                    'ID': 99,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.ChooseAttackTarget, (0, '')),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 159,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 160,
                            'Class': 'Condition',
                            'Method': (Func1, ()) },
                        {
                            'ID': 161,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 0,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 175,
                                    'Class': 'And',
                                    'Node': [
                                        {
                                            'ID': 176,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) },
                                        {
                                            'ID': 177,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) }] },
                                {
                                    'ID': 178,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 182,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 183,
                                                    'Class': 'Condition',
                                                    'Method': (Func4, ()) },
                                                {
                                                    'ID': 184,
                                                    'Class': 'Noop' },
                                                {
                                                    'ID': 185,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.ChooseAttackTarget, (0, False)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 181,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 223,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 224,
                                                    'Class': 'Condition',
                                                    'Method': (Func5, ()) },
                                                {
                                                    'ID': 227,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 228,
                                                            'Class': 'Condition',
                                                            'Method': (Func6, ()) },
                                                        {
                                                            'ID': 229,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.servantagent.CAgent.MoveToPos, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 230,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 231,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.servantagent.CAgent.ChooseOwnerAroundPos, (0, 6, 0, 60)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 232,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 238,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (1,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] },
                                                {
                                                    'ID': 226,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.MoveToLockEnemy, (2,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] },
                        {
                            'ID': 187,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 188,
                                    'Class': 'Condition',
                                    'Method': (Func7, ()) },
                                {
                                    'ID': 202,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 203,
                                            'Class': 'Condition',
                                            'Method': (Func8, ()) },
                                        {
                                            'ID': 204,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 0,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 205,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 207,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.servantagent.CAgent.ChooseOwnerAroundPos, (0, 6, 0, 60)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 208,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 217,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 0,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 219,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 220,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func9, ()) },
                                                                        {
                                                                            'ID': 221,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.servantagent.CAgent.StopMoving, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] },
                                                                {
                                                                    'ID': 222,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (1,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] },
                                                {
                                                    'ID': 206,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 210,
                                                            'Class': 'Action',
                                                            'Method': (Func10, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 211,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.servantagent.CAgent.ChoosePF, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 212,
                                                            'Class': 'Condition',
                                                            'Method': (Func11, ()) }] }] },
                                        {
                                            'ID': 213,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 214,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.ChooseRangedPos, (5, 1, 5, 90, 180)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 215,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 216,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (1,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 198,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 199,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.ChooseHateFlankPos, (2, 5, 0, 180)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 200,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 201,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.MoveToPos, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] }] },
                {
                    'ID': 142,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 255,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 0,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 143,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.Attack, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 256,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 257,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ChooseHateFlankPos, (2, 5, 0, 180)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 258,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 259,
                                    'Class': 'WaitFrame',
                                    'Frames': 50 }] }] },
                {
                    'ID': 107,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.UpdateInAdvance, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
