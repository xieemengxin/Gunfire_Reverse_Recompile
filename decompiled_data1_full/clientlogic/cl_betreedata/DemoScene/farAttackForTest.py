# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/farAttackForTest.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/farAttackForTest.pyc
# Source Generated with Decompyle++
# File: farAttackForTest.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), 4, 6, 80, 100, oAgent)


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == True

data = {
    'Name': 'farAttackForTest',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 158,
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
                    'ID': 290,
                    'Class': 'SelectorProbability',
                    'RandomGenerator': None,
                    'Node': [
                        {
                            'ID': 291,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 50,
                            'Node': [
                                {
                                    'ID': 293,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 294,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'IsSquat', '0')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 295,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 1,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 296,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 297,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 298,
                                                            'Class': 'Action',
                                                            'Method': (Func0, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 299,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 304,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 305,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'false')),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 306,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'true')),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 300,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 301,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 302,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 303,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 1,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 307,
                                                                    'Class': 'WaitFrame',
                                                                    'Frames': (cl_betree.monsteragent.CAgent.GetGuerrillaInterval, ()) },
                                                                {
                                                                    'ID': 308,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] },
                                        {
                                            'ID': 314,
                                            'Class': 'SelectorProbability',
                                            'RandomGenerator': None,
                                            'Node': [
                                                {
                                                    'ID': 315,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 50,
                                                    'Node': [
                                                        {
                                                            'ID': 324,
                                                            'Class': 'Noop' }] },
                                                {
                                                    'ID': 316,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 50,
                                                    'Node': [
                                                        {
                                                            'ID': 318,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 321,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'IsSquat', '1')),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 322,
                                                                    'Class': 'WaitFrame',
                                                                    'Frames': 17 }] }] }] }] }] },
                        {
                            'ID': 292,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 50,
                            'Node': [
                                {
                                    'ID': 309,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 312,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'IsSquat', '1')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 311,
                                            'Class': 'WaitFrame',
                                            'Frames': 17 },
                                        {
                                            'ID': 313,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] }] },
                {
                    'ID': 158,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 161,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 162,
                            'Class': 'And',
                            'Node': [
                                {
                                    'ID': 165,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 166,
                                    'Class': 'Condition',
                                    'Method': (Func2, ()) }] },
                        {
                            'ID': 163,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 220,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 225,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 226,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'true')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 227,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'false')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 167,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 170,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) },
                                        {
                                            'ID': 171,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 178,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHorizontalPos, (2, 3)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 276,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'IsSquat', '0')),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 179,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 239,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 241,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] },
                                        {
                                            'ID': 232,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 234,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] },
                        {
                            'ID': 164,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 196,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 205,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', '0')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 206,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'false')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 207,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', '1')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 277,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'IsSquat', '0')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 186,
                                    'Class': 'Action',
                                    'Method': (Func4, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 224,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 228,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 229,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'true')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 230,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'false')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 168,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 1,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 173,
                                            'Class': 'Condition',
                                            'Method': (Func5, ()) },
                                        {
                                            'ID': 174,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 181,
                                                    'Class': 'Action',
                                                    'Method': (Func6, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 182,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 169,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 175,
                                            'Class': 'Condition',
                                            'Method': (Func7, ()) },
                                        {
                                            'ID': 176,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 183,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHorizontalPos, (2, 3)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 184,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 246,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 248,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] },
                                        {
                                            'ID': 253,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 255,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] }] }] }] }
