# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st39746.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st39746.pyc
# Source Generated with Decompyle++
# File: st39746.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_PET, WARRIOR_SERVANT
from cl_item.defines import MSG_ITEM_REFRESHATTRIBUTE
from cl_newformula import Func756

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonCreateHeroSidePet(oTarget, oLifeCycle, 2084, 0, {
        'WeaponCreate': 1 }, 1, None, { }, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonWeaponMsgCallBack(oTarget, oLifeCycle, MSG_ITEM_REFRESHATTRIBUTE, 4, 0, 1)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckDamFromFightTypeInRange(oTarget, oEventCB, {
        WARRIOR_SERVANT: 1,
        WARRIOR_PET: 1 }, 1) and cl_evcon.CheckRandom(oTarget, oEventCB, 100, 50):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBTargetPosSummonSoul(oTarget, oEventCB, {
            'AddSoulValue': 3000,
            'Perform': 9796 })


def CallBack2(oEventCB, oTarget):
    if cl_evcon.EventCBCheckDamFromFightTypeInRange(oTarget, oEventCB, {
        WARRIOR_SERVANT: 1,
        WARRIOR_PET: 1 }, 1):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 39752, 1, 1, 0, 0) and cl_evcon.CheckRandom(oTarget, oEventCB, 100, 10):
            cl_evact.EventCBTargetPosSummonSoul(oTarget, oEventCB, {
                'AddSoulValue': 10000,
                'Perform': 9796 })


def CallBack4(oEventCB, oTarget):
    if cl_evcon.EventCBCheckItemRefreshAttribute(oTarget, oEventCB, 'AttSpeed'):
        cl_evact.StateCBSetHeroSidePetAttr(oTarget, oEventCB, 2084, 'AttSpeed', (lambda *a: 10000 // Func756(*a, **{
'sAttr': 'AttSpeed' })))


def CallBack5(oEventCB, oTarget):
    cl_evact.StateCBSetHeroSidePetAttr(oTarget, oEventCB, 2084, 'AttSpeed', (lambda *a: 10000 // Func756(*a, **{
'sAttr': 'AttSpeed' })))


class CState(cl_state.CState):
    m_SID = 39746
    m_Name = '#NT#召唤法杖初始状态'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
        2: CallBack2,
        4: CallBack4,
        5: CallBack5 }

