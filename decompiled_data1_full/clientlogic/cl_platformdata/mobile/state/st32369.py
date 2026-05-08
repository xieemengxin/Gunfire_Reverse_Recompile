# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32369.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32369.pyc
# Source Generated with Decompyle++
# File: st32369.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func331

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ArmorMax', 0, (lambda *a: Func331(*a, **{
'sid': 2416 }) * 1200), None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if oTarget.Armor() > 0 and cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2416) == 3:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, -1000, 0, '')


class CState(cl_state.CState):
    m_SID = 32369
    m_Name = '#NT#钢筋铁骨'
    m_DieRemove = 1
    m_IsShow = 1
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

