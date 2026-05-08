# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33921.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33921.pyc
# Source Generated with Decompyle++
# File: st33921.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_TYPE_FUNDAMENTALWEAPON, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxLayer'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': oLifeCycle.m_Owner.GetArgValue('DamAdd') })


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckEventWeaponType(oTarget, oEventCB, EQUIP_TYPE_FUNDAMENTALWEAPON):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func429(*a, **{
'sArg': 'DamAdd' }) * Func404(*a) * 2), 0, 0, '')
    else:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func429(*a, **{
'sArg': 'DamAdd' }) * Func404(*a)), 0, 0, '')


class CState(cl_state.CState):
    m_SID = 33921
    m_Name = '武器专精'
    m_IsShow = 1
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

