# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3010/monster.pyc
# RelativePath: clientlogic/cl_wardata/w3010/monster.pyc
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
            1004: (10000, 1) },
        2: {
            1004: (10000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData2005(baseconfig.CMonsterData):
    m_SID = 2005
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
            202: (0, 2),
            401: (10000, 1) },
        2: {
            202: (0, 2),
            401: (10000, 1) } }
    m_RunSpeedUpMul = 5000
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


class CMonsterData20011(baseconfig.CMonsterData):
    m_SID = 20011
    m_DataSID = 2001
    m_Name = '魔化 独角金龟'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * 7.5e-05 - 0.0039 * (Func10(*a) - 1)) + 0.1) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 900 + 486 * (Func10(*a) - 1) + 29000)),
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
            'Att': (lambda *a: 31 * (Func10(*a) - 1) + 600),
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
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * 7.5e-05 - 0.0043 * (Func10(*a) - 1)) + 0.11) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1300 + 3531 * (Func10(*a) - 1) + 54300)),
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
            'Att': (lambda *a: 39 * (Func10(*a) - 1) + 760),
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
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * 7.5e-05 - 0.0043 * (Func10(*a) - 1)) + 0.12) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 2100 + -1797 * (Func10(*a) - 1) + 78000)),
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
            'Att': (lambda *a: 50 * (Func10(*a) - 1) + 1010),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4000, 1),
            401: (400, 1),
            101: (3000, 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 90000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData20611(baseconfig.CMonsterData):
    m_SID = 20611
    m_DataSID = 2061
    m_Name = '魔化 投雷散兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 720 + 388 * (Func10(*a) - 1) + 23200)),
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
            'Att': (lambda *a: 122 * (Func10(*a) - 1) + 2000),
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
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1040 + 2824 * (Func10(*a) - 1) + 43440)),
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
            'Att': (lambda *a: 155 * (Func10(*a) - 1) + 2550),
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
            'IntervalTime': 40,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1680 + -1438 * (Func10(*a) - 1) + 62400)),
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
            'Att': (lambda *a: 199 * (Func10(*a) - 1) + 3380),
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
            'IntervalTime': 35,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4000, 1),
            401: (400, 1),
            101: (10000, 2),
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
    m_SpecialMHP = 0


class CMonsterData20621(baseconfig.CMonsterData):
    m_SID = 20621
    m_DataSID = 2062
    m_Name = '魔化 火雷散兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 720 + 388 * (Func10(*a) - 1) + 23200)),
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
            'Att': (lambda *a: 122 * (Func10(*a) - 1) + 2000),
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
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1040 + 2824 * (Func10(*a) - 1) + 43440)),
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
            'Att': (lambda *a: 155 * (Func10(*a) - 1) + 2550),
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
            'IntervalTime': 40,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1680 + -1438 * (Func10(*a) - 1) + 62400)),
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
            'Att': (lambda *a: 199 * (Func10(*a) - 1) + 3380),
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
            'IntervalTime': 35,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4000, 1),
            401: (400, 1),
            101: (10000, 2),
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
    m_SpecialMHP = 0


class CMonsterData20631(baseconfig.CMonsterData):
    m_SID = 20631
    m_DataSID = 2063
    m_Name = '魔化 电雷散兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 720 + 388 * (Func10(*a) - 1) + 23200)),
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
            'Att': (lambda *a: 122 * (Func10(*a) - 1) + 2000),
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
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1040 + 2824 * (Func10(*a) - 1) + 43440)),
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
            'Att': (lambda *a: 155 * (Func10(*a) - 1) + 2550),
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
            'IntervalTime': 40,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1680 + -1438 * (Func10(*a) - 1) + 62400)),
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
            'Att': (lambda *a: 199 * (Func10(*a) - 1) + 3380),
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
            'IntervalTime': 35,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4000, 1),
            401: (400, 1),
            101: (10000, 2),
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
    m_SpecialMHP = 0


class CMonsterData20641(baseconfig.CMonsterData):
    m_SID = 20641
    m_DataSID = 2064
    m_Name = '魔化 毒雷散兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 720 + 388 * (Func10(*a) - 1) + 23200)),
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
            'Att': (lambda *a: 122 * (Func10(*a) - 1) + 2000),
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
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1040 + 2824 * (Func10(*a) - 1) + 43440)),
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
            'Att': (lambda *a: 155 * (Func10(*a) - 1) + 2550),
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
            'IntervalTime': 40,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1680 + -1438 * (Func10(*a) - 1) + 62400)),
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
            'Att': (lambda *a: 199 * (Func10(*a) - 1) + 3380),
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
            'IntervalTime': 35,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4000, 1),
            401: (400, 1),
            101: (10000, 2),
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
    m_SpecialMHP = 0


class CMonsterData20811(baseconfig.CMonsterData):
    m_SID = 20811
    m_DataSID = 2081
    m_Name = '魔化 徒甲兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 225 + 121 * (Func10(*a) - 1) + 7250)),
            'RHP': 0,
            'ArmorMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 675 + 364 * (Func10(*a) - 1) + 21750)),
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
            'Att': (lambda *a: 122 * (Func10(*a) - 1) + 2000),
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
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 325 + 882 * (Func10(*a) - 1) + 13575)),
            'RHP': 0,
            'ArmorMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 975 + 2648 * (Func10(*a) - 1) + 40725)),
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
            'Att': (lambda *a: 155 * (Func10(*a) - 1) + 2550),
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
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 525 + -450 * (Func10(*a) - 1) + 19500)),
            'RHP': 0,
            'ArmorMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1575 + -1348 * (Func10(*a) - 1) + 58500)),
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
            'Att': (lambda *a: 199 * (Func10(*a) - 1) + 3380),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4000, 1),
            401: (400, 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 4285
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData20831(baseconfig.CMonsterData):
    m_SID = 20831
    m_DataSID = 2083
    m_Name = '魔化 右矛兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 270 + 145 * (Func10(*a) - 1) + 8700)),
            'RHP': 0,
            'ArmorMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 810 + 437 * (Func10(*a) - 1) + 26100)),
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
            'Att': (lambda *a: 122 * (Func10(*a) - 1) + 2000),
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
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 390 + 1059 * (Func10(*a) - 1) + 16290)),
            'RHP': 0,
            'ArmorMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1170 + 3177 * (Func10(*a) - 1) + 48870)),
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
            'Att': (lambda *a: 155 * (Func10(*a) - 1) + 2550),
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
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 630 + -539 * (Func10(*a) - 1) + 23400)),
            'RHP': 0,
            'ArmorMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1890 + -1617 * (Func10(*a) - 1) + 70200)),
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
            'Att': (lambda *a: 199 * (Func10(*a) - 1) + 3380),
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
            201: (4000, 1),
            401: (400, 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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


class CMonsterData21011(baseconfig.CMonsterData):
    m_SID = 21011
    m_DataSID = 2101
    m_Name = '魔化 左弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 720 + 388 * (Func10(*a) - 1) + 23200)),
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
            'Att': (lambda *a: 76 * (Func10(*a) - 1) + 1380),
            'MoveSpeed': 100,
            'AttSpeed': 13,
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
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1040 + 2824 * (Func10(*a) - 1) + 43440)),
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
            'Att': (lambda *a: 97 * (Func10(*a) - 1) + 1760),
            'MoveSpeed': 100,
            'AttSpeed': 11,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 60,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1680 + -1438 * (Func10(*a) - 1) + 62400)),
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
            'Att': (lambda *a: 124 * (Func10(*a) - 1) + 2340),
            'MoveSpeed': 100,
            'AttSpeed': 9,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 40,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4000, 1),
            401: (400, 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 26000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21012(baseconfig.CMonsterData):
    m_SID = 21012
    m_DataSID = 2101
    m_Name = '魔化 左弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 180 + 97 * (Func10(*a) - 1) + 5800)),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 540 + 291 * (Func10(*a) - 1) + 17400)),
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
            'Att': (lambda *a: 76 * (Func10(*a) - 1) + 1380),
            'MoveSpeed': 100,
            'AttSpeed': 13,
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
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 260 + 706 * (Func10(*a) - 1) + 10860)),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 780 + 2118 * (Func10(*a) - 1) + 32580)),
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
            'Att': (lambda *a: 97 * (Func10(*a) - 1) + 1760),
            'MoveSpeed': 100,
            'AttSpeed': 11,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 60,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 420 + -360 * (Func10(*a) - 1) + 15600)),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1260 + -1079 * (Func10(*a) - 1) + 46800)),
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
            'Att': (lambda *a: 124 * (Func10(*a) - 1) + 2340),
            'MoveSpeed': 100,
            'AttSpeed': 9,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 40,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4000, 1),
            401: (400, 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 26000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21021(baseconfig.CMonsterData):
    m_SID = 21021
    m_DataSID = 2102
    m_Name = '魔化 徒盾弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 180 + 97 * (Func10(*a) - 1) + 5800)),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 540 + 291 * (Func10(*a) - 1) + 17400)),
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
            'Att': (lambda *a: 122 * (Func10(*a) - 1) + 2000),
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
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 260 + 706 * (Func10(*a) - 1) + 10860)),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 780 + 2118 * (Func10(*a) - 1) + 32580)),
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
            'Att': (lambda *a: 155 * (Func10(*a) - 1) + 2550),
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
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 420 + -360 * (Func10(*a) - 1) + 15600)),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1260 + -1079 * (Func10(*a) - 1) + 46800)),
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
            'Att': (lambda *a: 199 * (Func10(*a) - 1) + 3380),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4000, 1),
            401: (400, 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 5000
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


class CMonsterData21231(baseconfig.CMonsterData):
    m_SID = 21231
    m_DataSID = 2123
    m_Name = '魔化 马头锐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1170 + 632 * (Func10(*a) - 1) + 37700)),
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
            'Att': (lambda *a: 122 * (Func10(*a) - 1) + 2000),
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
            'IntervalTime': 140,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1690 + 4590 * (Func10(*a) - 1) + 70590)),
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
            'Att': (lambda *a: 155 * (Func10(*a) - 1) + 2550),
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
            'IntervalTime': 120,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 2730 + -2336 * (Func10(*a) - 1) + 101400)),
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
            'Att': (lambda *a: 199 * (Func10(*a) - 1) + 3380),
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
            'IntervalTime': 100,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4000, 1),
            401: (400, 1),
            101: (10000, 2),
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
    m_SpecialMHP = 0


class CMonsterData21411(baseconfig.CMonsterData):
    m_SID = 21411
    m_DataSID = 2141
    m_Name = '魔化 重弩锐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.001 - 0.0702 * (Func10(*a) - 1)) + 4.875) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 180 + 97 * (Func10(*a) - 1) + 5800)),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.001 - 0.0702 * (Func10(*a) - 1)) + 4.875) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 540 + 291 * (Func10(*a) - 1) + 17400)),
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
            'Att': (lambda *a: 76 * (Func10(*a) - 1) + 1380),
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
            'IntervalTime': 80,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.001 - 0.0702 * (Func10(*a) - 1)) + 4.875) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 260 + 706 * (Func10(*a) - 1) + 10860)),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.001 - 0.0702 * (Func10(*a) - 1)) + 4.875) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 780 + 2118 * (Func10(*a) - 1) + 32580)),
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
            'Att': (lambda *a: 97 * (Func10(*a) - 1) + 1760),
            'MoveSpeed': 160,
            'AttSpeed': 11,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 60,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.001 - 0.0702 * (Func10(*a) - 1)) + 4.875) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 420 + -360 * (Func10(*a) - 1) + 15600)),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.001 - 0.0702 * (Func10(*a) - 1)) + 4.875) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1260 + -1079 * (Func10(*a) - 1) + 46800)),
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
            'Att': (lambda *a: 124 * (Func10(*a) - 1) + 2340),
            'MoveSpeed': 160,
            'AttSpeed': 10,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 70),
            'IntervalTime': 40,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4000, 1),
            401: (400, 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 3125
    m_SprintSpeedUpMul = 21250
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21611(baseconfig.CMonsterData):
    m_SID = 21611
    m_DataSID = 2161
    m_Name = '魔化 长弩锐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 202.5 + 109 * (Func10(*a) - 1) + 6525)),
            'RHP': 0,
            'ArmorMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 607.5 + 327 * (Func10(*a) - 1) + 19575)),
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
            'Att': (lambda *a: 122 * (Func10(*a) - 1) + 2000),
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
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 292.5 + 794 * (Func10(*a) - 1) + 12217)),
            'RHP': 0,
            'ArmorMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 877.5 + 2382 * (Func10(*a) - 1) + 36652)),
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
            'Att': (lambda *a: 155 * (Func10(*a) - 1) + 2550),
            'MoveSpeed': 120,
            'AttSpeed': 40,
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
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 472.5 + -405 * (Func10(*a) - 1) + 17550)),
            'RHP': 0,
            'ArmorMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1417.5 + -1213 * (Func10(*a) - 1) + 52650)),
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
            'Att': (lambda *a: 199 * (Func10(*a) - 1) + 3380),
            'MoveSpeed': 120,
            'AttSpeed': 35,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4000, 1),
            401: (400, 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22211(baseconfig.CMonsterData):
    m_SID = 22211
    m_DataSID = 2221
    m_Name = '魔化 硝石勇士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * 7.5e-05 - 0.0039 * (Func10(*a) - 1)) + 0.1) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 720 + 388 * (Func10(*a) - 1) + 23200)),
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
            'ThumpFrame': 0,
            'Att': (lambda *a: 232 * (Func10(*a) - 1) + 4500),
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
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * 7.5e-05 - 0.0043 * (Func10(*a) - 1)) + 0.11) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1040 + 2824 * (Func10(*a) - 1) + 43440)),
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
            'ThumpFrame': 0,
            'Att': (lambda *a: 297 * (Func10(*a) - 1) + 5750),
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
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * 7.5e-05 - 0.0043 * (Func10(*a) - 1)) + 0.12) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1680 + -1438 * (Func10(*a) - 1) + 62400)),
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
            'ThumpFrame': 0,
            'Att': (lambda *a: 380 * (Func10(*a) - 1) + 7620),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4000, 1),
            401: (400, 1),
            101: (5000, 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 190000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22221(baseconfig.CMonsterData):
    m_SID = 22221
    m_DataSID = 2222
    m_Name = '魔化 火硝勇士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * 7.5e-05 - 0.0039 * (Func10(*a) - 1)) + 0.1) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 720 + 388 * (Func10(*a) - 1) + 23200)),
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
            'ThumpFrame': 0,
            'Att': (lambda *a: 232 * (Func10(*a) - 1) + 4500),
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
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * 7.5e-05 - 0.0043 * (Func10(*a) - 1)) + 0.11) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1040 + 2824 * (Func10(*a) - 1) + 43440)),
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
            'ThumpFrame': 0,
            'Att': (lambda *a: 297 * (Func10(*a) - 1) + 5750),
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
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * 7.5e-05 - 0.0043 * (Func10(*a) - 1)) + 0.12) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1680 + -1438 * (Func10(*a) - 1) + 62400)),
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
            'ThumpFrame': 0,
            'Att': (lambda *a: 380 * (Func10(*a) - 1) + 7620),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4000, 1),
            401: (400, 1),
            101: (5000, 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 190000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22231(baseconfig.CMonsterData):
    m_SID = 22231
    m_DataSID = 2223
    m_Name = '魔化 电硝勇士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * 7.5e-05 - 0.0039 * (Func10(*a) - 1)) + 0.1) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 720 + 388 * (Func10(*a) - 1) + 23200)),
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
            'ThumpFrame': 0,
            'Att': (lambda *a: 232 * (Func10(*a) - 1) + 4500),
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
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * 7.5e-05 - 0.0043 * (Func10(*a) - 1)) + 0.11) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1040 + 2824 * (Func10(*a) - 1) + 43440)),
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
            'ThumpFrame': 0,
            'Att': (lambda *a: 297 * (Func10(*a) - 1) + 5750),
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
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * 7.5e-05 - 0.0043 * (Func10(*a) - 1)) + 0.12) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1680 + -1438 * (Func10(*a) - 1) + 62400)),
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
            'ThumpFrame': 0,
            'Att': (lambda *a: 380 * (Func10(*a) - 1) + 7620),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4000, 1),
            401: (400, 1),
            101: (5000, 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 190000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22241(baseconfig.CMonsterData):
    m_SID = 22241
    m_DataSID = 2224
    m_Name = '魔化 毒硝勇士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * 7.5e-05 - 0.0039 * (Func10(*a) - 1)) + 0.1) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 720 + 388 * (Func10(*a) - 1) + 23200)),
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
            'ThumpFrame': 0,
            'Att': (lambda *a: 232 * (Func10(*a) - 1) + 4500),
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
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * 7.5e-05 - 0.0043 * (Func10(*a) - 1)) + 0.11) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1040 + 2824 * (Func10(*a) - 1) + 43440)),
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
            'ThumpFrame': 0,
            'Att': (lambda *a: 297 * (Func10(*a) - 1) + 5750),
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
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * 7.5e-05 - 0.0043 * (Func10(*a) - 1)) + 0.12) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1680 + -1438 * (Func10(*a) - 1) + 62400)),
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
            'ThumpFrame': 0,
            'Att': (lambda *a: 380 * (Func10(*a) - 1) + 7620),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4000, 1),
            401: (400, 1),
            101: (5000, 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 190000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22411(baseconfig.CMonsterData):
    m_SID = 22411
    m_DataSID = 2241
    m_Name = '魔化 投戟兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 810 + 437 * (Func10(*a) - 1) + 26100)),
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
            'Att': (lambda *a: 122 * (Func10(*a) - 1) + 2000),
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
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1170 + 3177 * (Func10(*a) - 1) + 48870)),
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
            'Att': (lambda *a: 155 * (Func10(*a) - 1) + 2550),
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
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.0007 - 0.0418 * (Func10(*a) - 1)) + 3) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1890 + -1617 * (Func10(*a) - 1) + 70200)),
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
            'Att': (lambda *a: 199 * (Func10(*a) - 1) + 3380),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4000, 1),
            401: (400, 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 45556
    m_SprintSpeedUpMul = 40000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData30831(baseconfig.CMonsterData):
    m_SID = 30831
    m_DataSID = 3083
    m_Name = '精英右矛兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.012 - 0.1693 * (Func10(*a) - 1)) + 30) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 390 + 1059 * (Func10(*a) - 1) + 16290)),
            'RHP': 0,
            'ArmorMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.012 - 0.1693 * (Func10(*a) - 1)) + 30) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1170 + 3177 * (Func10(*a) - 1) + 48870)),
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
            'Att': (lambda *a: 165 * (Func10(*a) - 1) + 2400),
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
            'SpecialMHPWeight': 0 },
        2: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.012 - 0.1693 * (Func10(*a) - 1)) + 30) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 390 + 1059 * (Func10(*a) - 1) + 16290)),
            'RHP': 0,
            'ArmorMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.012 - 0.1693 * (Func10(*a) - 1)) + 30) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1170 + 3177 * (Func10(*a) - 1) + 48870)),
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
            'Att': (lambda *a: 211 * (Func10(*a) - 1) + 3060),
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
            'SpecialMHPWeight': 0 },
        3: {
            'HPMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.016 - 0.0533 * (Func10(*a) - 1)) + 30) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 630 + -539 * (Func10(*a) - 1) + 23400)),
            'RHP': 0,
            'ArmorMax': (lambda *a: (((Func10(*a) - 1) * (Func10(*a) - 1) * -0.016 - 0.0533 * (Func10(*a) - 1)) + 30) * ((Func10(*a) - 1) * (Func10(*a) - 1) * 1890 + -1617 * (Func10(*a) - 1) + 70200)),
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
            'Att': (lambda *a: 271 * (Func10(*a) - 1) + 4060),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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


class CMonsterData39011(baseconfig.CMonsterData):
    m_SID = 39011
    m_DataSID = 3901
    m_Name = '陆吾'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 4000000,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 400000,
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
            'AttSpeed': (lambda *a: 68 - Func205(*a) * 4),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0

