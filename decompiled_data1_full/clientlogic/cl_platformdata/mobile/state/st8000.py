# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8000.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8000.pyc
# Source Generated with Decompyle++
# File: st8000.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_SHIELD, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckMonsterPhase(oTarget, oEventCB, 6):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' }) * 0.3), CURE_TYPE_PERFORM | DAM_USE_SHIELD, -1, -1, 0)
    else:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 0.3), -1)


class CState(cl_state.CState):
    m_SID = 8000
    m_Name = '#NT#妖王-防御'
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

