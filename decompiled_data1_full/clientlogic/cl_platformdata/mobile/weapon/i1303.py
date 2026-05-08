# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/weapon/i1303.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/weapon/i1303.pyc
# Source Generated with Decompyle++
# File: i1303.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_NORMAL, EQUIP_SHOTGUN, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1303
    m_Shape = 1303
    m_Name = '幻道'
    m_Type = EQUIP_SHOTGUN
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 4000,
        'AttSpeed': 250,
        'CrazyEff': 20000,
        'Trajectory': 400,
        'ThumpProb': 0,
        'Radius': 0,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 250,
        'Pierce': 1,
        'BulletSpeed': 200,
        'AttDis': 50,
        'ReduceDis': 8,
        'MaxReducePercent': 80,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 500 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 24,
            'FillTime': 170,
            'BulletType': 4503,
            'Fill': 1011,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9303, 1, 0, 0) } },
        'Hold': {
            'WarriorAttr': {
                'MoveSpeed': (0, 0) },
            'HoldAction': None },
        'Spoolup': {
            'ContinueTime': 300,
            'Action': {
                'SpoolUp': {
                    1: {
                        'Trajectory': 200,
                        'AttSpeed': 80 },
                    2: {
                        'Trajectory': 400,
                        'AttSpeed': 150 },
                    3: {
                        'Trajectory': 600,
                        'AttSpeed': 250 } },
                'Bullet': { } } },
        'Snipe': {
            'IsSupport': 0,
            'Shape': 0,
            'WarriorAttr': {
                'MoveSpeed': (0, 0) },
            'ItemAttr': { },
            'SnipeFov': 0,
            'SnipeTime': 0 },
        'Inscription': { } }
    m_ClassifyTag = (5, 7, 16)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 660
    m_AIAccuracyRate = 60

