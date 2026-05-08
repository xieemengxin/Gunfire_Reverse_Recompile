# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3004/monster.pyc
# RelativePath: clientlogic/cl_wardata/w3004/monster.pyc
# Source Generated with Decompyle++
# File: monster.pyc (Python 3.6)

from cl_resmgr.resdata import CMonsterData as CCustom
import cl_resmgr.resdata as baseconfig
from cl_newformula import Func10, Func204, Func205

class CMonsterData1020(baseconfig.CMonsterData):
    m_SID = 1020
    m_DataSID = 1020
    m_Name = '靶子'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 200000,
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
            'StruckIgnoreFrame': 0,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 1000 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 500,
            'AttSpeed': 50,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            405: (10000, 1) },
        2: {
            405: (10000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData2001(baseconfig.CMonsterData):
    m_SID = 2001
    m_DataSID = 2081
    m_Name = '近战怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 100000,
            'RHP': 0,
            'ArmorMax': 100000,
            'ShieldMax': 100000,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 0,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 1000 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 500,
            'AttSpeed': 50,
            'Toughness': 100,
            'TurnSpeed': 14,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 10 + 0),
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            405: (10000, 1) },
        2: {
            405: (10000, 1) } }
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
    m_DataSID = 2101
    m_Name = '远程兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 20000 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 0,
            'StruckIgnoreFrame': 0,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': 100,
            'MoveSpeed': 500,
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
            406: (10000, 1) },
        2: {
            406: (10000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData2003(baseconfig.CMonsterData):
    m_SID = 2003
    m_DataSID = 2101
    m_Name = '远程兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 30000 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
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
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 2700 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 200,
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
            407: (10000, 1) },
        2: {
            407: (10000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData2004(baseconfig.CMonsterData):
    m_SID = 2004
    m_DataSID = 2081
    m_Name = '近战怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 20000 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
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
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 3600 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 450,
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
            408: (10000, 1) },
        2: {
            408: (10000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData2091(baseconfig.CMonsterData):
    m_SID = 2091
    m_DataSID = 1019
    m_Name = '【护甲木桩】左弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 10000000,
            'RHP': 0,
            'ArmorMax': 10000000,
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
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 1800 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 450,
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


class CMonsterData2093(baseconfig.CMonsterData):
    m_SID = 2093
    m_DataSID = 2081
    m_Name = '近战怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 20000 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
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
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 3600 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
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


class CMonsterData2099(baseconfig.CMonsterData):
    m_SID = 2099
    m_DataSID = 1019
    m_Name = '【护盾木桩】左弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 10000000,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 1000000,
            'RShield': 20,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 125,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 1800 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 450,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 1,
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
            4101: (10000, 1),
            1001: (10000, 1) },
        2: {
            4101: (10000, 1),
            1001: (10000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData3008(baseconfig.CMonsterData):
    m_SID = 3008
    m_DataSID = 2201
    m_Name = '喷火怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 8000 * (Func10(*a) - 1) + 10000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 8000 * (Func10(*a) - 1) + 10000),
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 500 * (Func10(*a) - 1) + 1000),
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


class CMonsterData3009(baseconfig.CMonsterData):
    m_SID = 3009
    m_DataSID = 2021
    m_Name = '四足怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 16000 * (Func10(*a) - 1) + 20000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 750 * (Func10(*a) - 1) + 1500),
            'MoveSpeed': 600,
            'AttSpeed': 50,
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


class CMonsterData3010(baseconfig.CMonsterData):
    m_SID = 3010
    m_DataSID = 2001
    m_Name = '一刀怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 200 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 0,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 3600 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 600,
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
            404: (10000, 1) },
        2: {
            404: (10000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData10221(baseconfig.CMonsterData):
    m_SID = 10221
    m_DataSID = 1022
    m_Name = '纯血木桩'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = {
        'HPMax': (lambda *a: 119880 * (Func10(*a) - 1) + 129600),
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
        'SpecialMHPWeight': 0 }
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
    m_SpecialMHP = 1000000


class CMonsterData20011(baseconfig.CMonsterData):
    m_SID = 20011
    m_DataSID = 2001
    m_Name = '一刀怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 3920 * (Func10(*a) - 1) + 9520),
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
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1200),
            'MoveSpeed': 700,
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


class CMonsterData20021(baseconfig.CMonsterData):
    m_SID = 20021
    m_DataSID = 2002
    m_Name = '【第二幕】一刀怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 3920 * (Func10(*a) - 1) + 9520),
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
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1200),
            'MoveSpeed': 700,
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


class CMonsterData20031(baseconfig.CMonsterData):
    m_SID = 20031
    m_DataSID = 2003
    m_Name = '【第三幕】一刀怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 3920 * (Func10(*a) - 1) + 9520),
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
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1200),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
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
    m_SpecialMHP = 0


class CMonsterData20041(baseconfig.CMonsterData):
    m_SID = 20041
    m_DataSID = 2004
    m_Name = '【第三幕】召唤一刀怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 3920 * (Func10(*a) - 1) + 9520),
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
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1200),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
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
    m_SpecialMHP = 0


class CMonsterData20221(baseconfig.CMonsterData):
    m_SID = 20221
    m_DataSID = 2022
    m_Name = '【第二幕】精英召唤四足怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 16000 * (Func10(*a) - 1) + 20000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 750 * (Func10(*a) - 1) + 1500),
            'MoveSpeed': 600,
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


class CMonsterData20431(baseconfig.CMonsterData):
    m_SID = 20431
    m_DataSID = 2043
    m_Name = '大漠飞虫'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 70,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1200),
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
            'IntervalTime': 75,
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


class CMonsterData20611(baseconfig.CMonsterData):
    m_SID = 20611
    m_DataSID = 2061
    m_Name = '投雷怪-普通投雷'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
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
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 80 * (Func10(*a) - 1) + 1700),
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
            'IntervalTime': 50,
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


class CMonsterData20621(baseconfig.CMonsterData):
    m_SID = 20621
    m_DataSID = 2062
    m_Name = '投雷怪-火系投雷'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
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
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 80 * (Func10(*a) - 1) + 1700),
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
            'IntervalTime': 50,
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


class CMonsterData20631(baseconfig.CMonsterData):
    m_SID = 20631
    m_DataSID = 2063
    m_Name = '投雷怪-电系投雷'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
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
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 80 * (Func10(*a) - 1) + 1700),
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
            'IntervalTime': 50,
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


class CMonsterData20641(baseconfig.CMonsterData):
    m_SID = 20641
    m_DataSID = 2064
    m_Name = '投雷怪-毒系投雷'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
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
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 80 * (Func10(*a) - 1) + 1700),
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
            'IntervalTime': 50,
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


class CMonsterData20651(baseconfig.CMonsterData):
    m_SID = 20651
    m_DataSID = 2065
    m_Name = '第四幕投雷怪'
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData20821(baseconfig.CMonsterData):
    m_SID = 20821
    m_DataSID = 2082
    m_Name = '小型近战-电击近战怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 20000 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 0,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 3600 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
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


class CMonsterData20861(baseconfig.CMonsterData):
    m_SID = 20861
    m_DataSID = 2086
    m_Name = '#NT#流寇驱虫者'
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData20871(baseconfig.CMonsterData):
    m_SID = 20871
    m_DataSID = 2087
    m_Name = '第三幕小型近战'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 20000 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 0,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 0,
            'ThumpFrame': 28,
            'Att': (lambda *a: 3600 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
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
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData20881(baseconfig.CMonsterData):
    m_SID = 20881
    m_DataSID = 2088
    m_Name = '【石化怪物】持矛近战'
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 2000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData20891(baseconfig.CMonsterData):
    m_SID = 20891
    m_DataSID = 2089
    m_Name = '四幕小近战'
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
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
    m_Name = '小型远程-基础远程怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
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
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1200),
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
            'IntervalTime': 75,
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


class CMonsterData21051(baseconfig.CMonsterData):
    m_SID = 21051
    m_DataSID = 2105
    m_Name = '【第三幕】小型远程-基础远程怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9720 * (Func10(*a) - 1) + 16200),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 32400 * (Func10(*a) - 1) + 54000),
            'RShield': 0,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 33,
            'DefThump': 0,
            'ThumpFrame': 33,
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1080),
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
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21061(baseconfig.CMonsterData):
    m_SID = 21061
    m_DataSID = 2106
    m_Name = '【第三幕】小型远程-远程小盾'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9720 * (Func10(*a) - 1) + 16200),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 32400 * (Func10(*a) - 1) + 54000),
            'RShield': 0,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 33,
            'DefThump': 0,
            'ThumpFrame': 33,
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1080),
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
            'IntervalTime': 25,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21081(baseconfig.CMonsterData):
    m_SID = 21081
    m_DataSID = 2108
    m_Name = '四幕火系远程'
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
            'AccuracyProb': 30,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 6667
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21082(baseconfig.CMonsterData):
    m_SID = 21082
    m_DataSID = 2108
    m_Name = '四幕火系远程'
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
            'AccuracyProb': 30,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': 20,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 6667
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21091(baseconfig.CMonsterData):
    m_SID = 21091
    m_DataSID = 2109
    m_Name = '四幕电系远程'
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
            'AccuracyProb': 30,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 6667
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21101(baseconfig.CMonsterData):
    m_SID = 21101
    m_DataSID = 2110
    m_Name = '四幕毒系远程'
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
            'AccuracyProb': 30,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 6667
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21111(baseconfig.CMonsterData):
    m_SID = 21111
    m_DataSID = 2111
    m_Name = '四幕boss火系远程'
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
            'AccuracyProb': 30,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 6667
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21121(baseconfig.CMonsterData):
    m_SID = 21121
    m_DataSID = 2112
    m_Name = '【第三幕】小型远程-毒系远程小盾'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9720 * (Func10(*a) - 1) + 16200),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 32400 * (Func10(*a) - 1) + 54000),
            'RShield': 0,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 33,
            'DefThump': 0,
            'ThumpFrame': 33,
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1080),
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
            'IntervalTime': 25,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21211(baseconfig.CMonsterData):
    m_SID = 21211
    m_DataSID = 2121
    m_Name = '中型基础近战怪测试'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 100000,
            'RHP': 0,
            'ArmorMax': 100000,
            'ShieldMax': 0,
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 0,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 1000 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
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


class CMonsterData21221(baseconfig.CMonsterData):
    m_SID = 21221
    m_DataSID = 2122
    m_Name = '重甲突击怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 70560 * (Func10(*a) - 1) + 171960),
            'RHP': 0,
            'ArmorMax': (lambda *a: 70560 * (Func10(*a) - 1) + 171960),
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 17,
            'DefThump': 10000,
            'ThumpFrame': 17,
            'Att': (lambda *a: 160 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 170,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 5,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 4700
    m_SprintSpeedUpMul = 13500
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
    m_Name = '中型近战-中型盾兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 61900 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
            'RShield': 10,
            'ShieldRecoverTime': 300,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 92,
            'DefThump': 5000,
            'ThumpFrame': 92,
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1200),
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
            'IntervalTime': 150,
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


class CMonsterData21241(baseconfig.CMonsterData):
    m_SID = 21241
    m_DataSID = 2124
    m_Name = '中型近战-霰弹枪兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 10000,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 32340 * (Func10(*a) - 1) + 78760),
            'RShield': 10,
            'ShieldRecoverTime': 300,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 33,
            'DefThump': 0,
            'ThumpFrame': 33,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1670),
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


class CMonsterData21261(baseconfig.CMonsterData):
    m_SID = 21261
    m_DataSID = 2126
    m_Name = '【第三幕】中型近战'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 10000,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 32340 * (Func10(*a) - 1) + 78760),
            'RShield': 10,
            'ShieldRecoverTime': 300,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 35,
            'DefThump': 0,
            'ThumpFrame': 35,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1670),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21271(baseconfig.CMonsterData):
    m_SID = 21271
    m_DataSID = 2127
    m_Name = '【石化怪物】马头盾兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 61900 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
            'RShield': 10,
            'ShieldRecoverTime': 300,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 92,
            'DefThump': 5000,
            'ThumpFrame': 92,
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1200),
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
            'IntervalTime': 150,
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


class CMonsterData21281(baseconfig.CMonsterData):
    m_SID = 21281
    m_DataSID = 2128
    m_Name = '弱点怪'
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21311(baseconfig.CMonsterData):
    m_SID = 21311
    m_DataSID = 2131
    m_Name = '蚂蚁盾兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 61900 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
            'RShield': 10,
            'ShieldRecoverTime': 300,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 70,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 92,
            'DefThump': 5000,
            'ThumpFrame': 92,
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1200),
            'MoveSpeed': 350,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 7,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 150,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 16667
    m_SprintSpeedUpMul = 30000
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
    m_Name = '中型基础远程怪测试'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 20000 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 0,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 3600 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 500,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 100,
            'IntervalTime': 75,
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


class CMonsterData21421(baseconfig.CMonsterData):
    m_SID = 21421
    m_DataSID = 2142
    m_Name = '【第二幕】中型远程-隐身远程怪'
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21431(baseconfig.CMonsterData):
    m_SID = 21431
    m_DataSID = 2143
    m_Name = '【第三幕】中型远程'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 20000 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 20000 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'RShield': 10,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 0,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 3600 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 250,
            'AttSpeed': 12,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21451(baseconfig.CMonsterData):
    m_SID = 21451
    m_DataSID = 2145
    m_Name = '【第三幕】火系中型远程'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 20000 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 20000 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'RShield': 10,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 0,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 3600 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 250,
            'AttSpeed': 12,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 10000
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
    m_Name = '狙击怪-追踪狙击怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1200),
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
            'IntervalTime': 75,
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


class CMonsterData21621(baseconfig.CMonsterData):
    m_SID = 21621
    m_DataSID = 2162
    m_Name = '狙击怪-破盾狙击怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 10000,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 23520 * (Func10(*a) - 1) + 57280),
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 160 * (Func10(*a) - 1) + 2500),
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
            'IntervalTime': 75,
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


class CMonsterData21631(baseconfig.CMonsterData):
    m_SID = 21631
    m_DataSID = 2163
    m_Name = '狙击怪-闪烁追踪怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 100 * (Func10(*a) - 1) + 1200),
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
            'IntervalTime': 75,
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


class CMonsterData21641(baseconfig.CMonsterData):
    m_SID = 21641
    m_DataSID = 2164
    m_Name = '四幕狙击怪'
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
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 0,
            'ThumpFrame': 28,
            'Att': (lambda *a: 180 * (Func10(*a) - 1) + 2100),
            'MoveSpeed': 120,
            'AttSpeed': 100,
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
    m_Reward = { }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21651(baseconfig.CMonsterData):
    m_SID = 21651
    m_DataSID = 2165
    m_Name = '四幕电狙击怪'
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
            'AccuracyProb': 100,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 0,
            'ThumpFrame': 28,
            'Att': (lambda *a: 180 * (Func10(*a) - 1) + 2100),
            'MoveSpeed': 120,
            'AttSpeed': 100,
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
    m_Reward = { }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21811(baseconfig.CMonsterData):
    m_SID = 21811
    m_DataSID = 2181
    m_Name = '【第三幕】重型锁链怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 88800 * (Func10(*a) - 1) + 216000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
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
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1660),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
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
    m_SpecialMHP = 0


class CMonsterData21821(baseconfig.CMonsterData):
    m_SID = 21821
    m_DataSID = 2182
    m_Name = '大胖坦克兵'
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
            'AccuracyProb': 95,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 37,
            'DefThump': 10000,
            'ThumpFrame': 37,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1880),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -2500
    m_SprintSpeedUpMul = 32353
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22011(baseconfig.CMonsterData):
    m_SID = 22011
    m_DataSID = 2201
    m_Name = '重型远程-喷火怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 47040 * (Func10(*a) - 1) + 114640),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 80 * (Func10(*a) - 1) + 1250),
            'MoveSpeed': 250,
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


class CMonsterData22021(baseconfig.CMonsterData):
    m_SID = 22021
    m_DataSID = 2202
    m_Name = '【第三幕】重型远程机枪兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 47040 * (Func10(*a) - 1) + 114640),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 50,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 80 * (Func10(*a) - 1) + 1250),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22031(baseconfig.CMonsterData):
    m_SID = 22031
    m_DataSID = 2203
    m_Name = '【第三幕】重型远程火炮兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 47040 * (Func10(*a) - 1) + 114640),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 80 * (Func10(*a) - 1) + 1250),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22051(baseconfig.CMonsterData):
    m_SID = 22051
    m_DataSID = 2205
    m_Name = '#NT#流寇电击者'
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 15000
    m_SprintSpeedUpMul = 23333
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
    m_Name = '自爆怪-火系自爆'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
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
            'KnockBackFrame': 17,
            'DefThump': 10000,
            'ThumpFrame': 17,
            'Att': (lambda *a: 240 * (Func10(*a) - 1) + 2500),
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


class CMonsterData22231(baseconfig.CMonsterData):
    m_SID = 22231
    m_DataSID = 2223
    m_Name = '自爆怪-电系自爆'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
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
            'KnockBackFrame': 17,
            'DefThump': 10000,
            'ThumpFrame': 17,
            'Att': (lambda *a: 240 * (Func10(*a) - 1) + 2500),
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


class CMonsterData22241(baseconfig.CMonsterData):
    m_SID = 22241
    m_DataSID = 2224
    m_Name = '自爆怪-毒系自爆'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
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
            'KnockBackFrame': 17,
            'DefThump': 10000,
            'ThumpFrame': 17,
            'Att': (lambda *a: 240 * (Func10(*a) - 1) + 2500),
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


class CMonsterData22251(baseconfig.CMonsterData):
    m_SID = 22251
    m_DataSID = 2225
    m_Name = '魔化 飞行自爆'
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
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 190000
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
    m_Name = '投射怪-投射法球怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1700),
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
            'IntervalTime': 50,
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


class CMonsterData22421(baseconfig.CMonsterData):
    m_SID = 22421
    m_DataSID = 2242
    m_Name = '大漠沙蜥-火'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 23100 * (Func10(*a) - 1) + 49500),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1660),
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
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22431(baseconfig.CMonsterData):
    m_SID = 22431
    m_DataSID = 2243
    m_Name = '大漠沙蜥-电'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 23100 * (Func10(*a) - 1) + 49500),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1660),
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
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22441(baseconfig.CMonsterData):
    m_SID = 22441
    m_DataSID = 2244
    m_Name = '大漠沙蜥-毒'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 23100 * (Func10(*a) - 1) + 49500),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1660),
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
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22451(baseconfig.CMonsterData):
    m_SID = 22451
    m_DataSID = 2245
    m_Name = '【石化怪物】投戟兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1700),
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
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22811(baseconfig.CMonsterData):
    m_SID = 22811
    m_DataSID = 2281
    m_Name = '定点法师怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 25200 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 0,
            'DefKnockBack': 0,
            'KnockBackFrame': 30,
            'DefThump': 0,
            'ThumpFrame': 30,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1660),
            'MoveSpeed': 150,
            'AttSpeed': 150,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22821(baseconfig.CMonsterData):
    m_SID = 22821
    m_DataSID = 2282
    m_Name = '召唤法师怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 14700 * (Func10(*a) - 1) + 35800),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 160 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 150,
            'AttSpeed': 50,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22831(baseconfig.CMonsterData):
    m_SID = 22831
    m_DataSID = 2283
    m_Name = '吸血法师怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 15526 * (Func10(*a) - 1) + 45000),
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
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 165 * (Func10(*a) - 1) + 1444),
            'MoveSpeed': 150,
            'AttSpeed': 50,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData23011(baseconfig.CMonsterData):
    m_SID = 23011
    m_DataSID = 2301
    m_Name = '伞妖'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 70,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1200),
            'MoveSpeed': 150,
            'AttSpeed': 12,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData23211(baseconfig.CMonsterData):
    m_SID = 23211
    m_DataSID = 2321
    m_Name = '招潮蟹'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 15500 * (Func10(*a) - 1) + 13500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 70,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1200),
            'MoveSpeed': 150,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 16667
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData23411(baseconfig.CMonsterData):
    m_SID = 23411
    m_DataSID = 2341
    m_Name = '宝箱怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 5850000,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 500000,
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
            'MoveSpeed': 800,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            101: (0, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * 0 + 0), 1),
            1001: (0, 1),
            2001: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData23511(baseconfig.CMonsterData):
    m_SID = 23511
    m_DataSID = 2401
    m_Name = '巨型召唤怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 999000 * (Func10(*a) - 1) + 1080000),
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
            'MoveSpeed': 250,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData23611(baseconfig.CMonsterData):
    m_SID = 23611
    m_DataSID = 2361
    m_Name = '炮灰怪'
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData23612(baseconfig.CMonsterData):
    m_SID = 23612
    m_DataSID = 2361
    m_Name = '炮灰怪'
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData23811(baseconfig.CMonsterData):
    m_SID = 23811
    m_DataSID = 2381
    m_Name = '骑乘怪'
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 23812
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData24011(baseconfig.CMonsterData):
    m_SID = 24011
    m_DataSID = 2401
    m_Name = '巨型召唤怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 999000 * (Func10(*a) - 1) + 1080000),
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
            'AttSpeed': 30,
            'Toughness': 50,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData24211(baseconfig.CMonsterData):
    m_SID = 24211
    m_DataSID = 2421
    m_Name = '大漠蜘蛛'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 3920 * (Func10(*a) - 1) + 9520),
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
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1200),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
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
    m_SpecialMHP = 0


class CMonsterData24221(baseconfig.CMonsterData):
    m_SID = 24221
    m_DataSID = 2422
    m_Name = '蜘蛛卫士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 70560 * (Func10(*a) - 1) + 171960),
            'RHP': 0,
            'ArmorMax': (lambda *a: 70560 * (Func10(*a) - 1) + 171960),
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 10000,
            'KnockBackFrame': 17,
            'DefThump': 10000,
            'ThumpFrame': 17,
            'Att': (lambda *a: 160 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 170,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 4700
    m_SprintSpeedUpMul = 13500
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData24231(baseconfig.CMonsterData):
    m_SID = 24231
    m_DataSID = 2423
    m_Name = '精英蜘蛛召唤一刀怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 3920 * (Func10(*a) - 1) + 9520),
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
            'Att': (lambda *a: 60 * (Func10(*a) - 1) + 1200),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
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
    m_SpecialMHP = 0


class CMonsterData30211(baseconfig.CMonsterData):
    m_SID = 30211
    m_DataSID = 3021
    m_Name = '精英四足怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 17640 * (Func10(*a) - 1) + 42960),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 80 * (Func10(*a) - 1) + 1250),
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


class CMonsterData30871(baseconfig.CMonsterData):
    m_SID = 30871
    m_DataSID = 3087
    m_Name = '精英小近战'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 17640 * (Func10(*a) - 1) + 42960),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 28,
            'DefThump': 0,
            'ThumpFrame': 28,
            'Att': (lambda *a: 80 * (Func10(*a) - 1) + 1250),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData31011(baseconfig.CMonsterData):
    m_SID = 31011
    m_DataSID = 2101
    m_Name = '精英远程怪（测试）'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 155200 * (Func10(*a) - 1) + 270000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 10000 * (Func10(*a) - 1) + 30000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 0,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 12,
            'Att': (lambda *a: 80 * (Func10(*a) - 1) + 1250),
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


class CMonsterData31251(baseconfig.CMonsterData):
    m_SID = 31251
    m_DataSID = 3125
    m_Name = '【第二幕】精英中型盾兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 155200 * (Func10(*a) - 1) + 270000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 10000 * (Func10(*a) - 1) + 30000),
            'RShield': 10,
            'ShieldRecoverTime': 500,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 80,
            'StruckIgnoreFrame': 0,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 12,
            'Att': (lambda *a: 80 * (Func10(*a) - 1) + 1250),
            'MoveSpeed': 150,
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
    m_Reward = { }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData31421(baseconfig.CMonsterData):
    m_SID = 31421
    m_DataSID = 3142
    m_Name = '【第二幕】精英中型远程-隐身远程怪'
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
            'IntervalTime': 0,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData32421(baseconfig.CMonsterData):
    m_SID = 32421
    m_DataSID = 3242
    m_Name = '投射法球怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 14700 * (Func10(*a) - 1) + 35800),
            'RHP': 0,
            'ArmorMax': (lambda *a: 14700 * (Func10(*a) - 1) + 35800),
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 160 * (Func10(*a) - 1) + 2500),
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


class CMonsterData34211(baseconfig.CMonsterData):
    m_SID = 34211
    m_DataSID = 3421
    m_Name = '精英蜘蛛卫士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 17640 * (Func10(*a) - 1) + 42960),
            'RHP': 0,
            'ArmorMax': (lambda *a: 10000 * (Func10(*a) - 1) + 30000),
            'ShieldMax': 0,
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 80 * (Func10(*a) - 1) + 1250),
            'MoveSpeed': 170,
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
    m_RunSpeedUpMul = 4700
    m_SprintSpeedUpMul = 13500
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


class CMonsterData39051(baseconfig.CMonsterData):
    m_SID = 39051
    m_DataSID = 3905
    m_Name = '第三幕BOSS船测试'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 800000,
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
            'StruckIgnoreFrame': 0,
            'DefKnockBack': 100000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 0,
            'Att': (lambda *a: 1000 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
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


class CMonsterData39052(baseconfig.CMonsterData):
    m_SID = 39052
    m_DataSID = 3906
    m_Name = '第三幕BOSS船的小炮'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 50000,
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
            'StruckIgnoreFrame': 0,
            'DefKnockBack': 100000,
            'KnockBackFrame': 0,
            'DefThump': 100000,
            'ThumpFrame': 0,
            'Att': (lambda *a: 1000 * 1.3 ** (Func10(*a) - 1) * 1 + 0),
            'MoveSpeed': 500,
            'AttSpeed': 50,
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

