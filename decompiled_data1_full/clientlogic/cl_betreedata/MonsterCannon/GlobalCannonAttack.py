# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterCannon/GlobalCannonAttack.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterCannon/GlobalCannonAttack.pyc
# Source Generated with Decompyle++
# File: GlobalCannonAttack.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.monsteragent.CAgent.CheckInLockEnemySight(60, 30, 0, oAgent) == True

data = {
    'Name': 'GlobalCannonAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 15,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseNearestHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 6,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (20, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 8,
                    'Class': 'Condition',
                    'Method': (Func0, ()) },
                {
                    'ID': 17,
                    'Class': 'Condition',
                    'Method': (Func1, ()) },
                {
                    'ID': 15,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ForceOccupyAttackToken, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 14,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 16,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ReleaseAttackToken, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
