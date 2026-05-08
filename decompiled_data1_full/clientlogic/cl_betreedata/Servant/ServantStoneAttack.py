# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Servant/ServantStoneAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Servant/ServantStoneAttack.pyc
# Source Generated with Decompyle++
# File: ServantStoneAttack.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.GetChoosePF(oAgent) == 7142

data = {
    'Name': 'ServantStoneAttack',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 98,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 28,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.ChooseHateTarget, (1, 0)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 7,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.FaceLockEnemy, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 116,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 0,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 119,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 114,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ChoosePFByArgs, (13.4,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 122,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 123,
                                            'Class': 'Condition',
                                            'Method': (Func0, ()) },
                                        {
                                            'ID': 124,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.SpecifyEndPosOffset, (-9.71, -0.02, 19.89, False, True)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 125,
                                            'Class': 'DecoratorAlwaysSuccess',
                                            'DecorateWhenChildEnds': False }] }] },
                        {
                            'ID': 117,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 110,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.SpecifyEndPosOffset, (-10.82, 0.12, 19.89, True, False)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 118,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (0.5,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 40,
                        'Class': 'Precondition',
                        'Method': (cl_betree.servantagent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.servantagent.CAgent.Attack, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 39,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.UpdateInAdvance, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
