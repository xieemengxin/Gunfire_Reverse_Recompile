# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/weapon/i1608.pyc
# RelativePath: clientlogic/cl_platformdata/pc/weapon/i1608.pyc
# Source Generated with Decompyle++
# File: i1608.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_NORMAL, EQUIP_TYPE_CLOSEWEAPON, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1608
    m_Shape = 1608
    m_Name = '凌云'
    m_Type = EQUIP_TYPE_CLOSEWEAPON
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 30000,
        'AttSpeed': 180,
        'CrazyEff': 20000,
        'Trajectory': 100,
        'ThumpProb': 10000,
        'Radius': 4.5,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 220,
        'Pierce': 1,
        'BulletSpeed': 200,
        'AttDis': 120,
        'ReduceDis': 8,
        'MaxReducePercent': 80,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 3000 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 1,
            'FillTime': 1,
            'BulletType': 4503,
            'Fill': 0,
            'Chamber': 0,
            'DualFill': 0,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 1,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9608, 1, 0, 0),
                1: (9609, 1, 0, 0),
                2: (9610, 1, 0, 0),
                3: (9611, 1, 0, 0),
                4: (9612, 1, 0, 0) },
            'MinorPerform': 9690,
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
                'MoveSpeed': (0, 1000) },
            'ItemAttr': { },
            'SnipeFov': 0,
            'SnipeTime': 0 },
        'Inscription': { } }
    m_ClassifyTag = (5, 6, 10, 1, 20, 24)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 0
    m_AIWeaponDam = 275
    m_AIAccuracyRate = 100
    m_AutoChangeAttPf = 1

