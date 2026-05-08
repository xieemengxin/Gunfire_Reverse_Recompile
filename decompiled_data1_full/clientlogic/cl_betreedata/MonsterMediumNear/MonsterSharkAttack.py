# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumNear/MonsterSharkAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumNear/MonsterSharkAttack.pyc
# Source Generated with Decompyle++
# File: MonsterSharkAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLastSucceededPF(oAgent) == 21337


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsLockEnemyPosAccessible(oAgent) == False


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformShotType(1, oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetCatchFrame(oAgent) >= 175


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 10


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 15


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetRandom(0, 99, oAgent) <= 50


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformShotType(3, oAgent) == True


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func11(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func12(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)

data = {
    'Name': 'MonsterSharkAttack',
    'ID': 0,
    'AgentType': '',
    'IsFSM': False,
    'Ver': 91,
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
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 234,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 235,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 236,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (21331,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 75,
                            'Class': 'DecoratorAlwaysSuccess',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 233,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 85,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 0,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 104,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 105,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 124,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseShotPF, (3,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 107,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 108,
                                            'Class': 'And',
                                            'Node': [
                                                {
                                                    'ID': 111,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) },
                                                {
                                                    'ID': 179,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) }] },
                                        {
                                            'ID': 109,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 123,
                                                    'Class': 'Condition',
                                                    'Method': (Func4, ()) },
                                                {
                                                    'ID': 114,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 121,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseShotPF, (3,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 115,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 122,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseShotPF, (2,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] },
                                        {
                                            'ID': 168,
                                            'Class': 'DecoratorAlwaysFailure',
                                            'DecorateWhenChildEnds': False,
                                            'Node': [
                                                {
                                                    'ID': 169,
                                                    'Class': 'Noop' }] }] }] },
                        {
                            'ID': 209,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 184,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 185,
                                            'Class': 'And',
                                            'Node': [
                                                {
                                                    'ID': 188,
                                                    'Class': 'Condition',
                                                    'Method': (Func5, ()) },
                                                {
                                                    'ID': 189,
                                                    'Class': 'Condition',
                                                    'Method': (Func6, ()) }] },
                                        {
                                            'ID': 220,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 0,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 221,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 223,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 224,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 225,
                                                                'Class': 'Precondition',
                                                                'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
                                                                'Phase': 2,
                                                                'Flag': 'precondition',
                                                                'BinaryOperator': 'And' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.KeepMoving, (8,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 222,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 40 }] },
                                        {
                                            'ID': 226,
                                            'Class': 'Noop' }] },
                                {
                                    'ID': 211,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 212,
                                            'Class': 'Condition',
                                            'Method': (Func7, ()) },
                                        {
                                            'ID': 213,
                                            'Class': 'Noop' },
                                        {
                                            'ID': 214,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 215,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 217,
                                                    'Class': 'Action',
                                                    'Attachment': ({
                                                        'ID': 219,
                                                        'Class': 'Precondition',
                                                        'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                        'Phase': 2,
                                                        'Flag': 'precondition',
                                                        'BinaryOperator': 'And' },),
                                                    'Method': (Func8, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] }] },
                {
                    'ID': 7,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 13,
                            'Class': 'Condition',
                            'Method': (Func9, ()) },
                        {
                            'ID': 144,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 161,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 232,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 145,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 146,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 148,
                                                    'Class': 'Condition',
                                                    'Method': (Func10, ()) },
                                                {
                                                    'ID': 172,
                                                    'Class': 'Condition',
                                                    'Method': (Func11, ()) },
                                                {
                                                    'ID': 149,
                                                    'Class': 'Action',
                                                    'Attachment': ({
                                                        'ID': 170,
                                                        'Class': 'Precondition',
                                                        'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
                                                        'Phase': 2,
                                                        'Flag': 'precondition',
                                                        'BinaryOperator': 'And' },),
                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 147,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 150,
                                                    'Class': 'Action',
                                                    'Method': (Func12, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 151,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 227,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 231,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 230,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 229,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.KeepMoving, (8,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 173,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 200 }] },
                                                {
                                                    'ID': 177,
                                                    'Class': 'Action',
                                                    'Attachment': ({
                                                        'ID': 178,
                                                        'Class': 'Precondition',
                                                        'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
                                                        'Phase': 2,
                                                        'Flag': 'precondition',
                                                        'BinaryOperator': 'And' },),
                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 162,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 0,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 163,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 165,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 166,
                                                    'Class': 'Action',
                                                    'Attachment': ({
                                                        'ID': 167,
                                                        'Class': 'Precondition',
                                                        'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
                                                        'Phase': 2,
                                                        'Flag': 'precondition',
                                                        'BinaryOperator': 'And' },),
                                                    'Method': (cl_betree.monsteragent.CAgent.KeepMoving, (8,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 164,
                                            'Class': 'WaitFrame',
                                            'Frames': 40 }] }] },
                        {
                            'ID': 198,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 199,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
                                'Phase': 2,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' },),
                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
