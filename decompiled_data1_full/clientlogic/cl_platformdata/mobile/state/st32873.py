# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32873.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32873.pyc
# Source Generated with Decompyle++
# File: st32873.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import COST_BAGBULLET_WEAPON, GAMBLER_CHOOSE_EQUITY, GAMBLER_REPLACE_DEFAULT, OBJ_SELF, QUALITY_TYPE_HIGH, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func208, Func215

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 1, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 40:
        cl_action.StateAddSelfCount(oTarget, oLifeCycle, -40, None)
        cl_action.CommonAppendQuality(oTarget, oLifeCycle, QUALITY_TYPE_HIGH, GAMBLER_CHOOSE_EQUITY, 0, 1, GAMBLER_REPLACE_DEFAULT, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckCostBulletType(oTarget, oEventCB, 4502):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func208(*a) * 1 + 0), None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckCostBulletType(oTarget, oEventCB, 4502):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func215(*a) * 1 + 0), None)


class CState(cl_state.CState):
    m_SID = 32873
    m_Name = '#NT#赌侠筹码兑换标准弹计数'
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

