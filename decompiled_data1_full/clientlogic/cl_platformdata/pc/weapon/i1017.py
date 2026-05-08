# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/weapon/i1017.pyc
# RelativePath: clientlogic/cl_platformdata/pc/weapon/i1017.pyc
# Source Generated with Decompyle++
# File: i1017.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_NORMAL, EQUIP_RIFLE, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1017
    m_Shape = 1017
    m_Name = '追猎'
    m_Type = EQUIP_RIFLE
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 9000,
        'AttSpeed': 900,
        'CrazyEff': 25000,
        'Trajectory': 100,
        'ThumpProb': 0,
        'Radius': 0,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 900,
        'Pierce': 1,
        'BulletSpeed': 300,
        'AttDis': 180,
        'ReduceDis': 12,
        'MaxReducePercent': 80,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 800 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 40,
            'FillTime': 200,
            'BulletType': 4502,
            'Fill': 1025,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9017, 1, 0, 0),
                1: (9017, 1, 0, 0),
                2: (9017, 1, 0, 0) },
            'MinorPerform': 9093,
            'MinorRepeatCnt': 0,
            'MinorRepeatCold': 0 },
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
    m_ClassifyTag = (5, 16, 24, 26)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 140
    m_AIAccuracyRate = 90

