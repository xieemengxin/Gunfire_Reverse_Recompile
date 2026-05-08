# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteNear/EliteNearMoveClaw.pyc
# RelativePath: clientlogic/cl_betreedata/EliteNear/EliteNearMoveClaw.pyc
# Source Generated with Decompyle++
# File: EliteNearMoveClaw.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.ChooseRangeHidePosAndAttPos(1, 10, oAgent) == 1


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckLockAlive(oAgent) != False


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockTargetDis(oAgent) <= 8

data = {
    'Name': 'EliteNearMoveClaw',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 94,
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
                    'ID': 55,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 56,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 90,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 83,
                            'Class': 'Parallel',
                            'FailurePolicy': 1,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 1,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 153,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 154,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseTargetAwayPos, (30, 90, 10, 0.5)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 156,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 162,
                                            'Class': 'IfElse',
                                            'Node': [
                                                {
                                                    'ID': 163,
                                                    'Class': 'Condition',
                                                    'Method': (Func0, ()) },
                                                {
                                                    'ID': 164,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 165,
                                                    'Class': 'Noop' }] },
                                        {
                                            'ID': 179,
                                            'Class': 'WaitFrame',
                                            'Frames': 300 }] },
                                {
                                    'ID': 166,
                                    'Class': 'WaitFrame',
                                    'Frames': 150 }] },
                        {
                            'ID': 206,
                            'Class': 'DecoratorAlwaysSuccess',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 185,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 186,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.HateAllPlayer, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 187,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseNearestHateTarget, (0,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 190,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 191,
                                    'Class': 'And',
                                    'Node': [
                                        {
                                            'ID': 199,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 192,
                                            'Class': 'Condition',
                                            'Method': (Func2, ()) }] },
                                {
                                    'ID': 194,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 195,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.ChooseHateFlankPos, (1, 2, 0, 90)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 204,
                                            'Class': 'Parallel',
                                            'FailurePolicy': 1,
                                            'SuccessPolicy': 0,
                                            'ExitPolicy': 1,
                                            'ChildFinishPolicy': 1,
                                            'Node': [
                                                {
                                                    'ID': 196,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 205,
                                                    'Class': 'WaitFrame',
                                                    'Frames': 125 }] },
                                        {
                                            'ID': 207,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.UseCertainPFToPos, (31840, 0, 0, 0)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 202,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.UseCertainPFToPos, (31840, 0, 0, 0)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 203,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetPhase, (4,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
