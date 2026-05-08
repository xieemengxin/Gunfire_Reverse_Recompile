# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33890.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33890.pyc
# Source Generated with Decompyle++
# File: st33890.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DICESHOP_INITGOODS, DICE_QUALITY_TALE, LEVEL_TYPE_BOSS, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func201, Func429

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CheckHasSavedData(oTarget, oLifeCycle, '33890ShopEff'):
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)
    else:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DICESHOP, DICESHOP_INITGOODS, 0, 0, 0)
    if not cl_condition.CheckHasSavedData(oTarget, oLifeCycle, '33890InitEff'):
        cl_action.CommonSetSavedData(oTarget, oLifeCycle, '33890InitEff', 1)
        cl_action.CommonChangeMaxAssemblyNum(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'AssemblyNum' })))
        cl_action.CommonChangeDiceEnergy(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'DiceEnergy' })), 'SpecialItem1020')
        cl_action.CommonSendMessage(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USEDICESPECIALITEM, -1, {
            'SpecialItemSID': (lambda *a: Func429(*a, **{
'sArg': 'SpecialItemSID' })) })


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_BOSS) and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func201(*a))) == 1:
        cl_evact.EventCBSetSavedData(oTarget, oEventCB, '33890ShopEff', 1, 0)
        cl_evact.EventCBAddDicePacketGood(oTarget, oEventCB, 1, {
            1: DICE_QUALITY_TALE })
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33890
    m_Name = '#NT提前解锁'
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
        0: CallBack0 }

