# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1742.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1742.pyc
# Source Generated with Decompyle++
# File: st1742.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateShareTreasureRelicRoomCnt(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'HPMax', (lambda *a: Func404(*a) * 250), 0, -1)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ArmorMax', (lambda *a: Func404(*a) * 250), 0, -1)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ShieldMax', (lambda *a: Func404(*a) * 250), 0, -1)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: Func404(*a) * 200), 0, -1)
    cl_action.StateRefreshMonsterRelicCnt(oTarget, oLifeCycle, 25726)


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * 300), 0, 0, '')


class CState(cl_state.CState):
    m_SID = 1742
    m_Name = '#NT#双刃之剑（怪物遗物）'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 20
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
        0: CallBack0 }

