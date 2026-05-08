# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33533.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33533.pyc
# Source Generated with Decompyle++
# File: st33533.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction33533 as CustomAction
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, PF_SUBMSG_CAREERPF, PF_TYPE_CONSHOOT, STATE_ADD_LONGORSYNC, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)


def CallBack0(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB, {
        'AddStateSID': 33534,
        'FromWeapon': 0 })


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0) == 0:
        CustomAction(oTarget, oEventCB, {
            'AddStateSID': 33534,
            'FromWeapon': 1 })


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1960, {
            'HitWeak': 1,
            'UseTrajectory': 0,
            'Dam': 200 }, None)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 7153, 1, 0):
        CustomAction(oTarget, oEventCB, {
            'AddStateSID': 33534,
            'FromWeapon': 0 })


def CallBack4(oEventCB, oTarget):
    if cl_condition.CheckHero(oTarget, oEventCB.GetCBLifeCycle(), 217):
        cl_action.CommonListenServantMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 3)
    elif cl_condition.CheckHero(oTarget, oEventCB.GetCBLifeCycle(), 212):
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 33533
    m_Name = '#NT#附武器伤2'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_LONGORSYNC
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
        4: CallBack4 }

