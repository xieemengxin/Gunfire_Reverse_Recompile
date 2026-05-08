# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33529.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33529.pyc
# Source Generated with Decompyle++
# File: st33529.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, PF_TYPE_CONSHOOT, STATE_ADD_LONGORSYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func619

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func619(*a, **{
'sAttr': 'StateCount' })))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0):
        cl_evact.EventChangeSkillCache(oTarget, oEventCB, 'LuckyHit', (lambda *a: 80 * Func404(*a)), 0)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0):
        cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, (lambda *a: 80 * Func404(*a)))
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33529
    m_Name = '幸运弹丸'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_LONGORSYNC
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
        1: CallBack1 }

