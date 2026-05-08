# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1557.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1557.pyc
# Source Generated with Decompyle++
# File: st1557.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, LEVEL_TYPE_HIDE, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func207, Func364, Func404, Func545, Func707

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COSTWARCASH, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 2)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_UPDATE_STATECOUNTEFF, -1, 4, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBAddSavedData(oTarget, oEventCB, 'PF5850', (lambda *a: -Func364(*a)), 1)
    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: ((Func545(*a) - Func207(*a) - Func364(*a)) // 100) * Func707(*a)))


def CallBack1(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * 100), 0, 0, '')


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckEnterNewSecne(oTarget, oEventCB) and cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_HIDE) == 0 and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func207(*a))) > 500:
        cl_action.CommonAddWarCash(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: -(Func207(*a) - 500)))


def CallBack4(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: ((Func545(*a) - Func207(*a)) // 100) * Func707(*a)))


class CState(cl_state.CState):
    m_SID = 1557
    m_Name = '挥金如土'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 60000
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        4: CallBack4 }

