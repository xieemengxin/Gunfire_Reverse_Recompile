# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1763.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1763.pyc
# Source Generated with Decompyle++
# File: st1763.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_NORMAL
from cl_newformula import Func595

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 4, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9312, 1, -1) and cl_evcon.CheckRandom(oTarget, oEventCB, 100, 20):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_NORMAL):
            cl_evact.EventCBAddSourceWeaponPFBullet(oTarget, oEventCB, 9396, 400, 0, 1)
        elif cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_ELITE):
            cl_evact.EventCBAddSourceWeaponPFBullet(oTarget, oEventCB, 9396, 1200, 0, 1)
        elif cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_BOSS):
            cl_evact.EventCBAddSourceWeaponPFBullet(oTarget, oEventCB, 9396, 2000, 0, 1)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func595(*a))) != 3:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1763
    m_Name = '海水亲和'
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
        4: CallBack4 }

