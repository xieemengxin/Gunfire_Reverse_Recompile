# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p40069.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p40069.pyc
# Source Generated with Decompyle++
# File: p40069.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func598
from cl_commondefines import NWARRIOR_NPC_SHOP, VIRTUAL_ITEM_EQUIP, VIRTUAL_ITEM_RELIC

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonShowShopHiddenGoods(oWarrior, oLifeCycle, 12)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GOODSPOSINITBEFORE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BUYGOODS, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BUYGSGOOD, -1, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetPlusRandom(oWarrior, oEventCB, (lambda *a: 100 * Func598(*a, **{
'sKey': '40069Plus' })))


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckCBCheckShopType(oWarrior, oEventCB, {
        VIRTUAL_ITEM_EQUIP: 1,
        VIRTUAL_ITEM_RELIC: 1 }) and cl_evcon.CheckNPCType(oWarrior, oEventCB, NWARRIOR_NPC_SHOP) and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, (lambda *a: Func598(*a, **{
'sKey': '40069Curse' }))):
        cl_evact.EventCBGetRandomCurseRelic(oWarrior, oEventCB, 1)


class CPerform(CCustomPerform):
    m_SID = 40069
    m_Name = '天降大任-商店会员'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        4: DoCallBackAction4 }
    m_BaseArgData = {
        '40069Random': 30 }
    m_DieDisable = 0

