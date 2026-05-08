# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/task/task1214.pyc
# RelativePath: clientlogic/cl_platformdata/pc/task/task1214.pyc
# Source Generated with Decompyle++
# File: task1214.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_task.mobject import CBaseTask
from cl_commondefines import NWARRIOR_NPC_SHOP, TASK_STATUS_FAIL, VIRTUAL_ITEM_SHOPREFRESH
from cl_newformula import Func247, Func598, Func716

def EnableAction(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREINTERACTSHOP, -1, 1, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, -1, 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BUYGOODS, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BUYGSGOOD, -1, 4, 0, 0)
    if not cl_condition.TaskCheckSelfSubTask(oWarrior, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)


def DisableAction(oWarrior, oLifeCycle):
    if cl_condition.TaskCheckTaskStatus(oWarrior, oLifeCycle, TASK_STATUS_FAIL):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 7, 0, 0)


def ClearAction(oWarrior, oLifeCycle):
    cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 33592, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckNPCType(oWarrior, oEventCB, NWARRIOR_NPC_SHOP) and cl_evcon.TaskCBCheckKeyInDataDict(oWarrior, oEventCB, '1214Interact', cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'ShopNpc')) == 0:
        cl_evact.TaskCBAddDataDict(oWarrior, oEventCB, '1214Interact', cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'ShopNpc'), 1)
        cl_action.TaskAddSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), '1214NPC', 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func247(*a))) != cl_action.TaskGetSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), '1214Level'):
        cl_action.TaskDelInfo(oWarrior, oEventCB.GetCBLifeCycle(), '1214Interact')
        cl_action.TaskSetSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), '1214Level', (lambda *a: Func247(*a)))
        cl_action.TaskSetSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), 'Temp', (lambda *a: Func716(*a, **{
'sAttr': '1214NPC' })))
        cl_action.TaskSetSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), '1214NPC', 0)
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 1, (lambda *a: Func716(*a, **{
'sAttr': 'Temp' })))


def DoCallBackAction3(oEventCB, oWarrior):
    if not cl_evcon.CheckCBCheckShopType(oWarrior, oEventCB, {
        VIRTUAL_ITEM_SHOPREFRESH: 1 }):
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckNPCType(oWarrior, oEventCB, NWARRIOR_NPC_SHOP) and cl_evcon.CheckCBCheckShopType(oWarrior, oEventCB, {
        VIRTUAL_ITEM_SHOPREFRESH: 1 }) == 0:
        cl_evact.TaskCBAddStat(oWarrior, oEventCB, 0, 1)


def DoCallBackAction5(oEventCB, oWarrior):
    if not cl_action.TaskGetSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), '1214First'):
        cl_action.TaskSetSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), '1214First', 1)
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': '40069Plus' }))) < 100:
            cl_action.CommonAddSavedData(oWarrior, oEventCB.GetCBLifeCycle(), '40069Plus', 20)
        cl_action.TaskSetSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), '1214NPC', 0)
        if not cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': '40069Relic' }))):
            cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), '40069Relic', 1)
        if not cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 'Have40069' }))):
            cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'Have40069', 1)
            cl_action.TaskAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 40069)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': '40069Plus' }))) < 100:
        cl_action.CommonAddSavedData(oWarrior, oEventCB.GetCBLifeCycle(), '40069Plus', 20)
    cl_action.TaskSetSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), '1214NPC', 0)
    if not cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': '40069Relic' }))):
        cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), '40069Relic', 1)
    if not cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 'Have40069' }))):
        cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'Have40069', 1)
        cl_action.TaskAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 40069)


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33592):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33592, 2, 0)
    else:
        cl_action.TaskAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 40073)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33592, 2, 0)


class CTask(CBaseTask):
    m_SID = 1214
    m_Name = '商店会员（3级）'
    m_Description = '在下1个交互的行脚商处购买的商品不超过2个'
    m_Quality = 3
    m_RewardPerformSID = 0
    m_PunishPerformSID = 0
    m_TargetStats = {
        1: 1 }
    m_LimitTarget = {
        0: 2 }
    m_RecordStats = { }
    m_StatsLimit = {
        0: 1,
        1: 0 }
    m_Action = (EnableAction, DisableAction)
    m_ClearAction = ClearAction
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7 }
    m_OnlyPunishInFightLevel = 0
    m_ExcludeTask = {
        1214: 1 }
    m_HasPunish = 1
    m_BeforeChooseCond = None

