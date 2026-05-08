# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/weapon/i1419.pyc
# RelativePath: clientlogic/cl_platformdata/pc/weapon/i1419.pyc
# Source Generated with Decompyle++
# File: i1419.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_item.defines import EQUIP_ROCKET_LAUNCHER, QUALITY_TYPE_LOW
from cl_commondefines import DAM_TYPE_NORMAL

class CItem(weapondata.CWeaponData):
    m_SID = 1419
    m_Shape = 1419
    m_Name = '锐鸣炮改'
    m_Type = EQUIP_ROCKET_LAUNCHER
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 55500,
        'AttSpeed': 175,
        'CrazyEff': 20000,
        'Trajectory': 100,
        'ThumpProb': 10000,
        'Radius': 3,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 175,
        'Pierce': 1,
        'BulletSpeed': 75,
        'AttDis': 40,
        'ReduceDis': 0,
        'MaxReducePercent': 0,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 2000 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 4,
            'FillTime': 160,
            'BulletType': 4504,
            'Fill': 1008,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0 },
        'Perform': {
            'AttPerform': {
                0: (9419, 1, 0, 0) },
            'InscriptionPerform': 9485 },
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
    m_ClassifyTag = (2, 5, 9, 26)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 710
    m_AIAccuracyRate = 80

