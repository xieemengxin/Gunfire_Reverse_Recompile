# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51605.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51605.pyc
# Source Generated with Decompyle++
# File: p51605.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION, DAM_TYPE_ELEMENT, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, MAIN_HOLD, OBJ_VICTIM
from cl_newformula import Func308, Func347, Func517, Func599, Func736

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_ELEMENT, -1):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_FIRE, 0):
            if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 20026, 0, 0, 0, 0):
                cl_evact.EventCBAddCustomInfo(oWarrior, oEventCB, 'Newbuff', 0)
            else:
                cl_evact.EventCBAddCustomInfo(oWarrior, oEventCB, 'Newbuff', 1)
            if cl_evcon.CheckWeaponBulletTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, 4502):
                cl_evact.EventCBAddHoldWeaponBagBullet(oWarrior, oEventCB, (lambda *a: ((Func736(*a, **{
'sKey': 'Newbuff' }) + Func599(*a)) * Func308(*a) * Func347(*a, **{
'sid': 4502 }) + 99) // 100), MAIN_HOLD)
            if cl_evcon.CheckWeaponBulletTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, 4503):
                cl_evact.EventCBAddHoldWeaponBagBullet(oWarrior, oEventCB, (lambda *a: ((Func736(*a, **{
'sKey': 'Newbuff' }) + Func599(*a)) * Func308(*a) * Func347(*a, **{
'sid': 4503 }) + 99) // 100), MAIN_HOLD)
            if cl_evcon.CheckWeaponBulletTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, 4504):
                cl_evact.EventCBAddHoldWeaponBagBullet(oWarrior, oEventCB, (lambda *a: ((Func736(*a, **{
'sKey': 'Newbuff' }) + Func599(*a)) * Func308(*a) * Func347(*a, **{
'sid': 4504 }) + 99) // 100), MAIN_HOLD)
            cl_evact.EventCBAddHoldWeaponComBullet(oWarrior, oEventCB, (lambda *a: (Func517(*a) * max(0, Func308(*a) - 2) + 99) // 100), MAIN_HOLD)
        elif cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_CORRISION, 0):
            if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 20027, 0, 0, 0, 0):
                cl_evact.EventCBAddCustomInfo(oWarrior, oEventCB, 'Newbuff', 0)
            else:
                cl_evact.EventCBAddCustomInfo(oWarrior, oEventCB, 'Newbuff', 1)
            if cl_evcon.CheckWeaponBulletTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, 4502):
                cl_evact.EventCBAddHoldWeaponBagBullet(oWarrior, oEventCB, (lambda *a: ((Func736(*a, **{
'sKey': 'Newbuff' }) + Func599(*a)) * Func308(*a) * Func347(*a, **{
'sid': 4502 }) + 99) // 100), MAIN_HOLD)
            if cl_evcon.CheckWeaponBulletTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, 4503):
                cl_evact.EventCBAddHoldWeaponBagBullet(oWarrior, oEventCB, (lambda *a: ((Func736(*a, **{
'sKey': 'Newbuff' }) + Func599(*a)) * Func308(*a) * Func347(*a, **{
'sid': 4503 }) + 99) // 100), MAIN_HOLD)
            if cl_evcon.CheckWeaponBulletTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, 4504):
                cl_evact.EventCBAddHoldWeaponBagBullet(oWarrior, oEventCB, (lambda *a: ((Func736(*a, **{
'sKey': 'Newbuff' }) + Func599(*a)) * Func308(*a) * Func347(*a, **{
'sid': 4504 }) + 99) // 100), MAIN_HOLD)
            cl_evact.EventCBAddHoldWeaponComBullet(oWarrior, oEventCB, (lambda *a: (Func517(*a) * max(0, Func308(*a) - 2) + 99) // 100), MAIN_HOLD)
        elif cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_THUNDER, 0):
            if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 20028, 0, 0, 0, 0):
                cl_evact.EventCBAddCustomInfo(oWarrior, oEventCB, 'Newbuff', 0)
            else:
                cl_evact.EventCBAddCustomInfo(oWarrior, oEventCB, 'Newbuff', 1)
            if cl_evcon.CheckWeaponBulletTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, 4502):
                cl_evact.EventCBAddHoldWeaponBagBullet(oWarrior, oEventCB, (lambda *a: ((Func736(*a, **{
'sKey': 'Newbuff' }) + Func599(*a)) * Func308(*a) * Func347(*a, **{
'sid': 4502 }) + 99) // 100), MAIN_HOLD)
            if cl_evcon.CheckWeaponBulletTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, 4503):
                cl_evact.EventCBAddHoldWeaponBagBullet(oWarrior, oEventCB, (lambda *a: ((Func736(*a, **{
'sKey': 'Newbuff' }) + Func599(*a)) * Func308(*a) * Func347(*a, **{
'sid': 4503 }) + 99) // 100), MAIN_HOLD)
            if cl_evcon.CheckWeaponBulletTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, 4504):
                cl_evact.EventCBAddHoldWeaponBagBullet(oWarrior, oEventCB, (lambda *a: ((Func736(*a, **{
'sKey': 'Newbuff' }) + Func599(*a)) * Func308(*a) * Func347(*a, **{
'sid': 4504 }) + 99) // 100), MAIN_HOLD)
            cl_evact.EventCBAddHoldWeaponComBullet(oWarrior, oEventCB, (lambda *a: (Func517(*a) * max(0, Func308(*a) - 2) + 99) // 100), MAIN_HOLD)


class CPerform(CCustomPerform):
    m_SID = 51605
    m_Name = '#NT#元素回弹'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

