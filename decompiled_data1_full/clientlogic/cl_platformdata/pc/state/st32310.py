# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32310.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32310.pyc
# Source Generated with Decompyle++
# File: st32310.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func331

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 32311, 0, 1, None, None):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2406) == 3:
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 12000, DAM_TYPE_WEAPON, '')
        else:
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func331(*a, **{
'sid': 2406 }) * 3000 + 3000), DAM_TYPE_WEAPON, '')


def CallBack4(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 32311, 0, 1, None, None):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2406) == 3:
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32375, 500, 0, { }, 0, None, None)


class CState(cl_state.CState):
    m_SID = 32310
    m_Name = '#NT#狂怒标记'
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
        4: CallBack4 }

