# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/weapon/i1517.pyc
# RelativePath: clientlogic/cl_platformdata/pc/weapon/i1517.pyc
# Source Generated with Decompyle++
# File: i1517.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_NORMAL, EQUIP_SNIPER, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1517
    m_Shape = 1517
    m_Name = '苍鹰'
    m_Type = EQUIP_SNIPER
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 40000,
        'AttSpeed': 260,
        'CrazyEff': 40000,
        'Trajectory': 100,
        'ThumpProb': 10000,
        'Radius': 0,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 200,
        'Pierce': 99,
        'BulletSpeed': 360,
        'AttDis': 360,
        'ReduceDis': 25,
        'MaxReducePercent': 80,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 2500 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 5,
            'FillTime': 205,
            'BulletType': 4504,
            'Fill': 1003,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9517, 1, 0, 0) },
            'MinorPerform': 9999,
            'MinorRepeatCnt': 0,
            'MinorRepeatCold': 0 },
        'Hold': {
            'WarriorAttr': {
                'MoveSpeed': (0, 0) },
            'HoldAction': None },
        'Snipe': {
            'IsSupport': 1,
            'Shape': 0,
            'WarriorAttr': {
                'MoveSpeed': (1, -1500) },
            'ItemAttr': { },
            'SnipeFov': 400,
            'SnipeTime': 20 },
        'Inscription': { } }
    m_ClassifyTag = (5, 9, 11, 18)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 520
    m_AIAccuracyRate = 95

