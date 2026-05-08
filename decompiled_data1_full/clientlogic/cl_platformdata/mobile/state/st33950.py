# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33950.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33950.pyc
# Source Generated with Decompyle++
# File: st33950.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func404, Func841

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonSetAttrCustomLimit(oTarget, oLifeCycle, 'AttSpeed', 100, 100)
    cl_action.CommonListenOwnerMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1)
    cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'AttSpeed', -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        7144: 1,
        7151: 1 }, 0, 0):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 8 / 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None)
        cl_evact.EventCBUpdateCustomPosInfo(oTarget, oEventCB, {
            'BigCannon': 1 })


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        7144: 1,
        7151: 1,
        1426: 1,
        8009: 1 }, 1, 0):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: max(Func404(*a), 0)), 0, '')


def CallBack2(oEventCB, oTarget):
    cl_action.CommonSetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33950, (lambda *a: Func841(*a, **{
'sAttr': 'AttSpeed' }) - 10000), 0)
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func404(*a))) >= 5000:
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 7144, 'Radius', 0, (lambda *a: Func404(*a) // 5000))
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 7151, 'Radius', 0, (lambda *a: Func404(*a) // 5000))
        cl_evact.EventCBGetTargetByBelongs(oTarget, oEventCB)
        cl_evact.EventCBChangeTargetPerformAttr(oTarget, oEventCB, 1426, 'Radius', 0, (lambda *a: Func404(*a) // 5000), 0)
        cl_evact.EventCBChangeTargetPerformAttr(oTarget, oEventCB, 8009, 'Radius', 0, (lambda *a: Func404(*a) // 5000), 0)
    else:
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 7144, 'Radius', 0, 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 7151, 'Radius', 0, 0)
        cl_evact.EventCBGetTargetByBelongs(oTarget, oEventCB)
        cl_evact.EventCBChangeTargetPerformAttr(oTarget, oEventCB, 1426, 'Radius', 0, 0, 0)
        cl_evact.EventCBChangeTargetPerformAttr(oTarget, oEventCB, 8009, 'Radius', 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 33950
    m_Name = '#NT#铁翼重炮模式'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

