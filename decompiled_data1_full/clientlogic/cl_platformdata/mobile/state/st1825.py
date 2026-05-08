# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1825.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1825.pyc
# Source Generated with Decompyle++
# File: st1825.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import INSCRIPTION_TYPE_EXCLUSIVE, INSCRIPTION_TYPE_GEMINI, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func402, Func404

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func402(*a))) == 1:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPON_BEFORECREATE, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_GREATEWEAPON, -1, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DROPWEAPON, -1, 5, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPON_BEFORECREATE, -1, 6, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_GREATEWEAPON, -1, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBTempOpenWeaponExclusiveIns(oTarget, oEventCB, 2)
    cl_evact.EventCBTempChangeWeaponInsNumUpperLimit(oTarget, oEventCB, 4)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, cl_evcon.GetDropWeaponExclusiveInscriptionNum(oTarget, oEventCB, 0))
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a))) < 2:
        if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func402(*a))) == 1:
            cl_evact.EventCBRandomAddInscriptionByExcType(oTarget, oEventCB, (lambda *a: 2 - Func404(*a)), {
                INSCRIPTION_TYPE_GEMINI: 1,
                INSCRIPTION_TYPE_EXCLUSIVE: 1 })
        else:
            cl_evact.EventCBAddInscriptionByType(oTarget, oEventCB, (lambda *a: 2 - Func404(*a)), INSCRIPTION_TYPE_EXCLUSIVE)
        if cl_evcon.GetDropWeaponExclusiveInscriptionNum(oTarget, oEventCB, INSCRIPTION_TYPE_EXCLUSIVE) < 2:
            cl_evact.EventCBChangeWeaponInscriptionNumBySource(oTarget, oEventCB, INSCRIPTION_TYPE_EXCLUSIVE, 2, {
                0: 1,
                1: 1,
                2: 1,
                3: 1,
                4: 1,
                5: 1,
                6: 1 }, INSCRIPTION_TYPE_EXCLUSIVE)
        elif cl_evcon.GetDropWeaponExclusiveInscriptionNum(oTarget, oEventCB, INSCRIPTION_TYPE_EXCLUSIVE) < 2:
            cl_evact.EventCBChangeWeaponInscriptionNumBySource(oTarget, oEventCB, INSCRIPTION_TYPE_EXCLUSIVE, 2, {
                0: 1,
                1: 1,
                2: 1,
                3: 1,
                4: 1,
                5: 1,
                6: 1 }, INSCRIPTION_TYPE_EXCLUSIVE)


def CallBack5(oEventCB, oTarget):
    cl_evact.EventCBRemoveTempWeaponInsNumUpperLimit(oTarget, oEventCB)
    cl_evact.EventCBRemoveTempOpenWeaponExclusiveIns(oTarget, oEventCB)


def CallBack6(oEventCB, oTarget):
    cl_evact.EventCBTempOpenWeaponExclusiveIns(oTarget, oEventCB, 3)


class CState(cl_state.CState):
    m_SID = 1825
    m_Name = '#NT#匠心独运'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 10
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
        1: CallBack1,
        5: CallBack5,
        6: CallBack6 }

