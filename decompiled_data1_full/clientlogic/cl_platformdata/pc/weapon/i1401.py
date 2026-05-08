# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/weapon/i1401.pyc
# RelativePath: clientlogic/cl_platformdata/pc/weapon/i1401.pyc
# Source Generated with Decompyle++
# File: i1401.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_NORMAL, EQUIP_ROCKET_LAUNCHER, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1401
    m_Shape = 1401
    m_Name = '青铜虎炮'
    m_Type = EQUIP_ROCKET_LAUNCHER
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 68000,
        'AttSpeed': 100,
        'CrazyEff': 10000,
        'Trajectory': 100,
        'ThumpProb': 5000,
        'Radius': 6,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 100,
        'Pierce': 1,
        'BulletSpeed': 25,
        'AttDis': 90,
        'ReduceDis': 0,
        'MaxReducePercent': 0,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 2500 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 1,
            'FillTime': 250,
            'BulletType': 4504,
            'Fill': 1003,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9401, 1, 0, 0) },
            'InscriptionPerform': 9488 },
        'Hold': {
            'WarriorAttr': {
                'MoveSpeed': (0, -1000) },
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
    m_ClassifyTag = (2, 5, 13, 14, 1, 26)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 1250
    m_AIAccuracyRate = 80

