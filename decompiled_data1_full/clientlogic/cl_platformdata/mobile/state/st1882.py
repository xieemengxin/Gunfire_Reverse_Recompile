# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1882.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1882.pyc
# Source Generated with Decompyle++
# File: st1882.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction1882 as CustomAction
import cl_state
from cl_commondefines import CRT_RANGECHECK_ENTER, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func686

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDisableWeaponPerform(oTarget, oLifeCycle, 4383)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCRT_RANGECHECK, CRT_RANGECHECK_ENTER, 1, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.GetWeaponPFBulletNum(oTarget, oLifeCycle, 9791) > 0:
        cl_action.CommonCostSourceWeaponPFBullet(oTarget, oLifeCycle, 9791, (lambda *a: Func686(*a, **{
'iPerform': 9791,
'sAttr': 'PFBulletUse' }) // 10))
    else:
        cl_action.StateHaltFromSkill(oTarget, oLifeCycle)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBSetTargetStateStatistics(oTarget, oEventCB, 1896, 'OnArea', 1, 1, 0, 1)


class CState(cl_state.CState):
    m_SID = 1882
    m_Name = '标记法杖耗能中'
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
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 10 }
    m_CBFuncAction = {
        1: CallBack1 }

