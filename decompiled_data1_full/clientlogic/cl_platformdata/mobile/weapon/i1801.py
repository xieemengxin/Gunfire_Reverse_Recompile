# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/weapon/i1801.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/weapon/i1801.pyc
# Source Generated with Decompyle++
# File: i1801.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_FIRE, EQUIP_ROCKET_LAUNCHER, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1801
    m_Shape = 1408
    m_Name = '蜥燚'
    m_Type = EQUIP_ROCKET_LAUNCHER
    m_ElementType = DAM_TYPE_FIRE
    m_ItemAttr = {
        'Att': 27000,
        'AttSpeed': 170,
        'CrazyEff': 10000,
        'Trajectory': 100,
        'ThumpProb': 3000,
        'Radius': 4,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 170,
        'Pierce': 1,
        'BulletSpeed': 30,
        'AttDis': 50,
        'ReduceDis': 0,
        'MaxReducePercent': 0,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 3000 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 6,
            'FillTime': 200,
            'BulletType': 4503,
            'Fill': 1003,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9801, 1, 0, 0) },
            'InscriptionPerform': 9486 },
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
    m_ClassifyTag = (2, 4, 13, 1)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 620
    m_AIAccuracyRate = 80

