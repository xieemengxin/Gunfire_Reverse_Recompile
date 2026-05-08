# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/weapon/i1405.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/weapon/i1405.pyc
# Source Generated with Decompyle++
# File: i1405.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_NORMAL, EQUIP_ROCKET_LAUNCHER, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1405
    m_Shape = 1405
    m_Name = '烟花发射器'
    m_Type = EQUIP_ROCKET_LAUNCHER
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 10000,
        'AttSpeed': 360,
        'CrazyEff': 10000,
        'Trajectory': 100,
        'ThumpProb': 0,
        'Radius': 3,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 360,
        'Pierce': 1,
        'BulletSpeed': 60,
        'AttDis': 90,
        'ReduceDis': 0,
        'MaxReducePercent': 0,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 1000 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 9,
            'FillTime': 200,
            'BulletType': 4503,
            'Fill': 1001,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9405, 1, 0, 0) },
            'MinorPerform': 9499,
            'MinorRepeatCnt': 3,
            'MinorRepeatCold': 300 },
        'Hold': {
            'WarriorAttr': {
                'MoveSpeed': (0, -1000) },
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
    m_ClassifyTag = (2, 5, 13)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 340
    m_AIAccuracyRate = 80

