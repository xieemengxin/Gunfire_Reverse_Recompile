# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33785.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33785.pyc
# Source Generated with Decompyle++
# File: st33785.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('StateCount'))
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, oLifeCycle.m_Owner.GetArgValue('Cache'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSetSourceItemTmpData(oTarget, oLifeCycle, 'RecordCount', cl_action.StateGetSelfCount(oTarget, oLifeCycle))


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckVictimFightType(oTarget, oEventCB, WARRIOR_MONSTER):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oEventCB.GetCBLifeCycle()):
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
            cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33786, 1, 0)
            cl_action.CommonTriggerStateRefreshBehavior(oTarget, oEventCB.GetCBLifeCycle(), 33786, { }, 0, 0)


class CState(cl_state.CState):
    m_SID = 33785
    m_Name = '不息之力统计状态'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0 }

