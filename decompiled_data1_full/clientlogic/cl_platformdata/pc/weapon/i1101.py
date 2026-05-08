# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/weapon/i1101.pyc
# RelativePath: clientlogic/cl_platformdata/pc/weapon/i1101.pyc
# Source Generated with Decompyle++
# File: i1101.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_THUNDER, EQUIP_SMG, QUALITY_TYPE_LOW

class CItem(weapondata.CWeaponData):
    m_SID = 1101
    m_Shape = 1101
    m_Name = '噬星者'
    m_Type = EQUIP_SMG
    m_ElementType = DAM_TYPE_THUNDER
    m_ItemAttr = {
        'Att': 3400,
        'AttSpeed': 1500,
        'CrazyEff': 30000,
        'Trajectory': 100,
        'ThumpProb': 0,
        'Radius': 0,
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
        'DebuffProb': 1000 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 40,
            'FillTime': 125,
            'BulletType': 4502,
            'Fill': 0,
            'Chamber': 0,
            'DualFill': 0,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 8,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9101, 1, 0, 0) } },
        'Hold': {
            'WarriorAttr': {
                'MoveSpeed': (0, 1000) },
            'HoldAction': None },
        'Spoolup': {
            'ContinueTime': 0,
            'Action': {
                'SpoolUp': { },
                'Bullet': {
                    8: {
                        'AttSpeed': -400 },
                    7: {
                        'AttSpeed': -400 },
                    6: {
                        'AttSpeed': -600 },
                    5: {
                        'AttSpeed': -600 },
                    4: {
                        'AttSpeed': -800 },
                    3: {
                        'AttSpeed': -800 },
                    2: {
                        'AttSpeed': -1000 },
                    1: {
                        'AttSpeed': -1000 },
                    0: {
                        'AttSpeed': 0 } } } },
        'Snipe': {
            'IsSupport': 0,
            'Shape': 0,
            'WarriorAttr': {
                'MoveSpeed': (0, 0) },
            'ItemAttr': { },
            'SnipeFov': 0,
            'SnipeTime': 0 },
        'Inscription': { } }
    m_ClassifyTag = (4, 6, 15, 26)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 200
    m_AIAccuracyRate = 60

