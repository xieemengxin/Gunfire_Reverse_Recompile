# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1681.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1681.pyc
# Source Generated with Decompyle++
# File: st1681.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomActionUsePerform1714 as CustomAction
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_NORMAL, DAM_TYPE_WEAPON, DAM_USE_ALL, MONSTER_PART_SHIELD, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func509

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 12011, 1, 0) and not cl_evcon.CheckHitPart(oTarget, oEventCB, MONSTER_PART_SHIELD):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if not cl_evcon.CheckTargetInSkillCollect(oTarget, oEventCB, 'st_1681'):
            if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1625, 0, 1, None, None):
                cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 1625, 2, 1, 0, None)
                if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), cl_evcon.GetTargetStateCount(oTarget, oEventCB, 1625, 1, 0) // 6) > 0:
                    cl_evact.EventClientBehavior(oTarget, oEventCB, 4328, 0)
                    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: 20 * Func509(*a, **{
'sAttr': 'Att' })), DAM_TYPE_WEAPON | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 0, 0, 0, 0, 0, 0, 0, None, None, None)
                    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 1625, -((cl_evact.EventCBGetTargetStateCount(oTarget, oEventCB, 1625, 1) // 6) * 6), 1, 0, None)
                    if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1624, 0, 1, None, None):
                        cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 1624, 1, 1, 0, None)
                        if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), cl_evcon.GetTargetStateCount(oTarget, oEventCB, 1624, 1, 0) // 3) > 0:
                            cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: 5 * Func509(*a, **{
'sAttr': 'Att' })), DAM_TYPE_WEAPON | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 0, 0, 0, 0, 0, 0, 0, None, None, None)
                            CustomAction(oTarget, oEventCB, {
                                'perform': 12011,
                                'state': 1624,
                                'count': 3 })
                            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 1624, -((cl_evact.EventCBGetTargetStateCount(oTarget, oEventCB, 1624, 1) // 3) * 3), 1, 0, None)
                    else:
                        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1624, 0, 0, { }, 0, None, None)
                        cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 1624, 1, 1, 0, None)
                cl_evact.EventCBRecordSkillCollectTarget(oTarget, oEventCB, 'st_1681', None)
            else:
                cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1625, 0, 0, { }, 0, None, None)
                cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 1625, 2, 1, 0, None)
                cl_evact.EventCBRecordSkillCollectTarget(oTarget, oEventCB, 'st_1681', None)


class CState(cl_state.CState):
    m_SID = 1681
    m_Name = '#NT#无悔散技能命中添加计数'
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
        0: CallBack0 }

