# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3005/monster.pyc
# RelativePath: clientlogic/cl_wardata/w3005/monster.pyc
# Source Generated with Decompyle++
# File: monster.pyc (Python 3.6)

from cl_resmgr.resdata import CMonsterData as CCustom
import cl_resmgr.resdata as baseconfig
from cl_newformula import Func10, Func204, Func205

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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (0, 1),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 110000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 110000
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1) } }
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (500, 1) },
        2: {
            201: (500, 1) },
        3: {
            201: (500, 1) } }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (0, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (0, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (0, 3),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (0, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (0, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (0, 3),
            402: (0, 2),
            403: (0, 1) } }
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
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
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) } }
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
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
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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


class CMonsterData20881(baseconfig.CMonsterData):
    m_SID = 20881
    m_DataSID = 2088
    m_Name = '石化 右矛兵'
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
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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


class CMonsterData20981(baseconfig.CMonsterData):
    m_SID = 20981
    m_DataSID = 2098
    m_Name = '【出生测试】小型近战怪'
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) } }
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 6667
    m_SprintSpeedUpMul = 23333
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) } }
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21071(baseconfig.CMonsterData):
    m_SID = 21071
    m_DataSID = 2107
    m_Name = '石化 徒盾弩兵'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 21840 * (Func10(*a) - 1) + 46800),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) } }
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) } }
    m_RunSpeedUpMul = 7650
    m_SprintSpeedUpMul = 32353
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) } }
    m_RunSpeedUpMul = -2500
    m_SprintSpeedUpMul = 8750
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) } }
    m_RunSpeedUpMul = -5000
    m_SprintSpeedUpMul = 4000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
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
            'DefKnockBack': 10000,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 3333
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) } }
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
    m_Name = '石化 马头锐士'
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) } }
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) } }
    m_RunSpeedUpMul = 3125
    m_SprintSpeedUpMul = 21250
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) } }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 2000), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 2000), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) } }
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData21441(baseconfig.CMonsterData):
    m_SID = 21441
    m_DataSID = 2144
    m_Name = '石化 重弩锐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 33280 * (Func10(*a) - 1) + 62400),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) } }
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) } }
    m_RunSpeedUpMul = 5000
    m_SprintSpeedUpMul = 27500
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) } }
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -900 + 3000), 1),
            101: (10000, 3),
            402: (0, 2),
            402: (0, 2) },
        2: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -900 + 3000), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) },
        3: {
            201: (6000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -900 + 3000), 1),
            101: (10000, 4),
            402: (0, 2),
            402: (0, 2) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 3),
            402: (0, 3) },
        2: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -2100 + 7000), 1),
            101: (10000, 6),
            402: (0, 3),
            402: (0, 3) },
        3: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -2100 + 7000), 1),
            101: (10000, 6),
            402: (0, 3),
            402: (0, 3) } }
    m_RunSpeedUpMul = 15000
    m_SprintSpeedUpMul = 23333
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
            'DefKnockBack': 0,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 3),
            402: (0, 3) },
        2: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -2100 + 7000), 1),
            101: (10000, 6),
            402: (0, 3),
            402: (0, 3) },
        3: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -2100 + 7000), 1),
            101: (10000, 6),
            402: (0, 3),
            402: (0, 3) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'DefKnockBack': 0,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
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
            'DefKnockBack': 0,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -1500 + 5000), 1),
            101: (10000, 4),
            402: (0, 3),
            402: (0, 3) },
        2: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -2100 + 7000), 1),
            101: (10000, 6),
            402: (0, 3),
            402: (0, 3) },
        3: {
            201: (8000, 2),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -2100 + 7000), 1),
            101: (10000, 6),
            402: (0, 3),
            402: (0, 3) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 23333
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
            'ThumpFrame': 0,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
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
            'ThumpFrame': 0,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
            'ThumpFrame': 0,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
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
            'ThumpFrame': 0,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
            'ThumpFrame': 0,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
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
            'ThumpFrame': 0,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
            'ThumpFrame': 0,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (1000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 1),
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
            'ThumpFrame': 0,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
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
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData22451(baseconfig.CMonsterData):
    m_SID = 22451
    m_DataSID = 2245
    m_Name = '石化 投戟兵'
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) } }
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) } }
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) } }
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
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 6667
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -30 + 1000), 1),
            101: (10000, 2),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (3000, 1),
            401: ((lambda *a: min(int((Func205(*a) - 1) * 0.5 + (Func204(*a) - 1) * 0.5), 1) * -60 + 200), 1),
            101: (10000, 3),
            402: (0, 2),
            403: (0, 1) } }
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
    m_Name = '钱龙'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) ** 1.7 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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


class CMonsterData23421(baseconfig.CMonsterData):
    m_SID = 23421
    m_DataSID = 2342
    m_Name = '钱龙'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) ** 1.7 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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


class CMonsterData23431(baseconfig.CMonsterData):
    m_SID = 23431
    m_DataSID = 2343
    m_Name = '钱龙'
    m_BaseAttrInfo = {
        1: {
            'HPMax': (lambda *a: 1200000 * (Func10(*a) - 1) + 260000 - ((Func205(*a) - 1) ** 1.7 + (Func204(*a) - 1) * 0.4) * (Func10(*a) - 1) * 150000),
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


class CMonsterData30011(baseconfig.CMonsterData):
    m_SID = 30011
    m_DataSID = 3001
    m_Name = '精英独角金龟'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 2000000,
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
            'Att': 2000,
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
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (500, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1) } }
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) } }
    m_RunSpeedUpMul = 4000
    m_SprintSpeedUpMul = 30000
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
            'HPMax': 599800,
            'RHP': 0,
            'ArmorMax': 2000000,
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
            'Att': 2000,
            'MoveSpeed': 225,
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
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 20000
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData31231(baseconfig.CMonsterData):
    m_SID = 31231
    m_DataSID = 3123
    m_Name = '精英马头锐士'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 2000000,
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
            'Att': 2100,
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
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) } }
    m_RunSpeedUpMul = -2500
    m_SprintSpeedUpMul = 8750
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 14000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 23333
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) } }
    m_RunSpeedUpMul = 15000
    m_SprintSpeedUpMul = 35138
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
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
            'AccuracyProb': 85,
            'StruckIgnoreFrame': 150,
            'DefKnockBack': 10000,
            'KnockBackFrame': 36,
            'DefThump': 10000,
            'ThumpFrame': 36,
            'Att': (lambda *a: 140 * (Func10(*a) - 1) + 1870),
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
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 23333
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 30000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1) },
        2: {
            201: (10000, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1) },
        3: {
            201: (10000, 1),
            401: (0, 1),
            101: (0, 1),
            402: (0, 2),
            403: (0, 1) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 10000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 2),
            401: (10000, 1),
            101: (10000, 12),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        2: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1) },
        3: {
            201: (10000, 2),
            401: (10000, 2),
            101: (10000, 15),
            402: (0, 5),
            403: (0, 2),
            4101: (2000, 1),
            2404: (10000, 1),
            101: (10000, 3),
            4101: (10000, 1),
            201: (10000, 3),
            2404: (10000, 1),
            101: (10000, 3),
            4101: (10000, 1),
            201: (10000, 3),
            2404: (10000, 1),
            101: (10000, 3),
            4101: (10000, 1),
            201: (10000, 3),
            2404: (10000, 1),
            101: (10000, 3),
            4101: (10000, 1),
            201: (10000, 3),
            2404: (10000, 1),
            101: (10000, 3),
            4101: (10000, 1),
            201: (10000, 3),
            2404: (10000, 1),
            101: (10000, 3),
            4101: (10000, 1),
            201: (10000, 3) } }
    m_RunSpeedUpMul = -2000
    m_SprintSpeedUpMul = 16667
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
            'ShieldMax': 300000,
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
            'Att': 2500,
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
    m_Reward = {
        1: {
            101: (10000, 30),
            201: (10000, 3),
            401: (10000, 3) },
        2: {
            101: (10000, 30),
            201: (10000, 3),
            401: (10000, 3) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 38000
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
    m_Name = '罗睺'
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
            'StruckIgnoreFrame': 300,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
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
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        0: {
            2404: (10000, 1),
            101: (10000, 3),
            4101: (10000, 1),
            201: (10000, 3),
            2404: (10000, 1),
            101: (10000, 3),
            4101: (10000, 1),
            201: (10000, 3),
            2404: (10000, 1),
            101: (10000, 3),
            4101: (10000, 1),
            201: (10000, 3) } }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


class CMonsterData39091(baseconfig.CMonsterData):
    m_SID = 39091
    m_DataSID = 3909
    m_Name = '连城'
    m_BaseAttrInfo = {
        1: {
            'HPMax': 30000000,
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
            'Att': 10000,
            'MoveSpeed': 500,
            'AttSpeed': 56,
            'Toughness': 100,
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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            101: (10000, 30),
            201: (10000, 3),
            401: (10000, 3) },
        2: {
            101: (10000, 30),
            201: (10000, 3),
            401: (10000, 3) } }
    m_RunSpeedUpMul = 10000
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        1: {
            201: (10000, 3),
            101: (10000, 20),
            4101: (10000, 1),
            2404: (10000, 1) },
        2: {
            201: (10000, 3),
            101: (10000, 25),
            4101: (10000, 1),
            2404: (10000, 1) },
        3: {
            201: (10000, 3),
            101: (10000, 25),
            4101: (10000, 1),
            2404: (10000, 1) } }
    m_RunSpeedUpMul = -5000
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = {
        0: {
            2404: (10000, 1),
            101: (10000, 3),
            4101: (10000, 1),
            201: (10000, 3),
            2404: (10000, 1),
            101: (10000, 3),
            4101: (10000, 1),
            201: (10000, 3),
            2404: (10000, 1),
            101: (10000, 3),
            4101: (10000, 1),
            201: (10000, 3),
            2404: (10000, 1),
            101: (10000, 3),
            4101: (10000, 1),
            201: (10000, 3),
            2404: (10000, 1),
            101: (10000, 3),
            4101: (10000, 1),
            201: (10000, 3),
            2404: (10000, 1),
            101: (10000, 3),
            4101: (10000, 1),
            201: (10000, 3) } }
    m_RunSpeedUpMul = -5000
    m_SprintSpeedUpMul = 0
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0


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
            'SpecialMHPWeight': 0 } }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_Reward = { }
    m_RunSpeedUpMul = 30000
    m_SprintSpeedUpMul = 38000
    m_MonsterPartSID = 0
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraPerform = {
        'Round': { },
        'Mode': { } }
    m_SpecialMHP = 0

