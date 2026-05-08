# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossDemon/bossDemonPhase4.pyc
# RelativePath: clientlogic/cl_betreedata/BossDemon/bossDemonPhase4.pyc
# Source Generated with Decompyle++
# File: bossDemonPhase4.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.IsChooseNoMaxHateTarget(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 5


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 25, oAgent) == True


def Func3(oAgent):
    return oAgent.GetData('CurPerformUseDis') <= 18


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)

data = {
    'Name': 'bossDemonPhase4',
    'ID': 0,
    'AgentType': '',
    'IsFSM': False,
    'Ver': 15,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusAttack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 33,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 59,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 60,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 61,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseNoMaxHateTarget, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 62,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 63,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 64,
                            'Class': 'Condition',
                            'Method': (Func1, ()) },
                        {
                            'ID': 65,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 24,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 25,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 74,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 28,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (6, 12, 1, 45)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 29,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 26,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 32,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) }] }] }] },
                {
                    'ID': 51,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 68,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 34,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 35,
                            'Class': 'Condition',
                            'Method': (Func3, ()) },
                        {
                            'ID': 52,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 53,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 54,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 69,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 70,
                                            'Class': 'Action',
                                            'Method': (Func4, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 71,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 72,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 50 },
                                                {
                                                    'ID': 73,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39243,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 56,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (0, 1)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 57,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 58,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' }, {
                                        'ID': 66,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StateTransition, (7994,)),
                                        'Phase': 2,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' }),
                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 37,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 38,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' }, {
                                'ID': 67,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StateTransition, (7994,)),
                                'Phase': 2,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' }),
                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
