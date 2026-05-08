# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossDemon/bossDemonPhase6.pyc
# RelativePath: clientlogic/cl_betreedata/BossDemon/bossDemonPhase6.pyc
# Source Generated with Decompyle++
# File: bossDemonPhase6.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.IsChooseNoMaxHateTarget(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 5


def Func2(oAgent):
    return oAgent.GetData('CurPerformUseDis') <= 18


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)

data = {
    'Name': 'bossDemonPhase6',
    'ID': 0,
    'AgentType': '',
    'IsFSM': False,
    'Ver': 3,
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
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 10,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 11,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseNoMaxHateTarget, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 12,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 6,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 13,
                            'Class': 'Condition',
                            'Method': (Func1, ()) },
                        {
                            'ID': 14,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 38,
                            'Class': 'Noop' }] },
                {
                    'ID': 7,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 8,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 9,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 16,
                            'Class': 'Condition',
                            'Method': (Func2, ()) },
                        {
                            'ID': 17,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 23,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 24,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 25,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 34,
                                            'Class': 'Action',
                                            'Method': (Func3, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 35,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 36,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 25 },
                                                {
                                                    'ID': 37,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39243,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 26,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (0, 1)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 27,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 28,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' }, {
                                        'ID': 29,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StateTransition, (7994,)),
                                        'Phase': 2,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' }),
                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 18,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 19,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' }, {
                                'ID': 20,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StateTransition, (7994,)),
                                'Phase': 2,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' }),
                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
