# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33790.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33790.pyc
# Source Generated with Decompyle++
# File: st33790.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PLANT_PHASE_NORMAL, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 100, 'TriggerCnt')
    if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'TriggerCnt') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect') and cl_condition.CheckSceneFightMonster(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TriggerCnt', 0)
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.EventGetAllMonsterByTargetScene(oTarget, oEventCB, 1, 0, 0)
        cl_evact.EventRandomTargetExecCBFuncAction(oTarget, oEventCB, 1, 0)
        if cl_evcon.GetThisTargetNum(oTarget, oEventCB) and cl_evcon.EventCBCheckSeedOrPlantPos(oTarget, oEventCB, 0, 0):
            cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -1, None)
            cl_evact.EventCBCreatePlantByTargetPos(oTarget, oEventCB, {
                'Dis': 1,
                'Dir': (1, 0, 0) }, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('HPMax'), 1, PLANT_PHASE_NORMAL, 1, 0)


class CState(cl_state.CState):
    m_SID = 33790
    m_Name = '#NT#园丁Boss关自动创建植物'
    m_IsShow = 1
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

