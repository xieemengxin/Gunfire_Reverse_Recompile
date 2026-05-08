# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33530.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33530.pyc
# Source Generated with Decompyle++
# File: st33530.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, JUMPFIGURE_BUYGOODS, OBJ_ATTACK, OBJ_SELF, PF_TYPE_CONSHOOT, STATE_ADD_LONGORSYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func207, Func404, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDCASH, -1, 0, 0, 0)
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: 60 + Func207(*a) * 5 / 1000))


def CallBack0(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: 60 + Func207(*a) * 5 / 1000))


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckPerformUnCrtByOwner(oTarget, oEventCB) == 0:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Cost', (lambda *a: Func207(*a) * 5 / 1000))
        cl_evact.EventCBAddCash(oTarget, oEventCB, (lambda *a: -Func437(*a, **{
'sKey': 'Cost' })), 0, JUMPFIGURE_BUYGOODS, 0, 0)
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, (lambda *a: Func404(*a) * 100), 0, 1, 0)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0) == 0:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Cost', (lambda *a: Func207(*a) * 5 / 1000))
        cl_evact.EventCBAddCash(oTarget, oEventCB, (lambda *a: -Func437(*a, **{
'sKey': 'Cost' })), 0, JUMPFIGURE_BUYGOODS, 0, 0)
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, (lambda *a: Func404(*a) * 100), 0, 1, 0)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Cost', (lambda *a: Func207(*a) * 5 / 1000))
        cl_evact.EventCBAddCash(oTarget, oEventCB, (lambda *a: -Func437(*a, **{
'sKey': 'Cost' })), 0, JUMPFIGURE_BUYGOODS, 0, 0)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func404(*a) * 100), 0, '')
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33530
    m_Name = '投币增幅'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_LONGORSYNC
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

