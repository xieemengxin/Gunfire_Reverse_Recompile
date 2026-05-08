# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/weapon/i1410.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/weapon/i1410.pyc
# Source Generated with Decompyle++
# File: i1410.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_THUNDER, EQUIP_LASER, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1410
    m_Shape = 1410
    m_Name = '雷霆手套'
    m_Type = EQUIP_LASER
    m_ElementType = DAM_TYPE_THUNDER
    m_ItemAttr = {
        'Att': 2000,
        'AttSpeed': 1600,
        'CrazyEff': 20000,
        'Trajectory': 100,
        'ThumpProb': 0,
        'Radius': 6,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 1600,
        'Pierce': 1,
        'BulletSpeed': 500,
        'AttDis': 75,
        'ReduceDis': 0,
        'MaxReducePercent': 0,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 500 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 80,
            'FillTime': 150,
            'BulletType': 4502,
            'Fill': 1003,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9410, 1, 0, 0) } },
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
    m_ClassifyTag = (4, 12, 13)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 60
    m_AIAccuracyRate = 90

