# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1809.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1809.pyc
# Source Generated with Decompyle++
# File: st1809.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_MASK_CLASS, DAM_MASK_ELEMENT, LINK_DISCONNECT, LINK_ONLINE, LINK_QUIT, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func218, Func402, Func574

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func402(*a))) == 1:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, None)
        cl_action.CommonListenAllHeroMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 0, 1)
        cl_action.CommonListenAllHeroMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 1, 1)
        cl_action.CommonListenAllHeroMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 2, 0)
        cl_action.CommonListenAllHeroMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 2, 1)
        cl_action.CommonListenAllHeroMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 2, 1)
        cl_action.CommonListenGlobalMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, -1, 3)
        cl_action.CommonModifyDamResistance(oTarget, oLifeCycle, cl_action.StateGetSelfCount(oTarget, oLifeCycle) * 500 + 2500, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, 0, None)
        cl_action.CommonListenAllHeroMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 5, 0)
        cl_action.CommonListenAllHeroMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 5, 1)
        cl_action.CommonListenAllHeroMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 5, 1)
        cl_action.CommonListenGlobalMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, -1, 3)
        cl_action.CommonModifyDamResistance(oTarget, oLifeCycle, cl_action.StateGetSelfCount(oTarget, oLifeCycle) * 500 + 2500, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonModifyDamResistance(oTarget, oLifeCycle, cl_action.StateGetSelfCount(oTarget, oLifeCycle) * 500 + 2500, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPointRelic(oTarget, oEventCB, 5851):
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckPointRelic(oTarget, oEventCB, 5851):
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -1, None)


def CallBack2(oEventCB, oTarget):
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func574(*a, **{
'sid': 5851 }) - 1))


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckPlayerLinkStatus(oTarget, oEventCB, LINK_DISCONNECT, 0) or cl_evcon.CheckPlayerLinkStatus(oTarget, oEventCB, LINK_QUIT, 0):
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -1, None)
    elif cl_evcon.CheckPlayerLinkStatus(oTarget, oEventCB, LINK_ONLINE, 0):
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)


def CallBack5(oEventCB, oTarget):
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func218(*a) - 1))


class CState(cl_state.CState):
    m_SID = 1809
    m_Name = '铁索连环'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 3
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
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        5: CallBack5 }

