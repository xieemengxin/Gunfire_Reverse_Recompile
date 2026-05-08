# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_hero/pc/h220.pyc
# RelativePath: clientlogic/cl_hero/pc/h220.pyc
# Source Generated with Decompyle++
# File: h220.pyc (Python 3.6)

from cl_hero import CBaseHeroData
from cl_commondefines import DEFEND_TREND_SHIELD

class CHeroData(CBaseHeroData):
    m_SID = 220
    m_HeroName = '苍玦'
    m_Shape = 1018
    m_Career = 118
    m_InitGrade = 0
    m_MaxGrade = 5
    m_DefendTrend = DEFEND_TREND_SHIELD
    m_GradeInfo = {
        1: {
            'Perform': 6916,
            'Cost': 700,
            'NeedPlayerGrade': 2 },
        2: {
            'Perform': 6917,
            'Cost': 1300,
            'NeedPlayerGrade': 6 },
        3: {
            'Perform': 6918,
            'Cost': 1900,
            'NeedPlayerGrade': 10 },
        4: {
            'Perform': 6919,
            'Cost': 2500,
            'NeedPlayerGrade': 14 },
        5: {
            'Perform': 6920,
            'Cost': 3100,
            'NeedPlayerGrade': 18 } }
    m_InitWeapon = 1202
    m_PerformList = (1334, 1435, 1329, 1434, 1310, 4249, 1330, 1336, 1332, 5337, 1331)
    m_HeroPerform = {
        'Career': 1329,
        'Throw': 1434,
        'Left': 1330,
        'Right': 1336,
        'Space': 1332,
        'Reload': 1331 }
    m_BaseAttr = {
        'HPMax': 9000,
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 5000,
        'RShield': 12,
        'ShieldRecoverTime': 280,
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
        'MoveSpeed': 550,
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
        'EnergyMax': 12000,
        'REnergy': 0,
        'SpecialMHPWeight': 0,
        'MaxDeviceEnergy': 0,
        'RDeviceEnergy': 0 }
    m_CustomConArgs = { }
    m_StateUseTransFactor = (33766, 33604)

