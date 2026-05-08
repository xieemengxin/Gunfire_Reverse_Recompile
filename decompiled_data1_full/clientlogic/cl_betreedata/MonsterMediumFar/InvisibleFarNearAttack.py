# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterMediumFar/InvisibleFarNearAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterMediumFar/InvisibleFarNearAttack.pyc
# Source Generated with Decompyle++
# File: InvisibleFarNearAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetPhase(oAgent) != 2


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.MoveToLockEnemy(oAgent.GetData('CurPerformUseDis'), oAgent)

data = {
    'Name': 'InvisibleFarNearAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 114,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 36,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 749,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 750,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 751,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 746,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (21423,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 747,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 752,
                            'Class': 'Noop' }] },
                {
                    'ID': 744,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (21422,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 737,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 738,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 745,
                    'Class': 'Action',
                    'Method': (Func1, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 740,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 110,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 741,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 748,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.RemoveState, (7063,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
