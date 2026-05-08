# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33424.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33424.pyc
# Source Generated with Decompyle++
# File: st33424.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, PF_TYPE_CAREERPF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func336, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CAREERPF, 0) and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, '33424_NoTrigger', 0) == 0:
        if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, '33424_TriggerCnt', 0) > 0:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            if not cl_evcon.CheckTargetInSkillCollect(oTarget, oEventCB, '33424_Trigger'):
                cl_evact.EventCBRecordSkillCollectTarget(oTarget, oEventCB, '33424_Trigger', 0)
                cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1954, {
                    'Att': 30000,
                    'Cnt': (lambda *a: Func336(*a, **{
'sKey': '33424_TriggerCnt' })),
                    '33425_NoTrigger': 1,
                    'TransDamFactor': cl_evact.EventCBGetPFTransDamFactor(oTarget, oEventCB) }, None)
            elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0:
                cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, '33424_TriggerCnt', (lambda *a: Func404(*a)))
                cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
                cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
                if not cl_evcon.CheckTargetInSkillCollect(oTarget, oEventCB, '33424_Trigger'):
                    cl_evact.EventCBRecordSkillCollectTarget(oTarget, oEventCB, '33424_Trigger', 0)
                    cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1954, {
                        'Att': 30000,
                        'Cnt': (lambda *a: Func336(*a, **{
'sKey': '33424_TriggerCnt' })),
                        '33425_NoTrigger': 1,
                        'TransDamFactor': cl_evact.EventCBGetPFTransDamFactor(oTarget, oEventCB) }, None)
                else:
                    cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, '33424_NoTrigger', 1)


class CState(cl_state.CState):
    m_SID = 33424
    m_Name = '#NT#连城玩家秘卷陨石计数'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 6
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

