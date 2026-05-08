# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/weapon/i1603.pyc
# RelativePath: clientlogic/cl_platformdata/pc/weapon/i1603.pyc
# Source Generated with Decompyle++
# File: i1603.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_CORRISION, EQUIP_TYPE_CLOSEWEAPON, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1603
    m_Shape = 1603
    m_Name = '鸩鬼'
    m_Type = EQUIP_TYPE_CLOSEWEAPON
    m_ElementType = DAM_TYPE_CORRISION
    m_ItemAttr = {
        'Att': 49000,
        'AttSpeed': 220,
        'CrazyEff': 20000,
        'Trajectory': 100,
        'ThumpProb': 10000,
        'Radius': 4.6,
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
            'MaxBullet': 15,
            'FillTime': 250,
            'BulletType': 4503,
            'Fill': 1003,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9603, 1, 0, DAM_TYPE_CORRISION),
                1: (9693, 1, 0, DAM_TYPE_CORRISION),
                2: (9694, 1, 0, DAM_TYPE_CORRISION) },
            'MinorPerform': 9697,
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
    m_ClassifyTag = (4, 1, 20, 24)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 0
    m_AIWeaponDam = 450
    m_AIAccuracyRate = 100
    m_AutoChangeAttPf = 1

