# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33373.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33373.pyc
# Source Generated with Decompyle++
# File: st33373.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_PERFORM, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func589

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 1)
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33373, (lambda *a: Func589(*a) * 0.1), 'MagicShieldCurValue')
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33373, (lambda *a: Func589(*a) * 0.1), 'MagicShieldMaxValue')
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckSrcDamType(oTarget, oEventCB, DAM_TYPE_PERFORM):
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'MagicShieldCurValue'):
            cl_evact.StateCBChangeDamageByStatistics(oTarget, oEventCB, 'MagicShieldCurValue')
            cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
                'MagicShieldCurValue': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'MagicShieldCurValue'),
                'MagicShieldMaxValue': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'MagicShieldMaxValue') }, 33373)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33394, 0, { }, None)
        else:
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33394, 0, { }, None)


def CallBack2(oEventCB, oTarget):
    cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'MagicShieldCurValue': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'MagicShieldCurValue'),
        'MagicShieldMaxValue': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'MagicShieldMaxValue') }, 33373)


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


class CState(cl_state.CState):
    m_SID = 33373
    m_Name = '#NT#怪物遗物法术护盾'
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

