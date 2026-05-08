# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterSniper/comboFuzzyAreamoveAwait.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterSniper/comboFuzzyAreamoveAwait.pyc
# Source Generated with Decompyle++
# File: comboFuzzyAreamoveAwait.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetFirstRangedArrivePosDis(oAgent) <= 5


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 4


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'comboFuzzyAreamoveAwait',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 134,
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
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (0, 0)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 318,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 0,
                    'Node': [
                        {
                            'ID': 469,
                            'Class': 'SelectorProbability',
                            'RandomGenerator': None,
                            'Node': [
                                {
                                    'ID': 470,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 20,
                                    'Node': [
                                        {
                                            'ID': 505,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 506,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (5, 8, 60, 105)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 507,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (2,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 508,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 509,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (15, 1)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 471,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 50,
                                    'Node': [
                                        {
                                            'ID': 473,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 477,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedAreaPos, (1, 10, 0)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 478,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 481,
                                                            'Class': 'Condition',
                                                            'Method': (Func0, ()) },
                                                        {
                                                            'ID': 482,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 486,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 487,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 488,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 511,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 512,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 515,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 514,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] }] }] },
                        {
                            'ID': 517,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 518,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 519,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 520,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) },
                                        {
                                            'ID': 521,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 522,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 55,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                'Phase': 1,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (40, 1)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 523,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] }] }] }] }
