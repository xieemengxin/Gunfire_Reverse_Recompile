# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33944.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33944.pyc
# Source Generated with Decompyle++
# File: st33944.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, MAGIC_WAND_DAMAGE, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func304, Func852

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'CanExplosion', 1)
    cl_action.CommonAddPerform(oTarget, oLifeCycle, 7175)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'HPMax', -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIEDIST, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 8, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'CanExplosion', 0)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonAddCustomValueWithReason(oTarget, oEventCB.GetCBLifeCycle(), '4332RobotRelife', (lambda *a: -min(2000, 1500 + (Func304(*a, **{
'sAttr': 'HPMax' }) // 10000) * 20)))
    cl_evact.EventCBGetTargetByBelongs(oTarget, oEventCB)
    cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 33946, (lambda *a: Func852(*a, **{
'sKey': '4332RobotRelife' })), 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 7175, 1, 0):
        cl_evact.EventCBSetDamShowTipsType(oTarget, oEventCB, MAGIC_WAND_DAMAGE)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventCBGetTargetByBelongs(oTarget, oEventCB)
    if not cl_evcon.EventCBCheckTargetRealDead(oTarget, oEventCB):
        cl_action.CommonUsePerform(oTarget, oEventCB.GetCBLifeCycle(), 7175, { })
        cl_evact.EventCBSetCustomData(oTarget, oEventCB, 'DelayDie', 0)


def CallBack8(oEventCB, oTarget):
    if cl_evact.EventCBGetCustomData(oTarget, oEventCB, 'DelayDie') == 0:
        cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 15, WARRIOR_MONSTER, 1, 0, 0, 0, 0, { }, 0, 0, 0, 0, None)
        if cl_evcon.GetTargetNum(oTarget, oEventCB) <= 0:
            cl_evact.EventCBSetCustomData(oTarget, oEventCB, 'DelayDie', 1)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33953, 300, {
                'KeepTime': 300,
                'DelayTime': 150 }, None)
            cl_evact.EventCBHaltFlow(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33944
    m_Name = '#NT#小玖心有灵犀仆从增伤状态'
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        3: CallBack3,
        4: CallBack4,
        8: CallBack8 }

