# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32742.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32742.pyc
# Source Generated with Decompyle++
# File: st32742.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func374

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 1, 0)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.CheckHasState(oTarget, oEventCB, 32743):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 8, WARRIOR_MONSTER, 1, 0, 0, 0, -1, None, None)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func374(*a) * 50 / 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_HP | DAM_USE_SHIELD | DAM_USE_ARMOR, 1, 0, 0, 0, 0, 1, 0, 0, None, None, None)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32743, 300, { }, None)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 32742
    m_Name = '#NT#劫后余波'
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
        0: CallBack0 }

