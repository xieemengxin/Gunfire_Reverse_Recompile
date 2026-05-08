# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1902.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1902.pyc
# Source Generated with Decompyle++
# File: st1902.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.StateCheckSourceWeaponHasInscription(oTarget, oLifeCycle, 13103):
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, 173)
    else:
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, 346)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.GetWeaponPFBulletNum(oTarget, oLifeCycle, 9094) >= cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: cl_condition.CommonGetWeaponPerformArgs(oTarget, oLifeCycle, 5309, 'IntervalCostTimes') * Func404(*a))):
        cl_action.CommonCostSourceWeaponPFBullet(oTarget, oLifeCycle, 9094, (lambda *a: cl_action.CommonGetWeaponPerformArgs(oTarget, oLifeCycle, 5309, 'IntervalCostTimes') * Func404(*a)))
    else:
        cl_action.CommonHaltPointPerform(oTarget, oLifeCycle, 9094)
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 1902, 0)


class CState(cl_state.CState):
    m_SID = 1902
    m_Name = '#NT#六方能量消耗'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 4 }

