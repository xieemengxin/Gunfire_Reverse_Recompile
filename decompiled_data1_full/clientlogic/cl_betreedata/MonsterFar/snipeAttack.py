# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFar/snipeAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFar/snipeAttack.pyc
# Source Generated with Decompyle++
# File: snipeAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.HasToStartGuerrilla(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)

data = {
    'Name': 'snipeAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 233,
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
                    'ID': 453,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 454,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 456,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 463,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) }] },
                        {
                            'ID': 455,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 464,
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
                                                            'ID': 516,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
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
                                                                                    'Frames': 20 }] }] },
                                                                {
                                                                    'ID': 512,
                                                                    'Class': 'DecoratorWeight',
                                                                    'DecorateWhenChildEnds': False,
                                                                    'Weight': 25,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 522,
                                                                            'Class': 'WaitFrame',
                                                                            'Frames': 35 }] }] }] }] },
                                        {
                                            'ID': 466,
                                            'Class': 'DecoratorWeight',
                                            'DecorateWhenChildEnds': False,
                                            'Weight': 20,
                                            'Node': [
                                                {
                                                    'ID': 469,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 471,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 472,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHorizontalPos, (3, 4)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 473,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 474,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 517,
                                                            'Class': 'SelectorProbability',
                                                            'RandomGenerator': None,
                                                            'Node': [
                                                                {
                                                                    'ID': 518,
                                                                    'Class': 'DecoratorWeight',
                                                                    'DecorateWhenChildEnds': False,
                                                                    'Weight': 25,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 520,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 521,
                                                                                    'Class': 'WaitFrame',
                                                                                    'Frames': 20 }] }] },
                                                                {
                                                                    'ID': 519,
                                                                    'Class': 'DecoratorWeight',
                                                                    'DecorateWhenChildEnds': False,
                                                                    'Weight': 25,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 523,
                                                                            'Class': 'Noop' }] }] }] }] },
                                        {
                                            'ID': 467,
                                            'Class': 'DecoratorWeight',
                                            'DecorateWhenChildEnds': False,
                                            'Weight': 20,
                                            'Node': [
                                                {
                                                    'ID': 475,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 476,
                                                            'Class': 'IfElse',
                                                            'Node': [
                                                                {
                                                                    'ID': 478,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func1, ()) },
                                                                {
                                                                    'ID': 479,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 481,
                                                                            'Class': 'Action',
                                                                            'Method': (Func2, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 482,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 483,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 484,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] },
                                                                {
                                                                    'ID': 480,
                                                                    'Class': 'Noop' }] },
                                                        {
                                                            'ID': 477,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 524,
                                                            'Class': 'SelectorProbability',
                                                            'RandomGenerator': None,
                                                            'Node': [
                                                                {
                                                                    'ID': 525,
                                                                    'Class': 'DecoratorWeight',
                                                                    'DecorateWhenChildEnds': False,
                                                                    'Weight': 25,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 527,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 529,
                                                                                    'Class': 'WaitFrame',
                                                                                    'Frames': 20 }] }] },
                                                                {
                                                                    'ID': 526,
                                                                    'Class': 'DecoratorWeight',
                                                                    'DecorateWhenChildEnds': False,
                                                                    'Weight': 25,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 528,
                                                                            'Class': 'Noop' }] }] }] }] }] }] }] },
                {
                    'ID': 364,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 366,
                            'Class': 'SelectorProbability',
                            'RandomGenerator': None,
                            'Node': [
                                {
                                    'ID': 371,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 25,
                                    'Node': [
                                        {
                                            'ID': 375,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 380,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 17 }] }] },
                                {
                                    'ID': 372,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 25,
                                    'Node': [
                                        {
                                            'ID': 376,
                                            'Class': 'Noop' }] }] },
                        {
                            'ID': 388,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 367,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 392,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' },),
                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
