# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossTornado/bossTornadoPhase1FirstAttack.pyc
# RelativePath: clientlogic/cl_betreedata/BossTornado/bossTornadoPhase1FirstAttack.pyc
# Source Generated with Decompyle++
# File: bossTornadoPhase1FirstAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'bossTornadoPhase1FirstAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 100,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 89,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusAttack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 157,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 0,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 158,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 162,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39152,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 163,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 166,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 172,
                                                    'Class': 'Condition',
                                                    'Method': (Func0, ()) },
                                                {
                                                    'ID': 173,
                                                    'Class': 'DecoratorAlwaysRunning',
                                                    'DecorateWhenChildEnds': False,
                                                    'Node': [
                                                        {
                                                            'ID': 178,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 179,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (8, 5, 15, 75, 105)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 180,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 181,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 182,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] }] },
                                                {
                                                    'ID': 174,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 60 }] },
                                        {
                                            'ID': 167,
                                            'Class': 'Action',
                                            'Attachment': ({
                                                'ID': 168,
                                                'Class': 'Precondition',
                                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                'Phase': 1,
                                                'Flag': 'precondition',
                                                'BinaryOperator': 'And' },),
                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 169,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] }] }] }] }
