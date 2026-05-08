# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Pet/CombatPatrol.pyc
# RelativePath: clientlogic/cl_betreedata/Pet/CombatPatrol.pyc
# Source Generated with Decompyle++
# File: CombatPatrol.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.GetHeroDis(oAgent) > 12


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.GetHeroDis(oAgent) > 12

data = {
    'Name': 'CombatPatrol',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 76,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.SetActionSM, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 41,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 62,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 63,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 64,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 65,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.MoveToHeroPos, (8,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 44,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 61,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 0,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 55,
                                            'Class': 'SelectorProbability',
                                            'RandomGenerator': None,
                                            'Node': [
                                                {
                                                    'ID': 56,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 10,
                                                    'Node': [
                                                        {
                                                            'ID': 54,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 125 }] },
                                                {
                                                    'ID': 57,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 10,
                                                    'Node': [
                                                        {
                                                            'ID': 59,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 175 }] },
                                                {
                                                    'ID': 58,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 10,
                                                    'Node': [
                                                        {
                                                            'ID': 60,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 225 }] }] },
                                        {
                                            'ID': 42,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) }] },
                                {
                                    'ID': 46,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ChooseOwnerAroundPos, (6, 10, 0, 180)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 47,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 48,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
