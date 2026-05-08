# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32312.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32312.pyc
# Source Generated with Decompyle++
# File: st32312.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import EQUIP_TYPE_CLOSEWEAPON, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func310

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_TYPE_CLOSEWEAPON) == 0:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            3: 2000 }, None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_TYPE_CLOSEWEAPON):
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            3: 2000 }, None)


def CallBack2(oEventCB, oTarget):
    cl_evact.CBTriggerGroup(oTarget, oEventCB, {
        3: 2000 }, None)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventReduceBulletUse(oTarget, oEventCB, 0)
    cl_evact.EventCBAddHoldWeaponComBullet(oTarget, oEventCB, (lambda *a: max(int(Func310(*a) * 1 + 0 + 0), 1)), 0)


class CState(cl_state.CState):
    m_SID = 32312
    m_Name = '#NT#无中生有'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
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

