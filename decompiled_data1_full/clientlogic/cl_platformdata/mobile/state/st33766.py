# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33766.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33766.pyc
# Source Generated with Decompyle++
# File: st33766.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import MAIN_SKILL_DURATION_BEGIN, MAIN_SKILL_DURATION_END, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func410, Func822

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 1330, 'ExplodeDelay', 0, 75)
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 1336, 'ExplodeDelay', 0, 75)
    cl_action.CommonSendMessage(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_BEGIN, {
        'StateSID': 33766 })
    cl_action.CommonSendStateStartMessage(oTarget, oLifeCycle, 1, 0)
    cl_action.CommonChangeAttrFixedAddition(oTarget, oLifeCycle, 'HPMax', (lambda *a: Func822(*a, **{
'sAttr': 'HPMax' })))


def StateRemoveAction(oTarget, oLifeCycle):
    if cl_condition.HasState(oTarget, oLifeCycle, 33604):
        cl_action.StateAddState(oTarget, oLifeCycle, 33711, 300, {
            'Att': (lambda *a: Func410(*a, **{
'sid': 33838 }) * 5000),
            'TransDamFactor': cl_action.StateGetSelfTransDamFactor(oTarget, oLifeCycle) }, 0)
        cl_action.CommonSetStateCount(oTarget, oLifeCycle, 33838, 0, 0)
    cl_action.CommonSendMessage(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_END, {
        'StateSID': 33766 })
    cl_action.CommonSendStateMessage(oTarget, oLifeCycle, 1, { })


class CState(cl_state.CState):
    m_SID = 33766
    m_Name = '无双'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 2
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)

