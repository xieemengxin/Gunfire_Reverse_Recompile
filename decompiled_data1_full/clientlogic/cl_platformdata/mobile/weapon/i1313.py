# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/weapon/i1313.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/weapon/i1313.pyc
# Source Generated with Decompyle++
# File: i1313.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_item.defines import EQUIP_SHOTGUN, QUALITY_TYPE_LOW
from cl_commondefines import DAM_TYPE_NORMAL

class CItem(weapondata.CWeaponData):
    m_SID = 1313
    m_Shape = 1313
    m_Name = '老虎机'
    m_Type = EQUIP_SHOTGUN
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 6300,
        'AttSpeed': 155,
        'CrazyEff': 20000,
        'Trajectory': 900,
        'ThumpProb': 0,
        'Radius': 0,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 155,
        'Pierce': 3,
        'BulletSpeed': 300,
        'AttDis': 50,
        'ReduceDis': 20,
        'MaxReducePercent': 80,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 800 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 6,
            'FillTime': 45,
            'BulletType': 4504,
            'Fill': 1003,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0 },
        'Perform': {
            'AttPerform': {
                0: (9313, 1, 0, 0) } },
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
    m_ClassifyTag = (5, 7, 19, 21)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 1070
    m_AIAccuracyRate = 60
    m_AutoChangeAttPf = 0

