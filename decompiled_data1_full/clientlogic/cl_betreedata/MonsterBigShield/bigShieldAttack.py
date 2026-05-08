# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterBigShield/bigShieldAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterBigShield/bigShieldAttack.pyc
# Source Generated with Decompyle++
# File: bigShieldAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(2, oAgent.GetConfig('IntervalTime'), oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 4


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 21232


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 31232


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 21252


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 31252


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == False


def Func10(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)

data = {
    'Name': 'bigShieldAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 111,
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
                    'ID': 37,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusAttack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 208,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 92,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 163,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 165,
                                            'Class': 'Condition',
                                            'Method': (Func0, ()) },
                                        {
                                            'ID': 179,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 78,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 93,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 183,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 184,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 185,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 186,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (4,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 187,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 181,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) },
                                        {
                                            'ID': 188,
                                            'Class': 'Condition',
                                            'Method': (Func3, ()) },
                                        {
                                            'ID': 182,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 209,
                            'Class': 'Condition',
                            'Method': (Func4, ()) }] },
                {
                    'ID': 189,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 206,
                            'Class': 'And',
                            'Node': [
                                {
                                    'ID': 199,
                                    'Class': 'Or',
                                    'Node': [
                                        {
                                            'ID': 200,
                                            'Class': 'Or',
                                            'Node': [
                                                {
                                                    'ID': 201,
                                                    'Class': 'Condition',
                                                    'Method': (Func5, ()) },
                                                {
                                                    'ID': 202,
                                                    'Class': 'Condition',
                                                    'Method': (Func6, ()) }] },
                                        {
                                            'ID': 203,
                                            'Class': 'Or',
                                            'Node': [
                                                {
                                                    'ID': 204,
                                                    'Class': 'Condition',
                                                    'Method': (Func7, ()) },
                                                {
                                                    'ID': 205,
                                                    'Class': 'Condition',
                                                    'Method': (Func8, ()) }] }] },
                                {
                                    'ID': 207,
                                    'Class': 'Condition',
                                    'Method': (Func9, ()) }] },
                        {
                            'ID': 194,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 142,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 174,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 143,
                                    'Class': 'Action',
                                    'Method': (Func10, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 198,
                            'Class': 'Noop' }] },
                {
                    'ID': 195,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 197,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (50, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 196,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
