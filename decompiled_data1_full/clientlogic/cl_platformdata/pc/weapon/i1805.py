# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/weapon/i1805.pyc
# RelativePath: clientlogic/cl_platformdata/pc/weapon/i1805.pyc
# Source Generated with Decompyle++
# File: i1805.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_NORMAL, EQUIP_SNIPER, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1805
    m_Shape = 1805
    m_Name = '啄木鸟（测试）'
    m_Type = EQUIP_SNIPER
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 12000,
        'AttSpeed': 1000,
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
        'BulletSpeed': 210,
        'AttDis': 360,
        'ReduceDis': 50,
        'MaxReducePercent': 80,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 3000 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 20,
            'FillTime': 160,
            'BulletType': 4503,
            'Fill': 1003,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9805, 1, 0, 0) },
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
                'MoveSpeed': (1, -1000) },
            'ItemAttr': { },
            'SnipeFov': 400,
            'SnipeTime': 15 },
        'Inscription': { } }
    m_ClassifyTag = (5, 11, 17, 18)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_SpecialAttr = {
        'EnergyBar': [
            0,
            0,
            100,
            0] }
    m_AIWeaponDam = 150
    m_AIAccuracyRate = 65

