# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pet/pet2282.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pet/pet2282.pyc
# Source Generated with Decompyle++
# File: pet2282.pyc (Python 3.6)

from cl_commondefines import PET_QUALITY_NORMAL, PET_TYPE_WIZARD, WARRIOR_ELITE, WARRIOR_SUMMON_STELE
from cl_resmgr.resdata import CPetData as CCustom

class CPetData(CCustom):
    m_SID = 2282
    m_MonsterDataSID = 2282
    m_Name = '虚妄僧'
    m_PetType = PET_TYPE_WIZARD
    m_Quality = PET_QUALITY_NORMAL
    m_AttPerform = 7306
    m_PerformList = (7306, 50701, 50714)
    m_AbilityGroup = (1018,)
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_HateFactor = 0.5
    m_Betree = 'Pet.RemotePetFsm'
    m_AIConfig = {
        'PFAI': 39286 }
    m_BaseAttrInfo = {
        'HPMax': 70000,
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
        'Att': 50000,
        'MoveSpeed': 350,
        'AttSpeed': 150,
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
        'RelifeTime': 1200,
        'SkillInterval': 800,
        'Scale': 100 }
    m_OffsetRange = {
        'HPMax': 20,
        'Att': 20,
        'AttSpeed': 20,
        'SkillInterval': 20 }
    m_Layer = 3
    m_Shape = 5639
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

