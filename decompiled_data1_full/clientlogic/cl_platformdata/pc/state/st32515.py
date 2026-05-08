# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32515.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32515.pyc
# Source Generated with Decompyle++
# File: st32515.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_NORMAL, DAM_TYPE_WEAPON, DAM_USE_ALL, EQUIP_LASER, OBJ_SELF, OBJ_VICTIM, PF_TYPE_CONSHOOT, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func410

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'pf32515', None) == 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: (cl_action.CommonGetTalentLevel(oTarget, oEventCB.GetCBLifeCycle(), 2411) * 0.05 + 0.05) * Func410(*a, **{
'sid': 32514 })), DAM_TYPE_WEAPON | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 0, 1, None, None, None, None, None, None, None)
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'pf32515', 1)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 0:
            cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 32514, 0)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, None) and cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_LASER) and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'pf32515', None) == 1:
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'pf32515', -1)


class CState(cl_state.CState):
    m_SID = 32515
    m_Name = '#NT#荡气回肠计数'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
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
        2: CallBack2 }

