# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterNear/AshAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterNear/AshAttack.pyc
# Source Generated with Decompyle++
# File: AshAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(7127, oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 8.5


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 23612


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 4


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 2

data = {
    'Name': 'AshAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 52,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 34,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 0,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 49,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 50,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 52,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 53,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 11,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (23611,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 54,
                                            'Class': 'Noop' }] },
                                {
                                    'ID': 51,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 33,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 29,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 7,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.MoveToSlopeLockEnemy, (8.5, 20)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 36,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 37,
                            'Class': 'Condition',
                            'Method': (Func2, ()) },
                        {
                            'ID': 47,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 48,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.AddState, (7127, 0)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 39,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 40,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) },
                                        {
                                            'ID': 43,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 44,
                                                    'Class': 'Condition',
                                                    'Method': (Func4, ()) },
                                                {
                                                    'ID': 38,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (4, 5, 135, 160)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 45,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (3.6, 4.5, 135, 160)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 41,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (2.5, 3.5, 135, 160)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 46,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.RemoveState, (7127,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 13,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 14,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 15,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
