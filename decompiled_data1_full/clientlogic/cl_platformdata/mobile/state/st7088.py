# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7088.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7088.pyc
# Source Generated with Decompyle++
# File: st7088.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func205, Func235, Func700

def DelayAction(oTarget, oLifeCycle):
    if cl_condition.CheckHasLockEnemy(oTarget, oLifeCycle) and cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func700(*a))) <= 30:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBSummonAreaMonster(oTarget, oEventCB, 10, {
        10: 10 }, {
        1: 10 }, 0, 0)
    cl_evact.EventCBSummonAreaMonster(oTarget, oEventCB, 11, {
        11: 10 }, {
        1: 10 }, 0, 0)


class CState(cl_state.CState):
    m_SID = 7088
    m_Name = '#NT#1幕BOSS三阶段刷怪辅助计时'
    m_DieRemove = 1
    m_DyingRemove = 1
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
        'delay': (lambda *a: (Func205(*a) - 0) * 0 + (Func235(*a, **{
'sType': 'RidingAlone' }) - 0) * -250 + 1800),
        'firsttime': 500 }
    m_CBFuncAction = {
        0: CallBack0 }

