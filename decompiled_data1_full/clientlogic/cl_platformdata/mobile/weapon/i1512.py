# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/weapon/i1512.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/weapon/i1512.pyc
# Source Generated with Decompyle++
# File: i1512.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_FIRE, EQUIP_HANDGUN, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1512
    m_Shape = 1512
    m_Name = '萤火'
    m_Type = EQUIP_HANDGUN
    m_ElementType = DAM_TYPE_FIRE
    m_ItemAttr = {
        'Att': 13500,
        'AttSpeed': 200,
        'CrazyEff': 20000,
        'Trajectory': 100,
        'ThumpProb': 0,
        'Radius': 3,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 200,
        'Pierce': 99,
        'BulletSpeed': 55,
        'AttDis': 360,
        'ReduceDis': 0,
        'MaxReducePercent': 0,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 1000 }
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
                0: (9512, 1, 0, 0) } },
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
    m_ClassifyTag = (2, 4, 6, 10, 13, 17)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 710
    m_AIAccuracyRate = 70

