# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1867.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1867.pyc
# Source Generated with Decompyle++
# File: st1867.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_item.defines import MSG_ITEM_REFRESHATTRIBUTE
from cl_newformula import Func404, Func409

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 1, 0, 0)
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 2, 0, 0)
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 4, 0, 0)
    cl_action.CommonWeaponMsgCallBack(oTarget, oLifeCycle, MSG_ITEM_REFRESHATTRIBUTE, 5, 0, 1)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 6, 0, 0)


def CallBack1(oEventCB, oTarget):
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_evcon.EventCBCheckTargetCDByMark(oTarget, oEventCB, 'State1867', None) == 0:
        cl_evact.EventCBAddTargetCDByMark(oTarget, oEventCB, 'State1867', 100, None)
        cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 1867, 10, 0, 0, 1000)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 1867, 5, 0, 0, 1000)
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func404(*a) * 75), DAM_TYPE_WEAPON, '')


def CallBack5(oEventCB, oTarget):
    if cl_evcon.EventCBCheckItemRefreshAttribute(oTarget, oEventCB, 'MaxBullet'):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 1867, (lambda *a: Func409(*a)), 0, None)


def CallBack6(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 1867, (lambda *a: Func409(*a)), 0, None)


class CState(cl_state.CState):
    m_SID = 1867
    m_Name = '弹夹连结'
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
        1: CallBack1,
        2: CallBack2,
        4: CallBack4,
        5: CallBack5,
        6: CallBack6 }

