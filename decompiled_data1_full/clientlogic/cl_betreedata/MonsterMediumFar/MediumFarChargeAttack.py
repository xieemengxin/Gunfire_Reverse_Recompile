# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumFar/MediumFarChargeAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumFar/MediumFarChargeAttack.pyc
# Source Generated with Decompyle++
# File: MediumFarChargeAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) <= 4


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 10


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, 50, oAgent) == True


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangedPos(oAgent.GetConfig('RangedPosR'), oAgent.GetConfig('RangedPosMinDis'), oAgent.GetConfig('RangedPosMaxDis'), oAgent.GetConfig('RangedPosMinAngle'), oAgent.GetConfig('RangedPosMaxAngle'), oAgent)


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True

data = {
    'Name': 'MediumFarChargeAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 123,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Attachment': ({
                'ID': 35,
                'Class': 'Effector',
                'Method': (cl_betree.monsteragent.CAgent.SetFightLogicType, (1,)),
                'Phase': 1,
                'Flag': 'effector' }, {
                'ID': 34,
                'Class': 'Precondition',
                'Method': (cl_betree.monsteragent.CAgent.SetFightLogicType, (2,)),
                'Phase': 1,
                'Flag': 'precondition',
                'BinaryOperator': 'And' }),
            'Node': [
                {
                    'ID': 36,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 37,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 38,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 111,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 112,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 113,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 114,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 770,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 115,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 735,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 736,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 737,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 738,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 740,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (7, 9, 15, 30)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 741,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 742,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 743,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 751,
                                                    'Class': 'Action',
                                                    'Attachment': ({
                                                        'ID': 752,
                                                        'Class': 'Precondition',
                                                        'Method': (cl_betree.monsteragent.CAgent.TryReChooseHateFlankPos, (3, 7, 9, 15, 30)),
                                                        'Phase': 1,
                                                        'Flag': 'precondition',
                                                        'BinaryOperator': 'And' },),
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 753,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 759,
                                                            'Class': 'And',
                                                            'Node': [
                                                                {
                                                                    'ID': 765,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func2, ()) },
                                                                {
                                                                    'ID': 766,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func3, ()) }] },
                                                        {
                                                            'ID': 760,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] }] },
                                        {
                                            'ID': 744,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 745,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                'Phase': 1,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 746,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 747,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                                'Phase': 1,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 771,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 748,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 739,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 0,
                                    'SuccessPolicy': 1,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 773,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 749,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 754,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 755,
                                                                'Class': 'Precondition',
                                                                'Method': (cl_betree.monsteragent.CAgent.KeepBulletFill, ()),
                                                                'Phase': 1,
                                                                'Flag': 'precondition',
                                                                'BinaryOperator': 'And' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 769,
                                                            'Class': 'Condition',
                                                            'Method': (Func4, ()) },
                                                        {
                                                            'ID': 767,
                                                            'Class': 'Condition',
                                                            'Method': (Func5, ()) },
                                                        {
                                                            'ID': 768,
                                                            'Class': 'Condition',
                                                            'Method': (Func6, ()) },
                                                        {
                                                            'ID': 772,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 757,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None }] },
                                                {
                                                    'ID': 750,
                                                    'Class': 'DecoratorAlwaysRunning',
                                                    'DecorateWhenChildEnds': False,
                                                    'Node': [
                                                        {
                                                            'ID': 758,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 763,
                                                                    'Class': 'Action',
                                                                    'Method': (Func7, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 764,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] },
                                        {
                                            'ID': 774,
                                            'Class': 'Condition',
                                            'Method': (Func8, ()) }] }] }] }] }] }
