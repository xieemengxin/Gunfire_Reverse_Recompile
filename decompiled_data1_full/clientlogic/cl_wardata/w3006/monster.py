# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3006/monster.pyc
# RelativePath: clientlogic/cl_wardata/w3006/monster.pyc
# Source Generated with Decompyle++
# File: monster.pyc (Python 3.6)

from cl_resmgr.resdata import CMonsterData as CCustom
import cl_resmgr.resdata as baseconfig
from cl_newformula import Func10, Func205

class CMonsterData1020(baseconfig.CMonsterData):
    m_SID = 1020
    m_DataSID = 1020
    m_Name = '靶子'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 13000 * 1.25 ** (Func10(*a) - 1) * 1 + 0),
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
            'KnockBackFrame': 10,
            'DefThump': 0,
            'ThumpFrame': 12,
            'Att': (lambda *a: 1800 * 1.15 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 500,
            'AttSpeed': 100,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            202: (10000, 2) },
        2: {
            202: (10000, 2) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData1021(baseconfig.CMonsterData):
    m_SID = 1021
    m_DataSID = 1020
    m_Name = '靶子'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 12000 * 1.25 ** (Func10(*a) - 1) * 1 + 0),
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
            'KnockBackFrame': 10,
            'DefThump': 0,
            'ThumpFrame': 12,
            'Att': (lambda *a: 1800 * 1.15 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 500,
            'AttSpeed': 100,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            1003: (10000, 1) },
        2: {
            1003: (10000, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData2001(baseconfig.CMonsterData):
    m_SID = 2001
    m_DataSID = 2098
    m_Name = '魔化 徒甲兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 3528 * (Func10(*a) - 1) + 8592),
            'RHP': 0,
            'ArmorMax': (lambda *a: 11760 * (Func10(*a) - 1) + 28640),
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
            'KnockBackFrame': 20,
            'DefThump': 0,
            'ThumpFrame': 20,
            'Att': (lambda *a: 160 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 350,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            202: (10000, 2) },
        2: {
            202: (10000, 2) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData2002(baseconfig.CMonsterData):
    m_SID = 2002
    m_DataSID = 2117
    m_Name = '魔化 左弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 10000 * 1.25 ** (Func10(*a) - 1) * 1 + 40500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 20,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': (lambda *a: 2300 * 1.15 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 100,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            202: (10000, 2) },
        2: {
            202: (10000, 2) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData2003(baseconfig.CMonsterData):
    m_SID = 2003
    m_DataSID = 2099
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            202: (10000, 2) },
        2: {
            202: (10000, 2) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData2004(baseconfig.CMonsterData):
    m_SID = 2004
    m_DataSID = 2117
    m_Name = '魔化 左弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 10000 * 1.25 ** (Func10(*a) - 1) * 1 + 0),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 20,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': (lambda *a: 2300 * 1.15 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 100,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            1003: (10000, 1) },
        2: {
            1003: (10000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData2012(baseconfig.CMonsterData):
    m_SID = 2012
    m_DataSID = 2117
    m_Name = '小型远程-连射'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 10000 * 1.25 ** (Func10(*a) - 1) * 1 + 0),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 20,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': (lambda *a: 2300 * 1.15 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 100,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            202: (10000, 2) },
        2: {
            202: (10000, 2) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData2026(baseconfig.CMonsterData):
    m_SID = 2026
    m_DataSID = 1019
    m_Name = '小型近战-木桩'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 12000 * 1.25 ** (Func10(*a) - 1) * 1 + 0),
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
            'KnockBackFrame': 10,
            'DefThump': 0,
            'ThumpFrame': 12,
            'Att': (lambda *a: 1800 * 1.15 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 500,
            'AttSpeed': 100,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            1001: (10000, 1) },
        2: {
            1001: (10000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData2027(baseconfig.CMonsterData):
    m_SID = 2027
    m_DataSID = 1019
    m_Name = '小型近战-木桩2'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 12000 * 1.25 ** (Func10(*a) - 1) * 1 + 0),
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
            'KnockBackFrame': 10,
            'DefThump': 0,
            'ThumpFrame': 12,
            'Att': (lambda *a: 1800 * 1.15 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 500,
            'AttSpeed': 100,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            202: (10000, 2) },
        2: {
            202: (10000, 2) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData20971(baseconfig.CMonsterData):
    m_SID = 20971
    m_DataSID = 2098
    m_Name = '魔化 徒甲兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 3528 * (Func10(*a) - 1) + 8592),
            'RHP': 0,
            'ArmorMax': (lambda *a: 11760 * (Func10(*a) - 1) + 28640),
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
            'KnockBackFrame': 20,
            'DefThump': 0,
            'ThumpFrame': 20,
            'Att': (lambda *a: 160 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 350,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            202: (10000, 2) },
        2: {
            202: (10000, 2) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData20981(baseconfig.CMonsterData):
    m_SID = 20981
    m_DataSID = 2098
    m_Name = '魔化 徒甲兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 3528 * (Func10(*a) - 1) + 8592),
            'RHP': 0,
            'ArmorMax': (lambda *a: 11760 * (Func10(*a) - 1) + 28640),
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
            'KnockBackFrame': 20,
            'DefThump': 0,
            'ThumpFrame': 20,
            'Att': (lambda *a: 160 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 350,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            202: (10000, 2) },
        2: {
            202: (10000, 2) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData20991(baseconfig.CMonsterData):
    m_SID = 20991
    m_DataSID = 2099
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            202: (10000, 2) },
        2: {
            202: (10000, 2) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21171(baseconfig.CMonsterData):
    m_SID = 21171
    m_DataSID = 2117
    m_Name = '魔化 左弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 10000 * 1.25 ** (Func10(*a) - 1) * 1 + 0),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 20,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': (lambda *a: 2300 * 1.15 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 100,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            1003: (10000, 1) },
        2: {
            1003: (10000, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21172(baseconfig.CMonsterData):
    m_SID = 21172
    m_DataSID = 2117
    m_Name = '魔化 左弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 10000 * 1.25 ** (Func10(*a) - 1) * 1 + 0),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 20,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': (lambda *a: 2300 * 1.15 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 100,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            202: (10000, 2) },
        2: {
            202: (10000, 2) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21181(baseconfig.CMonsterData):
    m_SID = 21181
    m_DataSID = 2117
    m_Name = '魔化 左弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 10000 * 1.25 ** (Func10(*a) - 1) * 1 + 0),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 20,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': (lambda *a: 2300 * 1.15 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 100,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            202: (10000, 2) },
        2: {
            202: (10000, 2) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21191(baseconfig.CMonsterData):
    m_SID = 21191
    m_DataSID = 2117
    m_Name = '魔化 左弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 10000 * 1.25 ** (Func10(*a) - 1) * 1 + 0),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 20,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': (lambda *a: 2300 * 1.15 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 100,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            202: (10000, 2) },
        2: {
            202: (10000, 2) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21192(baseconfig.CMonsterData):
    m_SID = 21192
    m_DataSID = 2098
    m_Name = '魔化 徒甲兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 7290 * (Func10(*a) - 1) + 12150),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 24300 * (Func10(*a) - 1) + 40500),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 20,
            'DefThump': 0,
            'ThumpFrame': 20,
            'Att': (lambda *a: 160 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 350,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            202: (10000, 2) },
        2: {
            202: (10000, 2) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21193(baseconfig.CMonsterData):
    m_SID = 21193
    m_DataSID = 2117
    m_Name = '魔化 左弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 7290 * (Func10(*a) - 1) + 12150),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 24300 * (Func10(*a) - 1) + 40500),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 20,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': (lambda *a: 2300 * 1.15 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 100,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            202: (10000, 2) },
        2: {
            202: (10000, 2) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21194(baseconfig.CMonsterData):
    m_SID = 21194
    m_DataSID = 2117
    m_Name = '魔化 左弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 17640 * (Func10(*a) - 1) + 42960),
            'RHP': 0,
            'ArmorMax': (lambda *a: 11760 * (Func10(*a) - 1) + 28640),
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 20,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': (lambda *a: 2300 * 1.15 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 100,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            202: (10000, 2) },
        2: {
            202: (10000, 2) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21195(baseconfig.CMonsterData):
    m_SID = 21195
    m_DataSID = 2098
    m_Name = '魔化 徒甲兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 17640 * (Func10(*a) - 1) + 42960),
            'RHP': 0,
            'ArmorMax': (lambda *a: 11760 * (Func10(*a) - 1) + 28640),
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
            'KnockBackFrame': 20,
            'DefThump': 0,
            'ThumpFrame': 20,
            'Att': (lambda *a: 160 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 350,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
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
    m_SpecialMHP = 0


class CMonsterData21196(baseconfig.CMonsterData):
    m_SID = 21196
    m_DataSID = 3083
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
            'Att': (lambda *a: 9999 * (Func10(*a) - 1) + 9999),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            202: (10000, 2) },
        2: {
            202: (10000, 2) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0

