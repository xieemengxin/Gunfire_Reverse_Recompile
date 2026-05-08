# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7979.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7979.pyc
# Source Generated with Decompyle++
# File: st7979.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_SCENE, DAM_TYPE_TRUE, DAM_USE_HP, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func205, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: (Func404(*a) // 2) * -500), 0, 1)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    cl_evact.StateCBAddTargetStatistics(oTarget, oEventCB, 'st7979', 1)
    if cl_evcon.StateCheckTargetStatistics(oTarget, oEventCB, 'st7979') >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func205(*a) * 2 + 4)):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
        cl_evact.EventTargetDamage(oTarget, oEventCB, 999999, DAM_TYPE_SCENE | DAM_TYPE_TRUE | DAM_USE_HP, 0, 0, 0, 0, None, None, None, None, None, None, None)
    cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


class CState(cl_state.CState):
    m_SID = 7979
    m_Name = '#NT#风神-龙卷风自动销毁'
    m_DieRemove = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 6
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

