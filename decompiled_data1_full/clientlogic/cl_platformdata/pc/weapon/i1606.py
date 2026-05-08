# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/weapon/i1606.pyc
# RelativePath: clientlogic/cl_platformdata/pc/weapon/i1606.pyc
# Source Generated with Decompyle++
# File: i1606.pyc (Python 3.6)

import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_msgcenter
from . import weapondata
from cl_commondefines import AUTOFILL_RULE_NONE, DAM_TYPE_NORMAL, EQUIP_TYPE_CLOSEWEAPON, ITEM_MODE_DRILLFOCUS, QUALITY_TYPE_LOW

def HoldAction(oOwner, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oOwner, oLifeCycle, cl_msgcenter.MSG_WAR_ITEM_CHANGE_MODE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oOwner, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERLOGIN, -1, 2, 0, 0)


def CallBack0(oEventCB, oOwner):
    if cl_evcon.EventCBCheckItemMode(oOwner, oEventCB, ITEM_MODE_DRILLFOCUS):
        cl_evact.ItemCBAddState(oOwner, oEventCB, 1849, 0, { }, 0)
    elif not cl_evcon.EventCBCheckWeaponModeByHoldType(oOwner, oEventCB, 0, ITEM_MODE_DRILLFOCUS):
        cl_evact.ItemCBRemoveState(oOwner, oEventCB, 1849)


def CallBack2(oEventCB, oOwner):
    cl_evact.ItemCBRemoveState(oOwner, oEventCB, 1849)


class CItem(weapondata.CWeaponData):
    m_SID = 1606
    m_Shape = 1606
    m_Name = '逐风'
    m_Type = EQUIP_TYPE_CLOSEWEAPON
    m_ElementType = DAM_TYPE_NORMAL
    m_ItemAttr = {
        'Att': 14000,
        'AttSpeed': 1000,
        'CrazyEff': 20000,
        'Trajectory': 100,
        'ThumpProb': 10000,
        'Radius': 4.5,
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
        'DebuffProb': 1500 }
    m_ExtItemAttr = { }
    m_ComponentAttr = {
        'Enhance': { },
        'Bullet': {
            'MaxBullet': 80,
            'FillTime': 260,
            'BulletType': 4502,
            'Fill': 1003,
            'Chamber': 0,
            'DualFill': 1004,
            'BulletVerticalAcc': 0,
            'DelayAutoFillFrame': 8,
            'AutoFillSpecialType': AUTOFILL_RULE_NONE,
            'FillBulletCnt': 1 },
        'Perform': {
            'AttPerform': {
                0: (9606, 1, 0, 0) } },
        'Hold': {
            'WarriorAttr': {
                'MoveSpeed': (0, 2000) },
            'HoldAction': HoldAction },
        'Spoolup': {
            'ContinueTime': 100,
            'Action': {
                'SpoolUp': {
                    1: {
                        'AttSpeed': 0 },
                    2: {
                        'AttSpeed': 0 },
                    3: {
                        'AttSpeed': 0 },
                    4: {
                        'AttSpeed': 0 },
                    5: {
                        'AttSpeed': 0 } },
                'Bullet': {
                    8: {
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
    m_ClassifyTag = (5, 1, 20)
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW
    m_ShopCash = 150
    m_CanDoubleHold = 1
    m_AIWeaponDam = 110
    m_AIAccuracyRate = 100

