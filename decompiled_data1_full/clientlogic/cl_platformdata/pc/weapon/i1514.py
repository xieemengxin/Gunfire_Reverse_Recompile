# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/weapon/i1514.pyc
# RelativePath: clientlogic/cl_platformdata/pc/weapon/i1514.pyc
# Source Generated with Decompyle++
# File: i1514.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_THUNDER, EQUIP_HANDGUN, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1514
    m_Shape = 1514
    m_Name = '弧光'
    m_Type = EQUIP_HANDGUN
    m_ElementType = DAM_TYPE_THUNDER
    m_ItemAttr = {
        'Att': 15000,
        'AttSpeed': 220,
        'CrazyEff': 30000,
        'Trajectory': 100,
        'ThumpProb': 0,
        'Radius': 0,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 220,
        'Pierce': 1,
        'BulletSpeed': 100,
        'AttDis': 360,
        'ReduceDis': 0,
        'MaxReducePercent': 0,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 2000 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 1,
            'FillTime': 6,
            'BulletType': 4503,
            'Fill': 0,
            'Chamber': 0,
            'DualFill': 0,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 2,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9514, 1, 0, 0),
                1: (9514, 1, 0, 0) },
            'MinorPerform': 9594,
            'MinorRepeatCnt': 1,
            'MinorRepeatCold': 0 },
        'Hold': {
            'WarriorAttr': {
                'MoveSpeed': (0, 2000) },
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
    m_ClassifyTag = (4, 6, 10, 13, 17, 24, 26)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 4540
    m_AIAccuracyRate = 10

