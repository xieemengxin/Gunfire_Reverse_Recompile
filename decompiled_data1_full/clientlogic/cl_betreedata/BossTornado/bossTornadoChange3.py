# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossTornado/bossTornadoChange3.pyc
# RelativePath: clientlogic/cl_betreedata/BossTornado/bossTornadoChange3.pyc
# Source Generated with Decompyle++
# File: bossTornadoChange3.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(7957, oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'bossTornadoChange3',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 9,
    'Node': [
        {
            'ID': 17,
            'Class': 'IfElse',
            'Node': [
                {
                    'ID': 18,
                    'Class': 'Condition',
                    'Method': (Func0, ()) },
                {
                    'ID': 19,
                    'Class': 'Noop' },
                {
                    'ID': 1,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 14,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 15,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39156,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 2,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 6,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 7,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 9,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 10,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (8, 5, 15, 75, 105)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 11,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (8, 5, 15, 75, 105)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 12,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 13,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] },
                                {
                                    'ID': 8,
                                    'Class': 'WaitFrame',
                                    'Frames': 250 }] },
                        {
                            'ID': 3,
                            'Class': 'Action',
                            'Attachment': ({
                                'ID': 4,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' },),
                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 5,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 16,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.AddState, (7957, 0)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
