# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFar/throwFuzzyAreamoveAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFar/throwFuzzyAreamoveAttack.pyc
# Source Generated with Decompyle++
# File: throwFuzzyAreamoveAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == False


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(0, 100, oAgent) == True

data = {
    'Name': 'throwFuzzyAreamoveAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 101,
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
                    'ID': 406,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 318,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 319,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 320,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 398,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 399,
                                    'Class': 'And',
                                    'Node': [
                                        {
                                            'ID': 400,
                                            'Class': 'And',
                                            'Node': [
                                                {
                                                    'ID': 402,
                                                    'Class': 'Condition',
                                                    'Method': (Func0, ()) },
                                                {
                                                    'ID': 403,
                                                    'Class': 'Condition',
                                                    'Method': (Func1, ()) }] },
                                        {
                                            'ID': 401,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) }] },
                                {
                                    'ID': 405,
                                    'Class': 'Condition',
                                    'Method': (Func3, ()) }] },
                        {
                            'ID': 199,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 200,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedAreaPos, (1, 10, 0)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 310,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 311,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 312,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 407,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 257,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
