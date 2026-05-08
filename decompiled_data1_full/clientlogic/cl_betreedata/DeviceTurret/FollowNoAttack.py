# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DeviceTurret/FollowNoAttack.pyc
# RelativePath: clientlogic/cl_betreedata/DeviceTurret/FollowNoAttack.pyc
# Source Generated with Decompyle++
# File: FollowNoAttack.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.CheckInHeroSight(30, oAgent) == True


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.GetHeroDis(oAgent) <= 12


def Func2(oAgent):
    return cl_betree.servantagent.CAgent.GetHeroDis(oAgent) >= 8


def Func3(oAgent):
    return cl_betree.servantagent.CAgent.CheckInHeroSight(40, oAgent) == False


def Func4(oAgent):
    return cl_betree.servantagent.CAgent.GetHeroDis(oAgent) > 15


def Func5(oAgent):
    return cl_betree.servantagent.CAgent.GetHeroDis(oAgent) < 5

data = {
    'Name': 'FollowNoAttack',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 44,
    'Node': [
        {
            'ID': 45,
            'Class': 'IfElse',
            'Node': [
                {
                    'ID': 46,
                    'Class': 'And',
                    'Node': [
                        {
                            'ID': 47,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 48,
                            'Class': 'And',
                            'Node': [
                                {
                                    'ID': 49,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 50,
                                    'Class': 'Condition',
                                    'Method': (Func2, ()) }] }] },
                {
                    'ID': 51,
                    'Class': 'Parallel',
                    'FailurePolicy': 0,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 0,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 21,
                            'Class': 'SelectorProbability',
                            'RandomGenerator': None,
                            'Node': [
                                {
                                    'ID': 22,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 10,
                                    'Node': [
                                        {
                                            'ID': 25,
                                            'Class': 'WaitFrame',
                                            'Frames': 50 }] },
                                {
                                    'ID': 23,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 10,
                                    'Node': [
                                        {
                                            'ID': 26,
                                            'Class': 'WaitFrame',
                                            'Frames': 75 }] },
                                {
                                    'ID': 24,
                                    'Class': 'DecoratorWeight',
                                    'DecorateWhenChildEnds': False,
                                    'Weight': 10,
                                    'Node': [
                                        {
                                            'ID': 27,
                                            'Class': 'WaitFrame',
                                            'Frames': 100 }] }] },
                        {
                            'ID': 52,
                            'Class': 'Or',
                            'Node': [
                                {
                                    'ID': 53,
                                    'Class': 'Condition',
                                    'Method': (Func3, ()) },
                                {
                                    'ID': 54,
                                    'Class': 'Or',
                                    'Node': [
                                        {
                                            'ID': 55,
                                            'Class': 'Condition',
                                            'Method': (Func4, ()) },
                                        {
                                            'ID': 56,
                                            'Class': 'Condition',
                                            'Method': (Func5, ()) }] }] }] },
                {
                    'ID': 39,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 35,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.ChooseOwnerAroundPos, (8, 12, 10, 30)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 41,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 57,
                            'Class': 'Parallel',
                            'FailurePolicy': 0,
                            'SuccessPolicy': 0,
                            'ExitPolicy': 0,
                            'ChildFinishPolicy': 1,
                            'Node': [
                                {
                                    'ID': 5,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (2,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 58,
                                    'Class': 'WaitFrame',
                                    'Frames': 10 }] }] }] }] }
