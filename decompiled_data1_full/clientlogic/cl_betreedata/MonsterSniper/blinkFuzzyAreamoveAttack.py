# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterSniper/blinkFuzzyAreamoveAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterSniper/blinkFuzzyAreamoveAttack.pyc
# Source Generated with Decompyle++
# File: blinkFuzzyAreamoveAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == False


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(1, 100, oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.GetFirstRangedArrivePosDis(oAgent) <= 5

data = {
    'Name': 'blinkFuzzyAreamoveAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 138,
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
                            'ID': 522,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 527,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedAreaPos, (1, 10, 0)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 528,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 529,
                                            'Class': 'Condition',
                                            'Method': (Func4, ()) },
                                        {
                                            'ID': 530,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 532,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 533,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 534,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 531,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 536,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 537,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 538,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 539,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] }] },
                {
                    'ID': 254,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 407,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 468,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' },),
                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 257,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
