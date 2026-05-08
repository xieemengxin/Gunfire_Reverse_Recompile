# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33259.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33259.pyc
# Source Generated with Decompyle++
# File: st33259.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_MASK_SRC, DAM_USE_HP, OBJ_SELF, PETPF_ACTIVE_ATTACK, PF_SUBMSG_PETACTIVE, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_PETACTIVE, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckPerformIsPetPerformType(oTarget, oEventCB, {
        PETPF_ACTIVE_ATTACK: 1 }):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, 10000, DAM_MASK_SRC, None, 0)


def CallBack1(oEventCB, oTarget):
    if oTarget.HP() > 10000:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventChangeDefValue(oTarget, oEventCB, (lambda *a: -max(int(Func304(*a, **{
'sAttr': 'HP' }) * 50 / 100), 10000)), DAM_USE_HP, 0)
    else:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventChangeDefValue(oTarget, oEventCB, (lambda *a: -Func304(*a, **{
'sAttr': 'HP' }) + 1), DAM_USE_HP, 0)


class CState(cl_state.CState):
    m_SID = 33259
    m_Name = '#NT#词条50525'
    m_Type = STATE_CLS_HELP
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
        0: CallBack0,
        1: CallBack1 }

