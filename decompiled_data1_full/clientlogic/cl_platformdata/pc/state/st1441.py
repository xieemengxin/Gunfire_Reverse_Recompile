# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1441.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1441.pyc
# Source Generated with Decompyle++
# File: st1441.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, OBJ_FRIEND, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func357

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUREED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckTotalCureSource(oTarget, oEventCB, 1069, DAM_USE_HP):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventGetHeroTarget(oTarget, oEventCB, 1, 1, 1, 0)
        cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 1)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1442, 0, 0, None, None):
        if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 1442, 0, None) == 0:
            cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func357(*a) * 25 / 100), CURE_TYPE_PERFORM | DAM_USE_SHIELD | DAM_USE_ARMOR, 0, 1, None)
        else:
            cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func357(*a) * 25 / 100), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, None)


class CState(cl_state.CState):
    m_SID = 1441
    m_Name = '#NT#强化有福同享'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_FRIEND
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

