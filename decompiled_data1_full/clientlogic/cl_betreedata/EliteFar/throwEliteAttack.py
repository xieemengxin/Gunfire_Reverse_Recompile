# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteFar/throwEliteAttack.pyc
# RelativePath: clientlogic/cl_betreedata/EliteFar/throwEliteAttack.pyc
# Source Generated with Decompyle++
# File: throwEliteAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 8


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.IsPerformUseArea(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockCoveredByMonster(oAgent) == False


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.StartAttack(0, 50, oAgent) == True


def Func5(oAgent):
    return cl_betree.monsteragent.CAgent.GetFirstRangedArrivePosDis(oAgent) >= 4


def Func6(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func7(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func8(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func9(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True

data = {
    'Name': 'throwEliteAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 151,
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
                    'ID': 218,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 243,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 244,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 245,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
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
                                    'ID': 187,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 146,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 198,
                                            'Class': 'And',
                                            'Node': [
                                                {
                                                    'ID': 108,
                                                    'Class': 'And',
                                                    'Node': [
                                                        {
                                                            'ID': 114,
                                                            'Class': 'Condition',
                                                            'Method': (Func1, ()) },
                                                        {
                                                            'ID': 113,
                                                            'Class': 'Condition',
                                                            'Method': (Func2, ()) }] },
                                                {
                                                    'ID': 199,
                                                    'Class': 'Condition',
                                                    'Method': (Func3, ()) }] },
                                        {
                                            'ID': 216,
                                            'Class': 'Condition',
                                            'Method': (Func4, ()) }] },
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
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (10, 4, 8, 75, 105)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 188,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 207,
                                                            'Class': 'Condition',
                                                            'Method': (Func5, ()) },
                                                        {
                                                            'ID': 208,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 210,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 211,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 219,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 229,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 230,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 235,
                                                                                    'Class': 'And',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 241,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func6, ()) },
                                                                                        {
                                                                                            'ID': 242,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func7, ()) }] },
                                                                                {
                                                                                    'ID': 236,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] }] }] },
                                                        {
                                                            'ID': 209,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 213,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 214,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 226,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 1,
                                                                    'SuccessPolicy': 0,
                                                                    'ExitPolicy': 1,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 227,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 228,
                                                                            'Class': 'Sequence',
                                                                            'Node': [
                                                                                {
                                                                                    'ID': 233,
                                                                                    'Class': 'And',
                                                                                    'Node': [
                                                                                        {
                                                                                            'ID': 239,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func8, ()) },
                                                                                        {
                                                                                            'ID': 240,
                                                                                            'Class': 'Condition',
                                                                                            'Method': (Func9, ()) }] },
                                                                                {
                                                                                    'ID': 234,
                                                                                    'Class': 'Action',
                                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                                    'ResultOption': 0,
                                                                                    'ResultFunctor': None }] }] }] }] }] }] }] }] }] }] }
