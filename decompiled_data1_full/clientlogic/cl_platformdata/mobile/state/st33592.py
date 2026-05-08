# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33592.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33592.pyc
# Source Generated with Decompyle++
# File: st33592.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import NWARRIOR_NPC_SHOP, OBJ_SELF, OBTAIN_WARCASH, STATE_ADD_EXCLUDE, STATE_CLS_SPECIAL, STATE_EFF_NONE, VIRTUAL_ITEM_EQUIP, VIRTUAL_ITEM_RELIC
from cl_newformula import Func240

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenGlobalMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_NPCCREATEOVER, -1, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_INITGOODS, -1, 1, 0, 9)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonSetSavedData(oTarget, oLifeCycle, 'st33592', cl_action.StateGetSelfCount(oTarget, oLifeCycle))


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0 and cl_evcon.CheckNPCType(oTarget, oEventCB, NWARRIOR_NPC_SHOP):
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -1, None)
        cl_evact.EventSetStateStatisticsData(oTarget, oEventCB, 33592, 'RandNpcShop', (lambda *a: Func240(*a)))
        cl_evact.EventCBSetShopNpcMaxRelic(oTarget, oEventCB, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckNPCType(oTarget, oEventCB, NWARRIOR_NPC_SHOP) and cl_evcon.EventCheckStateStatisticsData(oTarget, oEventCB, 33592, 'RandNpcShop', (lambda *a: Func240(*a))):
        if cl_condition.RandomTrigger(oTarget, oEventCB.GetCBLifeCycle(), 100, 5):
            cl_evact.EventCBReplaceGoodsToRandomByType(oTarget, oEventCB, 1, {
                VIRTUAL_ITEM_EQUIP: 1,
                VIRTUAL_ITEM_RELIC: 2 }, 1023, 1, 300, OBTAIN_WARCASH)
            cl_evact.EventCBReplaceGoodsToRandomByType(oTarget, oEventCB, 2, {
                VIRTUAL_ITEM_EQUIP: 1,
                VIRTUAL_ITEM_RELIC: 2 }, 1022, 1, 300, OBTAIN_WARCASH)
        else:
            cl_evact.EventCBReplaceGoodsToRandomByType(oTarget, oEventCB, 3, {
                VIRTUAL_ITEM_EQUIP: 1,
                VIRTUAL_ITEM_RELIC: 2 }, 1022, 1, 300, OBTAIN_WARCASH)


class CState(cl_state.CState):
    m_SID = 33592
    m_Name = '商店会员3级特殊效果'
    m_Type = STATE_CLS_SPECIAL
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

