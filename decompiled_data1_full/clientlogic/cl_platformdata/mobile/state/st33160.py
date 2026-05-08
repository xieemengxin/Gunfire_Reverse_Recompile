# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33160.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33160.pyc
# Source Generated with Decompyle++
# File: st33160.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, DAM_USE_HP, HP_TYPE_ARMOR, HP_TYPE_NORMAL, HP_TYPE_SHIELD, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' })), 1, DAM_USE_HP)
    cl_action.CommonChangeElementDam(oTarget, oLifeCycle, DAM_TYPE_FIRE, {
        HP_TYPE_SHIELD: -2500,
        HP_TYPE_ARMOR: -2500 })
    cl_action.CommonChangeElementDam(oTarget, oLifeCycle, DAM_TYPE_CORRISION, {
        HP_TYPE_SHIELD: -2500,
        HP_TYPE_NORMAL: -2500 })
    cl_action.CommonChangeElementDam(oTarget, oLifeCycle, DAM_TYPE_THUNDER, {
        HP_TYPE_NORMAL: -2500,
        HP_TYPE_ARMOR: -2500 })


class CState(cl_state.CState):
    m_SID = 33160
    m_Name = '#NT#妖化增幅-元素抵抗'
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

