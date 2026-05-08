# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33763.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33763.pyc
# Source Generated with Decompyle++
# File: st33763.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func505, Func759

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, oLifeCycle.m_Owner.GetArgValue('BagBulletRecoveryRatio'))
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': oLifeCycle.m_Owner.GetArgValue('BulletRecoveryRatio'),
        'SrcLV': oLifeCycle.m_Owner.GetArgValue('StatusEffect') })


def DelayAction(oTarget, oLifeCycle):
    if oLifeCycle.m_Owner.GetArgValue('BulletRecoveryRatio') and oLifeCycle.m_Owner.GetArgValue('BagBulletRecoveryRatio'):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBAddHoldWeaponBagBullet(oTarget, oEventCB, (lambda *a: Func759(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('BagBulletRecoveryRatio') // 100), 0)
    cl_evact.EventCBAddHoldWeaponComBullet(oTarget, oEventCB, (lambda *a: max(int(Func505(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('BulletRecoveryRatio') // 100), 1)), 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBAddHoldWeaponBagBullet(oTarget, oEventCB, (lambda *a: Func759(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('BagBulletRecoveryRatio') // 100), 0)


class CState(cl_state.CState):
    m_SID = 33763
    m_Name = '扩容弹夹'
    m_IsShow = 1
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

