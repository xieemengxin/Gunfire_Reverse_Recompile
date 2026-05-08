# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7951.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7951.pyc
# Source Generated with Decompyle++
# File: st7951.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction7951 as CustomAction
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func378
from cl_only import PY_FLAG_EXCLUDEPRIORITYHATE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 0, 3)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func378(*a))) <= 0:
        cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DIE_BEFORE, -1)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if cl_evcon.CheckTargetPointBaseMonsters(oTarget, oEventCB, {
            2221: 1,
            2222: 1,
            2223: 1,
            2224: 1,
            2004: 1,
            3004: 1,
            2421: 1,
            2423: 1 }):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            if not cl_evcon.CheckDamFromSelf(oTarget, oEventCB, None):
                cl_action.CommonSetPyFlag(oTarget, oEventCB.GetCBLifeCycle(), PY_FLAG_EXCLUDEPRIORITYHATE, 1)
                CustomAction(oTarget, oEventCB, { })
                cl_evact.EventChangeHP(oTarget, oEventCB, 100)
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1445, 500, 0, { }, 0, 0, None)
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7952, 0, 0, { }, 0, None, None)
                cl_evact.EventCBAddTargetCustomData(oTarget, oEventCB, 'DelayedDeath', 1)
                cl_evact.EventCBHaltFlow(oTarget, oEventCB)
            else:
                cl_action.CommonSetPyFlag(oTarget, oEventCB.GetCBLifeCycle(), PY_FLAG_EXCLUDEPRIORITYHATE, 1)
                CustomAction(oTarget, oEventCB, { })
                cl_evact.EventChangeHP(oTarget, oEventCB, 100)
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1445, 500, 0, { }, 0, None, None)
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 7952, 0, 0, { }, 0, None, None)
                cl_evact.EventCBAddTargetCustomData(oTarget, oEventCB, 'DelayedDeath', 1)
                cl_evact.EventCBHaltFlow(oTarget, oEventCB)
        None.CommonForbidSpawnFlaw(oTarget, oEventCB.GetCBLifeCycle())
        cl_evact.EventCBTriggerKillEffect(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 7951
    m_Name = '#NT#不朽被动-延迟死亡'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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

