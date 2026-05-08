# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterSniper/comboFuzzyAwait.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterSniper/comboFuzzyAwait.pyc
# Source Generated with Decompyle++
# File: comboFuzzyAwait.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.HasToStartGuerrilla(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetFirstRangedArrivePosDis(oAgent) >= 6


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func4(oAgent):
    return oAgent.GetConfig('GuerrillaInterval')


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 4


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'comboFuzzyAwait',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 269,
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
                    'ID': 635,
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
                            'ID': 579,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 580,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 581,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 583,
                                            'Class': 'Action',
                                            'Method': (Func1, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 584,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 587,
                                                    'Class': 'Condition',
                                                    'Method': (Func2, ()) },
                                                {
                                                    'ID': 588,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 594,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 595,
                                                            'Class': 'Action',
                                                            'Method': (Func3, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 596,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 597,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 598,
                                                    'Class': 'SelectorProbability',
                                                    'RandomGenerator': None,
                                                    'Node': [
                                                        {
                                                            'ID': 600,
                                                            'Class': 'DecoratorWeight',
                                                            'DecorateWhenChildEnds': False,
                                                            'Weight': 15,
                                                            'Node': [
                                                                {
                                                                    'ID': 603,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 609,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 610,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 612,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] },
                                                        {
                                                            'ID': 601,
                                                            'Class': 'DecoratorWeight',
                                                            'DecorateWhenChildEnds': False,
                                                            'Weight': 15,
                                                            'Node': [
                                                                {
                                                                    'ID': 604,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 613,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseDodgePos, (5, 8, 60, 105)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 614,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (2,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 615,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 616,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (15, 1)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] }] }] }] },
                                {
                                    'ID': 582,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 0,
                                    'SuccessPolicy': 1,
                                    'ExitPolicy': 0,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 617,
                                            'Class': 'SelectorProbability',
                                            'RandomGenerator': None,
                                            'Node': [
                                                {
                                                    'ID': 618,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 15,
                                                    'Node': [
                                                        {
                                                            'ID': 620,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 622,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 591,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHorizontalPos, (4, 5)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 623,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 624,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] },
                                                {
                                                    'ID': 619,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 15,
                                                    'Node': [
                                                        {
                                                            'ID': 625,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 626,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 627,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 628,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 629,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.KeepMoving, (3,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 633,
                                                                            'Class': 'WaitFrame',
                                                                            'Frames': 20 }] }] }] }] },
                                        {
                                            'ID': 586,
                                            'Class': 'WaitFrame',
                                            'Frames': (Func4, ()) }] }] },
                        {
                            'ID': 636,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 637,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 638,
                                            'Class': 'Condition',
                                            'Method': (Func5, ()) },
                                        {
                                            'ID': 639,
                                            'Class': 'Condition',
                                            'Method': (Func6, ()) },
                                        {
                                            'ID': 640,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 641,
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
                                            'ID': 642,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] }] }] }] }
