# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33345.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33345.pyc
# Source Generated with Decompyle++
# File: st33345.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJECT_CURPET, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_PET_MINI
from cl_newformula import Func404

def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oTarget, oLifeCycle, 0, (lambda *a: 500 * Func404(*a)), 0, 1)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByOwnObj(oTarget, oEventCB, OBJECT_CURPET)
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_PET_MINI):
        cl_evact.EventCBGetClonePet(oTarget, oEventCB)
        cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 2)
    else:
        cl_evact.EventCBChangeTargetBaseDamRatio(oTarget, oEventCB, (lambda *a: 500 * Func404(*a)), 0, 0)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventCBChangeTargetBaseDamRatio(oTarget, oEventCB, (lambda *a: 500 * Func404(*a)), 0, 0)


class CState(cl_state.CState):
    m_SID = 33345
    m_Name = '妖灵词条'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 50
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
        0: CallBack0,
        2: CallBack2 }

