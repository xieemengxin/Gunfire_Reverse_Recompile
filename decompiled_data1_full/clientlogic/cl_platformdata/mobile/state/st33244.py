# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33244.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33244.pyc
# Source Generated with Decompyle++
# File: st33244.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_REFRESHORSYNC_SAMEITEM, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
    cl_action.StateChangeSourceWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'LuckyHit', (lambda *a: 20 * Func404(*a)), 0)
    if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL)


class CState(cl_state.CState):
    m_SID = 33244
    m_Name = '#NT#法杖专属铭刻2幸运一击加成'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC_SAMEITEM
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
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

