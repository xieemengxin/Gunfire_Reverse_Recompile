# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterCannon/CannonIllusion.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterCannon/CannonIllusion.pyc
# Source Generated with Decompyle++
# File: CannonIllusion.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.ChoosePsychTarget(30, oAgent) == 1


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True

data = {
    'Name': 'CannonIllusion',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 23,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Attachment': ({
                'ID': 12,
                'Class': 'Precondition',
                'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                'Phase': 1,
                'Flag': 'precondition',
                'BinaryOperator': 'And' },),
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Condition',
                    'Method': (Func0, ()) },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (20412,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 8,
                    'Class': 'Condition',
                    'Method': (Func1, ()) },
                {
                    'ID': 15,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 16,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 7,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
