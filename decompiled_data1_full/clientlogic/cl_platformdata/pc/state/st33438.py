# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33438.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33438.pyc
# Source Generated with Decompyle++
# File: st33438.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, PF_TYPE_CAREERPF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func3, Func402, Func404, Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 8608, 0, 0):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'st33438')
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'st33438') >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'Att' }))):
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'st33438', 0)
            cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)
        if cl_evcon.GetSkillCacheValue(oTarget, oEventCB, 'Suit15130Att') and cl_evcon.CheckTargetSkillHitInfo(oTarget, oEventCB) == 0:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            cl_evact.EventGetTargetSkillHitInfo(oTarget, oEventCB)
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 8608, {
                'Att': cl_evcon.GetSkillCacheValue(oTarget, oEventCB, 'Suit15130Att'),
                'Cnt': cl_evcon.GetSkillCacheValue(oTarget, oEventCB, 'Suit15130Cnt'),
                'IsDouble': cl_evcon.GetSkillCacheValue(oTarget, oEventCB, 'Suit15130Double') }, None)
        elif cl_evcon.GetSkillCacheValue(oTarget, oEventCB, 'Suit15130Att') and cl_evcon.CheckTargetSkillHitInfo(oTarget, oEventCB) == 0:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            cl_evact.EventGetTargetSkillHitInfo(oTarget, oEventCB)
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 8608, {
                'Att': cl_evcon.GetSkillCacheValue(oTarget, oEventCB, 'Suit15130Att'),
                'Cnt': cl_evcon.GetSkillCacheValue(oTarget, oEventCB, 'Suit15130Cnt'),
                'IsDouble': cl_evcon.GetSkillCacheValue(oTarget, oEventCB, 'Suit15130Double') }, None)


def CallBack2(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) and cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CAREERPF, 0):
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func402(*a))) == 2 and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func3(*a, **{
'a': int(Func404(*a)),
'b': 3 }))) == 0:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'st33438', 0)
            cl_evact.EventSetSkillCache(oTarget, oEventCB, 'Suit15130Att', 6000)
            cl_evact.EventSetSkillCache(oTarget, oEventCB, 'Suit15130Cnt', (lambda *a: Func404(*a)))
            cl_evact.EventSetSkillCache(oTarget, oEventCB, 'Suit15130Doudle', 1)
        else:
            cl_evact.EventSetSkillCache(oTarget, oEventCB, 'Suit15130Att', 3000)
            cl_evact.EventSetSkillCache(oTarget, oEventCB, 'Suit15130Cnt', (lambda *a: Func404(*a)))
            cl_evact.EventSetSkillCache(oTarget, oEventCB, 'Suit15130Doudle', 0)
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'st33438', 0)


class CState(cl_state.CState):
    m_SID = 33438
    m_Name = '陨石秘法'
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

