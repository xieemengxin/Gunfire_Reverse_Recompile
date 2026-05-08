# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33684.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33684.pyc
# Source Generated with Decompyle++
# File: st33684.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, DEPUTY_HOLD, EXTGRADE_GROUP2, MAIN_HOLD, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_item.defines import MSG_ITEM_REFRESHATTRIBUTE
from math import ceil
from cl_newformula import Func304, Func518, Func785

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 1, 0, 0)
    cl_action.CommonListenHoldWeaponMsg(oTarget, oLifeCycle, DEPUTY_HOLD, MSG_ITEM_REFRESHATTRIBUTE, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREUNHOLDWEAPON, MAIN_HOLD, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPON_ELEMENTTYPE_REFRESH, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'DebuffFactor', -1, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckItemRefreshAttribute(oTarget, oEventCB, 'DebuffProb'):
        if cl_evcon.CheckWeaponElementTypeByHoldType(oTarget, oEventCB, DEPUTY_HOLD, DAM_TYPE_FIRE) or cl_evcon.CheckWeaponElementTypeByHoldType(oTarget, oEventCB, DEPUTY_HOLD, DAM_TYPE_THUNDER) or cl_evcon.CheckWeaponElementTypeByHoldType(oTarget, oEventCB, DEPUTY_HOLD, DAM_TYPE_CORRISION):
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func518(*a, **{
'sAttr': 'p51326_BaseAdd' }) + min(int(ceil(Func785(*a, **{
'sAttr': 'DebuffProb' }) * Func304(*a, **{
'sAttr': 'DebuffFactor' }) // 100000) * Func518(*a, **{
'sAttr': 'p51326_ExtraAddRatio' })), int(Func518(*a, **{
'sAttr': 'p51326_ExtAddMax' })))))
            cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()), DEPUTY_HOLD, 0)
        else:
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func518(*a, **{
'sAttr': 'p51326_BaseAdd' })))
            cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()), DEPUTY_HOLD, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckWeaponElementTypeByHoldType(oTarget, oEventCB, DEPUTY_HOLD, DAM_TYPE_FIRE) or cl_evcon.CheckWeaponElementTypeByHoldType(oTarget, oEventCB, DEPUTY_HOLD, DAM_TYPE_THUNDER) or cl_evcon.CheckWeaponElementTypeByHoldType(oTarget, oEventCB, DEPUTY_HOLD, DAM_TYPE_CORRISION):
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func518(*a, **{
'sAttr': 'p51326_BaseAdd' }) + min(int(ceil(Func785(*a, **{
'sAttr': 'DebuffProb' }) * Func304(*a, **{
'sAttr': 'DebuffFactor' }) // 100000) * Func518(*a, **{
'sAttr': 'p51326_ExtraAddRatio' })), int(Func518(*a, **{
'sAttr': 'p51326_ExtAddMax' })))))
        cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()), DEPUTY_HOLD, 0)
    else:
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func518(*a, **{
'sAttr': 'p51326_BaseAdd' })))
        cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()), DEPUTY_HOLD, 0)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckEventWeaponHoldType(oTarget, oEventCB, DEPUTY_HOLD):
        cl_action.CommonListenHoldWeaponMsg(oTarget, oEventCB.GetCBLifeCycle(), DEPUTY_HOLD, MSG_ITEM_REFRESHATTRIBUTE, 0)
        if cl_evcon.CheckWeaponElementTypeByHoldType(oTarget, oEventCB, DEPUTY_HOLD, DAM_TYPE_FIRE) or cl_evcon.CheckWeaponElementTypeByHoldType(oTarget, oEventCB, DEPUTY_HOLD, DAM_TYPE_THUNDER) or cl_evcon.CheckWeaponElementTypeByHoldType(oTarget, oEventCB, DEPUTY_HOLD, DAM_TYPE_CORRISION):
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func518(*a, **{
'sAttr': 'p51326_BaseAdd' }) + min(int(ceil(Func785(*a, **{
'sAttr': 'DebuffProb' }) * Func304(*a, **{
'sAttr': 'DebuffFactor' }) // 100000) * Func518(*a, **{
'sAttr': 'p51326_ExtraAddRatio' })), int(Func518(*a, **{
'sAttr': 'p51326_ExtAddMax' })))))
            cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()), DEPUTY_HOLD, 0)
        else:
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func518(*a, **{
'sAttr': 'p51326_BaseAdd' })))
            cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()), DEPUTY_HOLD, 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckEventWeaponHoldType(oTarget, oEventCB, DEPUTY_HOLD):
        cl_evact.EventCBClearExtGrade(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33684
    m_Name = '武器等级(副武器)'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

