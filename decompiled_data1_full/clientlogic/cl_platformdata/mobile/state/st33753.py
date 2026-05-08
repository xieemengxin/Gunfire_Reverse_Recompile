# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33753.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33753.pyc
# Source Generated with Decompyle++
# File: st33753.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func538

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 0, 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': oLifeCycle.m_Owner.GetArgValue('DamRatio') })
    cl_action.StateSetArgValue(oTarget, oLifeCycle, 'CurCostEnergy', 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oTarget, oLifeCycle, 0, (lambda *a: oLifeCycle.m_Owner.GetArgValue('DamRatio') * Func404(*a)), 0, 1)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBAddStateArgVal(oTarget, oEventCB, 33753, 'CurCostEnergy', (lambda *a: Func538(*a)))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CurCostEnergy') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('EnergyCondition'):
        cl_evact.EventCBSetStateArgVal(oTarget, oEventCB, 33753, 'CurCount', oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CurCostEnergy') // oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('EnergyCondition'))
        cl_evact.EventCBAddStateArgVal(oTarget, oEventCB, 33753, 'CurCostEnergy', -oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CurCount') * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('EnergyCondition'))
        cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33753, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CurCount'), oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('EffectTime'))


class CState(cl_state.CState):
    m_SID = 33753
    m_Name = '燃元破势'
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

