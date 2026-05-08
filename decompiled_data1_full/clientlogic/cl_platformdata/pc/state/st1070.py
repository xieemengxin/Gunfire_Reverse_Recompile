# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1070.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1070.pyc
# Source Generated with Decompyle++
# File: st1070.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ENEMY, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_ABNORMAL, STATE_EFF_VERTIGO

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 7939) == 1:
        cl_action.CommonPerformMonsterVertigo(oTarget, oEventCB.GetCBLifeCycle(), 'MonsterCannon.CannonIllusion', { })
    else:
        cl_action.CommonPerformMonsterVertigo(oTarget, oEventCB.GetCBLifeCycle(), 'Common.illusion', {
            2122: 'MonsterMediumNear.illusion',
            2123: 'MonsterBigShield.illusion',
            2201: 'MonsterNear.MonsterFireIllusion',
            2044: 'MonsterFlyable.FlyableIllusion',
            2225: 'MonsterFlyable.FlyableIllusion' })


class CState(cl_state.CState):
    m_SID = 1070
    m_Name = '#NT#致幻状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_VERTIGO
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_ENEMY
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

