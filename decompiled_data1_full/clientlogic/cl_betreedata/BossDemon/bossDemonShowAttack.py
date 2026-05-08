# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossDemon/bossDemonShowAttack.pyc
# RelativePath: clientlogic/cl_betreedata/BossDemon/bossDemonShowAttack.pyc
# Source Generated with Decompyle++
# File: bossDemonShowAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 50, oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 20


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func3(oAgent):
    return oAgent.GetData('CurPerformUseDis') <= 18


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)

data = {
    'Name': 'bossDemonShowAttack',
    'ID': 0,
    'AgentType': '',
    'IsFSM': False,
    'Ver': 14,
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
                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39243,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 10,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 39,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 40,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 6,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 11,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 18,
                                            'Class': 'Condition',
                                            'Method': (Func0, ()) }] },
                                {
                                    'ID': 12,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 19,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 13,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 20,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 27,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 29,
                                                            'Class': 'Condition',
                                                            'Method': (Func1, ()) },
                                                        {
                                                            'ID': 30,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (16, 25, 1, 60)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 31,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (15, 8, 12, 160, 180)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 28,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] },
                        {
                            'ID': 41,
                            'Class': 'Condition',
                            'Method': (Func2, ()) }] },
                {
                    'ID': 7,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 14,
                            'Class': 'Condition',
                            'Method': (Func3, ()) },
                        {
                            'ID': 15,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 21,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 22,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 34,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 35,
                                            'Class': 'Action',
                                            'Method': (Func4, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 36,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 37,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 50 },
                                                {
                                                    'ID': 38,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39243,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 24,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (0, 1)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 25,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 26,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' }, {
                                        'ID': 32,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StateTransition, (7994,)),
                                        'Phase': 2,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' }),
                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 16,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 17,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' }, {
                                'ID': 33,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StateTransition, (7994,)),
                                'Phase': 2,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' }),
                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
