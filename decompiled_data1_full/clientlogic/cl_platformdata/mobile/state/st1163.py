# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1163.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1163.pyc
# Source Generated with Decompyle++
# File: st1163.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 1, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.EventChangeSkillCache(oTarget, oEventCB, 'LuckyHit', (lambda *a: Func404(*a) * 6), 0)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1163
    m_Name = '#NT#铭刻4934蓄力计数'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 25
    m_StartCount = 0
    m_PerCountTime = 4
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

