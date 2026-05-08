# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterSniper/snipeFuzzyAwait.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterSniper/snipeFuzzyAwait.pyc
# Source Generated with Decompyle++
# File: snipeFuzzyAwait.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 4


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'snipeFuzzyAwait',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 258,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 98,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 583,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 453,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 0,
                    'Node': [
                        {
                            'ID': 535,
                            'Class': 'SelectorProbability',
                            'RandomGenerator': None,
                            'Node': [
                                {
                                    'ID': 465,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 15,
                                    'Node': [
                                        {
                                            'ID': 468,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 578,
                                                    'Class': 'Action',
                                                    'Attachment': ({
                                                        'ID': 581,
                                                        'Class': 'Precondition',
                                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                        'Phase': 1,
                                                        'Flag': 'precondition',
                                                        'BinaryOperator': 'And' },),
                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 510,
                                                    'Class': 'SelectorProbability',
                                                    'RandomGenerator': None,
                                                    'Node': [
                                                        {
                                                            'ID': 511,
                                                            'Class': 'DecoratorWeight',
                                                            'DecorateWhenChildEnds': False,
                                                            'Weight': 25,
                                                            'Node': [
                                                                {
                                                                    'ID': 513,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 515,
                                                                            'Class': 'WaitFrame',
                                                                            'Frames': 15 }] }] },
                                                        {
                                                            'ID': 512,
                                                            'Class': 'DecoratorWeight',
                                                            'DecorateWhenChildEnds': False,
                                                            'Weight': 25,
                                                            'Node': [
                                                                {
                                                                    'ID': 522,
                                                                    'Class': 'WaitFrame',
                                                                    'Frames': 22 }] }] }] }] },
                                {
                                    'ID': 536,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 20,
                                    'Node': [
                                        {
                                            'ID': 540,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 544,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 545,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 546,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHorizontalPos, (3, 4)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 547,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 539,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 20,
                                    'Node': [
                                        {
                                            'ID': 543,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 556,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 557,
                                                    'Class': 'Action',
                                                    'Method': (Func0, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 558,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 559,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] },
                        {
                            'ID': 584,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 585,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 586,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 587,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) },
                                        {
                                            'ID': 588,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 589,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 55,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                'Phase': 1,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 590,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] }] }] }] }
