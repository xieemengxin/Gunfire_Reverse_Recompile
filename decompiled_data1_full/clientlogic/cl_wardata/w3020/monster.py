# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3020/monster.pyc
# RelativePath: clientlogic/cl_wardata/w3020/monster.pyc
# Source Generated with Decompyle++
# File: monster.pyc (Python 3.6)

from cl_resmgr.resdata import CMonsterData as CCustom
import cl_resmgr.resdata as baseconfig
from cl_newformula import Func10, Func204, Func205

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


class CMonsterData20021(baseconfig.CMonsterData):
    m_SID = 20021
    m_DataSID = 2002
    m_Name = '大漠幼豚'
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
            'Att': (lambda *a: 1 * (Func10(*a) - 1) + 550),
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
            201: (1500, 1),
            401: (0, 1),
            104: (10000, 1),
            3120: (10000, 3),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 110000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.08
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 1 * (Func10(*a) - 1) + 550),
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
    m_Reward = {
        1: {
            201: (1500, 1),
            401: (0, 1),
            104: (10000, 1),
            3020: (10000, 1),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData20041(baseconfig.CMonsterData):
    m_SID = 20041
    m_DataSID = 2005
    m_Name = '自爆灯笼鬼'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 600 * (Func10(*a) - 1) + 1800),
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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 2750),
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
    m_Reward = {
        1: {
            201: (1500, 1),
            401: (0, 1),
            104: (0, 1),
            3020: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 1490),
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
    m_Reward = {
        1: {
            201: (4500, 1),
            401: ((lambda *a: 300 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 3),
            3120: (10000, 3),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 3) } }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.08
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 3 * (Func10(*a) - 1) + 2050),
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
            201: (4500, 1),
            401: (0, 1),
            104: (0, 6),
            3020: (0, 1),
            3021: (0, 1),
            103: (0, 6) } }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.08
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData20411(baseconfig.CMonsterData):
    m_SID = 20411
    m_DataSID = 2041
    m_Name = '大漠沙虫'
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
            'AccuracyProb': 10,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 29,
            'DefThump': 100000,
            'ThumpFrame': 29,
            'Att': (lambda *a: 1 * (Func10(*a) - 1) + 550),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: 300 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 8),
            3120: (10000, 5),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 8) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.08
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData20851(baseconfig.CMonsterData):
    m_SID = 20851
    m_DataSID = 2085
    m_Name = '流寇电刀手'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 31500 * (Func10(*a) - 1) + 67500),
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
            'Att': (lambda *a: 3 * (Func10(*a) - 1) + 2060),
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
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: 300 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 8),
            3120: (10000, 3),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 8),
            3121: (10000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.08
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 2060),
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
    m_Reward = {
        1: {
            201: (4500, 1),
            401: ((lambda *a: 300 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 5),
            3020: (10000, 1),
            3021: (10000, 1),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 5) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21031(baseconfig.CMonsterData):
    m_SID = 21031
    m_DataSID = 2103
    m_Name = '马贼枪手'
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
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 0,
            'KnockBackFrame': 27,
            'DefThump': 0,
            'ThumpFrame': 27,
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 1490),
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
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: 300 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 8),
            3120: (10000, 5),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 8) } }
    m_RunSpeedUpMul = 6667
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.08
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 1 * (Func10(*a) - 1) + 1490),
            'MoveSpeed': 150,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 90,
            'IntervalTime': 75,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4500, 1),
            401: ((lambda *a: 300 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 5),
            3020: (10000, 4),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 5) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 2060),
            'MoveSpeed': 150,
            'AttSpeed': 50,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': 90,
            'IntervalTime': 25,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4500, 1),
            401: ((lambda *a: 300 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 5),
            3021: (10000, 1),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 5) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21221(baseconfig.CMonsterData):
    m_SID = 21221
    m_DataSID = 2122
    m_Name = '黑面流寇'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 61920 * (Func10(*a) - 1) + 129600),
            'RHP': 0,
            'ArmorMax': (lambda *a: 206400 * (Func10(*a) - 1) + 432000),
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
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: ((lambda *a: 1200 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 8),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 8),
            3122: (10000, 4) } }
    m_RunSpeedUpMul = 7650
    m_SprintSpeedUpMul = 32353
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.08
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21241(baseconfig.CMonsterData):
    m_SID = 21241
    m_DataSID = 2124
    m_Name = '流寇恶徒'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 24960 * (Func10(*a) - 1) + 46800),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 83200 * (Func10(*a) - 1) + 156000),
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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 1442),
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
    m_Reward = {
        1: {
            201: (7500, 1),
            401: ((lambda *a: 800 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 8),
            3122: (10000, 2),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 8) } }
    m_RunSpeedUpMul = -5000
    m_SprintSpeedUpMul = 4000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.08
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21251(baseconfig.CMonsterData):
    m_SID = 21251
    m_DataSID = 2125
    m_Name = '流寇帮凶'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 83200 * (Func10(*a) - 1) + 156000),
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
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2060),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (7500, 1),
            401: ((lambda *a: 800 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 8),
            3122: (10000, 2),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 8) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 3333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.08
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 2060),
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
    m_Reward = {
        1: {
            201: (4500, 1),
            401: ((lambda *a: 500 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 5),
            3020: (10000, 3),
            3021: (10000, 1),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 5) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21421(baseconfig.CMonsterData):
    m_SID = 21421
    m_DataSID = 2142
    m_Name = '马贼隐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 23040 * (Func10(*a) - 1) + 43200),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 76800 * (Func10(*a) - 1) + 144000),
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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 1490),
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
    m_Reward = {
        1: {
            201: (7500, 1),
            401: ((lambda *a: 800 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 8),
            3121: (10000, 3),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 8) } }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.08
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 1 * (Func10(*a) - 1) + 1490),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4500, 1),
            401: ((lambda *a: 500 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 5),
            3020: (10000, 1),
            3021: (10000, 1),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 5) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21621(baseconfig.CMonsterData):
    m_SID = 21621
    m_DataSID = 2162
    m_Name = '马贼军师'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 16380 * (Func10(*a) - 1) + 35100),
            'RHP': 0,
            'ArmorMax': (lambda *a: 54600 * (Func10(*a) - 1) + 117000),
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
            'Att': (lambda *a: 6 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (7500, 1),
            401: ((lambda *a: 800 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 8),
            3121: (10000, 3),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 8) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.08
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21631(baseconfig.CMonsterData):
    m_SID = 21631
    m_DataSID = 2163
    m_Name = '马贼门客'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 16380 * (Func10(*a) - 1) + 35100),
            'RHP': 0,
            'ArmorMax': (lambda *a: 54600 * (Func10(*a) - 1) + 117000),
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
            'Att': (lambda *a: 5 * (Func10(*a) - 1) + 2310),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (7500, 1),
            401: ((lambda *a: 800 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 8),
            3121: (10000, 3),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 8) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.08
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 2060),
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
    m_Reward = {
        1: {
            201: (9000, 1),
            401: ((lambda *a: 800 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 5),
            3020: (0, 2),
            3022: (10000, 1),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 5) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22011(baseconfig.CMonsterData):
    m_SID = 22011
    m_DataSID = 2201
    m_Name = '流寇纵火者'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 77400 * (Func10(*a) - 1) + 162000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 258000 * (Func10(*a) - 1) + 540000),
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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 1490),
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
    m_Reward = {
        1: {
            201: (10000, 2),
            401: ((lambda *a: 1200 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 8),
            3122: (10000, 3),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 8) } }
    m_RunSpeedUpMul = 15000
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.08
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 1 * (Func10(*a) - 1) + 1490),
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
    m_Reward = {
        1: {
            201: (9000, 1),
            401: ((lambda *a: 800 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 5),
            3020: (0, 1),
            3021: (10000, 1),
            3022: (10000, 1),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 5) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 2060),
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
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: 800 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 5),
            3020: (0, 2),
            3022: (10000, 1),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 5) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22421(baseconfig.CMonsterData):
    m_SID = 22421
    m_DataSID = 2242
    m_Name = '烈焰沙蜥'
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
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2060),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: 300 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 8),
            3121: (10000, 1),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 8),
            3120: (10000, 2) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.08
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22431(baseconfig.CMonsterData):
    m_SID = 22431
    m_DataSID = 2243
    m_Name = '雷霆沙蜥'
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
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2060),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: 300 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 8),
            3121: (10000, 1),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 8),
            3120: (10000, 2) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.08
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22441(baseconfig.CMonsterData):
    m_SID = 22441
    m_DataSID = 2244
    m_Name = '剧毒沙蜥'
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
            'DefKnockBack': 0,
            'KnockBackFrame': 26,
            'DefThump': 0,
            'ThumpFrame': 26,
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2060),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: 300 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 8),
            3121: (10000, 1),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 8),
            3120: (10000, 2) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.08
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 1 * (Func10(*a) - 1) + 1490),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4500, 1),
            401: ((lambda *a: 300 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 5),
            3020: (10000, 4),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 5) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 2060),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4500, 1),
            401: ((lambda *a: 300 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 5),
            3021: (10000, 1),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 5) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4500, 1),
            401: ((lambda *a: 300 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 5),
            3021: (10000, 1),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 5) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 2060),
            'MoveSpeed': 300,
            'AttSpeed': 12,
            'Toughness': 0,
            'TurnSpeed': 28,
            'TurnThresholdAngle': 0,
            'TurnInterval': 0,
            'AdsorbDis': 0,
            'HardEff': 10000,
            'SaveTime': 0,
            'DodgeProb': (lambda *a: Func205(*a) * 30 + 0),
            'IntervalTime': 50,
            'EnergyMax': 0,
            'REnergy': 0,
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (4500, 1),
            401: ((lambda *a: 300 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 5),
            3020: (10000, 1),
            3021: (10000, 1),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 5) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 6667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
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
            'Att': (lambda *a: 1 * (Func10(*a) - 1) + 550),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1500, 1),
            401: (0, 1),
            104: (10000, 1),
            3020: (10000, 1),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 1) } }
    m_RunSpeedUpMul = 16667
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData23422(baseconfig.CMonsterData):
    m_SID = 23422
    m_DataSID = 2348
    m_Name = '钱龙'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 675000 * (Func10(*a) - 1) + 675000),
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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 2060),
            'MoveSpeed': 350,
            'AttSpeed': 50,
            'Toughness': 50,
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
    m_RunSpeedUpMul = 6667
    m_SprintSpeedUpMul = 12000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 10
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData23423(baseconfig.CMonsterData):
    m_SID = 23423
    m_DataSID = 2351
    m_Name = '钱龙'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 160000 * (Func10(*a) - 1) + 240000),
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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 2060),
            'MoveSpeed': 300,
            'AttSpeed': 50,
            'Toughness': 50,
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
    m_RunSpeedUpMul = 6667
    m_SprintSpeedUpMul = 12000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData23432(baseconfig.CMonsterData):
    m_SID = 23432
    m_DataSID = 2349
    m_Name = '钱龙'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 820000 * (Func10(*a) - 1) + 750000),
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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 2060),
            'MoveSpeed': 500,
            'AttSpeed': 50,
            'Toughness': 50,
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
    m_RunSpeedUpMul = 6667
    m_SprintSpeedUpMul = 12000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 10
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData23433(baseconfig.CMonsterData):
    m_SID = 23433
    m_DataSID = 2352
    m_Name = '钱龙'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 200000 * (Func10(*a) - 1) + 250000),
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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 2060),
            'MoveSpeed': 450,
            'AttSpeed': 50,
            'Toughness': 50,
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
    m_RunSpeedUpMul = 6667
    m_SprintSpeedUpMul = 12000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData24021(baseconfig.CMonsterData):
    m_SID = 24021
    m_DataSID = 2402
    m_Name = '黄金·巡海夜叉'
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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 2060),
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
    m_Reward = {
        1: {
            201: (4500, 1),
            401: ((lambda *a: 500 * (1 - (Func204(*a) - 1) * 0.1)), 1),
            104: (10000, 5),
            3020: (10000, 3),
            3021: (10000, 1),
            103: ((lambda *a: 10000 - (Func204(*a) - 1) * 3000), 5) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData30041(baseconfig.CMonsterData):
    m_SID = 30041
    m_DataSID = 3005
    m_Name = '炎爆灯笼鬼'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 3150 * (Func10(*a) - 1) + 6750),
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
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2750),
            'MoveSpeed': 250,
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
            201: (1500, 1),
            401: (0, 1),
            104: (0, 1),
            3020: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 12000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData30042(baseconfig.CMonsterData):
    m_SID = 30042
    m_DataSID = 3005
    m_Name = '炎爆灯笼鬼'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 3150 * (Func10(*a) - 1) + 6750),
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
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2750),
            'MoveSpeed': 250,
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
            201: (1500, 1),
            401: (0, 1),
            104: (0, 1),
            3020: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 12000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData30211(baseconfig.CMonsterData):
    m_SID = 30211
    m_DataSID = 3021
    m_Name = '精英土狼'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 599400 * (Func10(*a) - 1) + 648000),
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
            'Att': (lambda *a: 6 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 113),
            3022: (10000, 4) } }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData30212(baseconfig.CMonsterData):
    m_SID = 30212
    m_DataSID = 3021
    m_Name = '精英土狼'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 599400 * (Func10(*a) - 1) + 648000),
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
            'Att': (lambda *a: 6 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 600),
            3023: (10000, 20) } }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
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
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2750),
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
            104: (10000, 75),
            3022: (10000, 4) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2750),
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
            104: (10000, 600),
            3023: (10000, 14) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 75),
            3022: (10000, 4) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 600),
            3023: (10000, 14) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData31251(baseconfig.CMonsterData):
    m_SID = 31251
    m_DataSID = 3125
    m_Name = '精英流寇帮凶'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 749250 * (Func10(*a) - 1) + 810000),
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
            'Att': (lambda *a: 6 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 113),
            3022: (10000, 4) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 14000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData31252(baseconfig.CMonsterData):
    m_SID = 31252
    m_DataSID = 3125
    m_Name = '精英流寇帮凶'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 749250 * (Func10(*a) - 1) + 810000),
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
            'Att': (lambda *a: 6 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 600),
            3023: (10000, 20) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 14000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 3 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 75),
            3022: (10000, 4) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 3 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 600),
            3023: (10000, 14) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData31421(baseconfig.CMonsterData):
    m_SID = 31421
    m_DataSID = 3142
    m_Name = '精英马贼隐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 164835 * (Func10(*a) - 1) + 178200),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 549450 * (Func10(*a) - 1) + 594000),
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
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2050),
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
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 113),
            3022: (10000, 4) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData31422(baseconfig.CMonsterData):
    m_SID = 31422
    m_DataSID = 3142
    m_Name = '精英马贼隐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 164835 * (Func10(*a) - 1) + 178200),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 549450 * (Func10(*a) - 1) + 594000),
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
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2050),
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
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 600),
            3023: (10000, 20) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData32011(baseconfig.CMonsterData):
    m_SID = 32011
    m_DataSID = 3201
    m_Name = '精英流寇纵毒者'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 179820 * (Func10(*a) - 1) + 194400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 599400 * (Func10(*a) - 1) + 648000),
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
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2050),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 113),
            3022: (10000, 4) } }
    m_RunSpeedUpMul = 15000
    m_SprintSpeedUpMul = 35138
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData32012(baseconfig.CMonsterData):
    m_SID = 32012
    m_DataSID = 3201
    m_Name = '精英流寇纵毒者'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 179820 * (Func10(*a) - 1) + 194400),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 599400 * (Func10(*a) - 1) + 648000),
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
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2050),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 600),
            3023: (10000, 20) } }
    m_RunSpeedUpMul = 15000
    m_SprintSpeedUpMul = 35138
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData32013(baseconfig.CMonsterData):
    m_SID = 32013
    m_DataSID = 3201
    m_Name = '精英流寇纵毒者（高血量版）'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 17982000 * (Func10(*a) - 1) + 19440000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 59940000 * (Func10(*a) - 1) + 64800000),
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
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2050),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 600),
            3023: (10000, 15) } }
    m_RunSpeedUpMul = 18000
    m_SprintSpeedUpMul = 38138
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 2050),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 75),
            3022: (10000, 4) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 2050),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 600),
            3023: (10000, 14) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData32421(baseconfig.CMonsterData):
    m_SID = 32421
    m_DataSID = 3242
    m_Name = '精英沙蜥'
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
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 26,
            'DefThump': 10000,
            'ThumpFrame': 26,
            'Att': (lambda *a: 6 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 113),
            3022: (10000, 4) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData32422(baseconfig.CMonsterData):
    m_SID = 32422
    m_DataSID = 3242
    m_Name = '精英沙蜥'
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
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 225,
            'DefKnockBack': 10000,
            'KnockBackFrame': 26,
            'DefThump': 10000,
            'ThumpFrame': 26,
            'Att': (lambda *a: 6 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 600),
            3023: (10000, 20) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 2050),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 75),
            3022: (10000, 4) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 2 * (Func10(*a) - 1) + 2050),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 600),
            3023: (10000, 14) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 3 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 75),
            3022: (10000, 4) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 3 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: (0, 1),
            101: (0, 1),
            3021: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 3 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 600),
            3023: (10000, 14) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'Att': (lambda *a: 3 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: (0, 1),
            101: (0, 1),
            3021: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0.05
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData32831(baseconfig.CMonsterData):
    m_SID = 32831
    m_DataSID = 3284
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
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 75),
            3022: (10000, 4) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData32832(baseconfig.CMonsterData):
    m_SID = 32832
    m_DataSID = 3284
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
            'Att': (lambda *a: 4 * (Func10(*a) - 1) + 2750),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 600),
            3023: (10000, 14) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData33001(baseconfig.CMonsterData):
    m_SID = 33001
    m_DataSID = 3300
    m_Name = '黄金·精英巡海夜叉'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1198800 * (Func10(*a) - 1) + 1296000),
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
            'KnockBackFrame': 35,
            'DefThump': 10000,
            'ThumpFrame': 35,
            'Att': (lambda *a: 3 * (Func10(*a) - 1) + 2750),
            'MoveSpeed': 200,
            'AttSpeed': 60,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            104: (10000, 75),
            3022: (10000, 4) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 3
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData39021(baseconfig.CMonsterData):
    m_SID = 39021
    m_DataSID = 3902
    m_Name = '吞天'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 0x15752A000,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': 72000000,
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
            'Att': 17000,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            501: (10000, 30) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData39022(baseconfig.CMonsterData):
    m_SID = 39022
    m_DataSID = 3910
    m_Name = '#NT#罗睺-常驻弱点'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 1152000000,
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


class CMonsterData39023(baseconfig.CMonsterData):
    m_SID = 39023
    m_DataSID = 3911
    m_Name = '#NT#罗睺-阶段一弱点'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 288000000,
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

