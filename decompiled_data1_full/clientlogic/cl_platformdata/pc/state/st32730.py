# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32730.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32730.pyc
# Source Generated with Decompyle++
# File: st32730.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func333, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 1411, 'Att', 0, (lambda *a: Func404(*a) * 100))


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1411, 0, 0):
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, (lambda *a: Func333(*a) * 10000), DAM_TYPE_PERFORM, None, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckStateAddByIs(oTarget, oEventCB, None) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1411, 0, 1):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 2, None)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 32904, -1, 1, 0, 0):
            cl_evact.StateAddSelfCount(oTarget, oEventCB, 2, None)


class CState(cl_state.CState):
    m_SID = 32730
    m_Name = '残羹盛宴(灵界狂潮)'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 3000
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

