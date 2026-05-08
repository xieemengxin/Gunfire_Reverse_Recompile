# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterNear/MonsterSharkChaseLowHPCatch.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterNear/MonsterSharkChaseLowHPCatch.pyc
# Source Generated with Decompyle++
# File: MonsterSharkChaseLowHPCatch.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) == 1


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsLockEnemyPosAccessible(oAgent) == False


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetCatchFrame(oAgent) >= 75


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == False

data = {
    'Name': 'MonsterSharkChaseLowHPCatch',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 157,
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
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetLowHPChaseAsTarget, (33607,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 35,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 36,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 37,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 38,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (21336,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 39,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 40,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 41,
                            'Class': 'Noop' }] },
                {
                    'ID': 42,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 43,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 45,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 50,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 51,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                'Phase': 2,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (8,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 52,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (21337,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 46,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 54,
                                            'Class': 'Or',
                                            'Node': [
                                                {
                                                    'ID': 58,
                                                    'Class': 'Condition',
                                                    'Method': (Func1, ()) },
                                                {
                                                    'ID': 68,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) }] },
                                        {
                                            'ID': 55,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 56,
                                            'Class': 'DecoratorAlwaysFailure',
                                            'DecorateWhenChildEnds': False,
                                            'Node': [
                                                {
                                                    'ID': 60,
                                                    'Class': 'Noop' }] }] }] },
                        {
                            'ID': 44,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 47,
                                    'Class': 'Condition',
                                    'Method': (Func3, ()) },
                                {
                                    'ID': 48,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (21338,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 49,
                                    'Class': 'DecoratorAlwaysFailure',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 57,
                                            'Class': 'Noop' }] }] }] },
                {
                    'ID': 63,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 64,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.RemoveState, (33586,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 69,
                    'Class': 'Parallel',
                    'Attachment': ({
                        'ID': 74,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'FailurePolicy': 0,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 70,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 71,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
                                'Phase': 2,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' },),
                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 72,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 73,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (3,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
