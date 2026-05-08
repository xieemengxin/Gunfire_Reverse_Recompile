# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32051.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32051.pyc
# Source Generated with Decompyle++
# File: st32051.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func331

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2036) <= 3:
        cl_evact.EventAddBagBullet(oTarget, oEventCB, 4502, (lambda *a: 10 * Func331(*a, **{
'sid': 2036 })))
        cl_evact.EventAddBagBullet(oTarget, oEventCB, 4503, (lambda *a: 10 * Func331(*a, **{
'sid': 2036 })))
        cl_evact.EventAddBagBullet(oTarget, oEventCB, 4504, (lambda *a: 10 * Func331(*a, **{
'sid': 2036 })))


class CState(cl_state.CState):
    m_SID = 32051
    m_Name = '#NT#双持弹药专家'
    m_DieRemove = 1
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'cnt': 10800 }
    m_CBFuncAction = {
        0: CallBack0 }

