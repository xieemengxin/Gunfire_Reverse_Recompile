# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33099.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33099.pyc
# Source Generated with Decompyle++
# File: st33099.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 3:
        cl_action.CommonChangeSourceWeaponSpecialAttr(oTarget, oLifeCycle, 'MaxTarget', 3)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9709, 0, 0) and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'PF13113', 0) == 0:
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL)
        cl_action.CommonClearSourceWeaponSpecialAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MaxTarget')
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
        cl_evact.EventSetSkillCache(oTarget, oEventCB, 'DebuffProb', 10000)


class CState(cl_state.CState):
    m_SID = 33099
    m_Name = '缚妖'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

