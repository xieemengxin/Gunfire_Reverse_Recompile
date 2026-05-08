# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/farGuerrillaAttack.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/farGuerrillaAttack.pyc
# Source Generated with Decompyle++
# File: farGuerrillaAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.HasToStartGuerrilla(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == True


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == True

data = {
    'Name': 'farGuerrillaAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 170,
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
                    'ID': 262,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 263,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 264,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 269,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 270,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 271,
                                                    'Class': 'Condition',
                                                    'Method': (Func0, ()) },
                                                {
                                                    'ID': 272,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 274,
                                                            'Class': 'Action',
                                                            'Method': (Func1, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 275,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 278,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 279,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 280,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 281,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'false')),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 282,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'true')),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] },
                                                        {
                                                            'ID': 308,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 309,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'IsSquat', '0')),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 310,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 277,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 273,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 268,
                                            'Class': 'WaitFrame',
                                            'Frames': (cl_betree.monsteragent.CAgent.GetGuerrillaInterval, ()) }] }] }] },
                {
                    'ID': 235,
                    'Class': 'Sequence',
                    'Attachment': ({
                        'ID': 352,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Node': [
                        {
                            'ID': 236,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 237,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 238,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 239,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'true')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 240,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'false')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
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
                                    'Method': (Func2, ()) },
                                {
                                    'ID': 166,
                                    'Class': 'Condition',
                                    'Method': (Func3, ()) }] },
                        {
                            'ID': 163,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 167,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 170,
                                            'Class': 'Condition',
                                            'Method': (Func4, ()) },
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
                                                    'ID': 284,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 283,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'IsSquat', '0')),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 179,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] },
                                        {
                                            'ID': 234,
                                            'Class': 'Noop' }] },
                                {
                                    'ID': 288,
                                    'Class': 'SelectorProbability',
                                    'RandomGenerator': None,
                                    'Node': [
                                        {
                                            'ID': 289,
                                            'Class': 'DecoratorWeight',
                                            'DecorateWhenChildEnds': False,
                                            'Weight': 25,
                                            'Node': [
                                                {
                                                    'ID': 291,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 293,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'IsSquat', '1')),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 294,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 17 }] }] },
                                        {
                                            'ID': 290,
                                            'Class': 'DecoratorWeight',
                                            'DecorateWhenChildEnds': False,
                                            'Weight': 25,
                                            'Node': [
                                                {
                                                    'ID': 292,
                                                    'Class': 'Noop' }] }] },
                                {
                                    'ID': 172,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 164,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 302,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 303,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 304,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 305,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 306,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'false')),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 307,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'true')),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 312,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'IsSquat', '0')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 186,
                                    'Class': 'Action',
                                    'Method': (Func5, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 330,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 331,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 332,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 333,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 334,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'true')),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 335,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'false')),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 336,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 337,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 351,
                                                    'Class': 'Condition',
                                                    'Method': (Func6, ()) },
                                                {
                                                    'ID': 354,
                                                    'Class': 'DecoratorAlwaysRunning',
                                                    'DecorateWhenChildEnds': False,
                                                    'Node': [
                                                        {
                                                            'ID': 339,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 340,
                                                                    'Class': 'Action',
                                                                    'Method': (Func7, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 347,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] }] },
                                {
                                    'ID': 313,
                                    'Class': 'Sequence',
                                    'Attachment': ({
                                        'ID': 353,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Node': [
                                        {
                                            'ID': 314,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 317,
                                                    'Class': 'Condition',
                                                    'Method': (Func8, ()) },
                                                {
                                                    'ID': 318,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 322,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHorizontalPos, (2, 3)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 323,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 326,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'IsSquat', '0')),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 327,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] },
                                                {
                                                    'ID': 319,
                                                    'Class': 'Noop' }] },
                                        {
                                            'ID': 315,
                                            'Class': 'SelectorProbability',
                                            'RandomGenerator': None,
                                            'Node': [
                                                {
                                                    'ID': 320,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 25,
                                                    'Node': [
                                                        {
                                                            'ID': 324,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 328,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'IsSquat', '1')),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 329,
                                                                    'Class': 'WaitFrame',
                                                                    'Frames': 17 }] }] },
                                                {
                                                    'ID': 321,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 25,
                                                    'Node': [
                                                        {
                                                            'ID': 325,
                                                            'Class': 'Noop' }] }] },
                                        {
                                            'ID': 316,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] }] }] }] }
