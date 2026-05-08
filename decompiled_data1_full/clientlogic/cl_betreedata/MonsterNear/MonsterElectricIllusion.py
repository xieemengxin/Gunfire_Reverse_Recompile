# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterNear/MonsterElectricIllusion.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterNear/MonsterElectricIllusion.pyc
# Source Generated with Decompyle++
# File: MonsterElectricIllusion.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.ChoosePsychTarget(30, oAgent) == 1

data = {
    'Name': 'MonsterElectricIllusion',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 3,
    'Node': [
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
                    'Method': (Func0, ()) },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (22055,)),
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
                    'ResultFunctor': None }] }] }
