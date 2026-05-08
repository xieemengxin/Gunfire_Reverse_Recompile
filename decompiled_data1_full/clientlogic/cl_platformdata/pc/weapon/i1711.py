# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/weapon/i1711.pyc
# RelativePath: clientlogic/cl_platformdata/pc/weapon/i1711.pyc
# Source Generated with Decompyle++
# File: i1711.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_NORMAL, EQUIP_TYPE_AMULET, QUALITY_TYPE_LOW

def HoldAction(oOwner, oLifeCycle):
    cl_action.ItemAddState(oOwner, oLifeCycle, 39746, 0, { }, 1)


class CItem(weapondata.CWeaponData):
    m_SID = 1711
    m_Shape = 1711
    m_Name = '召唤法杖'
    m_Type = EQUIP_TYPE_AMULET
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 15000,
        'AttSpeed': 150,
        'CrazyEff': 10000,
        'Trajectory': 100,
        'ThumpProb': 0,
        'Radius': 0.8,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 150,
        'Pierce': 1,
        'BulletSpeed': 30,
        'AttDis': 70,
        'ReduceDis': 0,
        'MaxReducePercent': 0,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 2000 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 1,
            'FillTime': 1,
            'BulletType': 4503,
            'Fill': 0,
            'Chamber': 0,
            'DualFill': 0,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 2,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9711, 1, 0, 0),
                1: (9712, 1, 0, 0) },
            'MinorPerform': 9796,
            'MinorRepeatCnt': 1,
            'MinorRepeatCold': 0 },
        'Hold': {
            'WarriorAttr': {
                'MoveSpeed': (0, 0) },
            'HoldAction': HoldAction },
        'Snipe': {
            'IsSupport': 0,
            'Shape': 0,
            'WarriorAttr': {
                'MoveSpeed': (0, 0) },
            'ItemAttr': { },
            'SnipeFov': 0,
            'SnipeTime': 0 },
        'Inscription': { } }
    m_ClassifyTag = (5, 6, 10, 13, 1, 23, 24, 25)
    m_CBFuncAction = { }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 0
    m_AIWeaponDam = 1330
    m_AIAccuracyRate = 60
    m_AutoChangeAttPf = 1

