# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st20031.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st20031.pyc
# Source Generated with Decompyle++
# File: st20031.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_PERSISTENCE, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_ENEMY, OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func408, Func417

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 1, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: (Func408(*a) * 200 / 100) * Func417(*a, **{
'iType': 'FireAbnormalFactor' }) / 100 + 0), DAM_TYPE_PERSISTENCE | DAM_TYPE_TRUE | DAM_TYPE_CORRISION | DAM_TYPE_FIRE | DAM_USE_ALL, 1, 0, 0, 0, 0, 0, 0, 0, None, None, None)
    cl_evact.EventCBPushMonsterTarget(oTarget, oEventCB, 10, 3, 'StateAttacker')
    cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 5, WARRIOR_MONSTER, 1, 1, 0, 1, None, None, None)
    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: (Func408(*a) * 100 / 100) * Func417(*a, **{
'iType': 'FireAbnormalFactor' }) / 100 + 0), DAM_TYPE_PERSISTENCE | DAM_TYPE_TRUE | DAM_TYPE_CORRISION | DAM_TYPE_FIRE | DAM_USE_ALL, 1, 0, 0, 0, 0, 0, 0, 0, None, None, None)
    cl_evact.EventCBPushMonsterTarget(oTarget, oEventCB, 10, 3, 'Listener')


class CState(cl_state.CState):
    m_SID = 20031
    m_Name = '#NT#爆炸状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
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

