# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/weapon/i1508.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/weapon/i1508.pyc
# Source Generated with Decompyle++
# File: i1508.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_CORRISION, EQUIP_SNIPER, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1508
    m_Shape = 1508
    m_Name = '惊蛰'
    m_Type = EQUIP_SNIPER
    m_ElementType = DAM_TYPE_CORRISION
    m_ItemAttr = {
        'Att': 10500,
        'AttSpeed': 155,
        'CrazyEff': 30000,
        'Trajectory': 100,
        'ThumpProb': 0,
        'Radius': 5,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 155,
        'Pierce': 1,
        'BulletSpeed': 90,
        'AttDis': 360,
        'ReduceDis': 50,
        'MaxReducePercent': 80,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 2500 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 9,
            'FillTime': 238,
            'BulletType': 4503,
            'Fill': 1003,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9598, 1, 200, 0),
                1: (9597, 1, 200, 0),
                2: (9508, 1, 200, 0) } },
        'Hold': {
            'WarriorAttr': {
                'MoveSpeed': (0, 0) },
            'HoldAction': None },
        'Snipe': {
            'IsSupport': 0,
            'Shape': 0,
            'WarriorAttr': {
                'MoveSpeed': (1, -1000) },
            'ItemAttr': { },
            'SnipeFov': 300,
            'SnipeTime': 20 },
        'Inscription': { } }
    m_ClassifyTag = (2, 4, 16, 0, 27)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 670
    m_AIAccuracyRate = 95
    m_AutoChangeAttPf = 1

