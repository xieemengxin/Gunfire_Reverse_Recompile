# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3003/monster.pyc
# RelativePath: clientlogic/cl_wardata/w3003/monster.pyc
# Source Generated with Decompyle++
# File: monster.pyc (Python 3.6)

from cl_resmgr.resdata import CMonsterData as CCustom
import cl_resmgr.resdata as baseconfig
from cl_newformula import Func10

class CMonsterData2001(baseconfig.CMonsterData):
    m_SID = 2001
    m_DataSID = 2081
    m_Name = '近战怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData2002(baseconfig.CMonsterData):
    m_SID = 2002
    m_DataSID = 2101
    m_Name = '远程怪-单发'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 50 * (Func10(*a) - 1) + 1700),
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


class CMonsterData2003(baseconfig.CMonsterData):
    m_SID = 2003
    m_DataSID = 2101
    m_Name = '远程怪-连射'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData2004(baseconfig.CMonsterData):
    m_SID = 2004
    m_DataSID = 2083
    m_Name = '强化近战怪-跳砍'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData2007(baseconfig.CMonsterData):
    m_SID = 2007
    m_DataSID = 2101
    m_Name = '远程怪-蓄力单发'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 50 * (Func10(*a) - 1) + 1700),
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


class CMonsterData2022(baseconfig.CMonsterData):
    m_SID = 2022
    m_DataSID = 2102
    m_Name = '远程怪-单发-护盾'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 100,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
            'RShield': 10,
            'ShieldRecoverTime': 500,
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
            'Att': (lambda *a: 50 * (Func10(*a) - 1) + 1700),
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


class CMonsterData2023(baseconfig.CMonsterData):
    m_SID = 2023
    m_DataSID = 2102
    m_Name = '远程怪-连射-护盾'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 100,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
            'RShield': 10,
            'ShieldRecoverTime': 500,
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData2031(baseconfig.CMonsterData):
    m_SID = 2031
    m_DataSID = 2081
    m_Name = '近战怪-装甲'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 100,
            'RHP': 0,
            'ArmorMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData2034(baseconfig.CMonsterData):
    m_SID = 2034
    m_DataSID = 2083
    m_Name = '强化近战怪-跳砍-装甲'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 100,
            'RHP': 0,
            'ArmorMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData2101(baseconfig.CMonsterData):
    m_SID = 2101
    m_DataSID = 2083
    m_Name = '强化近战怪-跳砍-装甲-BOSS关'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 100,
            'RHP': 0,
            'ArmorMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData2102(baseconfig.CMonsterData):
    m_SID = 2102
    m_DataSID = 2102
    m_Name = '远程怪-连射-护盾-BOSS关'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 100,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
            'RShield': 10,
            'ShieldRecoverTime': 500,
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData3001(baseconfig.CMonsterData):
    m_SID = 3001
    m_DataSID = 2221
    m_Name = '自爆怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 4000 * (Func10(*a) - 1) + 5000),
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
            'Att': (lambda *a: 70 * (Func10(*a) - 1) + 2500),
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


class CMonsterData3002(baseconfig.CMonsterData):
    m_SID = 3002
    m_DataSID = 2061
    m_Name = '投雷怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 50 * (Func10(*a) - 1) + 1700),
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


class CMonsterData3003(baseconfig.CMonsterData):
    m_SID = 3003
    m_DataSID = 2123
    m_Name = '重型盾兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 38800 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 1000),
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


class CMonsterData3004(baseconfig.CMonsterData):
    m_SID = 3004
    m_DataSID = 2101
    m_Name = '小盾兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 1000),
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


class CMonsterData3005(baseconfig.CMonsterData):
    m_SID = 3005
    m_DataSID = 2201
    m_Name = '喷火怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 1000),
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


class CMonsterData3006(baseconfig.CMonsterData):
    m_SID = 3006
    m_DataSID = 2241
    m_Name = '投射怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 50 * (Func10(*a) - 1) + 1700),
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


class CMonsterData3007(baseconfig.CMonsterData):
    m_SID = 3007
    m_DataSID = 2122
    m_Name = '重装近战'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 38800 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 1000),
            'MoveSpeed': 350,
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


class CMonsterData3008(baseconfig.CMonsterData):
    m_SID = 3008
    m_DataSID = 2021
    m_Name = '四足怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 19400 * (Func10(*a) - 1) + 27000),
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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
    m_DataSID = 2124
    m_Name = '喷子怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 19400 * (Func10(*a) - 1) + 27000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 50 * (Func10(*a) - 1) + 1700),
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


class CMonsterData3010(baseconfig.CMonsterData):
    m_SID = 3010
    m_DataSID = 2161
    m_Name = '追踪子弹怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData3101(baseconfig.CMonsterData):
    m_SID = 3101
    m_DataSID = 2221
    m_Name = '自爆怪-BOSS关'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 4000 * (Func10(*a) - 1) + 5000),
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
            'Att': (lambda *a: 70 * (Func10(*a) - 1) + 2500),
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


class CMonsterData3102(baseconfig.CMonsterData):
    m_SID = 3102
    m_DataSID = 2061
    m_Name = '投雷怪-BOSS关'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 50 * (Func10(*a) - 1) + 1700),
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


class CMonsterData3103(baseconfig.CMonsterData):
    m_SID = 3103
    m_DataSID = 2123
    m_Name = '重型盾兵-BOSS关'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 38800 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 1000),
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


class CMonsterData3104(baseconfig.CMonsterData):
    m_SID = 3104
    m_DataSID = 2101
    m_Name = '小盾兵-连射-BOSS关'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 1000),
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


class CMonsterData3106(baseconfig.CMonsterData):
    m_SID = 3106
    m_DataSID = 2241
    m_Name = '投射怪-BOSS关'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 50 * (Func10(*a) - 1) + 1700),
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


class CMonsterData5001(baseconfig.CMonsterData):
    m_SID = 5001
    m_DataSID = 3901
    m_Name = '第一幕BOSS'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 400000 * (Func10(*a) - 1) + 600000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 30000 * (Func10(*a) - 1) + 50000),
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
            'Att': (lambda *a: 1000 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 600,
            'AttSpeed': 50,
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


class CMonsterData20211(baseconfig.CMonsterData):
    m_SID = 20211
    m_DataSID = 2021
    m_Name = '四足怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 19400 * (Func10(*a) - 1) + 27000),
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData20611(baseconfig.CMonsterData):
    m_SID = 20611
    m_DataSID = 2061
    m_Name = '投雷怪-普通投雷'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 50 * (Func10(*a) - 1) + 1700),
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


class CMonsterData20612(baseconfig.CMonsterData):
    m_SID = 20612
    m_DataSID = 2061
    m_Name = '投雷怪-普通投雷-BOSS关'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 50 * (Func10(*a) - 1) + 1700),
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


class CMonsterData20811(baseconfig.CMonsterData):
    m_SID = 20811
    m_DataSID = 2081
    m_Name = '近战怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData20812(baseconfig.CMonsterData):
    m_SID = 20812
    m_DataSID = 2081
    m_Name = '近战怪-装甲'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 100,
            'RHP': 0,
            'ArmorMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData20831(baseconfig.CMonsterData):
    m_SID = 20831
    m_DataSID = 2083
    m_Name = '强化近战怪-跳砍'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData20832(baseconfig.CMonsterData):
    m_SID = 20832
    m_DataSID = 2083
    m_Name = '强化近战怪-跳砍-装甲'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 100,
            'RHP': 0,
            'ArmorMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData20833(baseconfig.CMonsterData):
    m_SID = 20833
    m_DataSID = 2083
    m_Name = '强化近战怪-跳砍-装甲-BOSS关'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 100,
            'RHP': 0,
            'ArmorMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData21011(baseconfig.CMonsterData):
    m_SID = 21011
    m_DataSID = 2101
    m_Name = '小型远程-基础远程怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData21012(baseconfig.CMonsterData):
    m_SID = 21012
    m_DataSID = 2101
    m_Name = '小型远程-基础远程怪-护盾'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 100,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
            'RShield': 10,
            'ShieldRecoverTime': 500,
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData21013(baseconfig.CMonsterData):
    m_SID = 21013
    m_DataSID = 2101
    m_Name = '小型远程-基础远程怪-护盾-BOSS关'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 100,
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
            'RShield': 10,
            'ShieldRecoverTime': 500,
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
            'Att': (lambda *a: 40 * (Func10(*a) - 1) + 1200),
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


class CMonsterData21021(baseconfig.CMonsterData):
    m_SID = 21021
    m_DataSID = 2102
    m_Name = '小型远程-远程小盾兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 1000),
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


class CMonsterData21022(baseconfig.CMonsterData):
    m_SID = 21022
    m_DataSID = 2102
    m_Name = '小型远程-远程小盾兵-BOSS关'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
            'RShield': 0,
            'ShieldRecoverTime': 0,
            'DefPhysical': 0,
            'DefThunder': 0,
            'DefCorrision': 0,
            'DefFire': 0,
            'AccuracyProb': 90,
            'StruckIgnoreFrame': 75,
            'DefKnockBack': 0,
            'KnockBackFrame': 17,
            'DefThump': 0,
            'ThumpFrame': 17,
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 1000),
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
    m_Name = '中型近战-中型盾兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 38800 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 1000),
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


class CMonsterData21232(baseconfig.CMonsterData):
    m_SID = 21232
    m_DataSID = 2123
    m_Name = '中型近战-中型盾兵-BOSS关'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 38800 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 1000),
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


class CMonsterData21241(baseconfig.CMonsterData):
    m_SID = 21241
    m_DataSID = 2124
    m_Name = '中型近战-霰弹枪兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 38800 * (Func10(*a) - 1) + 54000),
            'RHP': 0,
            'ArmorMax': 0,
            'ShieldMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 30 * (Func10(*a) - 1) + 1000),
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


class CMonsterData22211(baseconfig.CMonsterData):
    m_SID = 22211
    m_DataSID = 2221
    m_Name = '自爆怪-普通自爆'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 4000 * (Func10(*a) - 1) + 5000),
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
            'Att': (lambda *a: 70 * (Func10(*a) - 1) + 2500),
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


class CMonsterData22212(baseconfig.CMonsterData):
    m_SID = 22212
    m_DataSID = 2221
    m_Name = '自爆怪-普通自爆-BOSS关'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 4000 * (Func10(*a) - 1) + 5000),
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
            'Att': (lambda *a: 70 * (Func10(*a) - 1) + 2500),
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


class CMonsterData22411(baseconfig.CMonsterData):
    m_SID = 22411
    m_DataSID = 2241
    m_Name = '投射怪-投射法球怪'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 50 * (Func10(*a) - 1) + 1700),
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


class CMonsterData22412(baseconfig.CMonsterData):
    m_SID = 22412
    m_DataSID = 2241
    m_Name = '投射怪-投射法球怪-BOSS关'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 9700 * (Func10(*a) - 1) + 13500),
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
            'Att': (lambda *a: 50 * (Func10(*a) - 1) + 1700),
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


class CMonsterData22821(baseconfig.CMonsterData):
    m_SID = 22821
    m_DataSID = 2281
    m_Name = '定点法师怪'
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
            'AttSpeed': 150,
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


class CMonsterData39021(baseconfig.CMonsterData):
    m_SID = 39021
    m_DataSID = 3902
    m_Name = 'boss罗睺'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 6000000,
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
            'Att': (lambda *a: 1000 * (Func10(*a) - 1) + 2500),
            'MoveSpeed': 600,
            'AttSpeed': 50,
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

