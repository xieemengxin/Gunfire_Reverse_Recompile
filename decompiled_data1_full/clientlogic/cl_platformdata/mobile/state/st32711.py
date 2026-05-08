# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32711.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32711.pyc
# Source Generated with Decompyle++
# File: st32711.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_PERFORM, OBJ_ENEMY, OBJ_VICTIM, STATE_ADD_SYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORMED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckStateAddByIs(oTarget, oEventCB, None) and cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1422: 1,
        1709: 1,
        1430: 1 }, 1, 0):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, (lambda *a: Func404(*a) * 3000), 0, DAM_TYPE_PERFORM, '')


class CState(cl_state.CState):
    m_SID = 32711
    m_Name = '#NT#通灵重击1（怪物）'
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
    m_TargetType = OBJ_ENEMY
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

