# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32277.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32277.pyc
# Source Generated with Decompyle++
# File: st32277.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_NORMAL, DAM_TYPE_PERFORM, DAM_USE_ALL, OBJ_ENEMY, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func404, Func410

def DelayAction(oTarget, oLifeCycle):
    if cl_condition.HasState(oTarget, oLifeCycle, 32278):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)
    else:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func410(*a, **{
'sid': 32278 }) * Func404(*a) * 0.2), DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 0, 0, None, None, None, None, None, None, None, None)
    cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 32278, 0, None)


class CState(cl_state.CState):
    m_SID = 32277
    m_Name = '#NT#强力电流3级'
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 10,
        'firsttime': 40,
        'cnt': 1 }
    m_CBFuncAction = {
        0: CallBack0 }

