# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1259.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1259.pyc
# Source Generated with Decompyle++
# File: st1259.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_HP, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func304

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetListenerHPRatio(oTarget, oEventCB) > 1:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 1 / 100 + 0), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_HP, 1, 0, 1, 0, None, None, None, None, None, None, None)


class CState(cl_state.CState):
    m_SID = 1259
    m_Name = '#NT#每日试炼4643每秒掉血'
    m_IsShow = 1
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0 }

