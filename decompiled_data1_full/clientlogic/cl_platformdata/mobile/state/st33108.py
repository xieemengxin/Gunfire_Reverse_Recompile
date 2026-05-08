# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33108.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33108.pyc
# Source Generated with Decompyle++
# File: st33108.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, NORMAL_DAMAGE, OBJ_SELF, OBJ_VICTIM, PF_SUBMSG_DEVICEACTIVE, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func336, Func369, Func437, Func604, Func610, Func637

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenDeviceMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DEVICEACTIVE_COST_BEFORE, -1, 2, 0, 0)
    cl_action.CommonListenDeviceMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_DEVICEACTIVE, 3)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.EventCBCheckDealTotalDamFromDevice(oTarget, oEventCB):
        cl_evact.EventCBAddStateStatistics(oTarget, oEventCB, (lambda *a: Func369(*a) * 0.1), 33127, 'Damage')


def CallBack1(oEventCB, oTarget):
    if cl_evcon.EventCBGetSkillCustomInfo(oTarget, oEventCB, '33108ExtDam'):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func604(*a, **{
'sKey': '33108ExtDam' }) * (1 + Func336(*a, **{
'sKey': 'EnergyCost' }) / 5000)), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 1, 1, 1, 1, NORMAL_DAMAGE, None, None)


def CallBack2(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'DeviceEnergy' }))):
        cl_evact.EventSetEnergyCost(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'DeviceEnergy' }) // 10 + Func637(*a, **{
'sid': 7200,
'sAttr': 'EnergyCost' })))
        cl_evact.EventCBAddCustomInfo(oTarget, oEventCB, '33108PreExtDam', 1)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.EventCBGetSkillCustomInfo(oTarget, oEventCB, '33108PreExtDam'):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'NowDam', (lambda *a: Func610(*a, **{
'iStateSID': 33127,
'sKey': 'Damage' }) * 0.5))
        cl_evact.EventCBAddStateStatistics(oTarget, oEventCB, (lambda *a: -Func437(*a, **{
'sKey': 'NowDam' })), 33127, 'Damage')
        cl_evact.EventCBSetSkillCustomInfo(oTarget, oEventCB, '33108ExtDam', (lambda *a: Func437(*a, **{
'sKey': 'NowDam' })))


class CState(cl_state.CState):
    m_SID = 33108
    m_Name = '#NT#炮台专属3玩家在范围内'
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
        2: CallBack2,
        3: CallBack3 }

