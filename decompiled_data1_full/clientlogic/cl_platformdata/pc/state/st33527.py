# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33527.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33527.pyc
# Source Generated with Decompyle++
# File: st33527.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func208, Func215, Func402

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func402(*a))) == 3:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, -1, 2, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, -1, 2, 0, 0)
    cl_action.CommonSetWandMaxCount(oTarget, oLifeCycle, 200)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, 0, 0)


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.CheckCostBulletType(oTarget, oEventCB, 4508):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func208(*a)), None)


def CallBack2(oEventCB, oTarget):
    if not cl_evcon.CheckCostBulletType(oTarget, oEventCB, 4508):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func215(*a)), None)


def CallBack3(oEventCB, oTarget):
    if cl_condition.RandomTrigger(oTarget, oEventCB.GetCBLifeCycle(), 100, 50):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func208(*a)), None)
    else:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func208(*a) * 2), None)


def CallBack4(oEventCB, oTarget):
    if cl_condition.RandomTrigger(oTarget, oEventCB.GetCBLifeCycle(), 100, 50):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func215(*a)), None)
    else:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func215(*a) * 2), None)


def CallBack5(oEventCB, oTarget):
    cl_evact.EventCBSetWandCount(oTarget, oEventCB, cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()))


class CState(cl_state.CState):
    m_SID = 33527
    m_Name = '电弧令牌'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 200
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5 }

