# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33516.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33516.pyc
# Source Generated with Decompyle++
# File: st33516.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, EQUIP_LASER, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, 10, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBSetCollectInfo(oTarget, oEventCB, 'p15104Reward', 1, 0)
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 5:
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -5, None)
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: (Func404(*a) + 5) * 150), 0, DAM_TYPE_WEAPON, 0, 0)
    elif cl_evcon.CheckEventWeaponType(oTarget, oEventCB, EQUIP_LASER):
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, 0, DAM_TYPE_WEAPON, 0, 0)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'p15104Reward', 0) == 0:
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: (Func404(*a) + 5) * 150), 0, DAM_TYPE_WEAPON, 0, 0)


class CState(cl_state.CState):
    m_SID = 33516
    m_Name = '充能射击'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 60
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

