# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/task/task1114.pyc
# RelativePath: clientlogic/cl_platformdata/pc/task/task1114.pyc
# Source Generated with Decompyle++
# File: task1114.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_task.mobject import CBaseTask
from cl_commondefines import NWARRIOR_NPC_SHOP, TASK_STATUS_SUCCESS, VIRTUAL_ITEM_SHOPREFRESH
from cl_newformula import Func247, Func598, Func716

def EnableAction(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_INITGOODS, -1, 1, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, -1, 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BUYGOODS, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BUYGSGOOD, -1, 4, 0, 0)
    if not cl_condition.TaskCheckSelfSubTask(oWarrior, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)


def DisableAction(oWarrior, oLifeCycle):
    if cl_condition.TaskCheckTaskStatus(oWarrior, oLifeCycle, TASK_STATUS_SUCCESS):
        cl_action.CommonAddSavedData(oWarrior, oLifeCycle, '40069Curse', -10)


def ClearAction(oWarrior, oLifeCycle):
    cl_action.CommonAddSavedData(oWarrior, oLifeCycle, '40069Curse', -10)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckNPCType(oWarrior, oEventCB, NWARRIOR_NPC_SHOP):
        cl_action.TaskAddSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), '1114NPC', 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func247(*a))) != cl_action.TaskGetSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), '1114Level'):
        cl_action.TaskSetSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), '1114Level', (lambda *a: Func247(*a)))
        cl_action.TaskSetSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), 'Temp', (lambda *a: Func716(*a, **{
'sAttr': '1114NPC' })))
        cl_action.TaskSetSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), '1114NPC', 0)
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
    if not cl_action.TaskGetSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), '1114First'):
        cl_action.TaskSetSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), '1114First', 1)
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': '40069Curse' }))) < 100:
            cl_action.CommonAddSavedData(oWarrior, oEventCB.GetCBLifeCycle(), '40069Curse', 10)
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': '40069Plus' }))) < 100:
            cl_action.CommonAddSavedData(oWarrior, oEventCB.GetCBLifeCycle(), '40069Plus', 10)
        cl_action.TaskSetSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), '1114NPC', 0)
        if not cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 'Have40069' }))):
            cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'Have40069', 1)
            cl_action.TaskAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 40069)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': '40069Curse' }))) < 100:
        cl_action.CommonAddSavedData(oWarrior, oEventCB.GetCBLifeCycle(), '40069Curse', 10)
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': '40069Plus' }))) < 100:
        cl_action.CommonAddSavedData(oWarrior, oEventCB.GetCBLifeCycle(), '40069Plus', 10)
    cl_action.TaskSetSaveInfo(oWarrior, oEventCB.GetCBLifeCycle(), '1114NPC', 0)
    if not cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 'Have40069' }))):
        cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'Have40069', 1)
        cl_action.TaskAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 40069)


class CTask(CBaseTask):
    m_SID = 1114
    m_Name = '商店会员（2级）'
    m_Description = '在下2个交互的行脚商处购买的商品不超过2个'
    m_Quality = 2
    m_RewardPerformSID = 0
    m_PunishPerformSID = 0
    m_TargetStats = {
        1: 2 }
    m_LimitTarget = {
        0: 3 }
    m_RecordStats = { }
    m_StatsLimit = {
        0: 0,
        1: 0 }
    m_Action = (EnableAction, DisableAction)
    m_ClearAction = ClearAction
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_OnlyPunishInFightLevel = 0
    m_ExcludeTask = { }
    m_HasPunish = 1
    m_BeforeChooseCond = None

