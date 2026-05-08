# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33875.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33875.pyc
# Source Generated with Decompyle++
# File: st33875.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func304, Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()) == 0 and cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        7168: 1,
        7170: 1,
        7171: 1 }, 1, 0) and cl_evcon.CheckRandom(oTarget, oEventCB, 100, (lambda *a: Func429(*a, **{
'sArg': 'ProbNum' }))):
        cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 100)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if not cl_evcon.EventCBCheckTargetIsLive(oTarget, oEventCB):
            cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HitRange' })), WARRIOR_MONSTER, 0, 0, 1, 0, 0, { }, 0, 0, 0, 1, None)
        if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 7168, 1, 0):
            cl_evact.StateCBUsePerform2EvtTarget(oTarget, oEventCB, 7169, { })
        elif cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 7170, 1, 0):
            cl_evact.StateCBUsePerform2EvtTarget(oTarget, oEventCB, 7172, { })
        elif cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 7171, 1, 0):
            cl_evact.StateCBUsePerform2EvtTarget(oTarget, oEventCB, 7174, { })


class CState(cl_state.CState):
    m_SID = 33875
    m_Name = '#NT#植物领域内额外攻击'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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
        0: CallBack0 }

