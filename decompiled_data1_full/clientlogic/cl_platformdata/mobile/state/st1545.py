# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1545.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1545.pyc
# Source Generated with Decompyle++
# File: st1545.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_USE_HP, OBJ_ATTACK, OBJ_SELF, STATE_ADD_LONG, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', 3000, 0, -1)


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 3 / 100 + 0), 0, DAM_USE_HP)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 3000, 0, 0, '')


class CState(cl_state.CState):
    m_SID = 1545
    m_Name = '#NT#团队之光状态'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_LONG
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100 }
    m_CBFuncAction = {
        0: CallBack0 }

