# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32500.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32500.pyc
# Source Generated with Decompyle++
# File: st32500.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_ENEMY, OBJ_SELF, STATE_ADD_REFRESHORSYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func520

def StateActAction(oTarget, oLifeCycle):
    CustomAction(oTarget, oLifeCycle, { })
    cl_action.CommonSendStateStartMessage(oTarget, oLifeCycle, 0, 1)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func520(*a, **{
'sid': 2708 }))):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 1)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSendStateMessage(oTarget, oLifeCycle, 1, { })
    cl_action.CommonSendStateMessage(oTarget, oLifeCycle, 0, { })


def CallBack0(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: -(Func520(*a, **{
'sid': 2708 }) * 15 + 15) * 100), 0, 0, '')


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1012, 0, 1, {
        'MoveSpeedMul': (lambda *a: -(Func520(*a, **{
'sid': 2708 }) * 2 + 1) * 1000) }, 2, 0, 0)


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonSendStateStartMessage(oTarget, oLifeCycle, 0, 1)


class CState(cl_state.CState):
    m_SID = 32500
    m_Name = '#NT#媚影标记'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC
    m_TargetType = OBJ_ENEMY
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
    m_Action = (StateActAction, StateRemoveAction)
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }


def CustomAction(oWarrior, oLifeCycle, dInfo):
    dEventInfo = oLifeCycle.AttrCache()
    iAttacker = dEventInfo['StateInfo']['AID'] if 'StateInfo' in dEventInfo else dEventInfo.get('AID', 0)
    oGame = oWarrior.m_Game
    oAttacker = oGame.GetObject(iAttacker)
    if not oAttacker:
        return None
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_MARKTARGET, oAttacker, {
        'VID': oWarrior.m_ID })

