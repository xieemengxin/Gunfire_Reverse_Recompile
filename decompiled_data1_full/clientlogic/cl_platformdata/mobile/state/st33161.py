# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33161.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33161.pyc
# Source Generated with Decompyle++
# File: st33161.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_SPECIAL, STATE_EFF_NONE, TYPE_RELIFE_PASSIVE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetSceneMonsterCnt(oTarget, oEventCB, 1) <= 30:
        cl_action.CommonSetRelifeAttr(oTarget, oEventCB.GetCBLifeCycle(), TYPE_RELIFE_PASSIVE, 700, 1, 1, {
            'Elite': 100,
            'Normal': 100 }, 1, None)


def CallBack1(oEventCB, oTarget):
    cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RELIFE, -1)
    cl_action.CommonClearSuperMonster(oTarget, oEventCB.GetCBLifeCycle())


class CState(cl_state.CState):
    m_SID = 33161
    m_Name = '#NT#妖化增幅-轮回不止'
    m_Type = STATE_CLS_SPECIAL
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
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

