# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1328.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1328.pyc
# Source Generated with Decompyle++
# File: st1328.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_ALL, OBJ_ENEMY, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_NONE, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_NORMAL
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_NORMAL):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' })), CURE_TYPE_PERFORM | DAM_USE_ALL, 0, 0, None)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    elif cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_ELITE):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' })) * 5 / 100), CURE_TYPE_PERFORM | DAM_USE_ALL, 0, 0, None)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    elif cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_BOSS):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' })) * 2 / 100), CURE_TYPE_PERFORM | DAM_USE_ALL, 0, 0, None)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1328
    m_Name = '#NT#每日挑战4673怪物回血状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
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

