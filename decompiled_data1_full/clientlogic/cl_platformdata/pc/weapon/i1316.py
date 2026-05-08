# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/weapon/i1316.pyc
# RelativePath: clientlogic/cl_platformdata/pc/weapon/i1316.pyc
# Source Generated with Decompyle++
# File: i1316.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_NORMAL, EQUIP_SHOTGUN, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1316
    m_Shape = 1316
    m_Name = '锯轮'
    m_Type = EQUIP_SHOTGUN
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 6500,
        'AttSpeed': 200,
        'CrazyEff': 20000,
        'Trajectory': 1000,
        'ThumpProb': 0,
        'Radius': 5,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 200,
        'Pierce': 1,
        'BulletSpeed': 200,
        'AttDis': 50,
        'ReduceDis': 12,
        'MaxReducePercent': 80,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 700 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 10,
            'FillTime': 90,
            'BulletType': 4503,
            'Fill': 1029,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9316, 1, 0, 0) },
            'MinorPerform': 9400,
            'MinorRepeatCnt': 1,
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
    m_ClassifyTag = (5, 7, 19, 26)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_SpecialAttr = {
        'EnergyBar': [
            20,
            20,
            30,
            20] }
    m_AIWeaponDam = 830
    m_AIAccuracyRate = 60

