# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1164.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1164.pyc
# Source Generated with Decompyle++
# File: st1164.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHitWeakness(oTarget, oEventCB, None) and cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
        cl_evact.StateAddSelfCountByFinalDamage(oTarget, oEventCB, 100, 1)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1619, 0, None):
        cl_evact.EventChangeSkillCache(oTarget, oEventCB, 'Att', 0, -10000)
        cl_evact.EventChangeSkillCache(oTarget, oEventCB, 'Att', (lambda *a: Func404(*a) * 1 + 0), 0)


class CState(cl_state.CState):
    m_SID = 1164
    m_Name = '#NT#铭刻4914'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 1000000
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

