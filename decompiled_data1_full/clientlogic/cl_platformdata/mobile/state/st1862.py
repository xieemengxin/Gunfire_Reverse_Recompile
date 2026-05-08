# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1862.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1862.pyc
# Source Generated with Decompyle++
# File: st1862.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, NWARRIOR_DROP_RELIC, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func598, Func651

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'EndlessRecycle' })))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECYCLEDROP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECYCLEGOLDENCUP, -1, 3, 0, 0)
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_MAGICPOWERCHANGE, -1, 4, 0, 0)
    if cl_condition.CheckOpenElement(oTarget, oLifeCycle, {
        'DeviceElement': 1 }):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECYCLE_DEVICECOMP, -1, 5, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonSetSavedData(oTarget, oLifeCycle, 'EndlessRecycle', (lambda *a: Func404(*a)))
    cl_action.CommonChangeCareerPerformAttr(oTarget, oLifeCycle, 'ColdTime', (lambda *a: max(int(-Func404(*a) * 100), -9000)), 0, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckEventRecycleDropType(oTarget, oEventCB, NWARRIOR_DROP_RELIC):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: 200 * Func404(*a)), 0, 0, '')


def CallBack2(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: 2000 * Func404(*a)), 0, 0, '')


def CallBack3(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'InteractTimes' }) * 2), None)
    cl_evact.EventCBSendNotify(oTarget, oEventCB, 1, 9457, {
        '$times': (lambda *a: Func651(*a, **{
'sKey': 'InteractTimes' }) * 2) })


def CallBack4(oEventCB, oTarget):
    if cl_evcon.EventCBCheckFullRelicTalent(oTarget, oEventCB):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack5(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


class CState(cl_state.CState):
    m_SID = 1862
    m_Name = '回收增益'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 60000
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5 }

