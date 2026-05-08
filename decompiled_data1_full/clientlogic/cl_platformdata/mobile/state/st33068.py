# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33068.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33068.pyc
# Source Generated with Decompyle++
# File: st33068.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction33068 as CustomAction
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def DelayAction(oTarget, oLifeCycle):
    if cl_condition.CheckSceneFightMonster(oTarget, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    CustomAction(oTarget, oLifeCycle, { })


def CallBack3(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_action.CommonUsePerform(oTarget, oEventCB.GetCBLifeCycle(), 1918, {
            'TransDamFactor': cl_action.CommonGetStateTransDamFactor(oTarget, oEventCB.GetCBLifeCycle(), 33058),
            'ParentActNum': (lambda *a: Func429(*a, **{
'sArg': 'ParentActNum' })) })
    else:
        cl_action.CommonUsePerform(oTarget, oEventCB.GetCBLifeCycle(), 1921, { })


class CState(cl_state.CState):
    m_SID = 33068
    m_Name = '#NT#浊墨领域管理'
    m_DieRemove = 1
    m_DyingRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
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
        'delay': 50 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        3: CallBack3 }

