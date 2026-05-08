# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7143.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7143.pyc
# Source Generated with Decompyle++
# File: st7143.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        39137: 10,
        39138: 10 }, 1, 0):
        cl_evact.EventCBSaveMonsterStatePolicy(oTarget, oEventCB, 'qianxing')
        cl_evact.EventCBSetMonsterStatePolicy(oTarget, oEventCB, 'qianxing', {
            1: (100, 0, 0),
            2: (0, 0, 0) })
    elif cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 39141, 1, 0):
        cl_evact.EventCBRecoverMonsterStatePolicy(oTarget, oEventCB, 'qianxing')


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        39137: 10,
        39138: 10 }, 1, 0) and cl_evcon.EventCBGetCurCrtData(oTarget, oEventCB, 'TriggerTimes'):
        cl_evact.EventCBMonsterHaltPFGroup(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 7143
    m_Name = '#NT#轮回9鱼龙后裔尾部'
    m_DieRemove = 1
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
        2: CallBack2 }

