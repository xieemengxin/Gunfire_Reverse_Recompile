# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st20030.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st20030.pyc
# Source Generated with Decompyle++
# File: st20030.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_CORRISION, DAM_TYPE_PERSISTENCE, DAM_TYPE_THUNDER, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_ENEMY, OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_NORBOX, WARRIOR_NORRIDE
from cl_newformula import Func204, Func304

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_BOSS):
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: ((Func304(*a, **{
'sAttr': 'HPMax' }) * 0.4 / 100 + 0) / Func204(*a)) * 100 / 100 + 0), DAM_TYPE_PERSISTENCE | DAM_TYPE_TRUE | DAM_TYPE_THUNDER | DAM_TYPE_CORRISION | DAM_USE_ALL, 1, 0, None, None, None, None, None, None, None, None, None)
    elif cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_NORRIDE):
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: ((Func304(*a, **{
'sAttr': 'HPMax' }) * 3 / 100 + 0) / Func204(*a)) * 100 / 100 + 0), DAM_TYPE_PERSISTENCE | DAM_TYPE_TRUE | DAM_TYPE_THUNDER | DAM_TYPE_CORRISION | DAM_USE_ALL, 1, 0, None, None, None, None, None, None, None, None, None)
    elif cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_ELITE):
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: ((Func304(*a, **{
'sAttr': 'HPMax' }) * 1 / 100 + 0) / Func204(*a)) * 100 / 100 + 0), DAM_TYPE_PERSISTENCE | DAM_TYPE_TRUE | DAM_TYPE_THUNDER | DAM_TYPE_CORRISION | DAM_USE_ALL, 1, 0, None, None, None, None, None, None, None, None, None)
    elif cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_NORBOX):
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: ((Func304(*a, **{
'sAttr': 'HPMax' }) * 1 / 100 + 0) / Func204(*a)) * 100 / 100 + 0), DAM_TYPE_PERSISTENCE | DAM_TYPE_TRUE | DAM_TYPE_THUNDER | DAM_TYPE_CORRISION | DAM_USE_ALL, 1, 0, None, None, None, None, None, None, None, None, None)
    else:
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: ((Func304(*a, **{
'sAttr': 'HPMax' }) * 12 / 100 + 0) / Func204(*a)) * 100 / 100 + 0), DAM_TYPE_PERSISTENCE | DAM_TYPE_TRUE | DAM_TYPE_THUNDER | DAM_TYPE_CORRISION | DAM_USE_ALL, 1, 0, None, None, None, None, None, None, None, None, None)


class CState(cl_state.CState):
    m_SID = 20030
    m_Name = '#NT#毒气状态'
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
    m_SyncMax = 9
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 50 }
    m_CBFuncAction = {
        0: CallBack0 }

