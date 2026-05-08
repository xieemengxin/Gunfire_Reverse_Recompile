# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterFourLeg/fourFuzzyChargeAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterFourLeg/fourFuzzyChargeAttack.pyc
# Source Generated with Decompyle++
# File: fourFuzzyChargeAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(3, 45, oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.IsLockEnemyPosRangeAccessible(1.5, oAgent) == False

data = {
    'Name': 'fourFuzzyChargeAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 94,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Attachment': ({
                'ID': 34,
                'Class': 'Precondition',
                'Method': (cl_betree.monsteragent.CAgent.SetFightLogicType, (3,)),
                'Phase': 1,
                'Flag': 'precondition',
                'BinaryOperator': 'And' },),
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
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 583,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 4,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 30,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 557,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 558,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (3, 6, 15, 30)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 559,
                                                    'Class': 'Sequence',
                                                    'Node': [
                                                        {
                                                            'ID': 560,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 561,
                                                            'Class': 'Action',
                                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 562,
                                                            'Class': 'Parallel',
                                                            'FailurePolicy': 1,
                                                            'SuccessPolicy': 0,
                                                            'ExitPolicy': 1,
                                                            'ChildFinishPolicy': 1,
                                                            'Node': [
                                                                {
                                                                    'ID': 563,
                                                                    'Class': 'Action',
                                                                    'Attachment': ({
                                                                        'ID': 575,
                                                                        'Class': 'Precondition',
                                                                        'Method': (cl_betree.monsteragent.CAgent.TryReChooseHateFlankPos, (3, 3, 6, 15, 30)),
                                                                        'Phase': 1,
                                                                        'Flag': 'precondition',
                                                                        'BinaryOperator': 'And' },),
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 564,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 565,
                                                                            'Class': 'And',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 567,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func0, ()) },
                                                                                {
                                                                                    'ID': 568,
                                                                                    'Class': 'Condition',
                                                                                    'Method': (Func1, ()) }] },
                                                                        {
                                                                            'ID': 566,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] }] }] }] },
                                {
                                    'ID': 7,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 5,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 584,
                            'Class': 'Condition',
                            'Method': (Func2, ()) }] },
                {
                    'ID': 37,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 556,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 576,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 577,
                                    'Class': 'Action',
                                    'Method': (Func3, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 578,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 581,
                                            'Class': 'Condition',
                                            'Method': (Func4, ()) },
                                        {
                                            'ID': 582,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (20211,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 517,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 554,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' },),
                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 421,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
