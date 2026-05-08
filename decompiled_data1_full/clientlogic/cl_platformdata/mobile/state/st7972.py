# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7972.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7972.pyc
# Source Generated with Decompyle++
# File: st7972.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func404(*a))) >= 10:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckCurrentPFAI(oTarget, oEventCB, 3001) or cl_evcon.CheckCurrentPFAI(oTarget, oEventCB, 3004):
        cl_evact.EventCBNonLockEnemyTarget(oTarget, oEventCB)
        cl_evact.EventCBTargetUsePerform(oTarget, oEventCB, (lambda *a: Func404(*a) / 10), {
            39202: 50 })
    elif cl_evcon.CheckCurrentPFAI(oTarget, oEventCB, 3002):
        cl_evact.EventCBNonLockEnemyTarget(oTarget, oEventCB)
        cl_evact.EventCBTargetUsePerform(oTarget, oEventCB, (lambda *a: Func404(*a) / 10), {
            39201: 100 })
    elif cl_evcon.CheckCurrentPFAI(oTarget, oEventCB, 3004):
        cl_evact.EventCBNonLockEnemyTarget(oTarget, oEventCB)
        cl_evact.EventCBTargetUsePerform(oTarget, oEventCB, (lambda *a: Func404(*a) / 10), {
            39202: 50 })
    elif cl_evcon.CheckCurrentPFAI(oTarget, oEventCB, 3005) or cl_evcon.CheckCurrentPFAI(oTarget, oEventCB, 3006) or cl_evcon.CheckCurrentPFAI(oTarget, oEventCB, 3008) or cl_evcon.CheckCurrentPFAI(oTarget, oEventCB, 3007):
        cl_evact.EventCBNonLockEnemyTarget(oTarget, oEventCB)
        cl_evact.EventCBTargetUsePerform(oTarget, oEventCB, (lambda *a: Func404(*a) / 10), {
            39202: 100 })


class CState(cl_state.CState):
    m_SID = 7972
    m_Name = '#NT#章鱼-阶段2施法'
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

