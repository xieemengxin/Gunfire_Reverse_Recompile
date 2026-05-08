# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterNear/MonsterSharkMovingAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterNear/MonsterSharkMovingAttack.pyc
# Source Generated with Decompyle++
# File: MonsterSharkMovingAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformShotType(1, oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetCatchFrame(oAgent) >= 75


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.IsLockEnemyPosAccessible(oAgent) == False


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 10


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetHPPercent('HP', oAgent) > 50


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformShotType(3, oAgent) == True

data = {
    'Name': 'MonsterSharkMovingAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 81,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Attachment': ({
                'ID': 3,
                'Class': 'Effector',
                'Method': (cl_betree.monsteragent.CAgent.SetFightLogicType, (1,)),
                'Phase': 1,
                'Flag': 'effector' }, {
                'ID': 2,
                'Class': 'Precondition',
                'Method': (cl_betree.monsteragent.CAgent.SetFightLogicType, (2,)),
                'Phase': 1,
                'Flag': 'precondition',
                'BinaryOperator': 'And' }),
            'Node': [
                {
                    'ID': 263,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusAttack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 43,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 401,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 350,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 0,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 355,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 1,
                            'ExitPolicy': 0,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 358,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 363,
                                            'Class': 'And',
                                            'Node': [
                                                {
                                                    'ID': 376,
                                                    'Class': 'Condition',
                                                    'Method': (Func0, ()) },
                                                {
                                                    'ID': 377,
                                                    'Class': 'Condition',
                                                    'Method': (Func1, ()) }] },
                                        {
                                            'ID': 364,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 378,
                                                    'Class': 'Or',
                                                    'Node': [
                                                        {
                                                            'ID': 384,
                                                            'Class': 'Condition',
                                                            'Method': (Func2, ()) },
                                                        {
                                                            'ID': 385,
                                                            'Class': 'And',
                                                            'Node': [
                                                                {
                                                                    'ID': 390,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func3, ()) },
                                                                {
                                                                    'ID': 391,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func4, ()) }] }] },
                                                {
                                                    'ID': 379,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 387,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseShotPF, (3,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 380,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 388,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseShotPF, (2,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] },
                                        {
                                            'ID': 404,
                                            'Class': 'Noop' }] },
                                {
                                    'ID': 406,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 402,
                                            'Class': 'Condition',
                                            'Method': (Func5, ()) },
                                        {
                                            'ID': 403,
                                            'Class': 'Condition',
                                            'Method': (Func6, ()) },
                                        {
                                            'ID': 394,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 351,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 352,
                                    'Class': 'Condition',
                                    'Method': (Func7, ()) },
                                {
                                    'ID': 397,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 398,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (8, 8, 15, 30, 80)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 399,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 405,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
                                                'Phase': 2,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 354,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 396,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                        'Phase': 2,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (4,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
