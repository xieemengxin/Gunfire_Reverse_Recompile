# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/servant/s301.pyc
# RelativePath: clientlogic/cl_platformdata/pc/servant/s301.pyc
# Source Generated with Decompyle++
# File: s301.pyc (Python 3.6)

from cl_commondefines import DEFEND_TREND_NONE, WARRIOR_ELITE, WARRIOR_MECH, WARRIOR_SUMMON_STELE
from cl_newformula import Func204, Func221, Func569
from cl_resmgr.resdata import CServantData as CCustom

class CServantData(CCustom):
    m_SID = 301
    m_Name = '铁翼'
    m_Shape = 1101
    m_FightType = WARRIOR_MECH
    m_AttPerform = 7141
    m_PerformList = (4332, 7142, 7143, 7144, 7145, 7146, 7153, 7154, 7151, 7152, 4357, 4359)
    m_DefaultPhase = 1
    m_PhasePF = {
        2: 4346 }
    m_Betree = 'Servant.ServantFsm'
    m_AIConfig = {
        'PFAI': 39245 }
    m_DefendTrend = DEFEND_TREND_NONE
    m_BaseAttrInfo = {
        1: {
            1: {
                'HPMax': (lambda *a: 40000 * (1 + Func569(*a) * 0.1)),
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
                'HPMax': (lambda *a: 40000 * (1 + Func569(*a) * 0.1)),
                'RHP': 0,
                'ArmorMax': 0,
                'ShieldMax': 0,
                'RShield': 0,
                'ShieldRecoverTime': 0,
                'DefPhysical': 1000,
                'DefThunder': 1000,
                'DefCorrision': 1000,
                'DefFire': 1000,
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
                'HPMax': (lambda *a: 40000 * (1 + Func569(*a) * 0.1)),
                'RHP': 0,
                'ArmorMax': 0,
                'ShieldMax': 0,
                'RShield': 0,
                'ShieldRecoverTime': 0,
                'DefPhysical': (lambda *a: 10000 * (1 - 1.4 / ((Func221(*a) * 0.2 + 1.8) * (1 + (Func204(*a) - 1) * 0.1 * (1 + (Func221(*a) // 8) * 1))))),
                'DefThunder': (lambda *a: 10000 * (1 - 1.4 / ((Func221(*a) * 0.2 + 1.8) * (1 + (Func204(*a) - 1) * 0.1 * (1 + (Func221(*a) // 8) * 1))))),
                'DefCorrision': (lambda *a: 10000 * (1 - 1.4 / ((Func221(*a) * 0.2 + 1.8) * (1 + (Func204(*a) - 1) * 0.1 * (1 + (Func221(*a) // 8) * 1))))),
                'DefFire': (lambda *a: 10000 * (1 - 1.4 / ((Func221(*a) * 0.2 + 1.8) * (1 + (Func204(*a) - 1) * 0.1 * (1 + (Func221(*a) // 8) * 1))))),
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

