# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33936.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33936.pyc
# Source Generated with Decompyle++
# File: st33936.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeBaseReceiveDamageRatio(oTarget, oLifeCycle, 0, (lambda *a: -Func429(*a, **{
'sArg': 'DamReduceMul' })))
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: Func429(*a, **{
'sArg': 'SpeedMul' })), 0, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'SaveTime', (lambda *a: -Func429(*a, **{
'sArg': 'RescueReduceMul' })), 0, 0)
    cl_action.CommonListenOwnerMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33936
    m_Name = '#NT#小玖倒地铁翼减伤'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

