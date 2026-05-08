# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Plant/PlantAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Plant/PlantAttack.pyc
# Source Generated with Decompyle++
# File: PlantAttack.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.HateAllTargetByType(oAgent.GetData('HateSummon'), oAgent.GetData('HataProtege'), oAgent)


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.ChooseSeeEnemy(1, oAgent.GetConfig('HitRange'), oAgent)

data = {
    'Name': 'PlantAttack',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 22,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 8,
                    'Class': 'Action',
                    'Method': (Func0, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 6,
                    'Class': 'Action',
                    'Method': (Func1, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.FaceLockEnemy, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.ChoosePF, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.Attack, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 7,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.UpdateInAdvance, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
