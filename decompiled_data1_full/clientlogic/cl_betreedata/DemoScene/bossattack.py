# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/bossattack.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/bossattack.pyc
# Source Generated with Decompyle++
# File: bossattack.pyc (Python 3.6)

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
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.HasToStartGuerrilla(oAgent) == True


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)

data = {
    'Name': 'bossattack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 104,
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
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetMoveStatusRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 145,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 146,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 147,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 148,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 149,
                                            'Class': 'Action',
                                            'Method': (Func0, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 150,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 154,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 155,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'true')),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 156,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'false')),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 151,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 152,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] }] },
                {
                    'ID': 6,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusAttack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 7,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 105,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 106,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'false')),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 107,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'true')),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 8,
                    'Class': 'IfElse',
                    'Attachment': ({
                        'ID': 101,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Node': [
                        {
                            'ID': 108,
                            'Class': 'And',
                            'Node': [
                                {
                                    'ID': 113,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 114,
                                    'Class': 'Condition',
                                    'Method': (Func2, ()) }] },
                        {
                            'ID': 109,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 115,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 122,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) },
                                        {
                                            'ID': 123,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 135,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHorizontalPos, (2, 3)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 136,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 137,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 124,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 110,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 116,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 117,
                                    'Class': 'Action',
                                    'Method': (Func4, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 118,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 119,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 125,
                                            'Class': 'Condition',
                                            'Method': (Func5, ()) },
                                        {
                                            'ID': 126,
                                            'Class': 'DecoratorAlwaysRunning',
                                            'DecorateWhenChildEnds': False,
                                            'Node': [
                                                {
                                                    'ID': 138,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (5,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 120,
                                    'Class': 'IfElse',
                                    'Attachment': ({
                                        'ID': 69,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Node': [
                                        {
                                            'ID': 127,
                                            'Class': 'Condition',
                                            'Method': (Func6, ()) },
                                        {
                                            'ID': 128,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 139,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHorizontalPos, (2, 3)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 140,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 141,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 129,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] }] },
                {
                    'ID': 157,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 158,
                            'Class': 'Condition',
                            'Method': (Func7, ()) },
                        {
                            'ID': 159,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 161,
                                    'Class': 'Action',
                                    'Method': (Func8, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 162,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 166,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 167,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'true')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 168,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'false')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 163,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 164,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 160,
                            'Class': 'Noop' }] }] }] }
