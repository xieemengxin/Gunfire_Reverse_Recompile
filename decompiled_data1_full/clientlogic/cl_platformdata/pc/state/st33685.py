# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33685.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33685.pyc
# Source Generated with Decompyle++
# File: st33685.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func598

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CheckHasSavedData(oTarget, oLifeCycle, '33685StateCount'):
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': '33685StateCount' })))


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSetSavedData(oTarget, oLifeCycle, '33685StateCount', (lambda *a: Func404(*a)))


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def StateRefreshAction(oTarget, oLifeCycle):
    if not cl_condition.CommonCheckStateArgsDict(oTarget, oLifeCycle, 33682, 'EnableCount', 0, 0):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 33685
    m_Name = '秘能魔匣（掉落次数）'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0 }

