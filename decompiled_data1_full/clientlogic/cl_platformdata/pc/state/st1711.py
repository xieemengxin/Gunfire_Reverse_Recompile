# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1711.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1711.pyc
# Source Generated with Decompyle++
# File: st1711.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventChangeShield(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' }) * 100 / 100))
    cl_evact.EventChangeArmor(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ArmorMax' }) * 100 / 100))
    cl_evact.EventChangeHP(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 100 / 100))
    cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1717, 100, { }, None)
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1711
    m_Name = '#NT#复原灵龛（怪物遗物）'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 4,
        'firsttime': 400,
        'cnt': 1 }
    m_CBFuncAction = {
        0: CallBack0 }

