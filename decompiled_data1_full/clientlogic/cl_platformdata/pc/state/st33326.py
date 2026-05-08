# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33326.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33326.pyc
# Source Generated with Decompyle++
# File: st33326.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_CORRISION, DAM_TYPE_ELEMENT, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, oLifeCycle.m_Owner.GetArgValue('StateCount'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromCareerPerform(oTarget, oEventCB) or cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1313: 1,
        8503: 1,
        1328: 1,
        1326: 1 }, 1, 0):
        cl_evact.EventSetSkillCache(oTarget, oEventCB, 'DebuffProb', 5000)
        if cl_evcon.CheckEleDamType(oTarget, oEventCB, DAM_TYPE_ELEMENT, 1) == 0:
            if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func404(*a))) <= 1:
                cl_evact.EventCBChangeEventPerformDamType(oTarget, oEventCB, DAM_TYPE_FIRE)
            elif cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func404(*a))) >= 3:
                cl_evact.EventCBChangeEventPerformDamType(oTarget, oEventCB, DAM_TYPE_THUNDER)
            else:
                cl_evact.EventCBChangeEventPerformDamType(oTarget, oEventCB, DAM_TYPE_CORRISION)


class CState(cl_state.CState):
    m_SID = 33326
    m_Name = '#NT#词条E1属性变更'
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

