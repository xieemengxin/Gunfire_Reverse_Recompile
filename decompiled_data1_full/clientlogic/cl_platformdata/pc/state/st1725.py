# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1725.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1725.pyc
# Source Generated with Decompyle++
# File: st1725.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_SCENE, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func224, Func404, Func557

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        12014: 1 }, -1, -1):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func224(*a))) < 3:
            cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func557(*a) * (20 - (Func224(*a) - 1) * 5) / 100), DAM_TYPE_SCENE | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, 0, 0, 0, 0, 0, None, None, None)
        else:
            cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func557(*a) * 10 / 100), DAM_TYPE_SCENE | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, 0, 0, 0, 0, 0, None, None, None)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: (2 ** Func404(*a) - Func404(*a)) * 1000), 0, 0, '')
    else:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: (2 ** Func404(*a) - Func404(*a)) * 1000), 0, 0, '')


class CState(cl_state.CState):
    m_SID = 1725
    m_Name = '#NT#黄金精英怪虚弱'
    m_DieRemove = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 4
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

