# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pet/pet2164.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pet/pet2164.pyc
# Source Generated with Decompyle++
# File: pet2164.pyc (Python 3.6)

from cl_commondefines import PET_QUALITY_NORMAL, PET_TYPE_SNIPER, WARRIOR_ELITE, WARRIOR_SUMMON_STELE
from cl_newformula import Func204, Func221
from cl_resmgr.resdata import CPetData as CCustom

class CPetData(CCustom):
    m_SID = 2164
    m_MonsterDataSID = 2164
    m_Name = '幽冥猎手'
    m_PetType = PET_TYPE_SNIPER
    m_Quality = PET_QUALITY_NORMAL
    m_AttPerform = 7317
    m_PerformList = (50701, 50714, 50721)
    m_AbilityGroup = (1019,)
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_HateFactor = 0.5
    m_Betree = 'Pet.RemotePetKeepFireFsm'
    m_AIConfig = {
        'PFAI': 39282 }
    m_BaseAttrInfo = {
        'HPMax': 40000,
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 0,
        'ShieldRecoverTime': 0,
        'DefPhysical': (lambda *a: 5000 * (1 - 1.4 / ((Func221(*a) * 0.2 + 1.8) * (1 + (Func204(*a) - 1) * 0.1 * (1 + (Func221(*a) // 8) * 1))))),
        'DefThunder': (lambda *a: 5000 * (1 - 1.4 / ((Func221(*a) * 0.2 + 1.8) * (1 + (Func204(*a) - 1) * 0.1 * (1 + (Func221(*a) // 8) * 1))))),
        'DefCorrision': (lambda *a: 5000 * (1 - 1.4 / ((Func221(*a) * 0.2 + 1.8) * (1 + (Func204(*a) - 1) * 0.1 * (1 + (Func221(*a) // 8) * 1))))),
        'DefFire': (lambda *a: 5000 * (1 - 1.4 / ((Func221(*a) * 0.2 + 1.8) * (1 + (Func204(*a) - 1) * 0.1 * (1 + (Func221(*a) // 8) * 1))))),
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 0,
        'DefKnockBack': 0,
        'KnockBackFrame': 0,
        'DefThump': 0,
        'ThumpFrame': 0,
        'Att': 60000,
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
        'SpecialMHPWeight': 0,
        'RelifeTime': 700,
        'SkillInterval': 1000,
        'Scale': 100 }
    m_OffsetRange = {
        'HPMax': 20,
        'Att': 20,
        'AttSpeed': 20,
        'SkillInterval': 20 }
    m_Layer = 4
    m_Shape = 5629
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

