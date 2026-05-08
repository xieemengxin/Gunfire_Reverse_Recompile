# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossDemon/bossDemonPhase2.pyc
# RelativePath: clientlogic/cl_betreedata/BossDemon/bossDemonPhase2.pyc
# Source Generated with Decompyle++
# File: bossDemonPhase2.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.IsChooseNoMaxHateTarget(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 6


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 40, oAgent) == True


def Func3(oAgent):
    return oAgent.GetData('CurPerformUseDis') <= 18


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)

data = {
    'Name': 'bossDemonPhase2',
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
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusAttack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 29,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 48,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 49,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 50,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseNoMaxHateTarget, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 51,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 52,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 53,
                            'Class': 'Condition',
                            'Method': (Func1, ()) },
                        {
                            'ID': 54,
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
                                            'ID': 28,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) }] },
                                {
                                    'ID': 26,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 30,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 27,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 31,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 35,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (15, 20, 1, 45)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 33,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] }] },
                {
                    'ID': 36,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 37,
                            'Class': 'Condition',
                            'Method': (Func3, ()) },
                        {
                            'ID': 41,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 42,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 43,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 57,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 58,
                                            'Class': 'Action',
                                            'Method': (Func4, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 59,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 60,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 50 },
                                                {
                                                    'ID': 61,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39243,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 45,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (0, 1)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 46,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 47,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' }, {
                                        'ID': 55,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StateTransition, (7994,)),
                                        'Phase': 2,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' }),
                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 39,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 40,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' }, {
                                'ID': 56,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StateTransition, (7994,)),
                                'Phase': 2,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' }),
                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
