# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33571.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33571.pyc
# Source Generated with Decompyle++
# File: st33571.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, COMMONACTIVE_TAG_SEASONWAND, DAM_MASK_ELEMENT, MAF_TYPE_SEASONWAND, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_ELITE
from cl_newformula import Func404, Func410

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func410(*a, **{
'sid': 33618 })))


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckPerfromInActivePerformTag(oTarget, oEventCB, COMMONACTIVE_TAG_SEASONWAND):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func404(*a) * 300 + 10000), DAM_MASK_ELEMENT, '')


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasAfPFType(oTarget, oEventCB, MAF_TYPE_SEASONWAND):
        if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_ELITE):
            cl_evact.StateAddSelfCount(oTarget, oEventCB, 25, None)
        else:
            cl_evact.StateAddSelfCount(oTarget, oEventCB, 2, None)


class CState(cl_state.CState):
    m_SID = 33571
    m_Name = '威能令珏'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 100
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

