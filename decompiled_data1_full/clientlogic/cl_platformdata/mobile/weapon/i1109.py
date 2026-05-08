# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/weapon/i1109.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/weapon/i1109.pyc
# Source Generated with Decompyle++
# File: i1109.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_item.defines import EQUIP_SMG, QUALITY_TYPE_LOW
from cl_commondefines import DAM_TYPE_NORMAL

class CItem(weapondata.CWeaponData):
    m_SID = 1109
    m_Shape = 1109
    m_Name = '隐弹魔王'
    m_Type = EQUIP_SMG
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 5200,
        'AttSpeed': 1350,
        'CrazyEff': 30000,
        'Trajectory': 100,
        'ThumpProb': 0,
        'Radius': 3,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 1000,
        'Pierce': 1,
        'BulletSpeed': 200,
        'AttDis': 120,
        'ReduceDis': 8,
        'MaxReducePercent': 80,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 500 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 28,
            'FillTime': 140,
            'BulletType': 4502,
            'Fill': 1003,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0 },
        'Perform': {
            'AttPerform': {
                0: (9109, 1, 0, 0) },
            'MinorPerform': 9204,
            'MinorRepeatCnt': 1,
            'MinorRepeatCold': 0,
            'InscriptionPerform': 9482 },
        'Hold': {
            'WarriorAttr': {
                'MoveSpeed': (0, 1000) },
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
    m_ClassifyTag = (2, 5, 15)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 200
    m_AIAccuracyRate = 60

