# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1772.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1772.pyc
# Source Generated with Decompyle++
# File: st1772.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_CORRISION, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def DelayAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 0:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, -1, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func404(*a) * 2000 + 0), DAM_TYPE_WEAPON | DAM_TYPE_CORRISION | DAM_USE_ALL, 1, 1, 0, 0, 1, 1, 1, 0, None, None, None)
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1772
    m_Name = '铭刻13062特效'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 50000
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
        'delay': 70,
        'firsttime': 70,
        'cnt': 1 }
    m_CBFuncAction = {
        0: CallBack0 }

