# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteBigShield/EliteDesertShieldFarAttack.pyc
# RelativePath: clientlogic/cl_betreedata/EliteBigShield/EliteDesertShieldFarAttack.pyc
# Source Generated with Decompyle++
# File: EliteDesertShieldFarAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == False


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.IsTooApproachedToTarget(4, 45, oAgent) == True


def Func4(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) == True

data = {
    'Name': 'EliteDesertShieldFarAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 191,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 207,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 2,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 184,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 183,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 185,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 204,
                                                    'Class': 'Condition',
                                                    'Method': (Func1, ()) },
                                                {
                                                    'ID': 187,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 190,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (8, 12, 15, 45)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 188,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 192,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 193,
                                                            'Class': 'Action',
                                                            'Attachment': ({
                                                                'ID': 199,
                                                                'Class': 'Precondition',
                                                                'Method': (cl_betree.monsteragent.CAgent.TryReChooseHateFlankPos, (3, 8, 12, 15, 45)),
                                                                'Phase': 1,
                                                                'Flag': 'precondition',
                                                                'BinaryOperator': 'And' },),
                                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                            'ResultOption': 0,
                                                            'ResultFunctor': None },
                                                        {
                                                            'ID': 194,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 200,
                                                                    'Class': 'And',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 205,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func2, ()) },
                                                                        {
                                                                            'ID': 206,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func3, ()) }] },
                                                                {
                                                                    'ID': 201,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] }] }] }] },
                        {
                            'ID': 208,
                            'Class': 'Condition',
                            'Method': (Func4, ()) }] },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 181,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 182,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
