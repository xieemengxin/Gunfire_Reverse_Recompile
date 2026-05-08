# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossTornado/bossTorandoSpin2.pyc
# RelativePath: clientlogic/cl_betreedata/BossTornado/bossTorandoSpin2.pyc
# Source Generated with Decompyle++
# File: bossTorandoSpin2.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(7967, oAgent) == True

data = {
    'Name': 'bossTorandoSpin2',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 3,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateHero, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (0, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 6,
                    'Class': 'Parallel',
                    'Attachment': ({
                        'ID': 7,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'FailurePolicy': 0,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 13,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 14,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 20,
                                    'Class': 'WaitFrame',
                                    'Frames': 37 },
                                {
                                    'ID': 21,
                                    'Class': 'DecoratorAlwaysRunning',
                                    'DecorateWhenChildEnds': False,
                                    'Node': [
                                        {
                                            'ID': 22,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 23,
                                                    'Class': 'Parallel',
                                                    'FailurePolicy': 1,
                                                    'SuccessPolicy': 0,
                                                    'ExitPolicy': 1,
                                                    'ChildFinishPolicy': 1,
                                                    'Node': [
                                                        {
                                                            'ID': 26,
                                                            'Class': 'DecoratorAlwaysRunning',
                                                            'DecorateWhenChildEnds': False,
                                                            'Node': [
                                                                {
                                                                    'ID': 28,
                                                                    'Class': 'Sequence',
                                                                    'Node': [
                                                                        {
                                                                            'ID': 29,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateHero, (0,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 30,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (0, 1)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None }] }] }] },
                                                {
                                                    'ID': 24,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 25,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 12 }] }] }] }] },
                {
                    'ID': 8,
                    'Class': 'IfElse',
                    'Attachment': ({
                        'ID': 9,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Node': [
                        {
                            'ID': 15,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 16,
                            'Class': 'WaitFrame',
                            'Frames': 38 },
                        {
                            'ID': 17,
                            'Class': 'WaitFrame',
                            'Frames': 28 }] }] }] }
