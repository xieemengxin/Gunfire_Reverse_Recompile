# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1558.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1558.pyc
# Source Generated with Decompyle++
# File: st1558.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHitWeakness(oTarget, oEventCB, 0) and cl_evcon.EventCBGetSkillCacheBallisticType(oTarget, oEventCB) == 1 and cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a))) >= 2:
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1515, 1000, { }, None)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1759, 1000, { }, None)


class CState(cl_state.CState):
    m_SID = 1558
    m_Name = '#NT#电弧狙专属铭刻'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
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
        0: CallBack0 }

