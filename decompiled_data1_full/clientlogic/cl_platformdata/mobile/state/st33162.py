# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33162.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33162.pyc
# Source Generated with Decompyle++
# File: st33162.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_HP, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func418

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 11, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 10, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetLiveMonsterPer(oTarget, oEventCB) >= 7500:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'HPMax', -2000, 0, 0)
        cl_action.CommonChangeBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, -2000, 0, 1)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 1000, 0, 0)
    elif cl_evcon.GetLiveMonsterPer(oTarget, oEventCB) >= 5500:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 1000, 0, 0)
    elif cl_evcon.GetLiveMonsterPer(oTarget, oEventCB) >= 3000:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'HPMax', 3000, 0, 0)
        cl_action.CommonChangeBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, 2000, 0, 1)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 2000, 0, 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1213, 0, 1, { }, 0, 0, 0)
    else:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'HPMax', 5000, 0, 0)
        cl_action.CommonChangeBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, 4000, 0, 1)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 3000, 0, 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1233, 0, 1, { }, 0, 0, 0)


def CallBack10(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func418(*a) * 13 / 100), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, 100)
    cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func418(*a) * 14 / 100), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, 200)
    cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func418(*a) * 16 / 100), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, 300)
    cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func418(*a) * 17 / 100), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, 400)


def CallBack11(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1208, 0, 1, { }, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 33162
    m_Name = '#NT#妖化增幅-愈挫愈勇'
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
    m_CBFuncAction = {
        0: CallBack0,
        10: CallBack10,
        11: CallBack11 }

