# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3001/monster.pyc
# RelativePath: clientlogic/cl_wardata/w3001/monster.pyc
# Source Generated with Decompyle++
# File: monster.pyc (Python 3.6)

from cl_resmgr.resdata import CMonsterData as CCustom
import cl_resmgr.resdata as baseconfig
from cl_newformula import Func10, Func204, Func205, Func515, Func592

class CMonsterData10221(baseconfig.CMonsterData):
    m_SID = 10221
    m_DataSID = 1022
    m_Name = '纯血木桩'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 409880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 999999,
            'KnockBackFrame': 30,
            'DefThump': 999999,
            'ThumpFrame': 30,
            'Att': 1,
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 409880 * (Func10(*a) - 1) + 129600),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 999999,
        'KnockBackFrame': 30,
        'DefThump': 999999,
        'ThumpFrame': 30,
        'Att': 1,
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 10000


class CMonsterData10231(baseconfig.CMonsterData):
    m_SID = 10231
    m_DataSID = 1023
    m_Name = '护盾木桩'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0x5D21DBA000,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 999999,
            'KnockBackFrame': 30,
            'DefThump': 999999,
            'ThumpFrame': 30,
            'Att': 1,
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0x5D21DBA000,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 999999,
        'KnockBackFrame': 30,
        'DefThump': 999999,
        'ThumpFrame': 30,
        'Att': 1,
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 10000


class CMonsterData10241(baseconfig.CMonsterData):
    m_SID = 10241
    m_DataSID = 1024
    m_Name = '护甲木桩'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': 0x5D21DBA000,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 999999,
            'KnockBackFrame': 30,
            'DefThump': 999999,
            'ThumpFrame': 30,
            'Att': 1,
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
        'RHP': 0,
        'ArmorMax': 0x5D21DBA000,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 999999,
        'KnockBackFrame': 30,
        'DefThump': 999999,
        'ThumpFrame': 30,
        'Att': 1,
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 10000


class CMonsterData10251(baseconfig.CMonsterData):
    m_SID = 10251
    m_DataSID = 1022
    m_Name = '纯血木桩(可位移)'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 409880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 30,
            'DefThump': 0,
            'ThumpFrame': 30,
            'Att': 1,
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 409880 * (Func10(*a) - 1) + 129600),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 30,
        'DefThump': 0,
        'ThumpFrame': 30,
        'Att': 1,
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 10000


class CMonsterData10321(baseconfig.CMonsterData):
    m_SID = 10321
    m_DataSID = 1025
    m_Name = '纯血小木桩'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 409880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 999999,
            'KnockBackFrame': 30,
            'DefThump': 999999,
            'ThumpFrame': 30,
            'Att': 1,
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 409880 * (Func10(*a) - 1) + 129600),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 999999,
        'KnockBackFrame': 30,
        'DefThump': 999999,
        'ThumpFrame': 30,
        'Att': 1,
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 10000


class CMonsterData10322(baseconfig.CMonsterData):
    m_SID = 10322
    m_DataSID = 1028
    m_Name = '纯血小木桩(可击杀)'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 409880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 999999,
            'KnockBackFrame': 30,
            'DefThump': 999999,
            'ThumpFrame': 30,
            'Att': 1,
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 409880 * (Func10(*a) - 1) + 129600),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 999999,
        'KnockBackFrame': 30,
        'DefThump': 999999,
        'ThumpFrame': 30,
        'Att': 1,
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 10000


class CMonsterData10331(baseconfig.CMonsterData):
    m_SID = 10331
    m_DataSID = 1026
    m_Name = '护盾小木桩'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0x5D21DBA000,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 999999,
            'KnockBackFrame': 30,
            'DefThump': 999999,
            'ThumpFrame': 30,
            'Att': 1,
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0x5D21DBA000,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 999999,
        'KnockBackFrame': 30,
        'DefThump': 999999,
        'ThumpFrame': 30,
        'Att': 1,
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 10000


class CMonsterData10341(baseconfig.CMonsterData):
    m_SID = 10341
    m_DataSID = 1027
    m_Name = '护甲小木桩'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': 0x5D21DBA000,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 999999,
            'KnockBackFrame': 30,
            'DefThump': 999999,
            'ThumpFrame': 30,
            'Att': 1,
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
        'RHP': 0,
        'ArmorMax': 0x5D21DBA000,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 999999,
        'KnockBackFrame': 30,
        'DefThump': 999999,
        'ThumpFrame': 30,
        'Att': 1,
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 10000


class CMonsterData10351(baseconfig.CMonsterData):
    m_SID = 10351
    m_DataSID = 1025
    m_Name = '纯血小木桩(可位移)'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 409880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 30,
            'DefThump': 0,
            'ThumpFrame': 30,
            'Att': 1,
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 409880 * (Func10(*a) - 1) + 129600),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 30,
        'DefThump': 0,
        'ThumpFrame': 30,
        'Att': 1,
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 10000


class CMonsterData20011(baseconfig.CMonsterData):
    m_SID = 20011
    m_DataSID = 2001
    m_Name = '魔化 独角金龟'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 800 * (Func10(*a) - 1) + 2400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 51,
            'DefThump': 0,
            'ThumpFrame': 51,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
            'MoveSpeed': 50,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 51,
        'DefThump': 0,
        'ThumpFrame': 51,
        'Att': (lambda *a: 5000 + 30 * Func592(*a)),
        'MoveSpeed': 50,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 90000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14028,) },
        'Mode': { } }
    m_SpecialMHP = 240


class CMonsterData20012(baseconfig.CMonsterData):
    m_SID = 20012
    m_DataSID = 2001
    m_Name = '魔化 独角金龟'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 800 * (Func10(*a) - 1) + 2400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 51,
            'DefThump': 0,
            'ThumpFrame': 51,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
            'MoveSpeed': 50,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 51,
        'DefThump': 0,
        'ThumpFrame': 51,
        'Att': (lambda *a: 5000 + 30 * Func592(*a)),
        'MoveSpeed': 50,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 90000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14028,) },
        'Mode': { } }
    m_SpecialMHP = 240


class CMonsterData20013(baseconfig.CMonsterData):
    m_SID = 20013
    m_DataSID = 2001
    m_Name = '魔化 独角金龟'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 800 * (Func10(*a) - 1) + 2400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 51,
            'DefThump': 0,
            'ThumpFrame': 51,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
            'MoveSpeed': 50,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 51,
        'DefThump': 0,
        'ThumpFrame': 51,
        'Att': (lambda *a: 5000 + 30 * Func592(*a)),
        'MoveSpeed': 50,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        2: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        3: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 90000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14028,) },
        'Mode': { } }
    m_SpecialMHP = 240


class CMonsterData20014(baseconfig.CMonsterData):
    m_SID = 20014
    m_DataSID = 2001
    m_Name = '魔化 独角金龟'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 800 * (Func10(*a) - 1) + 2400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 51,
            'DefThump': 0,
            'ThumpFrame': 51,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
            'MoveSpeed': 50,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 51,
        'DefThump': 0,
        'ThumpFrame': 51,
        'Att': (lambda *a: 5000 + 30 * Func592(*a)),
        'MoveSpeed': 50,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) },
        2: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) },
        3: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 90000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14028,) },
        'Mode': { } }
    m_SpecialMHP = 240


class CMonsterData20021(baseconfig.CMonsterData):
    m_SID = 20021
    m_DataSID = 2002
    m_Name = '大漠幼豚'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1000 * (Func10(*a) - 1) + 3000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 51,
            'DefThump': 0,
            'ThumpFrame': 51,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
            'MoveSpeed': 50,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 51,
        'DefThump': 0,
        'ThumpFrame': 51,
        'Att': (lambda *a: 5000 + 30 * Func592(*a)),
        'MoveSpeed': 50,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 110000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14043,) },
        'Mode': { } }
    m_SpecialMHP = 300


class CMonsterData20022(baseconfig.CMonsterData):
    m_SID = 20022
    m_DataSID = 2002
    m_Name = '大漠幼豚'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1000 * (Func10(*a) - 1) + 3000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 51,
            'DefThump': 0,
            'ThumpFrame': 51,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
            'MoveSpeed': 50,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 51,
        'DefThump': 0,
        'ThumpFrame': 51,
        'Att': (lambda *a: 5000 + 30 * Func592(*a)),
        'MoveSpeed': 50,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 110000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14043,) },
        'Mode': { } }
    m_SpecialMHP = 300


class CMonsterData20023(baseconfig.CMonsterData):
    m_SID = 20023
    m_DataSID = 2002
    m_Name = '大漠幼豚'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1000 * (Func10(*a) - 1) + 3000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 51,
            'DefThump': 0,
            'ThumpFrame': 51,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
            'MoveSpeed': 50,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 51,
        'DefThump': 0,
        'ThumpFrame': 51,
        'Att': (lambda *a: 5000 + 30 * Func592(*a)),
        'MoveSpeed': 50,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) },
        2: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) },
        3: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 110000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14043,) },
        'Mode': { } }
    m_SpecialMHP = 300


class CMonsterData20031(baseconfig.CMonsterData):
    m_SID = 20031
    m_DataSID = 2003
    m_Name = '灯笼鬼'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1200 * (Func10(*a) - 1) + 3600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 21,
            'DefThump': 0,
            'ThumpFrame': 21,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
            'MoveSpeed': 300,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 21,
        'DefThump': 0,
        'ThumpFrame': 21,
        'Att': (lambda *a: 5000 + 30 * Func592(*a)),
        'MoveSpeed': 300,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 360


class CMonsterData20041(baseconfig.CMonsterData):
    m_SID = 20041
    m_DataSID = 2004
    m_Name = '自爆灯笼鬼'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1200 * (Func10(*a) - 1) + 3600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 21,
            'DefThump': 0,
            'ThumpFrame': 21,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 300,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 21,
        'DefThump': 0,
        'ThumpFrame': 21,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 300,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 360


class CMonsterData20042(baseconfig.CMonsterData):
    m_SID = 20042
    m_DataSID = 2004
    m_Name = '自爆灯笼鬼'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1200 * (Func10(*a) - 1) + 3600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 21,
            'DefThump': 0,
            'ThumpFrame': 21,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 300,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 21,
        'DefThump': 0,
        'ThumpFrame': 21,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 300,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) },
        2: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) },
        3: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 360


class CMonsterData20061(baseconfig.CMonsterData):
    m_SID = 20061
    m_DataSID = 2006
    m_Name = '寄居蟹'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1200 * (Func10(*a) - 1) + 3600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 51,
            'DefThump': 0,
            'ThumpFrame': 51,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
            'MoveSpeed': 50,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 51,
        'DefThump': 0,
        'ThumpFrame': 51,
        'Att': (lambda *a: 5000 + 30 * Func592(*a)),
        'MoveSpeed': 50,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 110000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 360


class CMonsterData20071(baseconfig.CMonsterData):
    m_SID = 20071
    m_DataSID = 2007
    m_Name = '寄居蟹'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1200 * (Func10(*a) - 1) + 3600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 51,
            'DefThump': 0,
            'ThumpFrame': 51,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
            'MoveSpeed': 50,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 51,
        'DefThump': 0,
        'ThumpFrame': 51,
        'Att': (lambda *a: 5000 + 30 * Func592(*a)),
        'MoveSpeed': 50,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 110000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 360


class CMonsterData20211(baseconfig.CMonsterData):
    m_SID = 20211
    m_DataSID = 2021
    m_Name = '大漠土狼'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 8400 * (Func10(*a) - 1) + 18000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 66,
            'DefThump': 0,
            'ThumpFrame': 66,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 51330 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 66,
        'DefThump': 0,
        'ThumpFrame': 66,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 100,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14009,) },
        'Mode': { } }
    m_SpecialMHP = 1200


class CMonsterData20212(baseconfig.CMonsterData):
    m_SID = 20212
    m_DataSID = 2021
    m_Name = '大漠土狼'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 8400 * (Func10(*a) - 1) + 18000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 66,
            'DefThump': 0,
            'ThumpFrame': 66,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 37150 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 66,
        'DefThump': 0,
        'ThumpFrame': 66,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 100,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14009,) },
        'Mode': { } }
    m_SpecialMHP = 1200


class CMonsterData20221(baseconfig.CMonsterData):
    m_SID = 20221
    m_DataSID = 2022
    m_Name = '大漠土狼'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 18900 * (Func10(*a) - 1) + 40500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 66,
            'DefThump': 0,
            'ThumpFrame': 66,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 41800 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 66,
        'DefThump': 0,
        'ThumpFrame': 66,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        2: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        3: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) } }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14010,) },
        'Mode': { } }
    m_SpecialMHP = 1200


class CMonsterData20411(baseconfig.CMonsterData):
    m_SID = 20411
    m_DataSID = 2041
    m_Name = '大漠沙虫'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 6300 * (Func10(*a) - 1) + 13500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 21000 * (Func10(*a) - 1) + 45000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 10,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 29,
            'DefThump': 100000,
            'ThumpFrame': 29,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
            'MoveSpeed': 350,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 8820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 39400 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 10,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 29,
        'DefThump': 100000,
        'ThumpFrame': 29,
        'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
        'MoveSpeed': 350,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14013,) },
        'Mode': { } }
    m_SpecialMHP = 3000


class CMonsterData20421(baseconfig.CMonsterData):
    m_SID = 20421
    m_DataSID = 2042
    m_Name = '大漠沙虫'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1890 * (Func10(*a) - 1) + 4050),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 6300 * (Func10(*a) - 1) + 13500),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 10,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 29,
            'DefThump': 100000,
            'ThumpFrame': 29,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 350,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2646 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 8820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 10,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 29,
        'DefThump': 100000,
        'ThumpFrame': 29,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 350,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (0, 2),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (0, 3),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (0, 3),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 900


class CMonsterData20422(baseconfig.CMonsterData):
    m_SID = 20422
    m_DataSID = 2042
    m_Name = '大漠沙虫'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1890 * (Func10(*a) - 1) + 4050),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 6300 * (Func10(*a) - 1) + 13500),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 10,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 29,
            'DefThump': 100000,
            'ThumpFrame': 29,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
            'MoveSpeed': 350,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2646 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 8820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 10,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 29,
        'DefThump': 100000,
        'ThumpFrame': 29,
        'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
        'MoveSpeed': 350,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (0, 2),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (0, 3),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (0, 3),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 900


class CMonsterData20431(baseconfig.CMonsterData):
    m_SID = 20431
    m_DataSID = 2043
    m_Name = '#大漠飞虫'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1890 * (Func10(*a) - 1) + 4050),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 6300 * (Func10(*a) - 1) + 13500),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 70,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 29,
            'DefThump': 100000,
            'ThumpFrame': 29,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
            'MoveSpeed': 350,
            'AttSpeed': 30,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2646 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 8820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 10,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 29,
        'DefThump': 100000,
        'ThumpFrame': 29,
        'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
        'MoveSpeed': 350,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (0, 2),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (0, 3),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (0, 3),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 900


class CMonsterData20441(baseconfig.CMonsterData):
    m_SID = 20441
    m_DataSID = 2044
    m_Name = '大漠飞虫'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 2520 * (Func10(*a) - 1) + 5400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 8400 * (Func10(*a) - 1) + 18000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
            'MoveSpeed': 130,
            'AttSpeed': 40,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 5000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 3880 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 17336 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 300,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 5000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 50000
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14057,) },
        'Mode': { } }
    m_SpecialMHP = 600


class CMonsterData20611(baseconfig.CMonsterData):
    m_SID = 20611
    m_DataSID = 2061
    m_Name = '魔化 投雷散兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 16800 * (Func10(*a) - 1) + 36000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 130,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 41680 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 130,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14023,) },
        'Mode': { } }
    m_SpecialMHP = 2400


class CMonsterData20612(baseconfig.CMonsterData):
    m_SID = 20612
    m_DataSID = 2061
    m_Name = '魔化 投雷散兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 16800 * (Func10(*a) - 1) + 36000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 130,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 41680 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 130,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 2400


class CMonsterData20621(baseconfig.CMonsterData):
    m_SID = 20621
    m_DataSID = 2062
    m_Name = '魔化 火雷散兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 16800 * (Func10(*a) - 1) + 36000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 130,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 41680 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 130,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14051,) },
        'Mode': { } }
    m_SpecialMHP = 2400


class CMonsterData20622(baseconfig.CMonsterData):
    m_SID = 20622
    m_DataSID = 2062
    m_Name = '魔化 火雷散兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 16800 * (Func10(*a) - 1) + 36000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 130,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 41680 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 130,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 2400


class CMonsterData20631(baseconfig.CMonsterData):
    m_SID = 20631
    m_DataSID = 2063
    m_Name = '魔化 电雷散兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 16800 * (Func10(*a) - 1) + 36000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 130,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 41680 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 130,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14052,) },
        'Mode': { } }
    m_SpecialMHP = 2400


class CMonsterData20641(baseconfig.CMonsterData):
    m_SID = 20641
    m_DataSID = 2064
    m_Name = '魔化 毒雷散兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 16800 * (Func10(*a) - 1) + 36000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 130,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 41680 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 130,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14053,) },
        'Mode': { } }
    m_SpecialMHP = 2400


class CMonsterData20642(baseconfig.CMonsterData):
    m_SID = 20642
    m_DataSID = 2064
    m_Name = '魔化 毒雷散兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 16800 * (Func10(*a) - 1) + 36000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 130,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 41680 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 130,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 2400


class CMonsterData20651(baseconfig.CMonsterData):
    m_SID = 20651
    m_DataSID = 2065
    m_Name = '渔夫'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 35700 * (Func10(*a) - 1) + 76500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 130,
            'AttSpeed': 110,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 42480 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 130,
        'AttSpeed': 110,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 8000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14004,) },
        'Mode': { } }
    m_SpecialMHP = 5100


class CMonsterData20652(baseconfig.CMonsterData):
    m_SID = 20652
    m_DataSID = 2065
    m_Name = '渔夫'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 35700 * (Func10(*a) - 1) + 76500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 130,
            'AttSpeed': 110,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 42480 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 130,
        'AttSpeed': 110,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (5000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1) },
        2: {
            201: (5000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1) },
        3: {
            201: (5000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1) } }
    m_RunSpeedUpMul = 8000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14004,) },
        'Mode': { } }
    m_SpecialMHP = 5100


class CMonsterData20811(baseconfig.CMonsterData):
    m_SID = 20811
    m_DataSID = 2081
    m_Name = '魔化 徒甲兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 5040 * (Func10(*a) - 1) + 10800),
            'RHP': 0,
            'ArmorMax': (lambda *a: 16800 * (Func10(*a) - 1) + 36000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 23,
            'DefThump': 0,
            'ThumpFrame': 23,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 350,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 20000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 54780 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 23,
        'DefThump': 0,
        'ThumpFrame': 23,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 350,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 4285
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14029,) },
        'Mode': { } }
    m_SpecialMHP = 2400


class CMonsterData20812(baseconfig.CMonsterData):
    m_SID = 20812
    m_DataSID = 2081
    m_Name = '魔化 徒甲兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 5040 * (Func10(*a) - 1) + 10800),
            'RHP': 0,
            'ArmorMax': (lambda *a: 16800 * (Func10(*a) - 1) + 36000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 23,
            'DefThump': 0,
            'ThumpFrame': 23,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 350,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 20000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 54780 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 23,
        'DefThump': 0,
        'ThumpFrame': 23,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 350,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 4285
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14029,) },
        'Mode': { } }
    m_SpecialMHP = 2400


class CMonsterData20821(baseconfig.CMonsterData):
    m_SID = 20821
    m_DataSID = 2082
    m_Name = '魔化 徒甲兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 18900 * (Func10(*a) - 1) + 40500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 23,
            'DefThump': 0,
            'ThumpFrame': 23,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 350,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 74694 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 23,
        'DefThump': 0,
        'ThumpFrame': 23,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 350,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 4285
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14029,) },
        'Mode': { } }
    m_SpecialMHP = 2400


class CMonsterData20831(baseconfig.CMonsterData):
    m_SID = 20831
    m_DataSID = 2083
    m_Name = '魔化 右矛兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 5670 * (Func10(*a) - 1) + 12150),
            'RHP': 0,
            'ArmorMax': (lambda *a: 18900 * (Func10(*a) - 1) + 40500),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 30,
            'DefThump': 0,
            'ThumpFrame': 30,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 22000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 53000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 30,
        'DefThump': 0,
        'ThumpFrame': 30,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 1.5 * (32000 * (Func10(*a) - 1) + 60000)),
            'ArmorMax': (lambda *a: 1.5 * (32000 * (Func10(*a) - 1) + 60000)),
            'ShieldMax': 0,
            'Att': (lambda *a: 1.4 * (140 * (Func10(*a) - 1) + 1880)),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 150 },
        1: {
            'HPMax': (lambda *a: 33000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': (lambda *a: 79500 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ShieldMax': 0,
            'Att': (lambda *a: 1.4 * (140 * (Func10(*a) - 1) + 1880)),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 150 } }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14030,) },
        'Mode': { } }
    m_SpecialMHP = 2700


class CMonsterData20832(baseconfig.CMonsterData):
    m_SID = 20832
    m_DataSID = 2083
    m_Name = '魔化 右矛兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 5670 * (Func10(*a) - 1) + 12150),
            'RHP': 0,
            'ArmorMax': (lambda *a: 18900 * (Func10(*a) - 1) + 40500),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 30,
            'DefThump': 0,
            'ThumpFrame': 30,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 22000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 53000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 30,
        'DefThump': 0,
        'ThumpFrame': 30,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14030,) },
        'Mode': { } }
    m_SpecialMHP = 2700


class CMonsterData20833(baseconfig.CMonsterData):
    m_SID = 20833
    m_DataSID = 2083
    m_Name = '魔化 右矛兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 5670 * (Func10(*a) - 1) + 12150),
            'RHP': 0,
            'ArmorMax': (lambda *a: 18900 * (Func10(*a) - 1) + 40500),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 30,
            'DefThump': 0,
            'ThumpFrame': 30,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 22000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 53000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 30,
        'DefThump': 0,
        'ThumpFrame': 30,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14030,) },
        'Mode': { } }
    m_SpecialMHP = 2700


class CMonsterData20834(baseconfig.CMonsterData):
    m_SID = 20834
    m_DataSID = 2083
    m_Name = '魔化 右矛兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1890 * (Func10(*a) - 1) + 4050),
            'RHP': 0,
            'ArmorMax': (lambda *a: 6300 * (Func10(*a) - 1) + 13500),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 30,
            'DefThump': 0,
            'ThumpFrame': 30,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 7054 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 21600 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 30,
        'DefThump': 0,
        'ThumpFrame': 30,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14030,) },
        'Mode': { } }
    m_SpecialMHP = 900


class CMonsterData20841(baseconfig.CMonsterData):
    m_SID = 20841
    m_DataSID = 2084
    m_Name = '流寇刀手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 25200 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 125,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 75426 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 125,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 3600


class CMonsterData20851(baseconfig.CMonsterData):
    m_SID = 20851
    m_DataSID = 2085
    m_Name = '流寇电刀手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 21000 * (Func10(*a) - 1) + 45000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 125,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 76246 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 125,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14033,) },
        'Mode': { } }
    m_SpecialMHP = 3600


class CMonsterData20852(baseconfig.CMonsterData):
    m_SID = 20852
    m_DataSID = 2085
    m_Name = '流寇电刀手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 6300 * (Func10(*a) - 1) + 13500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 125,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 25415 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 125,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14033,) },
        'Mode': { } }
    m_SpecialMHP = 900


class CMonsterData20861(baseconfig.CMonsterData):
    m_SID = 20861
    m_DataSID = 2086
    m_Name = '流寇火炬手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 21000 * (Func10(*a) - 1) + 45000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 125,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 76246 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 125,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 5 * (21000 * (Func10(*a) - 1) + 45000)),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 125,
            'AttSpeed': 50,
            'DefKnockBack': 0,
            'DefThump': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'SpecialMHPWeight': 400 },
        1: {
            'HPMax': (lambda *a: 381230 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 125,
            'AttSpeed': 50,
            'DefKnockBack': 0,
            'DefThump': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'SpecialMHPWeight': 400 } }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14059,) },
        'Mode': { } }
    m_SpecialMHP = 3600


class CMonsterData20871(baseconfig.CMonsterData):
    m_SID = 20871
    m_DataSID = 2087
    m_Name = '鲶人武士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 7560 * (Func10(*a) - 1) + 16200),
            'RHP': 0,
            'ArmorMax': (lambda *a: 25200 * (Func10(*a) - 1) + 54000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 0,
            'ThumpFrame': 28,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 23340 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 53800 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 28,
        'DefThump': 0,
        'ThumpFrame': 28,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14016,) },
        'Mode': { } }
    m_SpecialMHP = 3600


class CMonsterData20872(baseconfig.CMonsterData):
    m_SID = 20872
    m_DataSID = 2087
    m_Name = '鲶人武士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1890 * (Func10(*a) - 1) + 4050),
            'RHP': 0,
            'ArmorMax': (lambda *a: 6300 * (Func10(*a) - 1) + 13500),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 0,
            'ThumpFrame': 28,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 6446 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 18140 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 28,
        'DefThump': 0,
        'ThumpFrame': 28,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2) },
        2: {
            201: (10000, 2) },
        3: {
            201: (10000, 2) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14016,) },
        'Mode': { } }
    m_SpecialMHP = 900


class CMonsterData20873(baseconfig.CMonsterData):
    m_SID = 20873
    m_DataSID = 2087
    m_Name = '鲶人武士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1890 * (Func10(*a) - 1) + 4050),
            'RHP': 0,
            'ArmorMax': (lambda *a: 6300 * (Func10(*a) - 1) + 13500),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 0,
            'ThumpFrame': 28,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 6446 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 18140 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 28,
        'DefThump': 0,
        'ThumpFrame': 28,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14016,) },
        'Mode': { } }
    m_SpecialMHP = 900


class CMonsterData20881(baseconfig.CMonsterData):
    m_SID = 20881
    m_DataSID = 2088
    m_Name = '魔化 右矛兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 10000 * (Func10(*a) - 1) + 20000),
            'RHP': 0,
            'ArmorMax': (lambda *a: 15000 * (Func10(*a) - 1) + 30000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 30,
            'DefThump': 0,
            'ThumpFrame': 30,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 28000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 53000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 30,
        'DefThump': 0,
        'ThumpFrame': 30,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            204: (3000, 1) },
        2: {
            204: (3000, 1) },
        3: {
            204: (3000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 2700


class CMonsterData20891(baseconfig.CMonsterData):
    m_SID = 20891
    m_DataSID = 2089
    m_Name = '六耳'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 11340 * (Func10(*a) - 1) + 24300),
            'RHP': 0,
            'ArmorMax': (lambda *a: 37800 * (Func10(*a) - 1) + 81000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 23608 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 55360 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 27,
        'DefThump': 0,
        'ThumpFrame': 27,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 6 * (11340 * (Func10(*a) - 1) + 24300)),
            'ArmorMax': (lambda *a: 6 * (37800 * (Func10(*a) - 1) + 81000)),
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 600 },
        1: {
            'HPMax': (lambda *a: 141648 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': (lambda *a: 332160 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 600 } }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14025,) },
        'Mode': { } }
    m_SpecialMHP = 5400


class CMonsterData20911(baseconfig.CMonsterData):
    m_SID = 20911
    m_DataSID = 2091
    m_Name = '魔化 左枪兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 5670 * (Func10(*a) - 1) + 12150),
            'RHP': 0,
            'ArmorMax': (lambda *a: 18900 * (Func10(*a) - 1) + 40500),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 30,
            'DefThump': 0,
            'ThumpFrame': 30,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 22000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 53000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 30,
        'DefThump': 0,
        'ThumpFrame': 30,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 1.5 * (32000 * (Func10(*a) - 1) + 60000)),
            'ArmorMax': (lambda *a: 1.5 * (32000 * (Func10(*a) - 1) + 60000)),
            'ShieldMax': 0,
            'Att': (lambda *a: 1.4 * (140 * (Func10(*a) - 1) + 1880)),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 150 },
        1: {
            'HPMax': (lambda *a: 33000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': (lambda *a: 79500 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ShieldMax': 0,
            'Att': (lambda *a: 1.4 * (140 * (Func10(*a) - 1) + 1880)),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 150 } }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14065,) },
        'Mode': { } }
    m_SpecialMHP = 2700


class CMonsterData20961(baseconfig.CMonsterData):
    m_SID = 20961
    m_DataSID = 2096
    m_Name = '魔化 右矛兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 3969 * (Func10(*a) - 1) + 8505),
            'RHP': 0,
            'ArmorMax': (lambda *a: 13230 * (Func10(*a) - 1) + 28350),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 30,
            'DefThump': 0,
            'ThumpFrame': 30,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 3969 * (Func10(*a) - 1) + 8505),
        'RHP': 0,
        'ArmorMax': (lambda *a: 13230 * (Func10(*a) - 1) + 28350),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 30,
        'DefThump': 0,
        'ThumpFrame': 30,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 0 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 2700


class CMonsterData20981(baseconfig.CMonsterData):
    m_SID = 20981
    m_DataSID = 2098
    m_Name = '#NT#【出生测试】小型近战怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 5670 * (Func10(*a) - 1) + 12150),
            'RHP': 0,
            'ArmorMax': (lambda *a: 18900 * (Func10(*a) - 1) + 40500),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 23,
            'DefThump': 0,
            'ThumpFrame': 23,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 500,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 5670 * (Func10(*a) - 1) + 12150),
        'RHP': 0,
        'ArmorMax': (lambda *a: 18900 * (Func10(*a) - 1) + 40500),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 0,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 23,
        'DefThump': 0,
        'ThumpFrame': 23,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 500,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 2700


class CMonsterData20991(baseconfig.CMonsterData):
    m_SID = 20991
    m_DataSID = 2099
    m_Name = '新手指引持矛近战怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 5670 * (Func10(*a) - 1) + 12150),
            'RHP': 0,
            'ArmorMax': (lambda *a: 18900 * (Func10(*a) - 1) + 40500),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 30,
            'DefThump': 0,
            'ThumpFrame': 30,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 5670 * (Func10(*a) - 1) + 12150),
        'RHP': 0,
        'ArmorMax': (lambda *a: 18900 * (Func10(*a) - 1) + 40500),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 30,
        'DefThump': 0,
        'ThumpFrame': 30,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 2700


class CMonsterData21011(baseconfig.CMonsterData):
    m_SID = 21011
    m_DataSID = 2101
    m_Name = '魔化 左弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 16800 * (Func10(*a) - 1) + 36000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 40,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 0,
            'ThumpFrame': 28,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 100,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 78000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 40,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 28,
        'DefThump': 0,
        'ThumpFrame': 28,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 100,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 26000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14046,) },
        'Mode': { } }
    m_SpecialMHP = 2400


class CMonsterData21012(baseconfig.CMonsterData):
    m_SID = 21012
    m_DataSID = 2101
    m_Name = '魔化 左弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 5040 * (Func10(*a) - 1) + 10800),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 16800 * (Func10(*a) - 1) + 36000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 40,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 0,
            'ThumpFrame': 28,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 100,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 26000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 72000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 40,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 28,
        'DefThump': 0,
        'ThumpFrame': 28,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 100,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 26000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14046,) },
        'Mode': { } }
    m_SpecialMHP = 2400


class CMonsterData21013(baseconfig.CMonsterData):
    m_SID = 21013
    m_DataSID = 2101
    m_Name = '魔化 左弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 5040 * (Func10(*a) - 1) + 10800),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 16800 * (Func10(*a) - 1) + 36000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 40,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 0,
            'ThumpFrame': 28,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 100,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 26000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 72000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 40,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 28,
        'DefThump': 0,
        'ThumpFrame': 28,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 100,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 26000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14046,) },
        'Mode': { } }
    m_SpecialMHP = 2400


class CMonsterData21021(baseconfig.CMonsterData):
    m_SID = 21021
    m_DataSID = 2102
    m_Name = '魔化 徒盾弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 5040 * (Func10(*a) - 1) + 10800),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 16800 * (Func10(*a) - 1) + 36000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 0,
            'ThumpFrame': 28,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 100,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 25,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 26000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 72000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 90,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 28,
        'DefThump': 0,
        'ThumpFrame': 28,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 100,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 25,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14006,) },
        'Mode': { } }
    m_SpecialMHP = 2400


class CMonsterData21022(baseconfig.CMonsterData):
    m_SID = 21022
    m_DataSID = 2102
    m_Name = '魔化 徒盾弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 5040 * (Func10(*a) - 1) + 10800),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 16800 * (Func10(*a) - 1) + 36000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 0,
            'ThumpFrame': 28,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 100,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 25,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 26000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 72000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 90,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 28,
        'DefThump': 0,
        'ThumpFrame': 28,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 100,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 25,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14006,) },
        'Mode': { } }
    m_SpecialMHP = 2400


class CMonsterData21031(baseconfig.CMonsterData):
    m_SID = 21031
    m_DataSID = 2103
    m_Name = '马贼枪手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 25200 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 150,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 54550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 90,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 27,
        'DefThump': 0,
        'ThumpFrame': 27,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 150,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 6667
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14034,) },
        'Mode': { } }
    m_SpecialMHP = 3600


class CMonsterData21051(baseconfig.CMonsterData):
    m_SID = 21051
    m_DataSID = 2105
    m_Name = '鲶人枪手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 27300 * (Func10(*a) - 1) + 58500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 33,
            'DefThump': 0,
            'ThumpFrame': 33,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 150,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 54600 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 33,
        'DefThump': 0,
        'ThumpFrame': 33,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 150,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14038,) },
        'Mode': { } }
    m_SpecialMHP = 3900


class CMonsterData21061(baseconfig.CMonsterData):
    m_SID = 21061
    m_DataSID = 2106
    m_Name = '鲶人蚌兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 8190 * (Func10(*a) - 1) + 17550),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 27300 * (Func10(*a) - 1) + 58500),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 33,
            'DefThump': 0,
            'ThumpFrame': 33,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 25,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 16380 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 48000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 90,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 33,
        'DefThump': 0,
        'ThumpFrame': 33,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 25,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14006,) },
        'Mode': { } }
    m_SpecialMHP = 3900


class CMonsterData21062(baseconfig.CMonsterData):
    m_SID = 21062
    m_DataSID = 2106
    m_Name = '鲶人蚌兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1890 * (Func10(*a) - 1) + 4050),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 6300 * (Func10(*a) - 1) + 13500),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 33,
            'DefThump': 0,
            'ThumpFrame': 33,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 25,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 3780 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 12600 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 90,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 33,
        'DefThump': 0,
        'ThumpFrame': 33,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 25,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14006,) },
        'Mode': { } }
    m_SpecialMHP = 900


class CMonsterData21071(baseconfig.CMonsterData):
    m_SID = 21071
    m_DataSID = 2107
    m_Name = '魔化 徒盾弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 22000 * (Func10(*a) - 1) + 46000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 0,
            'ThumpFrame': 28,
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 100,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 25,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 72000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 90,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 28,
        'DefThump': 0,
        'ThumpFrame': 28,
        'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 100,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 25,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            204: (3000, 1) },
        2: {
            204: (3000, 1) },
        3: {
            204: (3000, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14006,) },
        'Mode': { } }
    m_SpecialMHP = 3000


class CMonsterData21081(baseconfig.CMonsterData):
    m_SID = 21081
    m_DataSID = 2108
    m_Name = '玉面火枪手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 12480 * (Func10(*a) - 1) + 23400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 41600 * (Func10(*a) - 1) + 78000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 70,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 150,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 13728 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 45760 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 70,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 27,
        'DefThump': 0,
        'ThumpFrame': 27,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 150,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 6667
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14036,) },
        'Mode': { } }
    m_SpecialMHP = 6500


class CMonsterData21091(baseconfig.CMonsterData):
    m_SID = 21091
    m_DataSID = 2109
    m_Name = '玉面雷枪手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 12480 * (Func10(*a) - 1) + 23400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 41600 * (Func10(*a) - 1) + 78000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 70,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 150,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 13728 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 45760 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 70,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 27,
        'DefThump': 0,
        'ThumpFrame': 27,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 150,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 6667
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14036,) },
        'Mode': { } }
    m_SpecialMHP = 6500


class CMonsterData21101(baseconfig.CMonsterData):
    m_SID = 21101
    m_DataSID = 2110
    m_Name = '玉面毒枪手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 12480 * (Func10(*a) - 1) + 23400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 41600 * (Func10(*a) - 1) + 78000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 70,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 150,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 13728 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 45760 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 70,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 27,
        'DefThump': 0,
        'ThumpFrame': 27,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 150,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 6667
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14036,) },
        'Mode': { } }
    m_SpecialMHP = 6500


class CMonsterData21111(baseconfig.CMonsterData):
    m_SID = 21111
    m_DataSID = 2111
    m_Name = '玉面火枪手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 4160 * (Func10(*a) - 1) + 7800),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 13866 * (Func10(*a) - 1) + 26000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 70,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': 2000,
            'MoveSpeed': 150,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 4576 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 15253 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 70,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 27,
        'DefThump': 0,
        'ThumpFrame': 27,
        'Att': 2000,
        'MoveSpeed': 150,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            205: (10000, 4),
            203: (10000, 1) },
        2: {
            205: (10000, 4),
            203: (10000, 1) },
        3: {
            205: (10000, 4),
            203: (10000, 1) } }
    m_RunSpeedUpMul = 6667
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14036,) },
        'Mode': { } }
    m_SpecialMHP = 6500


class CMonsterData21121(baseconfig.CMonsterData):
    m_SID = 21121
    m_DataSID = 2112
    m_Name = '剧毒鲶兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 8190 * (Func10(*a) - 1) + 17550),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 27300 * (Func10(*a) - 1) + 58500),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 33,
            'DefThump': 0,
            'ThumpFrame': 33,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 25,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 16380 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 48000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 90,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 33,
        'DefThump': 0,
        'ThumpFrame': 33,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 25,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14060,) },
        'Mode': { } }
    m_SpecialMHP = 3900


class CMonsterData21211(baseconfig.CMonsterData):
    m_SID = 21211
    m_DataSID = 2121
    m_Name = '中型近战怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 28800 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 400,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 7,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 43200 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 27,
        'DefThump': 0,
        'ThumpFrame': 27,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 400,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 4500


class CMonsterData21221(baseconfig.CMonsterData):
    m_SID = 21221
    m_DataSID = 2122
    m_Name = '黑面流寇'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 30960 * (Func10(*a) - 1) + 64800),
            'RHP': 0,
            'ArmorMax': (lambda *a: 103200 * (Func10(*a) - 1) + 216000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 27,
            'DefThump': 10000,
            'ThumpFrame': 27,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 170,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 7,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 43344 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 132300 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 27,
        'DefThump': 10000,
        'ThumpFrame': 27,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 170,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 4 * (30960 * (Func10(*a) - 1) + 64800)),
            'ArmorMax': (lambda *a: 4 * (103200 * (Func10(*a) - 1) + 216000)),
            'ShieldMax': 0,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'Toughness': 35,
            'MoveSpeed': 170,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 400 },
        1: {
            'HPMax': (lambda *a: 173376 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': (lambda *a: 529200 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ShieldMax': 0,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'Toughness': 35,
            'MoveSpeed': 170,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 400 } }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 7650
    m_SprintSpeedUpMul = 32353
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14045,) },
        'Mode': { } }
    m_SpecialMHP = 14400


class CMonsterData21222(baseconfig.CMonsterData):
    m_SID = 21222
    m_DataSID = 2122
    m_Name = '黑面流寇'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 30960 * (Func10(*a) - 1) + 64800),
            'RHP': 0,
            'ArmorMax': (lambda *a: 103200 * (Func10(*a) - 1) + 216000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 27,
            'DefThump': 10000,
            'ThumpFrame': 27,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 170,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 7,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 43344 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 132300 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 27,
        'DefThump': 10000,
        'ThumpFrame': 27,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 170,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) },
        2: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) },
        3: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) } }
    m_RunSpeedUpMul = 7650
    m_SprintSpeedUpMul = 32353
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 14400


class CMonsterData21231(baseconfig.CMonsterData):
    m_SID = 21231
    m_DataSID = 2123
    m_Name = '魔化 马头锐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 32000 * (Func10(*a) - 1) + 60000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 33,
            'DefThump': 5000,
            'ThumpFrame': 33,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 80,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 2,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 150,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 170000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 33,
        'DefThump': 5000,
        'ThumpFrame': 33,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 80,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 3,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 150,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 3 * (32000 * (Func10(*a) - 1) + 60000)),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'Toughness': 35,
            'MoveSpeed': 80,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 300 },
        1: {
            'HPMax': (lambda *a: 300000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'Toughness': 35,
            'MoveSpeed': 80,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 300 } }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = -2500
    m_SprintSpeedUpMul = 8750
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14047,) },
        'Mode': { } }
    m_SpecialMHP = 5000


class CMonsterData21232(baseconfig.CMonsterData):
    m_SID = 21232
    m_DataSID = 2123
    m_Name = '魔化 马头锐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 32000 * (Func10(*a) - 1) + 60000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 33,
            'DefThump': 5000,
            'ThumpFrame': 33,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 80,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 2,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 150,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 170000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 33,
        'DefThump': 5000,
        'ThumpFrame': 33,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 80,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 3,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 150,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = -2500
    m_SprintSpeedUpMul = 8750
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 5000


class CMonsterData21233(baseconfig.CMonsterData):
    m_SID = 21233
    m_DataSID = 2123
    m_Name = '魔化 马头锐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 32000 * (Func10(*a) - 1) + 60000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 33,
            'DefThump': 5000,
            'ThumpFrame': 33,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 80,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 2,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 150,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 170000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 33,
        'DefThump': 5000,
        'ThumpFrame': 33,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 80,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 3,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 150,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) },
        2: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) },
        3: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) } }
    m_RunSpeedUpMul = -2500
    m_SprintSpeedUpMul = 8750
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14047,) },
        'Mode': { } }
    m_SpecialMHP = 5000


class CMonsterData21241(baseconfig.CMonsterData):
    m_SID = 21241
    m_DataSID = 2124
    m_Name = '流寇恶徒'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 11520 * (Func10(*a) - 1) + 21600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 38400 * (Func10(*a) - 1) + 72000),
            'RShield': 10,
            'ShieldRecoverTime': 300,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 22,
            'DefThump': 0,
            'ThumpFrame': 22,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 250,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 7,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 16256 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 56520 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 300,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 22,
        'DefThump': 0,
        'ThumpFrame': 22,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 250,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = -5000
    m_SprintSpeedUpMul = 4000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14027,) },
        'Mode': { } }
    m_SpecialMHP = 6000


class CMonsterData21251(baseconfig.CMonsterData):
    m_SID = 21251
    m_DataSID = 2125
    m_Name = '流寇帮凶'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 38400 * (Func10(*a) - 1) + 72000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 41,
            'DefThump': 5000,
            'ThumpFrame': 41,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 250,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 7,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 103760 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 41,
        'DefThump': 5000,
        'ThumpFrame': 41,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 250,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 100,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 4 * (38400 * (Func10(*a) - 1) + 72000)),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 250,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 400 },
        1: {
            'HPMax': (lambda *a: 415040 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 250,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 400 } }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 3333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14048,) },
        'Mode': { } }
    m_SpecialMHP = 6000


class CMonsterData21261(baseconfig.CMonsterData):
    m_SID = 21261
    m_DataSID = 2126
    m_Name = '巡海夜叉'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 11520 * (Func10(*a) - 1) + 21600),
            'RHP': 0,
            'ArmorMax': (lambda *a: 38400 * (Func10(*a) - 1) + 72000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 5000,
            'KnockBackFrame': 35,
            'DefThump': 5000,
            'ThumpFrame': 35,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 7,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 3500,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 32280 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 74600 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 5000,
        'KnockBackFrame': 35,
        'DefThump': 5000,
        'ThumpFrame': 35,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 3500,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14039,) },
        'Mode': { } }
    m_SpecialMHP = 6000


class CMonsterData21262(baseconfig.CMonsterData):
    m_SID = 21262
    m_DataSID = 2126
    m_Name = '巡海夜叉'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 7560 * (Func10(*a) - 1) + 16200),
            'RHP': 0,
            'ArmorMax': (lambda *a: 25200 * (Func10(*a) - 1) + 54000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 5000,
            'KnockBackFrame': 35,
            'DefThump': 5000,
            'ThumpFrame': 35,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 7,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 3500,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 32280 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 74600 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 5000,
        'KnockBackFrame': 35,
        'DefThump': 5000,
        'ThumpFrame': 35,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 3500,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14039,) },
        'Mode': { } }
    m_SpecialMHP = 6000


class CMonsterData21271(baseconfig.CMonsterData):
    m_SID = 21271
    m_DataSID = 2127
    m_Name = '魔化 马头锐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 32000 * (Func10(*a) - 1) + 60000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 33,
            'DefThump': 5000,
            'ThumpFrame': 33,
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 80,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 3,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 150,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 54400 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 33,
        'DefThump': 5000,
        'ThumpFrame': 33,
        'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 80,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 3,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 150,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            204: (3000, 1) },
        2: {
            204: (3000, 1) },
        3: {
            204: (3000, 1) } }
    m_RunSpeedUpMul = -2500
    m_SprintSpeedUpMul = 8750
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14047,) },
        'Mode': { } }
    m_SpecialMHP = 5000


class CMonsterData21281(baseconfig.CMonsterData):
    m_SID = 21281
    m_DataSID = 2128
    m_Name = '雪山守卫'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 33540 * (Func10(*a) - 1) + 70200),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 111800 * (Func10(*a) - 1) + 234000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 35,
            'DefThump': 5000,
            'ThumpFrame': 35,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 7,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 5000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 22894 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 92980 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 35,
        'DefThump': 5000,
        'ThumpFrame': 35,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 5000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 8 * (33540 * (Func10(*a) - 1) + 70200)),
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 8 * (111800 * (Func10(*a) - 1) + 234000)),
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 800 },
        1: {
            'HPMax': (lambda *a: 183152 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 743840 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 800 } }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14035,) },
        'Mode': { } }
    m_SpecialMHP = 15600


class CMonsterData21282(baseconfig.CMonsterData):
    m_SID = 21282
    m_DataSID = 2129
    m_Name = '雪山守卫'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 33540 * (Func10(*a) - 1) + 70200),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 111800 * (Func10(*a) - 1) + 234000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 35,
            'DefThump': 5000,
            'ThumpFrame': 35,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 7,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 5000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 22894 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 92980 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 35,
        'DefThump': 5000,
        'ThumpFrame': 35,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 5000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14035,) },
        'Mode': { } }
    m_SpecialMHP = 15600


class CMonsterData21311(baseconfig.CMonsterData):
    m_SID = 21311
    m_DataSID = 2131
    m_Name = '蚂蚁盾兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9600 * (Func10(*a) - 1) + 18000),
            'RHP': 0,
            'ArmorMax': (lambda *a: 32000 * (Func10(*a) - 1) + 60000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 70,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 41,
            'DefThump': 5000,
            'ThumpFrame': 41,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 7,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 32280 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 74600 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 41,
        'DefThump': 5000,
        'ThumpFrame': 41,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 100,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 4 * (9600 * (Func10(*a) - 1) + 18000)),
            'ArmorMax': (lambda *a: 4 * (32000 * (Func10(*a) - 1) + 60000)),
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 400 },
        1: {
            'HPMax': (lambda *a: 415040 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': (lambda *a: 4 * (203200 * (Func10(*a) - 1) + 216000)),
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 400 } }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 3333
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14056,) },
        'Mode': { } }
    m_SpecialMHP = 5500


class CMonsterData21331(baseconfig.CMonsterData):
    m_SID = 21331
    m_DataSID = 2133
    m_Name = '浪鳍'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 41600 * (Func10(*a) - 1) + 78000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 12480 * (Func10(*a) - 1) + 23400),
            'RShield': 0,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 37,
            'DefThump': 10000,
            'ThumpFrame': 37,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 5,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 16667
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14420,) },
        'Mode': { } }
    m_SpecialMHP = 15600


class CMonsterData21341(baseconfig.CMonsterData):
    m_SID = 21341
    m_DataSID = 2134
    m_Name = '魔化 幽焰剑卫'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9600 * (Func10(*a) - 1) + 18000),
            'RHP': 0,
            'ArmorMax': (lambda *a: 32000 * (Func10(*a) - 1) + 60000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 70,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 41,
            'DefThump': 5000,
            'ThumpFrame': 41,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 10,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 32280 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 74600 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 41,
        'DefThump': 5000,
        'ThumpFrame': 41,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 100,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 4 * (9600 * (Func10(*a) - 1) + 18000)),
            'ArmorMax': (lambda *a: 4 * (32000 * (Func10(*a) - 1) + 60000)),
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 400 },
        1: {
            'HPMax': (lambda *a: 415040 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': (lambda *a: 4 * (203200 * (Func10(*a) - 1) + 216000)),
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 400 } }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 3333
    m_SprintSpeedUpMul = 18000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 5000


class CMonsterData21351(baseconfig.CMonsterData):
    m_SID = 21351
    m_DataSID = 2135
    m_Name = '六耳PLUS'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 33540 * (Func10(*a) - 1) + 70200),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 111800 * (Func10(*a) - 1) + 234000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 35,
            'DefThump': 5000,
            'ThumpFrame': 35,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 7,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 5000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 22894 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 92980 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 35,
        'DefThump': 5000,
        'ThumpFrame': 35,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 5000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 15600


class CMonsterData21411(baseconfig.CMonsterData):
    m_SID = 21411
    m_DataSID = 2141
    m_Name = '魔化 重弩锐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 7680 * (Func10(*a) - 1) + 14400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 25600 * (Func10(*a) - 1) + 48000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 40,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 29,
            'DefThump': 0,
            'ThumpFrame': 29,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 160,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 33056 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 80000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 40,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 29,
        'DefThump': 0,
        'ThumpFrame': 29,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 160,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 3125
    m_SprintSpeedUpMul = 21250
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14031,) },
        'Mode': { } }
    m_SpecialMHP = 4000


class CMonsterData21412(baseconfig.CMonsterData):
    m_SID = 21412
    m_DataSID = 2141
    m_Name = '魔化 重弩锐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 7680 * (Func10(*a) - 1) + 14400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 25600 * (Func10(*a) - 1) + 48000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 40,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 29,
            'DefThump': 0,
            'ThumpFrame': 29,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 160,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 39056 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 80000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 40,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 29,
        'DefThump': 0,
        'ThumpFrame': 29,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 160,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 3125
    m_SprintSpeedUpMul = 21250
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14031,) },
        'Mode': { } }
    m_SpecialMHP = 4000


class CMonsterData21421(baseconfig.CMonsterData):
    m_SID = 21421
    m_DataSID = 2142
    m_Name = '马贼隐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 7680 * (Func10(*a) - 1) + 14400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 25600 * (Func10(*a) - 1) + 48000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 150,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 8820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 29400 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 90,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 150,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 4 * (38400 * (Func10(*a) - 1) + 72000)),
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 4 * (103200 * (Func10(*a) - 1) + 216000)),
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 12,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 500 },
        1: {
            'HPMax': (lambda *a: 275280 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 4 * (103200 * (Func10(*a) - 1) + 216000) * (1 + 0.1 * Func592(*a))),
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 12,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 500 } }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14044,) },
        'Mode': { } }
    m_SpecialMHP = 4000


class CMonsterData21422(baseconfig.CMonsterData):
    m_SID = 21422
    m_DataSID = 2142
    m_Name = '马贼隐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 6300 * (Func10(*a) - 1) + 13500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 21000 * (Func10(*a) - 1) + 45000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
            'MoveSpeed': 150,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 8820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 29400 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 90,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
        'MoveSpeed': 150,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14044,) },
        'Mode': { } }
    m_SpecialMHP = 4000


class CMonsterData21431(baseconfig.CMonsterData):
    m_SID = 21431
    m_DataSID = 2143
    m_Name = '奔波儿灞'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 11520 * (Func10(*a) - 1) + 21600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 38400 * (Func10(*a) - 1) + 72000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 250,
            'AttSpeed': 30,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 17280 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 50000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 250,
        'AttSpeed': 30,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 5 * (11520 * (Func10(*a) - 1) + 21600)),
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 5 * (38400 * (Func10(*a) - 1) + 72000)),
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'Toughness': 35,
            'MoveSpeed': 250,
            'AttSpeed': 30,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 250 },
        1: {
            'HPMax': (lambda *a: 86400 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 250000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'Toughness': 35,
            'MoveSpeed': 250,
            'AttSpeed': 30,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 250 } }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14037,) },
        'Mode': { } }
    m_SpecialMHP = 6000


class CMonsterData21441(baseconfig.CMonsterData):
    m_SID = 21441
    m_DataSID = 2144
    m_Name = '魔化 重弩锐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 33000 * (Func10(*a) - 1) + 62000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 40,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 29,
            'DefThump': 0,
            'ThumpFrame': 29,
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 160,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 86100 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 40,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 29,
        'DefThump': 0,
        'ThumpFrame': 29,
        'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 160,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            204: (3000, 1) },
        2: {
            204: (3000, 1) },
        3: {
            204: (3000, 1) } }
    m_RunSpeedUpMul = 3125
    m_SprintSpeedUpMul = 21250
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14031,) },
        'Mode': { } }
    m_SpecialMHP = 5500


class CMonsterData21451(baseconfig.CMonsterData):
    m_SID = 21451
    m_DataSID = 2145
    m_Name = '灞波儿奔'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 11520 * (Func10(*a) - 1) + 21600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 38400 * (Func10(*a) - 1) + 72000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 250,
            'AttSpeed': 30,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 17280 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 50000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 250,
        'AttSpeed': 30,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 5 * (11520 * (Func10(*a) - 1) + 21600)),
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 5 * (38400 * (Func10(*a) - 1) + 72000)),
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'Toughness': 35,
            'MoveSpeed': 250,
            'AttSpeed': 30,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 250 },
        1: {
            'HPMax': (lambda *a: 86400 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 250000 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'Toughness': 35,
            'MoveSpeed': 250,
            'AttSpeed': 30,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 250 } }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14037,) },
        'Mode': { } }
    m_SpecialMHP = 6000


class CMonsterData21611(baseconfig.CMonsterData):
    m_SID = 21611
    m_DataSID = 2161
    m_Name = '魔化 长弩锐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 5670 * (Func10(*a) - 1) + 12150),
            'RHP': 0,
            'ArmorMax': (lambda *a: 18900 * (Func10(*a) - 1) + 40500),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 0,
            'ThumpFrame': 28,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 120,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 19639 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 45130 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 28,
        'DefThump': 0,
        'ThumpFrame': 28,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 120,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 5 * (5670 * (Func10(*a) - 1) + 12150)),
            'ArmorMax': (lambda *a: 5 * (18900 * (Func10(*a) - 1) + 40500)),
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 120,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 500 },
        1: {
            'HPMax': (lambda *a: 98195 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': (lambda *a: 225650 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 120,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 500 } }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14032,) },
        'Mode': { } }
    m_SpecialMHP = 5000


class CMonsterData21621(baseconfig.CMonsterData):
    m_SID = 21621
    m_DataSID = 2162
    m_Name = '马贼军师'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 6300 * (Func10(*a) - 1) + 13500),
            'RHP': 0,
            'ArmorMax': (lambda *a: 21000 * (Func10(*a) - 1) + 45000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 10000,
            'ThumpFrame': 28,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 120,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 13230 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 44100 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 28,
        'DefThump': 10000,
        'ThumpFrame': 28,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 120,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 5 * (6300 * (Func10(*a) - 1) + 13500)),
            'ArmorMax': (lambda *a: 5 * (21000 * (Func10(*a) - 1) + 45000)),
            'ShieldMax': 0,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'Toughness': 35,
            'MoveSpeed': 120,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 250 },
        1: {
            'HPMax': (lambda *a: 66150 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': (lambda *a: 220500 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ShieldMax': 0,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'Toughness': 35,
            'MoveSpeed': 120,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 250 } }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14024,) },
        'Mode': { } }
    m_SpecialMHP = 3000


class CMonsterData21622(baseconfig.CMonsterData):
    m_SID = 21622
    m_DataSID = 2162
    m_Name = '马贼军师'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1890 * (Func10(*a) - 1) + 4050),
            'RHP': 0,
            'ArmorMax': (lambda *a: 6300 * (Func10(*a) - 1) + 13500),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 10000,
            'ThumpFrame': 28,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 120,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2650 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 8820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 28,
        'DefThump': 10000,
        'ThumpFrame': 28,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 120,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 900


class CMonsterData21631(baseconfig.CMonsterData):
    m_SID = 21631
    m_DataSID = 2163
    m_Name = '马贼门客'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 6930 * (Func10(*a) - 1) + 14850),
            'RHP': 0,
            'ArmorMax': (lambda *a: 23100 * (Func10(*a) - 1) + 49500),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 0,
            'ThumpFrame': 28,
            'Att': (lambda *a: 180 * (Func10(*a) - 1) + 2100),
            'MoveSpeed': 120,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 9702 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 32340 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 28,
        'DefThump': 0,
        'ThumpFrame': 28,
        'Att': (lambda *a: 180 * (Func10(*a) - 1) + 2100),
        'MoveSpeed': 120,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14026,) },
        'Mode': { } }
    m_SpecialMHP = 3300


class CMonsterData21641(baseconfig.CMonsterData):
    m_SID = 21641
    m_DataSID = 2164
    m_Name = '幽冥猎手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 10560 * (Func10(*a) - 1) + 19800),
            'RHP': 0,
            'ArmorMax': (lambda *a: 35200 * (Func10(*a) - 1) + 66000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 0,
            'ThumpFrame': 28,
            'Att': (lambda *a: 180 * (Func10(*a) - 1) + 2100),
            'MoveSpeed': 120,
            'AttSpeed': 80,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 11620 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 38750 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 28,
        'DefThump': 0,
        'ThumpFrame': 28,
        'Att': (lambda *a: 180 * (Func10(*a) - 1) + 2100),
        'MoveSpeed': 120,
        'AttSpeed': 80,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 9 * (10560 * (Func10(*a) - 1) + 19800)),
            'ArmorMax': (lambda *a: 9 * (35200 * (Func10(*a) - 1) + 66000)),
            'ShieldMax': 0,
            'Att': (lambda *a: 180 * (Func10(*a) - 1) + 2100),
            'Toughness': 35,
            'MoveSpeed': 120,
            'AttSpeed': 80,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 900 },
        1: {
            'HPMax': (lambda *a: 104580 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': (lambda *a: 348750 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ShieldMax': 0,
            'Att': (lambda *a: 180 * (Func10(*a) - 1) + 2100),
            'Toughness': 35,
            'MoveSpeed': 120,
            'AttSpeed': 80,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 900 } }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14049,) },
        'Mode': { } }
    m_SpecialMHP = 5500


class CMonsterData21651(baseconfig.CMonsterData):
    m_SID = 21651
    m_DataSID = 2165
    m_Name = '雷鸣猎手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 10560 * (Func10(*a) - 1) + 19800),
            'RHP': 0,
            'ArmorMax': (lambda *a: 35200 * (Func10(*a) - 1) + 66000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 0,
            'ThumpFrame': 28,
            'Att': (lambda *a: 180 * (Func10(*a) - 1) + 2100),
            'MoveSpeed': 120,
            'AttSpeed': 80,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 11616 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 38750 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 28,
        'DefThump': 0,
        'ThumpFrame': 28,
        'Att': (lambda *a: 180 * (Func10(*a) - 1) + 2100),
        'MoveSpeed': 120,
        'AttSpeed': 80,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 75,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 5500


class CMonsterData21811(baseconfig.CMonsterData):
    m_SID = 21811
    m_DataSID = 2181
    m_Name = '白鲛'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 111800 * (Func10(*a) - 1) + 234000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 37,
            'DefThump': 10000,
            'ThumpFrame': 37,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 7,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 107700 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 37,
        'DefThump': 10000,
        'ThumpFrame': 37,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 6 * (111800 * (Func10(*a) - 1) + 234000)),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 600 },
        1: {
            'HPMax': (lambda *a: 646200 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 600 } }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -900 + 3000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -900 + 3000), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -900 + 3000), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14040,) },
        'Mode': { } }
    m_SpecialMHP = 15600


class CMonsterData21812(baseconfig.CMonsterData):
    m_SID = 21812
    m_DataSID = 2181
    m_Name = '白鲛'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 111800 * (Func10(*a) - 1) + 234000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 37,
            'DefThump': 10000,
            'ThumpFrame': 37,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 7,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 107700 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 37,
        'DefThump': 10000,
        'ThumpFrame': 37,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) },
        2: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) },
        3: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14040,) },
        'Mode': { } }
    m_SpecialMHP = 15600


class CMonsterData21821(baseconfig.CMonsterData):
    m_SID = 21821
    m_DataSID = 2182
    m_Name = '荒漠泰坦'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 146200 * (Func10(*a) - 1) + 306000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 37,
            'DefThump': 10000,
            'ThumpFrame': 37,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 80,
            'AttSpeed': 50,
            'Toughness': 20,
            'TurnSpeed': 4,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 150780 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 37,
        'DefThump': 10000,
        'ThumpFrame': 37,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 20,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 5 * (111800 * (Func10(*a) - 1) + 234000)),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 500 },
        1: {
            'HPMax': (lambda *a: 538500 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 500 } }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 50000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14019,) },
        'Mode': { } }
    m_SpecialMHP = 14400


class CMonsterData21831(baseconfig.CMonsterData):
    m_SID = 21831
    m_DataSID = 2183
    m_Name = '蟹先锋'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 146200 * (Func10(*a) - 1) + 306000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 37,
            'DefThump': 10000,
            'ThumpFrame': 37,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 80,
            'AttSpeed': 50,
            'Toughness': 20,
            'TurnSpeed': 4,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 150780 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 37,
        'DefThump': 10000,
        'ThumpFrame': 37,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 20,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 5 * (111800 * (Func10(*a) - 1) + 234000)),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 500 },
        1: {
            'HPMax': (lambda *a: 538500 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 500 } }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 50000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14063,) },
        'Mode': { } }
    m_SpecialMHP = 14400


class CMonsterData22011(baseconfig.CMonsterData):
    m_SID = 22011
    m_DataSID = 2201
    m_Name = '流寇纵火者'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 23220 * (Func10(*a) - 1) + 48600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 77400 * (Func10(*a) - 1) + 162000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 36,
            'DefThump': 0,
            'ThumpFrame': 36,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 120,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 3,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 22508 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 96100 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 36,
        'DefThump': 0,
        'ThumpFrame': 36,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 120,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 3,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 4 * (23220 * (Func10(*a) - 1) + 48600)),
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 4 * (77400 * (Func10(*a) - 1) + 162000)),
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'Toughness': 35,
            'MoveSpeed': 120,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 400 },
        1: {
            'HPMax': (lambda *a: 90032 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 384400 * Func10(*a) * (1 + 0.1 * Func592(*a))),
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'Toughness': 35,
            'MoveSpeed': 120,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 400 } }
    m_Reward = {
        1: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 3),
            402: (0, 3),
            501: (3000, 1) },
        2: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -2100 + 7000), 1),
            101: (10000, 6),
            402: (0, 3),
            402: (0, 3),
            501: (4000, 1) },
        3: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -2100 + 7000), 1),
            101: (10000, 6),
            402: (0, 3),
            402: (0, 3),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 15000
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14017,) },
        'Mode': { } }
    m_SpecialMHP = 10800


class CMonsterData22021(baseconfig.CMonsterData):
    m_SID = 22021
    m_DataSID = 2202
    m_Name = '八腕目'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 30960 * (Func10(*a) - 1) + 64800),
            'RHP': 0,
            'ArmorMax': (lambda *a: 103200 * (Func10(*a) - 1) + 216000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 75,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 36,
            'DefThump': 0,
            'ThumpFrame': 36,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 150,
            'AttSpeed': 13,
            'Toughness': 0,
            'TurnSpeed': 3,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 26440 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 94800 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 75,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 36,
        'DefThump': 0,
        'ThumpFrame': 36,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 150,
        'AttSpeed': 13,
        'Toughness': 0,
        'TurnSpeed': 3,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 100,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 7 * (30960 * (Func10(*a) - 1) + 64800)),
            'ArmorMax': (lambda *a: 7 * (103200 * (Func10(*a) - 1) + 216000)),
            'ShieldMax': 0,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 13,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 700 },
        1: {
            'HPMax': (lambda *a: 7 * (30960 * (Func10(*a) - 1) + 64800) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': (lambda *a: 7 * (103200 * (Func10(*a) - 1) + 216000) * (1 + 0.1 * Func592(*a))),
            'ShieldMax': 0,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 13,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 700 } }
    m_Reward = {
        1: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 3),
            402: (0, 3),
            501: (3000, 1) },
        2: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -2100 + 7000), 1),
            101: (10000, 6),
            402: (0, 3),
            402: (0, 3),
            501: (4000, 1) },
        3: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -2100 + 7000), 1),
            101: (10000, 6),
            402: (0, 3),
            402: (0, 3),
            501: (5000, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14014,) },
        'Mode': { } }
    m_SpecialMHP = 14400


class CMonsterData22022(baseconfig.CMonsterData):
    m_SID = 22022
    m_DataSID = 2202
    m_Name = '运载 八腕目'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 20640 * (Func10(*a) - 1) + 43200),
            'RHP': 0,
            'ArmorMax': (lambda *a: 68800 * (Func10(*a) - 1) + 144000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 75,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 36,
            'DefThump': 10000,
            'ThumpFrame': 36,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 150,
            'AttSpeed': 13,
            'Toughness': 0,
            'TurnSpeed': 3,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 20960 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 83200 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 75,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 36,
        'DefThump': 10000,
        'ThumpFrame': 36,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 150,
        'AttSpeed': 13,
        'Toughness': 0,
        'TurnSpeed': 3,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 100,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            6001: (10000, 1) },
        2: {
            6001: (10000, 1) },
        3: {
            6001: (10000, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14015,) },
        'Mode': { } }
    m_SpecialMHP = 9600


class CMonsterData22031(baseconfig.CMonsterData):
    m_SID = 22031
    m_DataSID = 2203
    m_Name = '敖龙'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 111800 * (Func10(*a) - 1) + 234000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 36,
            'DefThump': 0,
            'ThumpFrame': 36,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 3,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 107700 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 36,
        'DefThump': 0,
        'ThumpFrame': 36,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 3,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 100,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 7 * (111800 * (Func10(*a) - 1) + 234000)),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 700 },
        1: {
            'HPMax': (lambda *a: 7 * (111800 * (Func10(*a) - 1) + 234000) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 700 } }
    m_Reward = {
        1: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 3),
            402: (0, 3),
            501: (3000, 1) },
        2: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -2100 + 7000), 1),
            101: (10000, 6),
            402: (0, 3),
            402: (0, 3),
            501: (4000, 1) },
        3: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -2100 + 7000), 1),
            101: (10000, 6),
            402: (0, 3),
            402: (0, 3),
            501: (5000, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14021,) },
        'Mode': { } }
    m_SpecialMHP = 15600


class CMonsterData22051(baseconfig.CMonsterData):
    m_SID = 22051
    m_DataSID = 2205
    m_Name = '流寇电击者'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 23220 * (Func10(*a) - 1) + 48600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 77400 * (Func10(*a) - 1) + 162000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 36,
            'DefThump': 0,
            'ThumpFrame': 36,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 120,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 3,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 22508 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 96100 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 36,
        'DefThump': 0,
        'ThumpFrame': 36,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 120,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 3,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 4 * (23220 * (Func10(*a) - 1) + 48600)),
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 4 * (77400 * (Func10(*a) - 1) + 162000)),
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'Toughness': 35,
            'MoveSpeed': 120,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 400 },
        1: {
            'HPMax': (lambda *a: 4 * (23220 * (Func10(*a) - 1) + 48600) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 4 * (77400 * (Func10(*a) - 1) + 162000) * (1 + 0.1 * Func592(*a))),
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'Toughness': 35,
            'MoveSpeed': 120,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 400 } }
    m_Reward = {
        1: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 3),
            402: (0, 3),
            501: (3000, 1) },
        2: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -2100 + 7000), 1),
            101: (10000, 6),
            402: (0, 3),
            402: (0, 3),
            501: (4000, 1) },
        3: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -2100 + 7000), 1),
            101: (10000, 6),
            402: (0, 3),
            402: (0, 3),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 15000
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14018,) },
        'Mode': { } }
    m_SpecialMHP = 10800


class CMonsterData22061(baseconfig.CMonsterData):
    m_SID = 22061
    m_DataSID = 2206
    m_Name = '鳌灼'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 111800 * (Func10(*a) - 1) + 234000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 33540 * (Func10(*a) - 1) + 70200),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 36,
            'DefThump': 0,
            'ThumpFrame': 36,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 2,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 107700 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 36,
        'DefThump': 0,
        'ThumpFrame': 36,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 3,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 100,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 3),
            402: (0, 3),
            501: (3000, 1) },
        2: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -2100 + 7000), 1),
            101: (10000, 6),
            402: (0, 3),
            402: (0, 3),
            501: (4000, 1) },
        3: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -2100 + 7000), 1),
            101: (10000, 6),
            402: (0, 3),
            402: (0, 3),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 6666
    m_SprintSpeedUpMul = 6666
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14062, 14064) },
        'Mode': { } }
    m_SpecialMHP = 15600


class CMonsterData22211(baseconfig.CMonsterData):
    m_SID = 22211
    m_DataSID = 2221
    m_Name = '魔化 硝石勇士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 800 * (Func10(*a) - 1) + 2400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 25,
            'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
            'MoveSpeed': 30,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 1360 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 0,
        'DefThump': 100000,
        'ThumpFrame': 25,
        'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
        'MoveSpeed': 30,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 190000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14042,) },
        'Mode': { } }
    m_SpecialMHP = 240


class CMonsterData22212(baseconfig.CMonsterData):
    m_SID = 22212
    m_DataSID = 2221
    m_Name = '魔化 硝石勇士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 800 * (Func10(*a) - 1) + 2400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 25,
            'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
            'MoveSpeed': 30,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 1360 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 0,
        'DefThump': 100000,
        'ThumpFrame': 25,
        'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
        'MoveSpeed': 30,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 190000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14042,) },
        'Mode': { } }
    m_SpecialMHP = 240


class CMonsterData22221(baseconfig.CMonsterData):
    m_SID = 22221
    m_DataSID = 2222
    m_Name = '魔化 火硝勇士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 800 * (Func10(*a) - 1) + 2400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 25,
            'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
            'MoveSpeed': 30,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 1360 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 0,
        'DefThump': 100000,
        'ThumpFrame': 25,
        'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
        'MoveSpeed': 30,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 190000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14042,) },
        'Mode': { } }
    m_SpecialMHP = 240


class CMonsterData22222(baseconfig.CMonsterData):
    m_SID = 22222
    m_DataSID = 2222
    m_Name = '魔化 火硝勇士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 800 * (Func10(*a) - 1) + 2400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 25,
            'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
            'MoveSpeed': 30,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 1360 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 0,
        'DefThump': 100000,
        'ThumpFrame': 25,
        'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
        'MoveSpeed': 30,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 190000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14042,) },
        'Mode': { } }
    m_SpecialMHP = 240


class CMonsterData22231(baseconfig.CMonsterData):
    m_SID = 22231
    m_DataSID = 2223
    m_Name = '魔化 电硝勇士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 800 * (Func10(*a) - 1) + 2400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 25,
            'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
            'MoveSpeed': 30,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 1360 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 0,
        'DefThump': 100000,
        'ThumpFrame': 25,
        'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
        'MoveSpeed': 30,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 190000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14042,) },
        'Mode': { } }
    m_SpecialMHP = 240


class CMonsterData22232(baseconfig.CMonsterData):
    m_SID = 22232
    m_DataSID = 2223
    m_Name = '魔化 电硝勇士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 800 * (Func10(*a) - 1) + 2400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 25,
            'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
            'MoveSpeed': 30,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 1360 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 0,
        'DefThump': 100000,
        'ThumpFrame': 25,
        'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
        'MoveSpeed': 30,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 190000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14042,) },
        'Mode': { } }
    m_SpecialMHP = 240


class CMonsterData22241(baseconfig.CMonsterData):
    m_SID = 22241
    m_DataSID = 2224
    m_Name = '魔化 毒硝勇士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 800 * (Func10(*a) - 1) + 2400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 25,
            'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
            'MoveSpeed': 30,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 1360 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 0,
        'DefThump': 100000,
        'ThumpFrame': 25,
        'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
        'MoveSpeed': 30,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 190000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14042,) },
        'Mode': { } }
    m_SpecialMHP = 240


class CMonsterData22242(baseconfig.CMonsterData):
    m_SID = 22242
    m_DataSID = 2224
    m_Name = '魔化 毒硝勇士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 800 * (Func10(*a) - 1) + 2400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 25,
            'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
            'MoveSpeed': 30,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 1360 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 0,
        'DefThump': 100000,
        'ThumpFrame': 25,
        'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
        'MoveSpeed': 30,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 190000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14042,) },
        'Mode': { } }
    m_SpecialMHP = 240


class CMonsterData22251(baseconfig.CMonsterData):
    m_SID = 22251
    m_DataSID = 2225
    m_Name = '魔化 硝石飞蝠'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 800 * (Func10(*a) - 1) + 2400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 25,
            'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
            'MoveSpeed': 50,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 1360 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 0,
        'DefThump': 100000,
        'ThumpFrame': 25,
        'Att': (lambda *a: 340 * (Func10(*a) - 1) + 5000),
        'MoveSpeed': 50,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 100000
    m_SprintSpeedUpMul = 75000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 240


class CMonsterData22411(baseconfig.CMonsterData):
    m_SID = 22411
    m_DataSID = 2241
    m_Name = '魔化 投戟兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 18900 * (Func10(*a) - 1) + 40500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 90,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 32130 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 90,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 45556
    m_SprintSpeedUpMul = 40000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14010,) },
        'Mode': { } }
    m_SpecialMHP = 2700


class CMonsterData22412(baseconfig.CMonsterData):
    m_SID = 22412
    m_DataSID = 2241
    m_Name = '魔化 投戟兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 18900 * (Func10(*a) - 1) + 40500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 90,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 32130 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 90,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 45556
    m_SprintSpeedUpMul = 40000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14010,) },
        'Mode': { } }
    m_SpecialMHP = 2700


class CMonsterData22421(baseconfig.CMonsterData):
    m_SID = 22421
    m_DataSID = 2242
    m_Name = '烈焰沙蜥'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 23100 * (Func10(*a) - 1) + 49500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 32340 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14050,) },
        'Mode': { } }
    m_SpecialMHP = 3300


class CMonsterData22422(baseconfig.CMonsterData):
    m_SID = 22422
    m_DataSID = 2242
    m_Name = '大漠沙蜥【任务目标】'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 23100 * (Func10(*a) - 1) + 49500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 32340 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 3300


class CMonsterData22423(baseconfig.CMonsterData):
    m_SID = 22423
    m_DataSID = 2242
    m_Name = '烈焰沙蜥'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 23100 * (Func10(*a) - 1) + 49500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 32340 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14050,) },
        'Mode': { } }
    m_SpecialMHP = 3300


class CMonsterData22431(baseconfig.CMonsterData):
    m_SID = 22431
    m_DataSID = 2243
    m_Name = '雷霆沙蜥'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 23100 * (Func10(*a) - 1) + 49500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 32340 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14054,) },
        'Mode': { } }
    m_SpecialMHP = 3300


class CMonsterData22432(baseconfig.CMonsterData):
    m_SID = 22432
    m_DataSID = 2243
    m_Name = '雷霆沙蜥'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 23100 * (Func10(*a) - 1) + 49500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 32340 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14054,) },
        'Mode': { } }
    m_SpecialMHP = 3300


class CMonsterData22441(baseconfig.CMonsterData):
    m_SID = 22441
    m_DataSID = 2244
    m_Name = '剧毒沙蜥'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 23100 * (Func10(*a) - 1) + 49500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 32340 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14055,) },
        'Mode': { } }
    m_SpecialMHP = 3300


class CMonsterData22442(baseconfig.CMonsterData):
    m_SID = 22442
    m_DataSID = 2244
    m_Name = '剧毒沙蜥'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 23100 * (Func10(*a) - 1) + 49500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 32340 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14055,) },
        'Mode': { } }
    m_SpecialMHP = 3300


class CMonsterData22451(baseconfig.CMonsterData):
    m_SID = 22451
    m_DataSID = 2245
    m_Name = '魔化 投戟兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 19000 * (Func10(*a) - 1) + 40000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 90,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 32300 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 90,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            204: (3000, 1) },
        2: {
            204: (3000, 1) },
        3: {
            204: (3000, 1) } }
    m_RunSpeedUpMul = 45556
    m_SprintSpeedUpMul = 40000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 2700


class CMonsterData22811(baseconfig.CMonsterData):
    m_SID = 22811
    m_DataSID = 2281
    m_Name = '河童'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 25200 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 30,
            'DefThump': 0,
            'ThumpFrame': 30,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 150,
            'AttSpeed': 150,
            'Toughness': 0,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 37800 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 30,
        'DefThump': 0,
        'ThumpFrame': 30,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 150,
        'AttSpeed': 150,
        'Toughness': 0,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 5 * (25200 * (Func10(*a) - 1) + 54000)),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 150,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 500 },
        1: {
            'HPMax': (lambda *a: 5 * (25200 * (Func10(*a) - 1) + 54000) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 150,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 500 } }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14001,) },
        'Mode': { } }
    m_SpecialMHP = 3600


class CMonsterData22821(baseconfig.CMonsterData):
    m_SID = 22821
    m_DataSID = 2282
    m_Name = '虚妄僧'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 25200 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 30,
            'DefThump': 0,
            'ThumpFrame': 30,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 37800 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 30,
        'DefThump': 0,
        'ThumpFrame': 30,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 5 * (25200 * (Func10(*a) - 1) + 54000)),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 500 },
        1: {
            'HPMax': (lambda *a: 5 * (25200 * (Func10(*a) - 1) + 54000) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'Toughness': 35,
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 500 } }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14012,) },
        'Mode': { } }
    m_SpecialMHP = 3600


class CMonsterData22831(baseconfig.CMonsterData):
    m_SID = 22831
    m_DataSID = 2283
    m_Name = '虚无僧'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 27300 * (Func10(*a) - 1) + 58500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 31,
            'DefThump': 10000,
            'ThumpFrame': 31,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 40950 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 31,
        'DefThump': 10000,
        'ThumpFrame': 31,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 5 * (27300 * (Func10(*a) - 1) + 58500)),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'Toughness': 35,
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 500 },
        1: {
            'HPMax': (lambda *a: 5 * (27300 * (Func10(*a) - 1) + 58500) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': 0,
            'ShieldMax': 0,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'Toughness': 35,
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 500 } }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14002,) },
        'Mode': { } }
    m_SpecialMHP = 3900


class CMonsterData22851(baseconfig.CMonsterData):
    m_SID = 22851
    m_DataSID = 2285
    m_Name = '虚空僧'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 35700 * (Func10(*a) - 1) + 76500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 31,
            'DefThump': 10000,
            'ThumpFrame': 31,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 53550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 30,
        'DefThump': 0,
        'ThumpFrame': 30,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 150,
        'Toughness': 0,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 27778
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14061,) },
        'Mode': { } }
    m_SpecialMHP = 5100


class CMonsterData23011(baseconfig.CMonsterData):
    m_SID = 23011
    m_DataSID = 2301
    m_Name = '伞妖'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 7560 * (Func10(*a) - 1) + 16200),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 25200 * (Func10(*a) - 1) + 54000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 300,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 5000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 11340 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 37800 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 300,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 5000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 6667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14003,) },
        'Mode': { } }
    m_SpecialMHP = 3600


class CMonsterData23012(baseconfig.CMonsterData):
    m_SID = 23012
    m_DataSID = 2302
    m_Name = '【测试】伞妖'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 7560 * (Func10(*a) - 1) + 16200),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 25200 * (Func10(*a) - 1) + 54000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 300,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 5000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 11340 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 37800 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 300,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 5000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 6667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14003,) },
        'Mode': { } }
    m_SpecialMHP = 3600


class CMonsterData23211(baseconfig.CMonsterData):
    m_SID = 23211
    m_DataSID = 2321
    m_Name = '招潮蟹'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 390 * (Func10(*a) - 1) + 1170),
            'RHP': 0,
            'ArmorMax': (lambda *a: 1300 * (Func10(*a) - 1) + 3900),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 70,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
            'MoveSpeed': 150,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 600 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 1950 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 0,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 70,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 17,
        'DefThump': 0,
        'ThumpFrame': 17,
        'Att': (lambda *a: 30 * (Func10(*a) - 1) + 500),
        'MoveSpeed': 150,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 16667
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14008,) },
        'Mode': { } }
    m_SpecialMHP = 390


class CMonsterData23411(baseconfig.CMonsterData):
    m_SID = 23411
    m_DataSID = 2341
    m_Name = '钱龙'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 2.4 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 1000,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 },
        2: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 2.4 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 950,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 },
        3: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 2.4 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 900,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 2.4 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
        'StruckIgnoreFrame': 75,
        'DefKnockBack': 10000,
        'KnockBackFrame': 14,
        'DefThump': 10000,
        'ThumpFrame': 14,
        'Att': 7000,
        'MoveSpeed': 900,
        'AttSpeed': 45,
        'Toughness': 80,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -4000
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 28800


class CMonsterData23412(baseconfig.CMonsterData):
    m_SID = 23412
    m_DataSID = 2344
    m_Name = '钱尤'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 2.4 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 1000,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 },
        2: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 2.4 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 950,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 },
        3: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 2.4 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 900,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 2.4 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
        'StruckIgnoreFrame': 75,
        'DefKnockBack': 10000,
        'KnockBackFrame': 14,
        'DefThump': 10000,
        'ThumpFrame': 14,
        'Att': 7000,
        'MoveSpeed': 900,
        'AttSpeed': 45,
        'Toughness': 80,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -4000
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 28800


class CMonsterData23421(baseconfig.CMonsterData):
    m_SID = 23421
    m_DataSID = 2342
    m_Name = '钱龙'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.8 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 1000,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 },
        2: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.8 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 950,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 },
        3: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.8 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 900,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.8 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
        'StruckIgnoreFrame': 75,
        'DefKnockBack': 10000,
        'KnockBackFrame': 14,
        'DefThump': 10000,
        'ThumpFrame': 14,
        'Att': 7000,
        'MoveSpeed': 900,
        'AttSpeed': 45,
        'Toughness': 80,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -4000
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 28800


class CMonsterData23422(baseconfig.CMonsterData):
    m_SID = 23422
    m_DataSID = 2345
    m_Name = '钱尤'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.8 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 1000,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 },
        2: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.8 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 950,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 },
        3: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.8 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 900,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.8 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
        'StruckIgnoreFrame': 75,
        'DefKnockBack': 10000,
        'KnockBackFrame': 14,
        'DefThump': 10000,
        'ThumpFrame': 14,
        'Att': 7000,
        'MoveSpeed': 900,
        'AttSpeed': 45,
        'Toughness': 80,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -4000
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 28800


class CMonsterData23431(baseconfig.CMonsterData):
    m_SID = 23431
    m_DataSID = 2343
    m_Name = '钱龙'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.4 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 1000,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 },
        2: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.4 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 950,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 },
        3: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.4 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 900,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.4 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
        'StruckIgnoreFrame': 75,
        'DefKnockBack': 10000,
        'KnockBackFrame': 14,
        'DefThump': 10000,
        'ThumpFrame': 14,
        'Att': 7000,
        'MoveSpeed': 900,
        'AttSpeed': 45,
        'Toughness': 80,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -4000
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 28800


class CMonsterData23432(baseconfig.CMonsterData):
    m_SID = 23432
    m_DataSID = 2346
    m_Name = '钱尤'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.4 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 1000,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 },
        2: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.4 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 950,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 },
        3: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.4 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 900,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.4 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
        'StruckIgnoreFrame': 75,
        'DefKnockBack': 10000,
        'KnockBackFrame': 14,
        'DefThump': 10000,
        'ThumpFrame': 14,
        'Att': 7000,
        'MoveSpeed': 900,
        'AttSpeed': 45,
        'Toughness': 80,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -4000
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 28800


class CMonsterData23611(baseconfig.CMonsterData):
    m_SID = 23611
    m_DataSID = 2361
    m_Name = '雪地原住'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9450 * (Func10(*a) - 1) + 20250),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 31500 * (Func10(*a) - 1) + 67500),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 80,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 10400 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 34650 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 90,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 80,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 13333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14041,) },
        'Mode': { } }
    m_SpecialMHP = 4500


class CMonsterData23612(baseconfig.CMonsterData):
    m_SID = 23612
    m_DataSID = 2361
    m_Name = '雪地原住'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9450 * (Func10(*a) - 1) + 20250),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 31500 * (Func10(*a) - 1) + 67500),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 80,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 10400 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 34650 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 90,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 80,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            205: (10000, 4),
            203: (10000, 1) },
        2: {
            205: (10000, 4),
            203: (10000, 1) },
        3: {
            205: (10000, 4),
            203: (10000, 1) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14041,) },
        'Mode': { } }
    m_SpecialMHP = 4500


class CMonsterData23613(baseconfig.CMonsterData):
    m_SID = 23613
    m_DataSID = 2361
    m_Name = '雪地原住'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9450 * (Func10(*a) - 1) + 20250),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 31500 * (Func10(*a) - 1) + 67500),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 80,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 10400 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 34650 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 90,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 80,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (5000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1) },
        2: {
            201: (5000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1) },
        3: {
            201: (5000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 13333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14041,) },
        'Mode': { } }
    m_SpecialMHP = 4500


class CMonsterData23614(baseconfig.CMonsterData):
    m_SID = 23614
    m_DataSID = 2361
    m_Name = '雪地原住'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 3150 * (Func10(*a) - 1) + 6750),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 10500 * (Func10(*a) - 1) + 22500),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 25,
            'DefThump': 0,
            'ThumpFrame': 25,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 80,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 3500 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 11550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 90,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 25,
        'DefThump': 0,
        'ThumpFrame': 25,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1360),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 80,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: (0, 1),
            101: (0, 2),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        2: {
            201: (3000, 1),
            401: (0, 1),
            101: (0, 3),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        3: {
            201: (3000, 1),
            401: (0, 1),
            101: (0, 3),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 13333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14041,) },
        'Mode': { } }
    m_SpecialMHP = 4500


class CMonsterData23811(baseconfig.CMonsterData):
    m_SID = 23811
    m_DataSID = 2381
    m_Name = '魈骑兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 111800 * (Func10(*a) - 1) + 234000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 40,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 250,
            'AttSpeed': 35,
            'Toughness': 0,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 122980 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 40,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 250,
        'AttSpeed': 35,
        'Toughness': 0,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 25000
    m_MonsterPartSID = 23812
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14020, 14011) },
        'Mode': { } }
    m_SpecialMHP = 15600


class CMonsterData23812(baseconfig.CMonsterData):
    m_SID = 23812
    m_DataSID = 2382
    m_Name = '黄眉枪手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 35700 * (Func10(*a) - 1) + 76500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 40,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 200,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 39270 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 40,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 200,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 25000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14005,) },
        'Mode': { } }
    m_SpecialMHP = 5100


class CMonsterData23813(baseconfig.CMonsterData):
    m_SID = 23813
    m_DataSID = 2382
    m_Name = '雪地山魈'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 111800 * (Func10(*a) - 1) + 234000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 40,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 250,
            'AttSpeed': 35,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 122980 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 40,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 250,
        'AttSpeed': 35,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 12500
    m_SprintSpeedUpMul = 25000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14011,) },
        'Mode': { } }
    m_SpecialMHP = 15600


class CMonsterData23831(baseconfig.CMonsterData):
    m_SID = 23831
    m_DataSID = 2383
    m_Name = '雪地山魈'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 103200 * (Func10(*a) - 1) + 216000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 40,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 250,
            'AttSpeed': 35,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 113520 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 40,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 250,
        'AttSpeed': 35,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 12500
    m_SprintSpeedUpMul = 25000
    m_MonsterPartSID = 23832
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14011,) },
        'Mode': { } }
    m_SpecialMHP = 15600


class CMonsterData23832(baseconfig.CMonsterData):
    m_SID = 23832
    m_DataSID = 2384
    m_Name = '#NT#【测试】黄眉枪手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 35700 * (Func10(*a) - 1) + 76500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 40,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 200,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 39270 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 40,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 200,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 16666
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 5100


class CMonsterData23833(baseconfig.CMonsterData):
    m_SID = 23833
    m_DataSID = 2384
    m_Name = '#NT#【测试】雪地山魈'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 103200 * (Func10(*a) - 1) + 216000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 40,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 250,
            'AttSpeed': 35,
            'Toughness': 0,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 113520 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 40,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 250,
        'AttSpeed': 35,
        'Toughness': 0,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 25000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 15600


class CMonsterData23851(baseconfig.CMonsterData):
    m_SID = 23851
    m_DataSID = 2385
    m_Name = '黄眉枪手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 52500 * (Func10(*a) - 1) + 112500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 40,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 200,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 57750 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 40,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 200,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14005,) },
        'Mode': { } }
    m_SpecialMHP = 7500


class CMonsterData23861(baseconfig.CMonsterData):
    m_SID = 23861
    m_DataSID = 2386
    m_Name = '飞鸟骑士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 111800 * (Func10(*a) - 1) + 234000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 40,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 250,
            'AttSpeed': 35,
            'Toughness': 0,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 122980 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 40,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 250,
        'AttSpeed': 35,
        'Toughness': 0,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 25000
    m_MonsterPartSID = 23812
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14020, 14011) },
        'Mode': { } }
    m_SpecialMHP = 15600


class CMonsterData23871(baseconfig.CMonsterData):
    m_SID = 23871
    m_DataSID = 2387
    m_Name = '黄眉炮手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 52500 * (Func10(*a) - 1) + 112500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 40,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 200,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 57750 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 40,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 200,
        'AttSpeed': 12,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14005,) },
        'Mode': { } }
    m_SpecialMHP = 7500


class CMonsterData24011(baseconfig.CMonsterData):
    m_SID = 24011
    m_DataSID = 2401
    m_Name = '贯月仓'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 50,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 30,
            'DefThump': 10000,
            'ThumpFrame': 30,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 600,
            'AttSpeed': 15,
            'Toughness': 0,
            'TurnSpeed': 4,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 157262 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 50,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 30,
        'DefThump': 10000,
        'ThumpFrame': 30,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 600,
        'AttSpeed': 15,
        'Toughness': 0,
        'TurnSpeed': 4,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            501: (10000, 9) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14022,) },
        'Mode': { } }
    m_SpecialMHP = 28800


class CMonsterData24211(baseconfig.CMonsterData):
    m_SID = 24211
    m_DataSID = 2421
    m_Name = '剧毒幼蛛'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 800 * (Func10(*a) - 1) + 2400),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 21,
            'DefThump': 0,
            'ThumpFrame': 21,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 50,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 21,
        'DefThump': 0,
        'ThumpFrame': 21,
        'Att': (lambda *a: 5000 + 30 * Func592(*a)),
        'MoveSpeed': 300,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (3000, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (4000, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 110000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14058,) },
        'Mode': { } }
    m_SpecialMHP = 300


class CMonsterData24221(baseconfig.CMonsterData):
    m_SID = 24221
    m_DataSID = 2422
    m_Name = '蜘蛛猎手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 8640 * (Func10(*a) - 1) + 16200),
            'RHP': 0,
            'ArmorMax': (lambda *a: 28800 * (Func10(*a) - 1) + 54000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 27,
            'DefThump': 10000,
            'ThumpFrame': 27,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 100,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 22894 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 92980 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 35,
        'DefThump': 5000,
        'ThumpFrame': 35,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 5000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = {
        0: {
            'HPMax': (lambda *a: 4 * (8640 * (Func10(*a) - 1) + 16200)),
            'ArmorMax': (lambda *a: 4 * (28800 * (Func10(*a) - 1) + 54000)),
            'ShieldMax': 0,
            'Att': (lambda *a: 160 * (Func10(*a) - 1) + 2500),
            'Toughness': 35,
            'MoveSpeed': 170,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 400 },
        1: {
            'HPMax': (lambda *a: 4 * (8640 * (Func10(*a) - 1) + 16200) * (1 + 0.1 * Func592(*a))),
            'ArmorMax': (lambda *a: 4 * (28800 * (Func10(*a) - 1) + 54000) * (1 + 0.1 * Func592(*a))),
            'ShieldMax': 0,
            'Att': (lambda *a: 160 * (Func10(*a) - 1) + 2500),
            'Toughness': 35,
            'MoveSpeed': 170,
            'AttSpeed': 50,
            'DefKnockBack': 10000,
            'DefThump': 10000,
            'DodgeProb': 100,
            'SpecialMHPWeight': 400 } }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 40000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 5000


class CMonsterData24231(baseconfig.CMonsterData):
    m_SID = 24231
    m_DataSID = 2423
    m_Name = '剧毒幼蛛'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 800 * (Func10(*a) - 1) + 2400),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 21,
            'DefThump': 0,
            'ThumpFrame': 21,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 50,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 2550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 21,
        'DefThump': 0,
        'ThumpFrame': 21,
        'Att': (lambda *a: 5000 + 30 * Func592(*a)),
        'MoveSpeed': 300,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        2: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        3: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 110000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 240


class CMonsterData30011(baseconfig.CMonsterData):
    m_SID = 30011
    m_DataSID = 3001
    m_Name = '精英独角金龟'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 51,
            'DefThump': 10000,
            'ThumpFrame': 51,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 429470 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 51,
        'DefThump': 10000,
        'ThumpFrame': 51,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 20011
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14304,) },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData30012(baseconfig.CMonsterData):
    m_SID = 30012
    m_DataSID = 3001
    m_Name = '精英独角金龟'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 51,
            'DefThump': 10000,
            'ThumpFrame': 51,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 429470 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 51,
        'DefThump': 10000,
        'ThumpFrame': 51,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 20011
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14304,) },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData30041(baseconfig.CMonsterData):
    m_SID = 30041
    m_DataSID = 3004
    m_Name = '炎爆灯笼鬼'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 6300 * (Func10(*a) - 1) + 13500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 21,
            'DefThump': 0,
            'ThumpFrame': 21,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 300,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 9450 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 21,
        'DefThump': 0,
        'ThumpFrame': 21,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 300,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        2: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        3: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 900


class CMonsterData30211(baseconfig.CMonsterData):
    m_SID = 30211
    m_DataSID = 3021
    m_Name = '精英土狼'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 299700 * (Func10(*a) - 1) + 324000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 66,
            'DefThump': 10000,
            'ThumpFrame': 66,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 225,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 5 + 85),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 375664 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 66,
        'DefThump': 10000,
        'ThumpFrame': 66,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 225,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 5 + 85),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 20211
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 21600
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData30212(baseconfig.CMonsterData):
    m_SID = 30212
    m_DataSID = 3021
    m_Name = '精英土狼'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 299700 * (Func10(*a) - 1) + 324000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 66,
            'DefThump': 10000,
            'ThumpFrame': 66,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 225,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 375664 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 66,
        'DefThump': 10000,
        'ThumpFrame': 66,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 225,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 20211
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 21600
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData30831(baseconfig.CMonsterData):
    m_SID = 30831
    m_DataSID = 3083
    m_Name = '精英右矛兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 999999,
            'KnockBackFrame': 30,
            'DefThump': 999999,
            'ThumpFrame': 30,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 119820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 319550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 999999,
        'KnockBackFrame': 30,
        'DefThump': 999999,
        'ThumpFrame': 30,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 20831
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData30832(baseconfig.CMonsterData):
    m_SID = 30832
    m_DataSID = 3083
    m_Name = '精英右矛兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 999999,
            'KnockBackFrame': 30,
            'DefThump': 999999,
            'ThumpFrame': 30,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 119820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 319550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 999999,
        'KnockBackFrame': 30,
        'DefThump': 999999,
        'ThumpFrame': 30,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 20831
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData30841(baseconfig.CMonsterData):
    m_SID = 30841
    m_DataSID = 3084
    m_Name = '精英右矛兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (9999 * (Func10(*a) - 1) + 12) * ((Func10(*a) - 1) * 3150 + 9999)),
            'RHP': 0,
            'ArmorMax': (lambda *a: (9999 * (Func10(*a) - 1) + 12) * ((Func10(*a) - 1) * 9450 + 99000)),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 999999,
            'KnockBackFrame': 30,
            'DefThump': 999999,
            'ThumpFrame': 30,
            'Att': 6000,
            'MoveSpeed': 250,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: (9999 * (Func10(*a) - 1) + 12) * ((Func10(*a) - 1) * 3150 + 9999)),
        'RHP': 0,
        'ArmorMax': (lambda *a: (9999 * (Func10(*a) - 1) + 12) * ((Func10(*a) - 1) * 9450 + 99000)),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 999999,
        'KnockBackFrame': 30,
        'DefThump': 999999,
        'ThumpFrame': 30,
        'Att': 6000,
        'MoveSpeed': 250,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 20831
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData30871(baseconfig.CMonsterData):
    m_SID = 30871
    m_DataSID = 3087
    m_Name = '精英鲶人武士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 28,
            'DefThump': 10000,
            'ThumpFrame': 28,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 109820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 359550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 28,
        'DefThump': 10000,
        'ThumpFrame': 28,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 20871
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14311,) },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData30872(baseconfig.CMonsterData):
    m_SID = 30872
    m_DataSID = 3087
    m_Name = '精英鲶人武士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 28,
            'DefThump': 10000,
            'ThumpFrame': 28,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 109820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 359550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 28,
        'DefThump': 10000,
        'ThumpFrame': 28,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 20871
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData30873(baseconfig.CMonsterData):
    m_SID = 30873
    m_DataSID = 3087
    m_Name = '精英鲶人武士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 28,
            'DefThump': 10000,
            'ThumpFrame': 28,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 109820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 359550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 28,
        'DefThump': 10000,
        'ThumpFrame': 28,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        3: {
            6001: (10000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 20871
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14311,) },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData30891(baseconfig.CMonsterData):
    m_SID = 30891
    m_DataSID = 3089
    m_Name = '精英鲶人武士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 28,
            'DefThump': 10000,
            'ThumpFrame': 28,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 109820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 359550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 28,
        'DefThump': 10000,
        'ThumpFrame': 28,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        3: {
            6001: (10000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 20871
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14311,) },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData31231(baseconfig.CMonsterData):
    m_SID = 31231
    m_DataSID = 3123
    m_Name = '精英马头锐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 33,
            'DefThump': 10000,
            'ThumpFrame': 33,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 80,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 2,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 429490 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 33,
        'DefThump': 10000,
        'ThumpFrame': 33,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 80,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 3,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = -2500
    m_SprintSpeedUpMul = 8750
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 21231
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14302, 14303) },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData31232(baseconfig.CMonsterData):
    m_SID = 31232
    m_DataSID = 3123
    m_Name = '精英马头锐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 33,
            'DefThump': 10000,
            'ThumpFrame': 33,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 80,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 2,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 429490 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 33,
        'DefThump': 10000,
        'ThumpFrame': 33,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 80,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 3,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = -2500
    m_SprintSpeedUpMul = 8750
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 21231
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14302, 14303) },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData31251(baseconfig.CMonsterData):
    m_SID = 31251
    m_DataSID = 3125
    m_Name = '精英流寇帮凶'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 17,
            'DefThump': 10000,
            'ThumpFrame': 12,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 250,
            'AttSpeed': 100,
            'Toughness': 0,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 437552 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 17,
        'DefThump': 10000,
        'ThumpFrame': 12,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 250,
        'AttSpeed': 100,
        'Toughness': 0,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 14000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 21251
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14314,) },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData31252(baseconfig.CMonsterData):
    m_SID = 31252
    m_DataSID = 3125
    m_Name = '精英流寇帮凶'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 17,
            'DefThump': 10000,
            'ThumpFrame': 12,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 250,
            'AttSpeed': 100,
            'Toughness': 0,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 437552 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 17,
        'DefThump': 10000,
        'ThumpFrame': 12,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 250,
        'AttSpeed': 100,
        'Toughness': 0,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 14000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 21251
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14314,) },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData31261(baseconfig.CMonsterData):
    m_SID = 31261
    m_DataSID = 3126
    m_Name = '精英巡海夜叉'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 35,
            'DefThump': 10000,
            'ThumpFrame': 35,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 225,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 3500,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 119820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 359550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 35,
        'DefThump': 10000,
        'ThumpFrame': 35,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 225,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 3500,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 21261
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14315,) },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData31262(baseconfig.CMonsterData):
    m_SID = 31262
    m_DataSID = 3126
    m_Name = '精英巡海夜叉'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 35,
            'DefThump': 10000,
            'ThumpFrame': 35,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 225,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 3500,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 119820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 359550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 35,
        'DefThump': 10000,
        'ThumpFrame': 35,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 225,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 3500,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 21261
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14315,) },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData31281(baseconfig.CMonsterData):
    m_SID = 31281
    m_DataSID = 3128
    m_Name = '精英雪山守卫'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 632700 * (Func10(*a) - 1) + 684000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 299700 * (Func10(*a) - 1) + 324000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 35,
            'DefThump': 5000,
            'ThumpFrame': 35,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 7,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 5000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 282700 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 199670 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 95,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 35,
        'DefThump': 5000,
        'ThumpFrame': 35,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 5000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 100), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2),
            501: (3000, 1) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (4000, 1) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2),
            501: (5000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 21281
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData31341(baseconfig.CMonsterData):
    m_SID = 31341
    m_DataSID = 3134
    m_Name = '精英幽焰剑卫'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 999999,
            'KnockBackFrame': 30,
            'DefThump': 999999,
            'ThumpFrame': 30,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 10,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 119820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 319550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 999999,
        'KnockBackFrame': 30,
        'DefThump': 999999,
        'ThumpFrame': 30,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 100,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = 3333
    m_SprintSpeedUpMul = 15000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 21341
    m_ExtraPerform = {
        'Round': {
            (3, 10): (51231,) },
        'Mode': { } }
    m_SpecialMHP = 28800


class CMonsterData31342(baseconfig.CMonsterData):
    m_SID = 31342
    m_DataSID = 3134
    m_Name = '精英幽焰剑卫'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 999999,
            'KnockBackFrame': 30,
            'DefThump': 999999,
            'ThumpFrame': 30,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 10,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 119820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 319550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 999999,
        'KnockBackFrame': 30,
        'DefThump': 999999,
        'ThumpFrame': 30,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
        'IntervalTime': 100,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = 3333
    m_SprintSpeedUpMul = 15000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 21341
    m_ExtraPerform = {
        'Round': {
            (3, 10): (51231,) },
        'Mode': { } }
    m_SpecialMHP = 28800


class CMonsterData31421(baseconfig.CMonsterData):
    m_SID = 31421
    m_DataSID = 3142
    m_Name = '精英马贼隐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 109890 * (Func10(*a) - 1) + 118800),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 366300 * (Func10(*a) - 1) + 396000),
            'RShield': 2,
            'ShieldRecoverTime': 1000,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 26,
            'DefThump': 10000,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 83846 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 322820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 2,
        'ShieldRecoverTime': 1000,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 26,
        'DefThump': 10000,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 21421
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14312,) },
        'Mode': { } }
    m_SpecialMHP = 26400
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData31422(baseconfig.CMonsterData):
    m_SID = 31422
    m_DataSID = 3142
    m_Name = '精英马贼隐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 109890 * (Func10(*a) - 1) + 118800),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 366300 * (Func10(*a) - 1) + 396000),
            'RShield': 2,
            'ShieldRecoverTime': 1000,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 26,
            'DefThump': 10000,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 83846 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 322820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 2,
        'ShieldRecoverTime': 1000,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 26,
        'DefThump': 10000,
        'ThumpFrame': 26,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 21421
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14312,) },
        'Mode': { } }
    m_SpecialMHP = 26400
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData31641(baseconfig.CMonsterData):
    m_SID = 31641
    m_DataSID = 3164
    m_Name = '精英雷鸣猎手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 149850 * (Func10(*a) - 1) + 162000),
            'RHP': 0,
            'ArmorMax': (lambda *a: 499500 * (Func10(*a) - 1) + 540000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 28,
            'DefThump': 10000,
            'ThumpFrame': 28,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 120,
            'AttSpeed': 160,
            'Toughness': 50,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 80,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 84835 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 329450 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 28,
        'DefThump': 10000,
        'ThumpFrame': 28,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 120,
        'AttSpeed': 160,
        'Toughness': 50,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 80,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 21651
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData31642(baseconfig.CMonsterData):
    m_SID = 31642
    m_DataSID = 3164
    m_Name = '精英雷鸣猎手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 149850 * (Func10(*a) - 1) + 162000),
            'RHP': 0,
            'ArmorMax': (lambda *a: 499500 * (Func10(*a) - 1) + 540000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 28,
            'DefThump': 10000,
            'ThumpFrame': 28,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 120,
            'AttSpeed': 100,
            'Toughness': 50,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 80,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 84835 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 329450 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 28,
        'DefThump': 10000,
        'ThumpFrame': 28,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 120,
        'AttSpeed': 100,
        'Toughness': 50,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 80,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 21651
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData31651(baseconfig.CMonsterData):
    m_SID = 31651
    m_DataSID = 3165
    m_Name = '精英雷鸣猎手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 49950 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': (lambda *a: 166500 * (Func10(*a) - 1) + 180000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 28,
            'DefThump': 10000,
            'ThumpFrame': 28,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1000),
            'MoveSpeed': 120,
            'AttSpeed': 100,
            'Toughness': 50,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 44945 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 163150 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 28,
        'DefThump': 10000,
        'ThumpFrame': 28,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1000),
        'MoveSpeed': 120,
        'AttSpeed': 100,
        'Toughness': 50,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 100,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 21651
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14305,) },
        'Mode': { } }
    m_SpecialMHP = 9600


class CMonsterData31652(baseconfig.CMonsterData):
    m_SID = 31652
    m_DataSID = 3165
    m_Name = '精英雷鸣猎手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 49950 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': (lambda *a: 166500 * (Func10(*a) - 1) + 180000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 28,
            'DefThump': 10000,
            'ThumpFrame': 28,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1000),
            'MoveSpeed': 120,
            'AttSpeed': 100,
            'Toughness': 50,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 44945 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 163150 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 28,
        'DefThump': 10000,
        'ThumpFrame': 28,
        'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1000),
        'MoveSpeed': 120,
        'AttSpeed': 100,
        'Toughness': 50,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 100,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) },
        2: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) },
        3: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 21651
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14305,) },
        'Mode': { } }
    m_SpecialMHP = 9600
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData31831(baseconfig.CMonsterData):
    m_SID = 31831
    m_DataSID = 3183
    m_Name = '精英蟹先锋'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 37,
            'DefThump': 10000,
            'ThumpFrame': 37,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 80,
            'AttSpeed': 50,
            'Toughness': 20,
            'TurnSpeed': 4,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 47832 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 399440 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 37,
        'DefThump': 10000,
        'ThumpFrame': 37,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 20,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 50000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 21831
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14318,),
            (3, 9): (14317,) },
        'Mode': { } }
    m_SpecialMHP = 14400
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData31832(baseconfig.CMonsterData):
    m_SID = 31832
    m_DataSID = 3183
    m_Name = '精英蟹先锋'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 37,
            'DefThump': 10000,
            'ThumpFrame': 37,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 80,
            'AttSpeed': 50,
            'Toughness': 20,
            'TurnSpeed': 4,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 47832 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 399440 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 37,
        'DefThump': 10000,
        'ThumpFrame': 37,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 20,
        'TurnSpeed': 7,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 50000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 21831
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14318,),
            (3, 9): (14317,) },
        'Mode': { } }
    m_SpecialMHP = 14400
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData32011(baseconfig.CMonsterData):
    m_SID = 32011
    m_DataSID = 3201
    m_Name = '精英流寇纵毒者'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'RShield': 2,
            'ShieldRecoverTime': 1000,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 36,
            'DefThump': 10000,
            'ThumpFrame': 36,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 144,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 5,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 47832 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 399440 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 2,
        'ShieldRecoverTime': 1000,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 36,
        'DefThump': 10000,
        'ThumpFrame': 36,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 144,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 5,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = 15000
    m_SprintSpeedUpMul = 35138
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 22011
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14308,) },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData32012(baseconfig.CMonsterData):
    m_SID = 32012
    m_DataSID = 3201
    m_Name = '精英流寇纵毒者'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'RShield': 2,
            'ShieldRecoverTime': 1000,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 36,
            'DefThump': 10000,
            'ThumpFrame': 36,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 144,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 5,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 47832 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 399440 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RShield': 2,
        'ShieldRecoverTime': 1000,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 36,
        'DefThump': 10000,
        'ThumpFrame': 36,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 144,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 5,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = 15000
    m_SprintSpeedUpMul = 35138
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 22011
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14308,) },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData32031(baseconfig.CMonsterData):
    m_SID = 32031
    m_DataSID = 3203
    m_Name = '精英敖龙'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 566100 * (Func10(*a) - 1) + 612000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 36,
            'DefThump': 10000,
            'ThumpFrame': 36,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 3,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 0,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 409150 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 36,
        'DefThump': 10000,
        'ThumpFrame': 36,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 3,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 0,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 22031
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 40800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData32032(baseconfig.CMonsterData):
    m_SID = 32032
    m_DataSID = 3203
    m_Name = '精英敖龙'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 566100 * (Func10(*a) - 1) + 612000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 36,
            'DefThump': 10000,
            'ThumpFrame': 36,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 3,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 0,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 409150 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 36,
        'DefThump': 10000,
        'ThumpFrame': 36,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 3,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 0,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 22031
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 40800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData32421(baseconfig.CMonsterData):
    m_SID = 32421
    m_DataSID = 3242
    m_Name = '精英沙蜥'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 99900 * (Func10(*a) - 1) + 108000),
            'RHP': 0,
            'ArmorMax': (lambda *a: 333000 * (Func10(*a) - 1) + 360000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 26,
            'DefThump': 10000,
            'ThumpFrame': 26,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 79860 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 296200 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 26,
        'DefThump': 10000,
        'ThumpFrame': 26,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 22421
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14313,) },
        'Mode': { } }
    m_SpecialMHP = 24000
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData32422(baseconfig.CMonsterData):
    m_SID = 32422
    m_DataSID = 3242
    m_Name = '精英沙蜥'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 99900 * (Func10(*a) - 1) + 108000),
            'RHP': 0,
            'ArmorMax': (lambda *a: 333000 * (Func10(*a) - 1) + 360000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 26,
            'DefThump': 10000,
            'ThumpFrame': 26,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 79860 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 296200 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 26,
        'DefThump': 10000,
        'ThumpFrame': 26,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 150,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 22421
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14313,) },
        'Mode': { } }
    m_SpecialMHP = 24000
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData32811(baseconfig.CMonsterData):
    m_SID = 32811
    m_DataSID = 3281
    m_Name = '精英河童'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 31,
            'DefThump': 10000,
            'ThumpFrame': 31,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 399400 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 0,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 31,
        'DefThump': 10000,
        'ThumpFrame': 31,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 22811
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14316,) },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData32812(baseconfig.CMonsterData):
    m_SID = 32812
    m_DataSID = 3281
    m_Name = '精英河童'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 399600 * (Func10(*a) - 1) + 432000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 31,
            'DefThump': 10000,
            'ThumpFrame': 31,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 399400 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 0,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 31,
        'DefThump': 10000,
        'ThumpFrame': 31,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 22811
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14316,) },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData32821(baseconfig.CMonsterData):
    m_SID = 32821
    m_DataSID = 3282
    m_Name = '精英虚妄僧'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 499500 * (Func10(*a) - 1) + 540000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 30,
            'DefThump': 0,
            'ThumpFrame': 30,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 389250 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 30,
        'DefThump': 0,
        'ThumpFrame': 30,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 22821
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14310,) },
        'Mode': { } }
    m_SpecialMHP = 36000
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData32822(baseconfig.CMonsterData):
    m_SID = 32822
    m_DataSID = 3299
    m_Name = '虚妄僧残影'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 49950 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 30,
            'DefThump': 0,
            'ThumpFrame': 30,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 58925 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 30,
        'DefThump': 0,
        'ThumpFrame': 30,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        2: {
            201: (10000, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) },
        3: {
            201: (10000, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1),
            501: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14310,) },
        'Mode': { } }
    m_SpecialMHP = 3600


class CMonsterData32823(baseconfig.CMonsterData):
    m_SID = 32823
    m_DataSID = 3282
    m_Name = '精英虚妄僧'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 499500 * (Func10(*a) - 1) + 540000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 30,
            'DefThump': 0,
            'ThumpFrame': 30,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 389250 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 30,
        'DefThump': 0,
        'ThumpFrame': 30,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 22821
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14310,) },
        'Mode': { } }
    m_SpecialMHP = 36000
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData32824(baseconfig.CMonsterData):
    m_SID = 32824
    m_DataSID = 3299
    m_Name = '虚妄僧残影'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 49950 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 30,
            'DefThump': 0,
            'ThumpFrame': 30,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 58925 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 80,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 30,
        'DefThump': 0,
        'ThumpFrame': 30,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) },
        2: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) },
        3: {
            201: (6000, 1),
            401: (0, 1),
            101: (0, 4),
            402: (0, 2),
            402: (0, 2),
            501: (0, 1) } }
    m_RunSpeedUpMul = 12500
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14310,) },
        'Mode': { } }
    m_SpecialMHP = 3600


class CMonsterData32831(baseconfig.CMonsterData):
    m_SID = 32831
    m_DataSID = 3283
    m_Name = '精英虚无僧'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 299700 * (Func10(*a) - 1) + 324000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 31,
            'DefThump': 10000,
            'ThumpFrame': 31,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 409550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 31,
        'DefThump': 10000,
        'ThumpFrame': 31,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 22831
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 21600
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData32832(baseconfig.CMonsterData):
    m_SID = 32832
    m_DataSID = 3283
    m_Name = '精英虚无僧'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 299700 * (Func10(*a) - 1) + 324000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 31,
            'DefThump': 10000,
            'ThumpFrame': 31,
            'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 409550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 225,
        'DefKnockBack': 10000,
        'KnockBackFrame': 31,
        'DefThump': 10000,
        'ThumpFrame': 31,
        'Att': (lambda *a: 260 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 22831
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 21600
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData33811(baseconfig.CMonsterData):
    m_SID = 33811
    m_DataSID = 3381
    m_Name = '精英魈骑兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 566100 * (Func10(*a) - 1) + 612000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 280,
            'AttSpeed': 35,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 392710 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 280,
        'AttSpeed': 35,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = 12500
    m_SprintSpeedUpMul = 25000
    m_MonsterPartSID = 33812
    m_SurvivorGSCash = 0
    m_NormalMonster = 23811
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14307,) },
        'Mode': { } }
    m_SpecialMHP = 40800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData33812(baseconfig.CMonsterData):
    m_SID = 33812
    m_DataSID = 3382
    m_Name = '精英黄眉枪手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 299700 * (Func10(*a) - 1) + 324000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 100000,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 250,
            'AttSpeed': 35,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 269670 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 0,
        'ShieldRecoverTime': 100000,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 250,
        'AttSpeed': 35,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 40000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 21600


class CMonsterData33813(baseconfig.CMonsterData):
    m_SID = 33813
    m_DataSID = 3384
    m_Name = '精英魈骑兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 566100 * (Func10(*a) - 1) + 612000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 280,
            'AttSpeed': 35,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 392710 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 280,
        'AttSpeed': 35,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = 12500
    m_SprintSpeedUpMul = 25000
    m_MonsterPartSID = 33812
    m_SurvivorGSCash = 0
    m_NormalMonster = 23811
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14307,) },
        'Mode': { } }
    m_SpecialMHP = 40800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData33814(baseconfig.CMonsterData):
    m_SID = 33814
    m_DataSID = 3382
    m_Name = '精英黄眉枪手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 299700 * (Func10(*a) - 1) + 324000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 100000,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 250,
            'AttSpeed': 35,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 249670 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 0,
        'ShieldRecoverTime': 100000,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 250,
        'AttSpeed': 35,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 40000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 21600


class CMonsterData33815(baseconfig.CMonsterData):
    m_SID = 33815
    m_DataSID = 3383
    m_Name = '精英黄眉枪手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 566100 * (Func10(*a) - 1) + 612000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 280,
            'AttSpeed': 35,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 372710 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 280,
        'AttSpeed': 35,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = 12500
    m_SprintSpeedUpMul = 25000
    m_MonsterPartSID = 33812
    m_SurvivorGSCash = 0
    m_NormalMonster = 23851
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 21600
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData33851(baseconfig.CMonsterData):
    m_SID = 33851
    m_DataSID = 3385
    m_Name = '精英雪地山魈'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 566100 * (Func10(*a) - 1) + 612000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 280,
            'AttSpeed': 35,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 392710 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 0,
        'KnockBackFrame': 26,
        'DefThump': 0,
        'ThumpFrame': 26,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 280,
        'AttSpeed': 35,
        'Toughness': 0,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 50,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 12500
    m_SprintSpeedUpMul = 25000
    m_MonsterPartSID = 33851
    m_SurvivorGSCash = 0
    m_NormalMonster = 23813
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 20400
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData34011(baseconfig.CMonsterData):
    m_SID = 34011
    m_DataSID = 3401
    m_Name = '精英贯月仓'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 566100 * (Func10(*a) - 1) + 612000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 36,
            'DefThump': 10000,
            'ThumpFrame': 36,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
            'MoveSpeed': 180,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 3,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 0,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 402710 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 85,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 36,
        'DefThump': 10000,
        'ThumpFrame': 36,
        'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
        'MoveSpeed': 180,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 3,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 0,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 24011
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 28800
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData34211(baseconfig.CMonsterData):
    m_SID = 34211
    m_DataSID = 3421
    m_Name = '精英蜘蛛猎手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 109890 * (Func10(*a) - 1) + 118800),
            'RHP': 0,
            'ArmorMax': (lambda *a: 366300 * (Func10(*a) - 1) + 396000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 26,
            'DefThump': 10000,
            'ThumpFrame': 26,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 200,
            'AttSpeed': 100,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 0,
            'IntervalTime': (lambda *a: 150 - Func205(*a) * 25),
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 119820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 359550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 28,
        'DefThump': 10000,
        'ThumpFrame': 28,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 120,
        'AttSpeed': 160,
        'Toughness': 50,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 80,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 7) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2401: (2000, 1),
            1001: (10000, 1),
            501: (10000, 9) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 15000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 24221
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14309,) },
        'Mode': { } }
    m_SpecialMHP = 21600
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData34212(baseconfig.CMonsterData):
    m_SID = 34212
    m_DataSID = 3422
    m_Name = '精英蜘蛛猎手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 109890 * (Func10(*a) - 1) + 118800),
            'RHP': 0,
            'ArmorMax': (lambda *a: 366300 * (Func10(*a) - 1) + 396000),
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 26,
            'DefThump': 10000,
            'ThumpFrame': 26,
            'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 200,
            'AttSpeed': 100,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 0,
            'IntervalTime': (lambda *a: 150 - Func205(*a) * 25),
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 119820 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'RHP': 0,
        'ArmorMax': (lambda *a: 359550 * Func10(*a) * (1 + 0.1 * Func592(*a))),
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 150,
        'DefKnockBack': 10000,
        'KnockBackFrame': 28,
        'DefThump': 10000,
        'ThumpFrame': 28,
        'Att': (lambda *a: 250 * (Func10(*a) - 1) + 2500),
        'MoveSpeed': 120,
        'AttSpeed': 160,
        'Toughness': 50,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': (lambda *a: Func205(*a) * 20 + 40),
        'IntervalTime': 80,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        2: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) },
        3: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (0, 1),
            2401: (0, 0),
            1001: (10000, 1),
            501: (10000, 5) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 15000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 24221
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 21600
    m_DeviceEnergyPoint = {
        3: 10 }


class CMonsterData39011(baseconfig.CMonsterData):
    m_SID = 39011
    m_DataSID = 3901
    m_Name = '陆吾'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 8000000,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 800000,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 250,
            'AttSpeed': 56,
            'Toughness': 50,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 165681818 + 16568182 * Func592(*a)),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 16568182 + 1656818 * Func592(*a)),
        'RShield': 0,
        'ShieldRecoverTime': 0,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 10000,
        'KnockBackFrame': 14,
        'DefThump': 10000,
        'ThumpFrame': 14,
        'Att': 24000,
        'MoveSpeed': 250,
        'AttSpeed': 56,
        'Toughness': 50,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            501: (10000, 10),
            2404: (10000, 1),
            101: (10000, 9),
            4101: (10000, 1),
            1001: (10000, 2),
            201: (10000, 3) },
        2: {
            501: (10000, 15),
            2404: (10000, 1),
            101: (10000, 12),
            4101: (10000, 1),
            1001: (10000, 2),
            201: (10000, 3) },
        3: {
            501: (10000, 20),
            2404: (10000, 1),
            101: (10000, 15),
            4101: (10000, 1),
            1001: (10000, 2),
            201: (10000, 3) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14413,),
            (3, 9): (14401,) },
        'Mode': { } }
    m_SpecialMHP = 180000
    m_DeviceEnergyPoint = {
        5: 10 }


class CMonsterData39021(baseconfig.CMonsterData):
    m_SID = 39021
    m_DataSID = 3902
    m_Name = '吞天'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 144000000,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 1800000,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 15000,
            'MoveSpeed': 250,
            'AttSpeed': 56,
            'Toughness': 50,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 180000000 + 18000000 * Func592(*a)),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 2250000 + 225000 * Func592(*a)),
        'RShield': 0,
        'ShieldRecoverTime': 0,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 10000,
        'KnockBackFrame': 14,
        'DefThump': 10000,
        'ThumpFrame': 14,
        'Att': 30000,
        'MoveSpeed': 250,
        'AttSpeed': 56,
        'Toughness': 50,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            501: (10000, 25) },
        2: {
            501: (10000, 30) },
        3: {
            501: (10000, 35) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14416,) },
        'Mode': { } }
    m_SpecialMHP = 180000
    m_DeviceEnergyPoint = {
        5: 10 }


class CMonsterData39022(baseconfig.CMonsterData):
    m_SID = 39022
    m_DataSID = 3910
    m_Name = '#NT#罗睺-常驻弱点'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 1600000,
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
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 250,
            'AttSpeed': 56,
            'Toughness': 50,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 1600000 + 160000 * Func592(*a)),
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
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 10000,
        'KnockBackFrame': 14,
        'DefThump': 10000,
        'ThumpFrame': 14,
        'Att': 14000,
        'MoveSpeed': 250,
        'AttSpeed': 56,
        'Toughness': 50,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 2000


class CMonsterData39023(baseconfig.CMonsterData):
    m_SID = 39023
    m_DataSID = 3911
    m_Name = '#NT#罗睺-阶段一弱点'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 400000,
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
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 250,
            'AttSpeed': 56,
            'Toughness': 50,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 400000 + 40000 * Func592(*a)),
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
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 10000,
        'KnockBackFrame': 14,
        'DefThump': 10000,
        'ThumpFrame': 14,
        'Att': 14000,
        'MoveSpeed': 250,
        'AttSpeed': 56,
        'Toughness': 50,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 500


class CMonsterData39024(baseconfig.CMonsterData):
    m_SID = 39024
    m_DataSID = 3904
    m_Name = '吞天'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 180000000,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 2250000,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 18750,
            'MoveSpeed': 250,
            'AttSpeed': 56,
            'Toughness': 50,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 180000000 + 18000000 * Func592(*a)),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': (lambda *a: 2250000 + 225000 * Func592(*a)),
        'RShield': 0,
        'ShieldRecoverTime': 0,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 10000,
        'KnockBackFrame': 14,
        'DefThump': 10000,
        'ThumpFrame': 14,
        'Att': 37500,
        'MoveSpeed': 250,
        'AttSpeed': 56,
        'Toughness': 50,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            501: (10000, 25) },
        2: {
            501: (10000, 30) },
        3: {
            501: (10000, 35) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14416,),
            (3, 9): (14408,) },
        'Mode': { } }
    m_SpecialMHP = 180000
    m_DeviceEnergyPoint = {
        5: 10 }


class CMonsterData39031(baseconfig.CMonsterData):
    m_SID = 39031
    m_DataSID = 3913
    m_Name = '鱼龙后裔'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 10507200,
            'RHP': 0,
            'ArmorMax': 10507200,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 10000,
            'KnockBackFrame': 17,
            'DefThump': 10000,
            'ThumpFrame': 17,
            'Att': 7000,
            'MoveSpeed': 1200,
            'AttSpeed': 50,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 1000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 91125000 + 9112500 * Func592(*a)),
        'RHP': 0,
        'ArmorMax': (lambda *a: 91125000 + 9112500 * Func592(*a)),
        'ShieldMax': 0,
        'RShield': 0,
        'ShieldRecoverTime': 0,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 10000,
        'KnockBackFrame': 17,
        'DefThump': 10000,
        'ThumpFrame': 17,
        'Att': 28000,
        'MoveSpeed': 1200,
        'AttSpeed': 50,
        'Toughness': 80,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 1000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -5000
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 180000


class CMonsterData39051(baseconfig.CMonsterData):
    m_SID = 39051
    m_DataSID = 3905
    m_Name = '夜姬丸'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 32000000,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 100000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 0,
            'Att': 15000,
            'MoveSpeed': 500,
            'AttSpeed': 50,
            'Toughness': 80,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 0,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 182250000 + 18225000 * Func592(*a)),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 100000,
        'KnockBackFrame': 0,
        'DefThump': 100000,
        'ThumpFrame': 0,
        'Att': 30000,
        'MoveSpeed': 500,
        'AttSpeed': 50,
        'Toughness': 80,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 0,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            501: (10000, 20),
            1001: (10000, 2),
            101: (10000, 20),
            201: (10000, 3),
            4101: (10000, 1),
            2404: (10000, 1) },
        2: {
            501: (10000, 25),
            1001: (10000, 2),
            101: (10000, 25),
            201: (10000, 4),
            4101: (10000, 1),
            2404: (10000, 1) },
        3: {
            501: (10000, 30),
            1001: (10000, 2),
            101: (10000, 30),
            201: (10000, 5),
            4101: (10000, 1),
            2404: (10000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14414,),
            (3, 9): (14402,) },
        'Mode': { } }
    m_SpecialMHP = 180000
    m_DeviceEnergyPoint = {
        5: 10 }


class CMonsterData39052(baseconfig.CMonsterData):
    m_SID = 39052
    m_DataSID = 3906
    m_Name = '夜姬丸'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 2000100,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 100000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 0,
            'Att': 15000,
            'MoveSpeed': 500,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 0,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: Func515(*a, **{
'sAttr': 'HPMax' }) * 0.0625),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 100000,
        'KnockBackFrame': 0,
        'DefThump': 100000,
        'ThumpFrame': 0,
        'Att': 30000,
        'MoveSpeed': 500,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 0,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 11200


class CMonsterData39091(baseconfig.CMonsterData):
    m_SID = 39091
    m_DataSID = 3909
    m_Name = '连城'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 8000000,
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
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 100000,
            'KnockBackFrame': 2,
            'DefThump': 100000,
            'ThumpFrame': 2,
            'Att': 9000,
            'MoveSpeed': 500,
            'AttSpeed': 56,
            'Toughness': 100,
            'TurnSpeed': 2,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2500,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 182250000 + 18225000 * Func592(*a)),
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
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 100000,
        'KnockBackFrame': 2,
        'DefThump': 100000,
        'ThumpFrame': 2,
        'Att': 28000,
        'MoveSpeed': 500,
        'AttSpeed': 56,
        'Toughness': 100,
        'TurnSpeed': 2,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2500,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            501: (10000, 10),
            2404: (10000, 1),
            101: (10000, 9),
            4101: (10000, 1),
            1001: (10000, 2),
            201: (10000, 3) },
        2: {
            501: (10000, 15),
            2404: (10000, 1),
            101: (10000, 12),
            4101: (10000, 1),
            1001: (10000, 2),
            201: (10000, 3) },
        3: {
            501: (10000, 20),
            2404: (10000, 1),
            101: (10000, 15),
            4101: (10000, 1),
            1001: (10000, 2),
            201: (10000, 3) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14412,),
            (3, 9): (14403,) },
        'Mode': { } }
    m_SpecialMHP = 180000
    m_DeviceEnergyPoint = {
        5: 10 }


class CMonsterData39131(baseconfig.CMonsterData):
    m_SID = 39131
    m_DataSID = 3913
    m_Name = '鱼龙后裔'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 13134000,
            'RHP': 0,
            'ArmorMax': 13134000,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 10000,
            'KnockBackFrame': 17,
            'DefThump': 10000,
            'ThumpFrame': 17,
            'Att': 10000,
            'MoveSpeed': 1800,
            'AttSpeed': 50,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 1000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 91125000 + 9112500 * Func592(*a)),
        'RHP': 0,
        'ArmorMax': (lambda *a: 91125000 + 9112500 * Func592(*a)),
        'ShieldMax': 0,
        'RShield': 0,
        'ShieldRecoverTime': 0,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 10000,
        'KnockBackFrame': 17,
        'DefThump': 10000,
        'ThumpFrame': 17,
        'Att': 30000,
        'MoveSpeed': 1800,
        'AttSpeed': 50,
        'Toughness': 80,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 1000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 3),
            101: (10000, 18),
            4101: (10000, 1),
            2404: (10000, 1),
            1001: (10000, 2),
            501: (10000, 15) },
        2: {
            201: (10000, 3),
            101: (10000, 24),
            4101: (10000, 1),
            2404: (10000, 1),
            1001: (10000, 2),
            501: (10000, 20) },
        3: {
            201: (10000, 3),
            101: (10000, 30),
            4101: (10000, 1),
            2404: (10000, 1),
            1001: (10000, 2),
            501: (10000, 25) } }
    m_RunSpeedUpMul = -5000
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14418,),
            (3, 9): (14405,),
            (1, 0): (5323,) },
        'Mode': { } }
    m_SpecialMHP = 180000
    m_DeviceEnergyPoint = {
        5: 10 }


class CMonsterData39141(baseconfig.CMonsterData):
    m_SID = 39141
    m_DataSID = 3914
    m_Name = '鱼龙后裔'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 10507200,
            'RHP': 0,
            'ArmorMax': 10507200,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 10000,
            'KnockBackFrame': 17,
            'DefThump': 10000,
            'ThumpFrame': 17,
            'Att': 7000,
            'MoveSpeed': 1200,
            'AttSpeed': 50,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 1000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 91125000 + 9112500 * Func592(*a)),
        'RHP': 0,
        'ArmorMax': (lambda *a: 91125000 + 9112500 * Func592(*a)),
        'ShieldMax': 0,
        'RShield': 0,
        'ShieldRecoverTime': 0,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 10000,
        'KnockBackFrame': 17,
        'DefThump': 10000,
        'ThumpFrame': 17,
        'Att': 24000,
        'MoveSpeed': 1200,
        'AttSpeed': 50,
        'Toughness': 80,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 1000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -5000
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 180000


class CMonsterData39151(baseconfig.CMonsterData):
    m_SID = 39151
    m_DataSID = 3915
    m_Name = '风神'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 24516800,
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
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 250,
            'AttSpeed': 56,
            'Toughness': 50,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 182250000 + 18225000 * Func592(*a)),
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
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 10000,
        'KnockBackFrame': 14,
        'DefThump': 10000,
        'ThumpFrame': 14,
        'Att': 28000,
        'MoveSpeed': 250,
        'AttSpeed': 56,
        'Toughness': 50,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            501: (10000, 15),
            2404: (10000, 1),
            101: (10000, 18),
            4101: (10000, 1),
            1001: (10000, 2),
            201: (10000, 3) },
        2: {
            501: (10000, 20),
            2404: (10000, 1),
            101: (10000, 24),
            4101: (10000, 1),
            1001: (10000, 2),
            201: (10000, 3) },
        3: {
            501: (10000, 25),
            2404: (10000, 1),
            101: (10000, 30),
            4101: (10000, 1),
            1001: (10000, 2),
            201: (10000, 3) } }
    m_RunSpeedUpMul = 30000
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14419,),
            (3, 9): (14404,) },
        'Mode': { } }
    m_SpecialMHP = 180000
    m_DeviceEnergyPoint = {
        5: 10 }


class CMonsterData39201(baseconfig.CMonsterData):
    m_SID = 39201
    m_DataSID = 3920
    m_Name = '虬蛇'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 64000000,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 100000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 0,
            'Att': 15000,
            'MoveSpeed': 4000,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 0,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 182250000 + 18225000 * Func592(*a)),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 100000,
        'KnockBackFrame': 0,
        'DefThump': 100000,
        'ThumpFrame': 0,
        'Att': 40000,
        'MoveSpeed': 4000,
        'AttSpeed': 50,
        'Toughness': 0,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 0,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            501: (10000, 20),
            1001: (10000, 2),
            101: (10000, 20),
            201: (10000, 3),
            4101: (10000, 1),
            2404: (10000, 1) },
        2: {
            501: (10000, 25),
            1001: (10000, 2),
            101: (10000, 25),
            201: (10000, 4),
            4101: (10000, 1),
            2404: (10000, 1) },
        3: {
            501: (10000, 30),
            1001: (10000, 2),
            101: (10000, 30),
            201: (10000, 5),
            4101: (10000, 1),
            2404: (10000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14406,) },
        'Mode': { } }
    m_SpecialMHP = 180000
    m_DeviceEnergyPoint = {
        5: 10 }


class CMonsterData39211(baseconfig.CMonsterData):
    m_SID = 39211
    m_DataSID = 3921
    m_Name = '虬蛇'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 64000000,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 100000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 0,
            'Att': 15000,
            'MoveSpeed': 500,
            'AttSpeed': 50,
            'Toughness': 80,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 500,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 182250000 + 18225000 * Func592(*a)),
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 10,
        'ShieldRecoverTime': 500,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 100000,
        'KnockBackFrame': 0,
        'DefThump': 100000,
        'ThumpFrame': 0,
        'Att': 40000,
        'MoveSpeed': 500,
        'AttSpeed': 50,
        'Toughness': 80,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 500,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14407,) },
        'Mode': { } }
    m_SpecialMHP = 180000


class CMonsterData39241(baseconfig.CMonsterData):
    m_SID = 39241
    m_DataSID = 3924
    m_Name = '极地妖王'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 144000000,
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
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 100000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 0,
            'Att': 15000,
            'MoveSpeed': 250,
            'AttSpeed': 50,
            'Toughness': 80,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 5000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 30000,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 182250000 + 18225000 * Func592(*a)),
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
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 100000,
        'KnockBackFrame': 0,
        'DefThump': 100000,
        'ThumpFrame': 0,
        'Att': 40000,
        'MoveSpeed': 250,
        'AttSpeed': 50,
        'Toughness': 80,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 5000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 30000,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            501: (10000, 25) },
        2: {
            501: (10000, 30) },
        3: {
            501: (10000, 35) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14415,),
            (3, 9): (14409,) },
        'Mode': { } }
    m_SpecialMHP = 180000
    m_DeviceEnergyPoint = {
        5: 10 }


class CMonsterData39251(baseconfig.CMonsterData):
    m_SID = 39251
    m_DataSID = 3925
    m_Name = '极地妖王'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 144000000,
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
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 100000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 0,
            'Att': 15000,
            'MoveSpeed': 250,
            'AttSpeed': 50,
            'Toughness': 80,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2500,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 30000,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 182250000 + 18225000 * Func592(*a)),
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
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 100000,
        'KnockBackFrame': 0,
        'DefThump': 100000,
        'ThumpFrame': 0,
        'Att': 40000,
        'MoveSpeed': 250,
        'AttSpeed': 50,
        'Toughness': 80,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2500,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 30000,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            501: (10000, 25) },
        2: {
            501: (10000, 30) },
        3: {
            501: (10000, 35) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 10): (14415,),
            (3, 9): (14409,) },
        'Mode': { } }
    m_SpecialMHP = 180000
    m_DeviceEnergyPoint = {
        5: 10 }


class CMonsterData39261(baseconfig.CMonsterData):
    m_SID = 39261
    m_DataSID = 3926
    m_Name = '极地妖王'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 144000000,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 288000000,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 100000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 0,
            'Att': 15000,
            'MoveSpeed': 250,
            'AttSpeed': 50,
            'Toughness': 80,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 2500,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 30000,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': 144000000,
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 288000000,
        'RShield': 0,
        'ShieldRecoverTime': 0,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 100,
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 100000,
        'KnockBackFrame': 0,
        'DefThump': 100000,
        'ThumpFrame': 0,
        'Att': 30000,
        'MoveSpeed': 250,
        'AttSpeed': 50,
        'Toughness': 80,
        'TurnSpeed': 14,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 2500,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 30000,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': {
            (3, 9): (14409,) },
        'Mode': { } }
    m_SpecialMHP = 180000


class CMonsterData39991(baseconfig.CMonsterData):
    m_SID = 39991
    m_DataSID = 3999
    m_Name = '#NT#测试怪物-蜘蛛'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 8000000,
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
            'StruckIgnoreFrame': 300,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 400,
            'AttSpeed': 56,
            'Toughness': 50,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': 8000000,
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
        'StruckIgnoreFrame': 300,
        'DefKnockBack': 10000,
        'KnockBackFrame': 14,
        'DefThump': 10000,
        'ThumpFrame': 14,
        'Att': 7000,
        'MoveSpeed': 400,
        'AttSpeed': 56,
        'Toughness': 50,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 180000


class CMonsterData39992(baseconfig.CMonsterData):
    m_SID = 39992
    m_DataSID = 4000
    m_Name = '钱龙【挑战事件】'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.8 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 1000,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 },
        2: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.8 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 950,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 },
        3: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.8 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 14,
            'DefThump': 10000,
            'ThumpFrame': 14,
            'Att': 7000,
            'MoveSpeed': 900,
            'AttSpeed': 45,
            'Toughness': 80,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 100 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) * 1.8 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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
        'StruckIgnoreFrame': 75,
        'DefKnockBack': 10000,
        'KnockBackFrame': 14,
        'DefThump': 10000,
        'ThumpFrame': 14,
        'Att': 7000,
        'MoveSpeed': 900,
        'AttSpeed': 45,
        'Toughness': 80,
        'TurnSpeed': 28,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 10000,
        'SaveTime': 0,
        'DodgeProb': 100,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 100 }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -4000
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 28800

