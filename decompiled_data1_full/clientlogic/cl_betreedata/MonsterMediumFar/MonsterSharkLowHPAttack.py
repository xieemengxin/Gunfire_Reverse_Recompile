# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumFar/MonsterSharkLowHPAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumFar/MonsterSharkLowHPAttack.pyc
# Source Generated with Decompyle++
# File: MonsterSharkLowHPAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.IsLockEnemyPosAccessible(oAgent) == False


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformShotType(1, oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetCatchFrame(oAgent) >= 175


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 8


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformShotType(3, oAgent) == True


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)

data = {
    'Name': 'MonsterSharkLowHPAttack',
    'ID': 0,
    'AgentType': '',
    'IsFSM': False,
    'Ver': 13,
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
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 70,
                    'Class': 'DecoratorAlwaysSuccess',
                    'DecorateWhenChildEnds': False,
                    'Node': [
                        {
                            'ID': 71,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 5,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 0,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 8,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 13,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 14,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseShotPF, (3,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 15,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 24,
                                            'Class': 'And',
                                            'Node': [
                                                {
                                                    'ID': 38,
                                                    'Class': 'Condition',
                                                    'Method': (Func1, ()) },
                                                {
                                                    'ID': 39,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) }] },
                                        {
                                            'ID': 25,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 40,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) },
                                                {
                                                    'ID': 41,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 58,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseShotPF, (3,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 42,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 59,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseShotPF, (2,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] },
                                        {
                                            'ID': 26,
                                            'Class': 'DecoratorAlwaysFailure',
                                            'DecorateWhenChildEnds': False,
                                            'Node': [
                                                {
                                                    'ID': 43,
                                                    'Class': 'Noop' }] }] }] },
                        {
                            'ID': 18,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 62,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 63,
                                            'Class': 'Condition',
                                            'Method': (Func4, ()) },
                                        {
                                            'ID': 64,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 65,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 32,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 33,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                        'Phase': 2,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (Func5, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 22,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 23,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
                        'Phase': 2,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
