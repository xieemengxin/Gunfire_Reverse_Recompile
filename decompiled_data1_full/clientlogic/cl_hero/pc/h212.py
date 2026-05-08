# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_hero/pc/h212.pyc
# RelativePath: clientlogic/cl_hero/pc/h212.pyc
# Source Generated with Decompyle++
# File: h212.pyc (Python 3.6)

from cl_hero import CBaseHeroData
from cl_commondefines import DEFEND_TREND_SHIELD

class CHeroData(CBaseHeroData):
    m_SID = 212
    m_HeroName = '桃'
    m_Shape = 1009
    m_Career = 109
    m_InitGrade = 0
    m_MaxGrade = 5
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_GradeInfo = {
        1: {
            'Perform': 6071,
            'Cost': 700,
            'NeedPlayerGrade': 2 },
        2: {
            'Perform': 6072,
            'Cost': 1300,
            'NeedPlayerGrade': 6 },
        3: {
            'Perform': 6073,
            'Cost': 1900,
            'NeedPlayerGrade': 10 },
        4: {
            'Perform': 6074,
            'Cost': 2500,
            'NeedPlayerGrade': 14 },
        5: {
            'Perform': 6075,
            'Cost': 3100,
            'NeedPlayerGrade': 18 } }
    m_InitWeapon = 1202
    m_PerformList = (1312, 1419, 1310, 4215, 4249)
    m_HeroPerform = {
        'Career': 1312,
        'Throw': 1419 }
    m_BaseAttr = {
        'HPMax': 5000,
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 8000,
        'RShield': 8,
        'ShieldRecoverTime': 350,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 0,
        'StruckIgnoreFrame': 0,
        'DefKnockBack': 0,
        'KnockBackFrame': 0,
        'DefThump': 0,
        'ThumpFrame': 0,
        'Att': 0,
        'MoveSpeed': 520,
        'AttSpeed': 0,
        'Toughness': 0,
        'TurnSpeed': 0,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 500,
        'HardEff': 0,
        'SaveTime': 300,
        'DodgeProb': 0,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 0,
        'MaxDeviceEnergy': 0,
        'RDeviceEnergy': 0 }
    m_CustomConArgs = { }
    m_StateUseTransFactor = ()

