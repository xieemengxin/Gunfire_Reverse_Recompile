# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/weapon/i1604.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/weapon/i1604.pyc
# Source Generated with Decompyle++
# File: i1604.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_THUNDER, EQUIP_TYPE_CLOSEWEAPON, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1604
    m_Shape = 1604
    m_Name = '神圣标枪'
    m_Type = EQUIP_TYPE_CLOSEWEAPON
    m_ElementType = DAM_TYPE_THUNDER
    m_ItemAttr = {
        'Att': 450,
        'AttSpeed': 190,
        'CrazyEff': 30000,
        'Trajectory': 100,
        'ThumpProb': 10000,
        'Radius': 4.3,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 190,
        'Pierce': 1,
        'BulletSpeed': 200,
        'AttDis': 120,
        'ReduceDis': 8,
        'MaxReducePercent': 80,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 5000 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 10,
            'FillTime': 145,
            'BulletType': 4503,
            'Fill': 1003,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9602, 1, 0, DAM_TYPE_THUNDER),
                1: (9695, 1, 0, DAM_TYPE_THUNDER) },
            'MinorPerform': 9698,
            'MinorRepeatCnt': 1,
            'MinorRepeatCold': 0 },
        'Hold': {
            'WarriorAttr': {
                'MoveSpeed': (0, 3000) },
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
    m_ClassifyTag = (4, 9, 1, 20)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 750
    m_AIAccuracyRate = 70
    m_AutoChangeAttPf = 1

