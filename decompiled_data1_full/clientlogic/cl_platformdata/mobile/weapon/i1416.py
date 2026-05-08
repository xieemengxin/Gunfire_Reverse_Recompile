# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/weapon/i1416.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/weapon/i1416.pyc
# Source Generated with Decompyle++
# File: i1416.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import DAM_TYPE_NORMAL, EQUIP_ROCKET_LAUNCHER, QUALITY_TYPE_LOW

def AddAction(oOwner, oLifeCycle):
    cl_action.ItemSetSelfForceAttr(oOwner, oLifeCycle, 'AttSpeed', 60)


class CItem(weapondata.CWeaponData):
    m_SID = 1416
    m_Shape = 1416
    m_Name = '龙息'
    m_Type = EQUIP_ROCKET_LAUNCHER
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 80000,
        'AttSpeed': 70,
        'CrazyEff': 10000,
        'Trajectory': 100,
        'ThumpProb': 10000,
        'Radius': 2,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 70,
        'Pierce': 1,
        'BulletSpeed': 800,
        'AttDis': 360,
        'ReduceDis': 0,
        'MaxReducePercent': 0,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 2500 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 1,
            'FillTime': 1,
            'BulletType': 4504,
            'Fill': 0,
            'Chamber': 0,
            'DualFill': 0,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 2,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9416, 1, 0, 0) } },
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
    m_ClassifyTag = (2, 5, 6, 9, 10, 1)
    m_CBFuncAction = { }
    m_Action = (AddAction, None)
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_SpecialAttr = {
        'EnergyBar': [
            1,
            1,
            2,
            1],
        'ExplodeControl': [
            0,
            0,
            100,
            0] }
    m_AIWeaponDam = 1660
    m_AIAccuracyRate = 80

