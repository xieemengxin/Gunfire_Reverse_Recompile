# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/servant/s303.pyc
# RelativePath: clientlogic/cl_platformdata/pc/servant/s303.pyc
# Source Generated with Decompyle++
# File: s303.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_NONE, WARRIOR_ELITE, WARRIOR_SPARE, WARRIOR_SUMMON_STELE
from cl_resmgr.resdata import CServantData as CCustom

class CServantData(CCustom):
    m_SID = 303
    m_Name = '天袭分身'
    m_Shape = 5611
    m_FightType = WARRIOR_SPARE
    m_AttPerform = 7176
    m_PerformList = (5372,)
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_Betree = 'Spare.SpareTestFsm'
    m_AIConfig = {
        'PFAI': 39301 }
    m_DefendTrend = DEFEND_TREND_NONE
    m_BaseAttrInfo = {
        1: {
            1: {
                'HPMax': 2000,
                'RHP': 0,
                'ArmorMax': 0,
                'ShieldMax': 0,
                'RShield': 0,
                'ShieldRecoverTime': 0,
                'DefPhysical': 0,
                'DefThunder': 0,
                'DefCorrision': 0,
                'DefFire': 0,
                'AccuracyProb': 100,
                'StruckIgnoreFrame': 0,
                'DefKnockBack': 0,
                'KnockBackFrame': 0,
                'DefThump': 0,
                'ThumpFrame': 0,
                'Att': 50000,
                'MoveSpeed': 700,
                'AttSpeed': 100,
                'Toughness': 0,
                'TurnSpeed': 14,
                'TurnThresholdAngle': 0,
                'TurnInterval': 0,
                'AdsorbDis': 0,
                'HardEff': 0,
                'SaveTime': 300,
                'DodgeProb': 0,
                'IntervalTime': 0,
                'EnergyMax': 0,
                'REnergy': 0,
                'SpecialMHPWeight': 0,
                'LifeTime': 0,
                'HitRange': 0 } },
        2: {
            1: {
                'HPMax': 2000,
                'RHP': 0,
                'ArmorMax': 0,
                'ShieldMax': 0,
                'RShield': 0,
                'ShieldRecoverTime': 0,
                'DefPhysical': 0,
                'DefThunder': 0,
                'DefCorrision': 0,
                'DefFire': 0,
                'AccuracyProb': 100,
                'StruckIgnoreFrame': 0,
                'DefKnockBack': 0,
                'KnockBackFrame': 0,
                'DefThump': 0,
                'ThumpFrame': 0,
                'Att': 50000,
                'MoveSpeed': 700,
                'AttSpeed': 100,
                'Toughness': 0,
                'TurnSpeed': 14,
                'TurnThresholdAngle': 0,
                'TurnInterval': 0,
                'AdsorbDis': 0,
                'HardEff': 0,
                'SaveTime': 300,
                'DodgeProb': 0,
                'IntervalTime': 0,
                'EnergyMax': 0,
                'REnergy': 0,
                'SpecialMHPWeight': 0,
                'LifeTime': 0,
                'HitRange': 0 } },
        3: {
            1: {
                'HPMax': 2000,
                'RHP': 0,
                'ArmorMax': 0,
                'ShieldMax': 0,
                'RShield': 0,
                'ShieldRecoverTime': 0,
                'DefPhysical': 0,
                'DefThunder': 0,
                'DefCorrision': 0,
                'DefFire': 0,
                'AccuracyProb': 100,
                'StruckIgnoreFrame': 0,
                'DefKnockBack': 0,
                'KnockBackFrame': 0,
                'DefThump': 0,
                'ThumpFrame': 0,
                'Att': 50000,
                'MoveSpeed': 700,
                'AttSpeed': 100,
                'Toughness': 0,
                'TurnSpeed': 14,
                'TurnThresholdAngle': 0,
                'TurnInterval': 0,
                'AdsorbDis': 0,
                'HardEff': 0,
                'SaveTime': 300,
                'DodgeProb': 0,
                'IntervalTime': 0,
                'EnergyMax': 0,
                'REnergy': 0,
                'SpecialMHPWeight': 0,
                'LifeTime': 0,
                'HitRange': 0 } } }
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

