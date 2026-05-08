# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32384.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32384.pyc
# Source Generated with Decompyle++
# File: st32384.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, STATE_ADD_HIGH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func432, Func514

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, (lambda *a: (Func514(*a, **{
'sAttr': 'DamReduce' }) * (Func514(*a, **{
'sAttr': 'GainEffect' }) + 10000) / 10000) * (100 + Func514(*a, **{
'sAttr': 'StatusEffect' })) / 100), None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.StateAddState(oTarget, oLifeCycle, 32453, (lambda *a: Func432(*a)), { }, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, (lambda *a: -Func404(*a)), 0, 0, '')


class CState(cl_state.CState):
    m_SID = 32384
    m_Name = '#NT#肾上腺素-伤害减免'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_HIGH
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

