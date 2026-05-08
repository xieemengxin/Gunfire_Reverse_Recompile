# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33703.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33703.pyc
# Source Generated with Decompyle++
# File: st33703.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FIGHT_KEY_IGNOREDAMAGE, OBJ_SELF, PLANT_PHASE_NORMAL, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 100, 'TriggerCnt')
    if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'TriggerCnt') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect'):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TriggerCnt', 0)
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.EventTargetGetSectorTargetByFightType(oTarget, oEventCB, WARRIOR_MONSTER, 20, 20, 40, 0, 1, FIGHT_KEY_IGNOREDAMAGE, 0, 1, 0, None)
        if cl_evcon.GetThisTargetNum(oTarget, oEventCB) and cl_evcon.EventCBCheckSeedOrPlantPos(oTarget, oEventCB, 0, 0):
            cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -1, None)
            cl_evact.EventCBCreatePlantByTargetPos(oTarget, oEventCB, {
                'Dis': 1,
                'Dir': (1, 0, 0) }, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('HPMax'), 0, PLANT_PHASE_NORMAL, 1, 0)


class CState(cl_state.CState):
    m_SID = 33703
    m_Name = '#NT#园丁E3创建植物'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 1
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0 }

