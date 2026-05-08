# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/weapon/i1310.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/weapon/i1310.pyc
# Source Generated with Decompyle++
# File: i1310.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_NORMAL, EQUIP_SHOTGUN, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1310
    m_Shape = 1310
    m_Name = '锯轮'
    m_Type = EQUIP_SHOTGUN
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 7000,
        'AttSpeed': 200,
        'CrazyEff': 20000,
        'Trajectory': 1000,
        'ThumpProb': 0,
        'Radius': 5,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 200,
        'Pierce': 1,
        'BulletSpeed': 200,
        'AttDis': 50,
        'ReduceDis': 5,
        'MaxReducePercent': 80,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 700 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 5,
            'FillTime': 90,
            'BulletType': 4503,
            'Fill': 1022,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9310, 1, 0, 0) },
            'MinorPerform': 9390,
            'MinorRepeatCnt': 1,
            'MinorRepeatCold': 0 },
        'Hold': {
            'WarriorAttr': {
                'MoveSpeed': (0, 0) },
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
    m_ClassifyTag = (5, 7, 19)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 830
    m_AIAccuracyRate = 60

