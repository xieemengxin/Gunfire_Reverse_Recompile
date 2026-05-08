# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/weapon/i1506.pyc
# RelativePath: clientlogic/cl_platformdata/pc/weapon/i1506.pyc
# Source Generated with Decompyle++
# File: i1506.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_CORRISION, EQUIP_SNIPER, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1506
    m_Shape = 1506
    m_Name = '破甲专家'
    m_Type = EQUIP_SNIPER
    m_ElementType = DAM_TYPE_CORRISION
    m_ItemAttr = {
        'Att': 23500,
        'AttSpeed': 100,
        'CrazyEff': 25000,
        'Trajectory': 100,
        'ThumpProb': 0,
        'Radius': 0,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 100,
        'Pierce': 1,
        'BulletSpeed': 500,
        'AttDis': 360,
        'ReduceDis': 30,
        'MaxReducePercent': 80,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 7000 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 10,
            'FillTime': 250,
            'BulletType': 4504,
            'Fill': 1001,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9506, 1, 0, 0) },
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
            'SnipeFov': 220,
            'SnipeTime': 20 },
        'Inscription': { } }
    m_ClassifyTag = (4, 11, 18)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 1050
    m_AIAccuracyRate = 95

