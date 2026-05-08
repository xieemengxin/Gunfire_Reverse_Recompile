# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/weapon/i1703.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/weapon/i1703.pyc
# Source Generated with Decompyle++
# File: i1703.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_NORMAL, EQUIP_TYPE_AMULET, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1703
    m_Shape = 1703
    m_Name = '浮游炮'
    m_Type = EQUIP_TYPE_AMULET
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 12500,
        'AttSpeed': 400,
        'CrazyEff': 10000,
        'Trajectory': 100,
        'ThumpProb': 3000,
        'Radius': 4,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 400,
        'Pierce': 1,
        'BulletSpeed': 120,
        'AttDis': 60,
        'ReduceDis': 0,
        'MaxReducePercent': 0,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 2000 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 60,
            'FillTime': 100,
            'BulletType': 4503,
            'Fill': 1024,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9703, 1, 0, 0) },
            'MinorPerform': 9793,
            'MinorRepeatCnt': 0,
            'MinorRepeatCold': 0,
            'InscriptionPerform': 9486 },
        'Hold': {
            'WarriorAttr': {
                'MoveSpeed': (0, 1000) },
            'HoldAction': None },
        'Snipe': {
            'IsSupport': 0,
            'Shape': 0,
            'WarriorAttr': {
                'MoveSpeed': (0, 0) },
            'ItemAttr': { },
            'SnipeFov': 0,
            'SnipeTime': 0 },
        'Inscription': { } }
    m_ClassifyTag = (2, 13, 1, 21)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_SpecialAttr = {
        'EnergyBar': [
            0,
            0,
            100,
            0],
        'StartUpControl': [
            100,
            0,
            100,
            100] }
    m_AIWeaponDam = 620
    m_AIAccuracyRate = 80

