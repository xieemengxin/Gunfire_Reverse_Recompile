# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/weapon/i1010.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/weapon/i1010.pyc
# Source Generated with Decompyle++
# File: i1010.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_NORMAL, EQUIP_RIFLE, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1010
    m_Shape = 1010
    m_Name = '大河马'
    m_Type = EQUIP_RIFLE
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 8500,
        'AttSpeed': 550,
        'CrazyEff': 20000,
        'Trajectory': 100,
        'ThumpProb': 0,
        'Radius': 0,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 550,
        'Pierce': 1,
        'BulletSpeed': 300,
        'AttDis': 180,
        'ReduceDis': 15,
        'MaxReducePercent': 80,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 500 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 80,
            'FillTime': 250,
            'BulletType': 4502,
            'Fill': 1003,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 0,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9010, 1, 0, 0) } },
        'Hold': {
            'WarriorAttr': {
                'MoveSpeed': (0, -500) },
            'HoldAction': None },
        'Spoolup': {
            'ContinueTime': 300,
            'Action': {
                'SpoolUp': {
                    1: {
                        'AttSpeed': 100 },
                    2: {
                        'AttSpeed': 200 },
                    3: {
                        'AttSpeed': 350 },
                    4: {
                        'AttSpeed': 500 },
                    5: {
                        'AttSpeed': 650 } },
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
    m_ClassifyTag = (5, 16)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 360
    m_AIAccuracyRate = 50

