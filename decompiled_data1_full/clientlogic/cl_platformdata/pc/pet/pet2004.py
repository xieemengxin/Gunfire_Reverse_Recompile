# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pet/pet2004.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pet/pet2004.pyc
# Source Generated with Decompyle++
# File: pet2004.pyc (Python 3.6)

from cl_commondefines import PET_QUALITY_NORMAL, PET_TYPE_SHIELD, WARRIOR_ELITE, WARRIOR_SUMMON_STELE
from cl_resmgr.resdata import CPetData as CCustom

class CPetData(CCustom):
    m_SID = 2004
    m_MonsterDataSID = 2004
    m_Name = '自爆灯笼鬼'
    m_PetType = PET_TYPE_SHIELD
    m_Quality = PET_QUALITY_NORMAL
    m_AttPerform = 7319
    m_PerformList = (7319, 50701, 50714, 50716, 50718)
    m_AbilityGroup = (1016,)
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_HateFactor = 0.2
    m_Betree = 'Pet.CombatPetFsm'
    m_AIConfig = {
        'PFAI': 39288 }
    m_BaseAttrInfo = {
        'HPMax': 15000,
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 0,
        'ShieldRecoverTime': 0,
        'DefPhysical': (0, None, ((221,), (204,), (221,), (lambda a0, a1, a2: 5000 * (1 - 1.4 / ((a0 * 0.2 + 1.8) * (1 + (a1 - 1) * 0.1 * (1 + (a2 // 8) * 1))))))),
        'DefThunder': (0, None, ((221,), (204,), (221,), (lambda a0, a1, a2: 5000 * (1 - 1.4 / ((a0 * 0.2 + 1.8) * (1 + (a1 - 1) * 0.1 * (1 + (a2 // 8) * 1))))))),
        'DefCorrision': (0, None, ((221,), (204,), (221,), (lambda a0, a1, a2: 5000 * (1 - 1.4 / ((a0 * 0.2 + 1.8) * (1 + (a1 - 1) * 0.1 * (1 + (a2 // 8) * 1))))))),
        'DefFire': (0, None, ((221,), (204,), (221,), (lambda a0, a1, a2: 5000 * (1 - 1.4 / ((a0 * 0.2 + 1.8) * (1 + (a1 - 1) * 0.1 * (1 + (a2 // 8) * 1))))))),
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 0,
        'DefKnockBack': 0,
        'KnockBackFrame': 0,
        'DefThump': 0,
        'ThumpFrame': 0,
        'Att': 90000,
        'MoveSpeed': 1200,
        'AttSpeed': 20,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 300,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'RelifeTime': 300,
        'SkillInterval': 1000,
        'Scale': 100 }
    m_OffsetRange = {
        'HPMax': 20,
        'Att': 20,
        'AttSpeed': 20,
        'SkillInterval': 20 }
    m_Layer = 1
    m_Shape = 5602
    m_BaseHate = {
        'Default': 50,
        'FightType': {
            WARRIOR_SUMMON_STELE: 80,
            WARRIOR_ELITE: 100 },
        2201: 100,
        3905: 500,
        2202: 100,
        2341: 500,
        2342: 500,
        2343: 500,
        3925: 500 }
    m_HateDisEff = {
        'HeroDisEff': ((22, 1), (30, 0.5), (40, 0.3)),
        'ServantDisEff': ((5, 1), (15, 0.75)) }

