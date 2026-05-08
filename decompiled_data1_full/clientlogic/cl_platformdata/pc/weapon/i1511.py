# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/weapon/i1511.pyc
# RelativePath: clientlogic/cl_platformdata/pc/weapon/i1511.pyc
# Source Generated with Decompyle++
# File: i1511.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_NORMAL, EQUIP_SNIPER, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1511
    m_Shape = 1505
    m_Name = '双弧弓'
    m_Type = EQUIP_SNIPER
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 18000,
        'AttSpeed': 200,
        'CrazyEff': 40000,
        'Trajectory': 100,
        'ThumpProb': 0,
        'Radius': 2,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 200,
        'Pierce': 1,
        'BulletSpeed': 60,
        'AttDis': 360,
        'ReduceDis': 0,
        'MaxReducePercent': 0,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 3000 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 1,
            'FillTime': 6,
            'BulletType': 4504,
            'Fill': 0,
            'Chamber': 0,
            'DualFill': 0,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 2,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9505, 1, 0, 0) } },
        'Hold': {
            'WarriorAttr': {
                'MoveSpeed': (0, 0) },
            'HoldAction': None },
        'Snipe': {
            'IsSupport': 1,
            'Shape': 0,
            'WarriorAttr': {
                'MoveSpeed': (1, 1000) },
            'ItemAttr': { },
            'SnipeFov': 300,
            'SnipeTime': 20 },
        'Inscription': { } }
    m_ClassifyTag = (2, 5, 6, 10, 13)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 0
    m_AIWeaponDam = 1000
    m_AIAccuracyRate = 50

