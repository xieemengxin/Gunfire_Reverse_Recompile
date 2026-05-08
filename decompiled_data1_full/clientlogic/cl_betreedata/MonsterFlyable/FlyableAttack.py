# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFlyable/FlyableAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFlyable/FlyableAttack.pyc
# Source Generated with Decompyle++
# File: FlyableAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedFlyPos(oAgent.GetConfig('RangedPosR'), 1, 3, 120, 180, 1, 3, oAgent)


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(1, 50, oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == False


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'FlyableAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 149,
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
                    'ID': 206,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 267,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 269,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 235,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 259,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 268,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 249,
                                            'Class': 'Action',
                                            'Method': (Func0, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 280,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 0,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 0,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 250,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 281,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 50 }] },
                                        {
                                            'ID': 274,
                                            'Class': 'SelectorProbability',
                                            'RandomGenerator': None,
                                            'Node': [
                                                {
                                                    'ID': 275,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 10,
                                                    'Node': [
                                                        {
                                                            'ID': 273,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 10 }] },
                                                {
                                                    'ID': 276,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 10,
                                                    'Node': [
                                                        {
                                                            'ID': 278,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 20 }] },
                                                {
                                                    'ID': 277,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 10,
                                                    'Node': [
                                                        {
                                                            'ID': 279,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 30 }] }] }] }] },
                        {
                            'ID': 270,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 207,
                                    'Class': 'And',
                                    'Node': [
                                        {
                                            'ID': 239,
                                            'Class': 'And',
                                            'Node': [
                                                {
                                                    'ID': 245,
                                                    'Class': 'And',
                                                    'Node': [
                                                        {
                                                            'ID': 282,
                                                            'Class': 'Condition',
                                                            'Method': (Func1, ()) },
                                                        {
                                                            'ID': 237,
                                                            'Class': 'Condition',
                                                            'Method': (Func2, ()) }] },
                                                {
                                                    'ID': 211,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) }] },
                                        {
                                            'ID': 215,
                                            'Class': 'Condition',
                                            'Method': (Func4, ()) }] },
                                {
                                    'ID': 5,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 266,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 256,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
