# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33485.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33485.pyc
# Source Generated with Decompyle++
# File: st33485.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomActionCollectSkill
from cl_platformdata.custom.state.customaction import CustomActionAddState
from cl_platformdata.custom.state.customaction import CustomActionCollectDurativeSkill
from cl_platformdata.custom.state.customaction import CustomActionAddStateByDurativeInfo
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DUAL_STATE_BEGIN, DUAL_STATE_END, OBJ_SELF, PF_SUBMSG_CAREERPF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CheckHero(oTarget, oLifeCycle, 205) or cl_condition.CheckHero(oTarget, oLifeCycle, 206) or cl_condition.CheckHero(oTarget, oLifeCycle, 215) or cl_condition.CheckHero(oTarget, oLifeCycle, 216) or cl_condition.CheckHero(oTarget, oLifeCycle, 218) or cl_condition.CheckHero(oTarget, oLifeCycle, 212):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 201):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 2, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 4, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 207):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDER, -1, 5, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 213):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_HOLD, -1, 5, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 217):
        cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 219):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 6, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 214):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONPEOFROM_START, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHasState(oTarget, oEventCB, 33493):
        CustomActionCollectSkill(oTarget, oEventCB.GetCBLifeCycle(), { })


def CallBack1(oEventCB, oTarget):
    CustomActionAddState(oTarget, oEventCB.GetCBLifeCycle(), {
        'AddStateSID': 8068,
        'Time': 200 })


def CallBack2(oEventCB, oTarget):
    CustomActionCollectDurativeSkill(oTarget, oEventCB.GetCBLifeCycle(), { })
    cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def CallBack3(oEventCB, oTarget):
    cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL)


def CallBack4(oEventCB, oTarget):
    CustomActionAddStateByDurativeInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'CD': 600,
        'AddStateSID': 8068,
        'Time': 200 })


def CallBack5(oEventCB, oTarget):
    CustomActionCollectDurativeSkill(oTarget, oEventCB.GetCBLifeCycle(), { })


def CallBack6(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1325, 1, 0):
        CustomActionCollectDurativeSkill(oTarget, oEventCB.GetCBLifeCycle(), { })


class CState(cl_state.CState):
    m_SID = 33485
    m_Name = '套装寸步难行状态效果'
    m_IsShow = 1
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
        4: CallBack4,
        5: CallBack5,
        6: CallBack6 }

