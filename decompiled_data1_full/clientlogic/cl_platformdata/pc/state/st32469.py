# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32469.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32469.pyc
# Source Generated with Decompyle++
# File: st32469.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import COST_BAGBULLET_WEAPON, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func208, Func215, Func402

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckCostBulletType(oTarget, oEventCB, 4504):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func208(*a)), None)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: 35 - Func402(*a) * 5)):
            cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func402(*a) * 5 - 35), None)
            cl_action.CommonAddThrowBagBullet(oTarget, oEventCB.GetCBLifeCycle(), 1, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckCostBulletType(oTarget, oEventCB, 4504):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func215(*a)), None)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: 35 - Func402(*a) * 5)):
            cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func402(*a) * 5 - 35), None)
            cl_action.CommonAddThrowBagBullet(oTarget, oEventCB.GetCBLifeCycle(), 1, 0)


class CState(cl_state.CState):
    m_SID = 32469
    m_Name = '#NT#战地补给-特种弹'
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
        1: CallBack1 }

