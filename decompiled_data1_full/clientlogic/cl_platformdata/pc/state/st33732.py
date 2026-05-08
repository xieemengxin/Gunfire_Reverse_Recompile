# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33732.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33732.pyc
# Source Generated with Decompyle++
# File: st33732.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction33732_0 as CustomAction0, CustomAction33732_1 as CustomAction1, CustomAction33732_2 as CustomAction2, CustomAction33732_3 as CustomAction3
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WANDCOMP_SUBMSG_ADD, WANDCOMP_SUBMSG_REMOVE, WAND_SUBMSG_ADD, WAND_SUBMSG_EXTACTIONSLOT, WAND_SUBMSG_UPGRADE
from cl_newformula import Func793

def StateActAction(oTarget, oLifeCycle):
    CustomAction1(oTarget, oLifeCycle, { })
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_ADD, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_REMOVE, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCHANGE, WAND_SUBMSG_ADD, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_EXTACTIONSLOT, 6, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCHANGE, WAND_SUBMSG_UPGRADE, 6, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'WandSID') == 1022 and cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'CompType') == 0:
        cl_evact.EventCBSetWandExtActionCompNum(oTarget, oEventCB, (lambda *a: Func793(*a)), 1)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'WandSID') == 1022:
        cl_evact.EventCBSetWandExtActionCompNum(oTarget, oEventCB, (lambda *a: Func793(*a)), 1)
        CustomAction0(oTarget, oEventCB, { })


def CallBack2(oEventCB, oTarget):
    if cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'WandSID') == 1022:
        if cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'CompType') == 0:
            cl_evact.EventCBSetWandExtActionCompNum(oTarget, oEventCB, (lambda *a: Func793(*a)), 1)
        else:
            CustomAction2(oTarget, oEventCB, {
                'AddComp': 1 })


def CallBack3(oEventCB, oTarget):
    if cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'WandSID') == 1022:
        if cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'CompType') == 0:
            cl_evact.EventCBSetWandExtActionCompNum(oTarget, oEventCB, (lambda *a: Func793(*a)), 1)
        else:
            CustomAction2(oTarget, oEventCB, { })


def CallBack6(oEventCB, oTarget):
    CustomAction3(oTarget, oEventCB, { })


class CState(cl_state.CState):
    m_SID = 33732
    m_Name = '#NT#搭配法杖管理状态'
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
        2: CallBack2,
        3: CallBack3,
        6: CallBack6 }

