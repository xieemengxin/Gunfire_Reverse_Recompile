# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/weapon/i1709.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/weapon/i1709.pyc
# Source Generated with Decompyle++
# File: i1709.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from cl_platformdata.custom.weapon.customaction import CustomActionWeapon1709 as CustomAction
from . import weapondata
from cl_commondefines import DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_NORMAL, DAM_TYPE_THUNDER, EQUIP_TYPE_AMULET, QUALITY_TYPE_LOW

def HoldAction(oOwner, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oOwner, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_ATT_PERFORM, -1, 0, 0, 0)


def CallBack0(oEventCB, oOwner):
    if cl_evcon.CheckFromPointPerform(oOwner, oEventCB, 9709, 1, 0):
        CustomAction(oOwner, oEventCB, {
            'StateSID': 8139 })


class CItem(weapondata.CWeaponData):
    m_SID = 1709
    m_Shape = 1709
    m_Name = '缚妖'
    m_Type = EQUIP_TYPE_AMULET
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 8500,
        'AttSpeed': 175,
        'CrazyEff': 10000,
        'Trajectory': 100,
        'ThumpProb': 0,
        'Radius': 0,
        'UnwieldTime': 10,
        'WieldTime': 30,
        'LuckyHit': 0,
        'MultipleExplodeCnt': 0,
        'AIAttSpeed': 150,
        'Pierce': 1,
        'BulletSpeed': 60,
        'AttDis': 70,
        'ReduceDis': 0,
        'MaxReducePercent': 0,
        'Accuracy': 0,
        'Stability': 0,
        'DebuffProb': 3000 }
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
                0: (9709, 1, 0, DAM_TYPE_FIRE),
                1: (9709, 1, 0, DAM_TYPE_CORRISION),
                2: (9709, 1, 0, DAM_TYPE_THUNDER) },
            'MinorPerform': 9799,
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
    m_ClassifyTag = (4, 6, 10, 13, 1, 23)
    m_CBFuncAction = {
        0: CallBack0 }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 0
    m_SpecialAttr = {
        'MaxTarget': [
            4,
            4,
            7,
            4] }
    m_AIWeaponDam = 1330
    m_AIAccuracyRate = 60

