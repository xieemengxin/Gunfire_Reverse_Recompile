# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/weapon/i1020.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/weapon/i1020.pyc
# Source Generated with Decompyle++
# File: i1020.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_NORMAL, EQUIP_RIFLE, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1020
    m_Shape = 1020
    m_Name = '彻幽'
    m_Type = EQUIP_RIFLE
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 12000,
        'AttSpeed': 250,
        'CrazyEff': 35000,
        'Trajectory': 100,
        'ThumpProb': 0,
        'Radius': 0,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 1000,
        'Pierce': 1,
        'BulletSpeed': 500,
        'AttDis': 200,
        'ReduceDis': 18,
        'MaxReducePercent': 40,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 1000 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 24,
            'FillTime': 140,
            'BulletType': 4502,
            'Fill': 1031,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9020, 2, 300, 0),
                1: (9020, 2, 300, 0) },
            'MinorPerform': 9997,
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
                'MoveSpeed': (0, 0) },
            'ItemAttr': { },
            'SnipeFov': 0,
            'SnipeTime': 0 },
        'Inscription': { } }
    m_ClassifyTag = (5, 11, 16)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 200
    m_AIAccuracyRate = 50

