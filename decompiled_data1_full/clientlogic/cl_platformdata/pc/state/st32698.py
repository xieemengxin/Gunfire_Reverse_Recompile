# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32698.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32698.pyc
# Source Generated with Decompyle++
# File: st32698.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_SELF, PF_TYPE_CAREERPF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func336, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: 3000 * Func404(*a)), 0, DAM_TYPE_WEAPON, '')
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CAREERPF, None) and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'mengji_hitidx', None) != cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'p13530_hitidx', None):
        cl_evact.EventCBClearCollectInfo(oTarget, oEventCB, 'p13530_hitidx', None)
        cl_evact.EventCBAddCollectInfo(oTarget, oEventCB, 'p13530_hitidx', (lambda *a: Func336(*a, **{
'sKey': 'mengji_hitidx' })), 0)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_MONSTER):
        if cl_condition.CheckHasPerform(oTarget, oEventCB.GetCBLifeCycle(), 15066):
            cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        else:
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 32698
    m_Name = '次元法阵'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 10
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
        0: CallBack0,
        3: CallBack3 }

