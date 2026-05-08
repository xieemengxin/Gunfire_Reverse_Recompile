# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/EliteFar/EliteRidePhase2.pyc
# RelativePath: clientlogic/cl_betreedata/EliteFar/EliteRidePhase2.pyc
# Source Generated with Decompyle++
# File: EliteRidePhase2.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.ChoosePF(1, oAgent) == 1


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.GetChoosePF(oAgent) == 33817


def Func2(oAgent):
    return cl_betree.monsteragent.CAgent.GetLockEnemyDis(oAgent) >= 12


def Func3(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == False

data = {
    'Name': 'EliteRidePhase2',
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
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 27,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 8,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 9,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 10,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 4,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 6,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 7,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 11,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 12,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 5,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 13,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 14,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 15,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 16,
                                                    'Class': 'IfElse',
                                                    'Node': [
                                                        {
                                                            'ID': 24,
                                                            'Class': 'Or',
                                                            'Node': [
                                                                {
                                                                    'ID': 17,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func2, ()) },
                                                                {
                                                                    'ID': 25,
                                                                    'Class': 'Condition',
                                                                    'Method': (Func3, ()) }] },
                                                        {
                                                            'ID': 19,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 20,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (33811,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 26,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (0,)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 21,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 22,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.monsteragent.CAgent.AddState, (7117, 100)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None }] },
                                                        {
                                                            'ID': 18,
                                                            'Class': 'Noop' }] }] }] }] },
                        {
                            'ID': 28,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 30,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseTargetAwayPos, (20, 90, 10, 0.5)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 31,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 32,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 33,
                                    'Class': 'WaitFrame',
                                    'Frames': 25 }] }] }] }] }
