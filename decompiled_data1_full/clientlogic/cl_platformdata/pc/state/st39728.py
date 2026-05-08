# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39728.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39728.pyc
# Source Generated with Decompyle++
# File: st39728.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAKNESS, DPSUBMSG_DEFAULT, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, DPSUBMSG_DEFAULT, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 39728, (lambda *a: Func404(*a) * 34), 'DamRate')
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
        if cl_evcon.CheckRandom(oTarget, oEventCB, 100, (lambda *a: Func437(*a, **{
'sKey': 'DamRate' }))):
            cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'st39728', 1)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st39728', None):
        cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)


class CState(cl_state.CState):
    m_SID = 39728
    m_Name = '武器-低频暴击'
    m_IsShow = 1
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

