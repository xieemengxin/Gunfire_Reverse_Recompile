# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33081.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33081.pyc
# Source Generated with Decompyle++
# File: st33081.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ATTACK, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_COUNT_MAX, STATE_EFF_NONE
from cl_newformula import Func402, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeStateAttr(oTarget, oLifeCycle, 0, (lambda *a: 80 + 80 * Func402(*a)), STATE_COUNT_MAX, 1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORMED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1918: 1,
        1921: 1,
        1920: 1,
        1326: 1 }, -1, -1):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func404(*a) * 100), 0, '')
        if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
            1326: 1 }, -1, -1) == 0:
            cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: 10 + 10 * Func402(*a)), None)


class CState(cl_state.CState):
    m_SID = 33081
    m_Name = '#NT#水墨大师E4敌方效果'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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

