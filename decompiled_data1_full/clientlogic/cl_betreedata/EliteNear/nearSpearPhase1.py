# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteNear/nearSpearPhase1.pyc
# RelativePath: clientlogic/cl_betreedata/EliteNear/nearSpearPhase1.pyc
# Source Generated with Decompyle++
# File: nearSpearPhase1.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.IsLockEnemyPosRangeAccessible(1.5, oAgent) == False

data = {
    'Name': 'nearSpearPhase1',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 87,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 30,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 48,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 22,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 25,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 46,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.LimitChoosePFDistance, (0, 12)),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' },),
                            'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 23,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 50,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (5,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 37,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 28,
                            'Class': 'Action',
                            'Method': (Func0, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 39,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 40,
                                    'Class': 'WaitFrame',
                                    'Frames': 25 },
                                {
                                    'ID': 56,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 38,
                                    'Class': 'Condition',
                                    'Method': (Func2, ()) },
                                {
                                    'ID': 44,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 45,
                                        'Class': 'Precondition',
                                        'Attachment': ({
                                            'ID': 63,
                                            'Class': 'Precondition',
                                            'Method': (cl_betree.monsteragent.CAgent.LimitChoosePFDistance, (12, 0)),
                                            'Phase': 1,
                                            'Flag': 'precondition',
                                            'BinaryOperator': 'And' },),
                                        'Method': (cl_betree.monsteragent.CAgent.LimitChoosePFDistance, (12, 0)),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 61,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 60,
                                    'Class': 'WaitFrame',
                                    'Frames': 250 },
                                {
                                    'ID': 62,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 64,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.monsteragent.CAgent.LimitChoosePFDistance, (12, 0)),
                                        'Phase': 1,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
