# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossDemon/bossDemonPhase3.pyc
# RelativePath: clientlogic/cl_betreedata/BossDemon/bossDemonPhase3.pyc
# Source Generated with Decompyle++
# File: bossDemonPhase3.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.IsChooseNoMaxHateTarget(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 6


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 30, oAgent) == True


def Func3(oAgent):
    return oAgent.GetData('CurPerformUseDis') <= 18


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)

data = {
    'Name': 'bossDemonPhase3',
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
                    'ID': 18,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 44,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 45,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 46,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseNoMaxHateTarget, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 47,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 48,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 49,
                            'Class': 'Condition',
                            'Method': (Func1, ()) },
                        {
                            'ID': 50,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 9,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 10,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 12,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 13,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (6, 12, 1, 45)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 14,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 11,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 17,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) }] }] }] },
                {
                    'ID': 36,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 19,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 20,
                            'Class': 'Condition',
                            'Method': (Func3, ()) },
                        {
                            'ID': 37,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 38,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 39,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 53,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 54,
                                            'Class': 'Action',
                                            'Method': (Func4, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 55,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 56,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 50 },
                                                {
                                                    'ID': 57,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39243,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 41,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (0, 1)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 42,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 43,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' }, {
                                        'ID': 51,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StateTransition, (7994,)),
                                        'Phase': 2,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' }),
                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 22,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 23,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' }, {
                                'ID': 52,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StateTransition, (7994,)),
                                'Phase': 2,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' }),
                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
