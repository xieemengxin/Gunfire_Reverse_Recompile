# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/device/d1002.pyc
# RelativePath: clientlogic/cl_platformdata/pc/device/d1002.pyc
# Source Generated with Decompyle++
# File: d1002.pyc (Python 3.6)

from cl_commondefines import WARRIOR_DEVICE_TURRET, WARRIOR_ELITE, WARRIOR_SUMMON_STELE
from cl_resmgr.resdata import CDeviceData as CCustom

class CDeviceData(CCustom):
    m_SID = 1002
    m_Name = '碧霄'
    m_HeroExtAttr = {
        'MaxDeviceEnergy': 10000,
        'RDeviceEnergy': 300 }
    m_HeroExtPassive = (7010, 50257)
    m_HeroPerformInfo = {
        'Arrange': 50330,
        'Recycle': 50331,
        'Command': 50332 }
    m_ActiveDisablePerform = ()
    m_Shape = 5555
    m_FightType = WARRIOR_DEVICE_TURRET
    m_AttPerform = 7200
    m_PerformList = (7200, 7013, 7205, 7213, 7214)
    m_Betree = 'DeviceTurret.Fsm'
    m_AIConfig = {
        'PFAI': 39246 }
    m_BaseAttrInfo = {
        'HPMax': 100,
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 0,
        'ShieldRecoverTime': 0,
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
        'Att': 50000,
        'MoveSpeed': 1000,
        'AttSpeed': 200,
        'Toughness': 0,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 0,
        'SaveTime': 0,
        'DodgeProb': 0,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 0,
        'HitRange': 40 }
    m_ActiveStopEnergyRecover = 0
    m_BaseHate = {
        'Default': 50,
        'FightType': {
            WARRIOR_SUMMON_STELE: 60,
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

