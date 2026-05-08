# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32402.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32402.pyc
# Source Generated with Decompyle++
# File: st32402.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_NORMAL, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 6, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a))) == 1:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1677, 0, None) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 2502, 0, None):
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 2500, DAM_TYPE_NORMAL, '')
        else:
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 1500, DAM_TYPE_NORMAL, '')
    elif cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a))) == 2:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1677, 0, None) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 2502, 0, None):
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 4000, DAM_TYPE_NORMAL, '')
        else:
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 2500, DAM_TYPE_NORMAL, '')
    elif cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a))) == 3:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1677, 0, None) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 2502, 0, None):
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 6000, DAM_TYPE_NORMAL, '')
        else:
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 4000, DAM_TYPE_NORMAL, '')


def CallBack6(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a))) == 1:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, -1500, 0, '')
    elif cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a))) == 2:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, -2500, 0, '')
    elif cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a))) == 3:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, -4000, 0, '')


class CState(cl_state.CState):
    m_SID = 32402
    m_Name = '#NT#破坏屏障标记'
    m_DieRemove = 1
    m_Type = STATE_CLS_ABNORMAL
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
        6: CallBack6 }

