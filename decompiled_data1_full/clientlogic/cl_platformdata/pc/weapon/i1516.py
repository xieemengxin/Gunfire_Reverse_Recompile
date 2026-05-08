# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/weapon/i1516.pyc
# RelativePath: clientlogic/cl_platformdata/pc/weapon/i1516.pyc
# Source Generated with Decompyle++
# File: i1516.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import AUTOFILL_RULE_REPEATEND, DAM_TYPE_NORMAL, EQUIP_SNIPER, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1516
    m_Shape = 1516
    m_Name = '碎珏'
    m_Type = EQUIP_SNIPER
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 13500,
        'AttSpeed': 260,
        'CrazyEff': 35000,
        'Trajectory': 100,
        'ThumpProb': 0,
        'Radius': 0,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 200,
        'Pierce': 1,
        'BulletSpeed': 170,
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
            'MaxBullet': 4,
            'FillTime': 4,
            'BulletType': 4502,
            'Fill': 0,
            'Chamber': 0,
            'DualFill': 0,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 2,
            'AutoFillSpecialType': AUTOFILL_RULE_REPEATEND,
            'FillBulletCnt': 4 },
        'Perform': {
            'AttPerform': {
                0: (9516, 4, 200, 0) },
            'MinorPerform': 9795,
            'MinorRepeatCnt': 0,
            'MinorRepeatCold': 0 },
        'Hold': {
            'WarriorAttr': {
                'MoveSpeed': (0, 0) },
            'HoldAction': None },
        'Spoolup': {
            'ContinueTime': 40,
            'Action': {
                'SpoolUp': { },
                'Bullet': { } } },
        'Snipe': {
            'IsSupport': 1,
            'Shape': 0,
            'WarriorAttr': {
                'MoveSpeed': (1, 1000) },
            'ItemAttr': { },
            'SnipeFov': 300,
            'SnipeTime': 20 },
        'Inscription': { } }
    m_ClassifyTag = (5, 6, 10, 13, 18, 24, 25)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 0
    m_AIWeaponDam = 1000
    m_AIAccuracyRate = 50

