# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8014.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8014.pyc
# Source Generated with Decompyle++
# File: st8014.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PF_SUBMSG_THROW, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func538

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDPERFORMCD, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'REnergy', 0, 3000, -1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 2, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 217):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, None)
        cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDPERFORMCD, -1, 3)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBSetCurPerformCD(oTarget, oEventCB, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventReduceBulletUse(oTarget, oEventCB, 1011)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventChangeEnergy(oTarget, oEventCB, (lambda *a: Func538(*a)))


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        7150: 1,
        7151: 1 }, 0, 0):
        cl_evact.EventCBSetCurPerformCD(oTarget, oEventCB, 0)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventGetTargetByServant(oTarget, oEventCB)
    cl_evact.EventCBSubTargetPerformColdTime(oTarget, oEventCB, 7151, 0, 10000)
    cl_evact.EventCBSubTargetPerformColdTime(oTarget, oEventCB, 7150, 0, 10000)


class CState(cl_state.CState):
    m_SID = 8014
    m_Name = '#NT#妖王-逆散期间无限技能'
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
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

