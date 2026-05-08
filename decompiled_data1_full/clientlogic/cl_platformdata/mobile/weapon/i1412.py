# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/weapon/i1412.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/weapon/i1412.pyc
# Source Generated with Decompyle++
# File: i1412.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_FIRE, EQUIP_LASER, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1412
    m_Shape = 1412
    m_Name = '火焰狂龙'
    m_Type = EQUIP_LASER
    m_ElementType = DAM_TYPE_FIRE
    m_ItemAttr = {
        'Att': 4500,
        'AttSpeed': 1200,
        'CrazyEff': 20000,
        'Trajectory': 100,
        'ThumpProb': 0,
        'Radius': 0,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 1200,
        'Pierce': 99,
        'BulletSpeed': 40,
        'AttDis': 15,
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
            'FillTime': 250,
            'BulletType': 4502,
            'Fill': 1003,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9412, 1, 0, 0) },
            'OpPerform': 9494 },
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
    m_AIWeaponDam = 90
    m_AIAccuracyRate = 90

