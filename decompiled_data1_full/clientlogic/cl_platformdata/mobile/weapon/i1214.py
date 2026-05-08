# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/weapon/i1214.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/weapon/i1214.pyc
# Source Generated with Decompyle++
# File: i1214.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_NORMAL, EQUIP_HANDGUN, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1214
    m_Shape = 1214
    m_Name = '织云'
    m_Type = EQUIP_HANDGUN
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 7700,
        'AttSpeed': 100,
        'CrazyEff': 30000,
        'Trajectory': 100,
        'ThumpProb': 0,
        'Radius': 0,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 100,
        'Pierce': 1,
        'BulletSpeed': 25,
        'AttDis': 50,
        'ReduceDis': 0,
        'MaxReducePercent': 0,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 1000 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 40,
            'FillTime': 70,
            'BulletType': 4502,
            'Fill': 1017,
            'Chamber': 0,
            'DualFill': 1018,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9214, 1, 0, 0) },
            'MinorPerform': 9294,
            'MinorRepeatCnt': 0,
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
    m_ClassifyTag = (5, 6, 7, 9, 17)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 1000
    m_AIAccuracyRate = 100

