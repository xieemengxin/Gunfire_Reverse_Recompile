# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterNear/MonsterSharkChaseCatch.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterNear/MonsterSharkChaseCatch.pyc
# Source Generated with Decompyle++
# File: MonsterSharkChaseCatch.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.IsLockEnemyPosAccessible(oAgent) == False


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetCatchFrame(oAgent) >= 75


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == False

data = {
    'Name': 'MonsterSharkChaseCatch',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 59,
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
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 71,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 113,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 144,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 145,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 115,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 116,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                'Phase': 2,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (10,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 146,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (21337,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 117,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 150,
                                            'Class': 'Or',
                                            'Node': [
                                                {
                                                    'ID': 118,
                                                    'Class': 'Condition',
                                                    'Method': (Func0, ()) },
                                                {
                                                    'ID': 179,
                                                    'Class': 'Condition',
                                                    'Method': (Func1, ()) }] },
                                        {
                                            'ID': 167,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 164,
                                            'Class': 'DecoratorAlwaysFailure',
                                            'DecorateWhenChildEnds': False,
                                            'Node': [
                                                {
                                                    'ID': 165,
                                                    'Class': 'Noop' }] }] }] },
                        {
                            'ID': 105,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 106,
                                    'Class': 'Condition',
                                    'Method': (Func2, ()) },
                                {
                                    'ID': 172,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (21338,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 142,
                                    'Class': 'DecoratorAlwaysFailure',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 143,
                                            'Class': 'Noop' }] }] }] },
                {
                    'ID': 170,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 169,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.RemoveState, (33586,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 180,
                    'Class': 'Parallel',
                    'Attachment': ({
                        'ID': 183,
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
                            'ID': 174,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 175,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
                                'Phase': 2,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' },),
                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 182,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 181,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (3,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
