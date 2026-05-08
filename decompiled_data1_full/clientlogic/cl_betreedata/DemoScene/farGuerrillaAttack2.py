# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/farGuerrillaAttack2.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/farGuerrillaAttack2.pyc
# Source Generated with Decompyle++
# File: farGuerrillaAttack2.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) >= 20


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetConfig('RangedPosR'), oAgent)


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.HasToStartGuerrilla(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), 4, 6, 80, 100, oAgent)


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'farGuerrillaAttack2',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 109,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 115,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 92,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 58,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 0,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 61,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 62,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 111,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 112,
                                            'Class': 'DecoratorAlwaysRunning',
                                            'DecorateWhenChildEnds': False },
                                        {
                                            'ID': 113,
                                            'Class': 'Condition',
                                            'Method': (Func0, ()) }] },
                                {
                                    'ID': 114,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 5,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 60,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 64,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 72,
                                            'Class': 'Action',
                                            'Method': (Func2, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 93,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 94,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 96,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) },
                                                {
                                                    'ID': 97,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 102,
                                                            'Class': 'Action',
                                                            'Method': (Func4, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 103,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 104,
                                                            'Class': 'WaitFrame',
                                                            'Frames': (cl_betree.monsteragent.CAgent.GetGuerrillaInterval, ()) }] },
                                                {
                                                    'ID': 98,
                                                    'Class': 'WaitFrame',
                                                    'Frames': (cl_betree.monsteragent.CAgent.GetGuerrillaInterval, ()) }] },
                                        {
                                            'ID': 95,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 99,
                                                    'Class': 'Condition',
                                                    'Method': (Func5, ()) },
                                                {
                                                    'ID': 100,
                                                    'Class': 'Noop' },
                                                {
                                                    'ID': 101,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 1,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 105,
                                                            'Class': 'Condition',
                                                            'Method': (Func6, ()) },
                                                        {
                                                            'ID': 106,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 1,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 107,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 109,
                                                                            'Class': 'Action',
                                                                            'Method': (Func7, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 110,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] },
                                                                {
                                                                    'ID': 108,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func8, ()) }] }] }] }] }] }] }] }] }
