# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7112.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7112.pyc
# Source Generated with Decompyle++
# File: st7112.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_NORMAL, DAM_TYPE_WEAPON, DAM_USE_ALL, DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, STATUS_PUSH, WARRIOR_HERO, WARRIOR_MONSTER
from cl_newformula import Func401

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 3, WARRIOR_HERO, 1, 1, 1, 0, None, { }, None, None, None, None, None)
    cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 1)
    cl_action.CommonDirectEventCBFunc(oTarget, oEventCB.GetCBLifeCycle(), 2, None, None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckTargetMoveStatus(oTarget, oEventCB, STATUS_PUSH) == 0:
        cl_evact.EventCBPushHeroTarget(oTarget, oEventCB, 10, 5, 9, 18, 30)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func401(*a) * 120 / 100 + 0), DAM_TYPE_WEAPON | DAM_TYPE_NORMAL | DAM_USE_HP | DAM_USE_SHIELD | DAM_USE_ARMOR | DAM_USE_ALL, 1, 1, 1, 1, None, None, None, None, None, None, None)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 3, WARRIOR_MONSTER, 1, 1, 1, 0, 0, { }, None, None, None, None, None)
    cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 3)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckTargetMoveStatus(oTarget, oEventCB, STATUS_PUSH) == 0:
        cl_evact.EventCBPushMonsterTarget(oTarget, oEventCB, 20, 6, 'Listener')
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func401(*a) * 100), DAM_TYPE_WEAPON | DAM_TYPE_NORMAL | DAM_USE_HP | DAM_USE_SHIELD | DAM_USE_ARMOR | DAM_USE_ALL, 0, 1, 1, 0, None, None, None, None, None, None, None)


class CState(cl_state.CState):
    m_SID = 7112
    m_Name = '#NT#骑乘怪坐骑触发伤害'
    m_DieRemove = 1
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 20,
        'firsttime': 4 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

