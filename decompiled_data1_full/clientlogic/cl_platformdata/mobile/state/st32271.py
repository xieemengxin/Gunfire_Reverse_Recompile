# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32271.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32271.pyc
# Source Generated with Decompyle++
# File: st32271.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_SELF, PF_TYPE_CONSHOOT, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func331

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPFReason(oTarget, oEventCB):
        if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, None):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func331(*a, **{
'sid': 2308 }) * 7500 + 7500), 0, DAM_TYPE_WEAPON, '')
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        else:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
            cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func331(*a, **{
'sid': 2308 }) * 7500 + 7500), 0, DAM_TYPE_WEAPON, None, 0)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func331(*a, **{
'sid': 2308 }) * 7500 + 7500), 0, DAM_TYPE_WEAPON, '')
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 32271
    m_Name = '#NT#亿万伏特'
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
        0: CallBack0 }

