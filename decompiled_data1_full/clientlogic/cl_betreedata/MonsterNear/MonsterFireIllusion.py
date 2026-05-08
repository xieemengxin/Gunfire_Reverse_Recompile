# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterNear/MonsterFireIllusion.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterNear/MonsterFireIllusion.pyc
# Source Generated with Decompyle++
# File: MonsterFireIllusion.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckArriveShowPos(oAgent) == False


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.ChoosePsychTarget(30, oAgent) == 1

data = {
    'Name': 'MonsterFireIllusion',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 3,
    'Node': [
        {
            'ID': 7,
            'Class': 'Sequence',
            'Node': [
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
                                    'ID': 13,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseShowPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 14,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 15,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 16,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 17,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.AddState, (8094, 0)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 1,
                            'Class': 'Sequence',
                            'Attachment': ({
                                'ID': 2,
                                'Class': 'Precondition',
                                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                                'Phase': 1,
                                'Flag': 'precondition',
                                'BinaryOperator': 'And' },),
                            'Node': [
                                {
                                    'ID': 3,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 4,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (22015,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 5,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (0, 0)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 6,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
