# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st39703.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st39703.pyc
# Source Generated with Decompyle++
# File: st39703.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_MASK_ELEMENT, OBJ_SELF, STATE_ADD_REFRESHORSYNC_SAMEITEM, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429

def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oTarget, oLifeCycle, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'AddDam' })), 0, DAM_MASK_ELEMENT, 1)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'SrcLV': (lambda *a: Func429(*a, **{
'sArg': 'AddDam' }) // 100) })


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 39703
    m_Name = '武器-武器技能'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC_SAMEITEM
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
    m_SendExtraInfo = 1
    m_CountFunc = {
        'action': StateCountAction }
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0 }

