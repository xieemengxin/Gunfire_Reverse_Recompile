# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1596.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1596.pyc
# Source Generated with Decompyle++
# File: st1596.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, EQUIP_LASER, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st1596', None) == 0 or cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0 or cl_evcon.CheckEventWeaponType(oTarget, oEventCB, EQUIP_LASER):
        cl_evact.EventCBAddCollectInfo(oTarget, oEventCB, 'st1596', 1, None)
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func404(*a) * 1000), 0, DAM_TYPE_WEAPON, None, 0)
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 1596
    m_Name = '蓄势待发'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 100
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

