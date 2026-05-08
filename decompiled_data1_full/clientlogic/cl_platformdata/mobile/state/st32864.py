# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32864.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32864.pyc
# Source Generated with Decompyle++
# File: st32864.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction32587 as CustomAction
import cl_state
from cl_commondefines import DAM_MASK_CLASS, DAM_MASK_ELEMENT, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func402, Func404

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonModifyDamResistance(oTarget, oLifeCycle, (lambda *a: Func404(*a) * 100), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 10, WARRIOR_MONSTER, 1, 0, 0, 0, 0, { }, 0, None, None, None, None)
    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: CustomAction(oTarget, oEventCB, {
'Normal': 1,
'Elite': 2,
'Boss': 3,
'ExAdd': 0 }) * (Func402(*a) + 1)))


class CState(cl_state.CState):
    m_SID = 32864
    m_Name = '固若金汤'
    m_IsShow = 1
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
        'delay': 100,
        'firsttime': 100 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

