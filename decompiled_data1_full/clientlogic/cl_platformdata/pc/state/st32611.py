# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32611.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32611.pyc
# Source Generated with Decompyle++
# File: st32611.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_SELF, PF_TYPE_CONSHOOT, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func331

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 2, 0, 1)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'ST32578', None):
        if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2913) < 3:
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: 5000 + 5000 * Func331(*a, **{
'sid': 2913 })), 0, DAM_TYPE_WEAPON, '')
        else:
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: 5000 + 5000 * Func331(*a, **{
'sid': 2913 })), 0, DAM_TYPE_WEAPON, '')
            cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, 30)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, None) and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'ST32578', None):
        cl_evact.EventCBAddCollectInfo(oTarget, oEventCB, 'ST32578', -1, None)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'ST32578', None) or cl_evcon.CheckFromSkillCollectInfo(oTarget, oEventCB, 'ST32578'):
        cl_evact.EventCBSubCareerPerformColdTime(oTarget, oEventCB, (lambda *a: 50 * Func331(*a, **{
'sid': 2913 })), 0)


class CState(cl_state.CState):
    m_SID = 32611
    m_Name = '#NT#摧枯拉朽加成'
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
        2: CallBack2,
        3: CallBack3 }

