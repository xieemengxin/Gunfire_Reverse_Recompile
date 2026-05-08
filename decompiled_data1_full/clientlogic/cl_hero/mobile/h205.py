# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_hero/mobile/h205.pyc
# RelativePath: clientlogic/cl_hero/mobile/h205.pyc
# Source Generated with Decompyle++
# File: h205.pyc (Python 3.6)

from cl_hero import CBaseHeroData
from cl_commondefines import DEFEND_TREND_SHIELD

class CHeroData(CBaseHeroData):
    m_SID = 205
    m_HeroName = '太子'
    m_Shape = 1001
    m_Career = 102
    m_InitGrade = 0
    m_MaxGrade = 5
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_GradeInfo = {
        1: {
            'Perform': 6006,
            'Cost': 700,
            'NeedPlayerGrade': 2 },
        2: {
            'Perform': 6007,
            'Cost': 1300,
            'NeedPlayerGrade': 6 },
        3: {
            'Perform': 6008,
            'Cost': 1900,
            'NeedPlayerGrade': 10 },
        4: {
            'Perform': 6009,
            'Cost': 2500,
            'NeedPlayerGrade': 14 },
        5: {
            'Perform': 6010,
            'Cost': 3100,
            'NeedPlayerGrade': 18 } }
    m_InitWeapon = 1202
    m_PerformList = (1302, 1410, 1310, 4162, 4249)
    m_HeroPerform = {
        'Career': 1302,
        'Throw': 1410 }
    m_BaseAttr = {
        'HPMax': 6500,
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 6500,
        'RShield': 10,
        'ShieldRecoverTime': 300,
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
        'MoveSpeed': 500,
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

