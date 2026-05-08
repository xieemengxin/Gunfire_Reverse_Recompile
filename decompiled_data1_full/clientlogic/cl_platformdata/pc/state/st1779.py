# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1779.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1779.pyc
# Source Generated with Decompyle++
# File: st1779.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func410

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        12014: 1 }, -1, -1):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: (2 ** Func410(*a, **{
'sid': 1725 }) - Func410(*a, **{
'sid': 1725 })) * 10))
        cl_action.CommonSendNotify(oTarget, oEventCB.GetCBLifeCycle(), 0, 9407, {
            '$cur': cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) })


class CState(cl_state.CState):
    m_SID = 1779
    m_Name = '#NT#黄金精英怪虚弱计数'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
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

