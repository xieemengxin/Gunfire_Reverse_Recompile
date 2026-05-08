# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33693.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33693.pyc
# Source Generated with Decompyle++
# File: st33693.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction33693_0 as CustomAction0
from cl_platformdata.custom.state.customaction import CustomAction33693_1 as CustomAction1
from cl_platformdata.custom.state.customaction import CustomAction33693_2 as CustomAction2
from cl_platformdata.custom.state.customaction import CustomAction33693_3 as CustomAction3
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WAND_SUBMSG_ADD, WAND_SUBMSG_ADDABILITY, WAND_SUBMSG_REMOVE, WAND_SUBMSG_REMOVEABILITY

def StateActAction(oTarget, oLifeCycle):
    CustomAction2(oTarget, oLifeCycle, { })
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_ADDABILITY, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_REMOVEABILITY, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCHANGE, WAND_SUBMSG_ADD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCHANGE, WAND_SUBMSG_REMOVE, 1, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WARMGR_ADDPLAYER, -1, 2)


def CallBack0(oEventCB, oTarget):
    CustomAction0(oTarget, oEventCB, { })


def CallBack1(oEventCB, oTarget):
    CustomAction1(oTarget, oEventCB, { })


def CallBack2(oEventCB, oTarget):
    CustomAction3(oTarget, oEventCB, { })


class CState(cl_state.CState):
    m_SID = 33693
    m_Name = '#NT#槽位增加词条'
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
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

