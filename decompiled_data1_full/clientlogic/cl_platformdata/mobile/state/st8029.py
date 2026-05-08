# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8029.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8029.pyc
# Source Generated with Decompyle++
# File: st8029.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_commondefines import TYPE_RELIFE_PASS, STATE_CLS_ABNORMAL
import cl_state
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_HP, DAM_USE_SHIELD, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 5, 0, 0)
    cl_action.CommonForceSetAttr(oTarget, oLifeCycle, 'ShieldMax', (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' })))
    cl_action.CommonPausePlayerStateCounter(oTarget, oLifeCycle, 950, 1005)


def CallBack3(oEventCB, oTarget):
    if oTarget.Shield() > 0:
        cl_evact.EventCBConvertFamageToPoinType(oTarget, oEventCB, DAM_USE_SHIELD)


def CallBack4(oEventCB, oTarget):
    if oTarget.Shield() == 0:
        cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1)


def CallBack5(oEventCB, oTarget):
    if oTarget.Shield() > 0:
        cl_evact.EventCBHaltFlow(oTarget, oEventCB)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, 100, CURE_TYPE_PERFORM | DAM_USE_HP, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 8029
    m_Name = '#NT#妖王-第六阶段'
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
        3: CallBack3,
        4: CallBack4,
        5: CallBack5 }


def CustomAction(oTarget, oEventCB, dInfo):
    oGame = oTarget.m_Game
    for iHero in oGame.m_WarMgr.GetRoomHero():
        oHero = oGame.GetObject(iHero)
        if not oHero:
            continue
        if oHero.IsDying():
            dReason = {
                'Type': TYPE_RELIFE_PASS }
            dRelife = {
                'HP': max(100, oHero.QueryAttr('HPMax') // 10),
                'Shield': 0,
                'Armor': 0 }
            oHero.Relife(dReason, dRelife)
        cl_action.CommonRemoveAllStateByType(oHero, oEventCB.GetCBLifeCycle(), STATE_CLS_ABNORMAL)
        cl_action.StateAddState(oHero, oEventCB.GetCBLifeCycle(), dInfo['StateSID'], dInfo['Time'], { })
    

