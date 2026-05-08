# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7985.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7985.pyc
# Source Generated with Decompyle++
# File: st7985.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_commondefines import TYPE_RELIFE_PASS, STATE_CLS_ABNORMAL
import cl_state
from cl_commondefines import DAM_USE_SHIELD, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func423

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 6, 0, 0)
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 8008, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventChangeEnergy(oTarget, oEventCB, -3000)
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'ST7985')
    if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'ST7985') == 10 and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) == 0:
        if oTarget.HP() == 0 or cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) == 0:
            cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1)
            cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_HP_CHANGE, -1)
            cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 8005, 0, { }, None)
            CustomAction(oTarget, oEventCB, {
                'StateSID': 1009,
                'Time': 1840 })
        else:
            cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
            cl_action.CommonTriggerCG(oTarget.m_Game, 99, 1)
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.CommonRemoveAllStateByType(oTarget, oEventCB.GetCBLifeCycle(), STATE_CLS_ABNORMAL)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1009, 0, 0, { }, -1, None, None)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 8028, 885, 0, { }, -1, None, None)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 8029, 0, 0, { }, -1, None, None)
            cl_evact.EventGetHeroTarget(oTarget, oEventCB, 0, 1, 0, None)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1009, 930, 0, { }, -1, None, None)


def CallBack3(oEventCB, oTarget):
    if oTarget.Shield() > 0:
        cl_evact.EventCBConvertFamageToPoinType(oTarget, oEventCB, DAM_USE_SHIELD)


def CallBack5(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) == 0:
        cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1)
        cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_HP_CHANGE, -1)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 8005, 0, { }, None)
        CustomAction(oTarget, oEventCB, {
            'StateSID': 1009,
            'Time': 1840 })


def CallBack6(oEventCB, oTarget):
    if oTarget.Shield() > 0:
        cl_evact.EventCBConvertPredictDamToPoinType(oTarget, oEventCB, DAM_USE_SHIELD)
        if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 20030):
            cl_evact.EventCBReducePredictDam(oTarget, oEventCB, (lambda *a: Func423(*a) * 0.75), None)
        elif cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 20030):
            cl_evact.EventCBReducePredictDam(oTarget, oEventCB, (lambda *a: Func423(*a) * 0.75), None)


class CState(cl_state.CState):
    m_SID = 7985
    m_Name = '#NT#妖王-妖气散逆'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 99 }
    m_CBFuncAction = {
        1: CallBack1,
        3: CallBack3,
        5: CallBack5,
        6: CallBack6 }


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
    

