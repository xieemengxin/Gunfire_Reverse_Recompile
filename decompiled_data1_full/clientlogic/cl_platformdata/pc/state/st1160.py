# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1160.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1160.pyc
# Source Generated with Decompyle++
# File: st1160.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_FIRE, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func404

def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 0:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func404(*a) * 1000 + 0), DAM_TYPE_WEAPON | DAM_TYPE_FIRE | DAM_USE_ALL, 1, 1, 0, 0, 1, 1, 1, 0, None, None, None)
    cl_evact.EventCBPushMonsterTarget(oTarget, oEventCB, 10, 3, 'StateAttacker')
    cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 4, WARRIOR_MONSTER, 1, 1, 0, None, None, None, None)
    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func404(*a) * 1000 + 0), DAM_TYPE_WEAPON | DAM_TYPE_FIRE | DAM_USE_ALL, 1, 1, 0, 0, 1, 1, 1, 0, None, None, None)
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1160
    m_Name = '#NT#1212触发'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 50000
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

