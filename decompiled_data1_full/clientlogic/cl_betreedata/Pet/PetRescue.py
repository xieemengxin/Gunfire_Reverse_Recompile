# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Pet/PetRescue.pyc
# RelativePath: clientlogic/cl_betreedata/Pet/PetRescue.pyc
# Source Generated with Decompyle++
# File: PetRescue.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.CheckToRescueTargetDis(4, oAgent) == True

data = {
    'Name': 'PetRescue',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 25,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 0,
                    'ExitPolicy': 0,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 6,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 7,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 8,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 9,
                                    'Class': 'Action',
                                    'Attachment': ({
                                        'ID': 10,
                                        'Class': 'Precondition',
                                        'Method': (cl_betree.servantagent.CAgent.ChooseRescueTargetPos, (4,)),
                                        'Phase': 2,
                                        'Flag': 'precondition',
                                        'BinaryOperator': 'And' },),
                                    'Method': (cl_betree.servantagent.CAgent.MoveToPos, (4,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.StopMoving, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.FaceRescueTarget, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.RescueTarget, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
