# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33826.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33826.pyc
# Source Generated with Decompyle++
# File: st33826.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, BOX_TREBLE_DAMAGE, DAM_TYPE_CORRISION, DAM_TYPE_PERFORM, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_ENEMY, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func332, Func404, Func429, Func816

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33826, 0, 'KillCnt')
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oTarget, oLifeCycle, 0, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'AddDam' })), DAM_TYPE_WEAPON, 1)
    cl_action.CommonChangeCareerPerformAttr(oTarget, oLifeCycle, 'Radius', 0, 0.1 * cl_action.StateGetSelfCount(oTarget, oLifeCycle), 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 100:
        cl_action.CommonDoneEvent(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'KillCnt')
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'KillCnt') >= 10:
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -10, 'KillCnt')
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 8506, 1, 0):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetSideType(oTarget, oEventCB, OBJ_ENEMY):
            cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: 50000 + 50000 * Func332(*a)), DAM_TYPE_PERFORM | DAM_TYPE_CORRISION | DAM_USE_ALL, 1, 1, 0, 0, 0, 1, 0, 0, BOX_TREBLE_DAMAGE, 0, None)
            cl_evact.EventSetSkillCache(oTarget, oEventCB, 'ElementType', 512)
            cl_evact.EventSetSkillCache(oTarget, oEventCB, 'DebuffProb', 2000)
            cl_evact.EventTriggerTargetEleAbnormal(oTarget, oEventCB, 0)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventCBSetTargetByID(oTarget, oEventCB, (lambda *a: Func816(*a)))
    cl_evact.EventCBChangeTargetModel(oTarget, oEventCB, (lambda *a: 100 + Func404(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CountChangeScale')))
    CustomAction(oTarget, oEventCB, {
        'Scale': (lambda *a: 100 + Func404(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CountChangeScale')) })


class CState(cl_state.CState):
    m_SID = 33826
    m_Name = '领域扩张'
    m_IsShow = 1
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
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        4: CallBack4 }

