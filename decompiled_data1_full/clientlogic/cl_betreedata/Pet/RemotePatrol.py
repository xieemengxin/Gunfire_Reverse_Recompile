# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Pet/RemotePatrol.pyc
# RelativePath: clientlogic/cl_betreedata/Pet/RemotePatrol.pyc
# Source Generated with Decompyle++
# File: RemotePatrol.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.GetHeroDis(oAgent) > 12


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.GetHeroDis(oAgent) > 12

data = {
    'Name': 'RemotePatrol',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 68,
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
                    'ID': 26,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 27,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 44,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 45,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 46,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.MoveToHeroPos, (8,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 29,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 35,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 0,
                                    'ChildFinishPolicy': 1,
                                    'Node': [
                                        {
                                            'ID': 37,
                                            'Class': 'SelectorProbability',
                                            'RandomGenerator': None,
                                            'Node': [
                                                {
                                                    'ID': 38,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 10,
                                                    'Node': [
                                                        {
                                                            'ID': 30,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 125 }] },
                                                {
                                                    'ID': 39,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 10,
                                                    'Node': [
                                                        {
                                                            'ID': 42,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 175 }] },
                                                {
                                                    'ID': 40,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 10,
                                                    'Node': [
                                                        {
                                                            'ID': 43,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 225 }] }] },
                                        {
                                            'ID': 41,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) }] },
                                {
                                    'ID': 31,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ChooseOwnerAroundPos, (2, 5, 0, 180)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 32,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 33,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (1,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
