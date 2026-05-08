# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7162.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7162.pyc
# Source Generated with Decompyle++
# File: st7162.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_SPECIAL, STATE_EFF_NONE
from cl_newformula import Func304, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if oTarget.Armor() > 0:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'StoreArmor', (lambda *a: Func304(*a, **{
'sAttr': 'Armor' })))
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventChangeArmor(oTarget, oEventCB, (lambda *a: -Func437(*a, **{
'sKey': 'StoreArmor' })))
        cl_evact.DelayTriggerGroup(oTarget, oEventCB, 1, 1, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('KeepTime'), 0, 0, { })


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventChangeArmor(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'StoreArmor' })))
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 7162
    m_Name = '#NT#精英冲锋怪护甲破碎及延迟恢复'
    m_Type = STATE_CLS_SPECIAL
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
        0: CallBack0,
        1: CallBack1 }

