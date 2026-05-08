# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32335.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32335.pyc
# Source Generated with Decompyle++
# File: st32335.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_LASER, OBJ_SELF, PF_TYPE_CONSHOOT, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 3, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 32317, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'pf2402', None) == 0:
        cl_evact.EventCBAddCollectInfo(oTarget, oEventCB, 'pf2402', 1, None)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'AttSpeed', 0, (lambda *a: Func404(*a) * 100), 0)
        if cl_evcon.CheckHasState(oTarget, oEventCB, 32317) == 0 and cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 30:
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32317, 0, { }, None)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'AttSpeed', 0, (lambda *a: Func404(*a) * 100), 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, None) and cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_LASER) and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'pf2402', None) == 1:
        cl_evact.EventCBAddCollectInfo(oTarget, oEventCB, 'pf2402', -1, None)


class CState(cl_state.CState):
    m_SID = 32335
    m_Name = '#NT#火力风暴2级'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 30
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
        0: CallBack0,
        1: CallBack1,
        3: CallBack3 }

