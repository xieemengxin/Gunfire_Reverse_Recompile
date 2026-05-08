# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5766.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5766.pyc
# Source Generated with Decompyle++
# File: p5766.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL, WARRIOR_BOSS, WARRIOR_ELITE
from cl_newformula import Func410, Func598, Func707

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1138, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UPDATE_STATECOUNTEFF, -1, 4, 0, 0)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'PF5766' }))) > 0:
        cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 1138, (lambda *a: Func598(*a, **{
'sKey': 'PF5766' }) * Func707(*a)), None)
    else:
        cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, -1, 3)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1138, 0, { }, 1)
    cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 1138, (lambda *a: Func707(*a) * cl_action.CommonGetAssistKill(oWarrior, oLifeCycle, WARRIOR_BOSS | WARRIOR_ELITE)), None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UPDATE_STATECOUNTEFF, -1, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if not cl_evcon.CheckTargetPointBaseMonsters(oWarrior, oEventCB, {
        3906: 1 }):
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE):
            cl_action.CommonAddSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'PF5766', 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1138, (lambda *a: Func707(*a) * Func598(*a, **{
'sKey': 'PF5766' })))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if not cl_evcon.CheckTargetPointBaseMonsters(oWarrior, oEventCB, {
        3906: 1 }):
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE):
            cl_action.CommonAddSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'PF5766', 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1138, (lambda *a: Func707(*a) * (cl_action.CommonGetAssistKill(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_BOSS | WARRIOR_ELITE) + 1)))


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'PF5766', (lambda *a: Func410(*a, **{
'sid': 1138 })))


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1138, (lambda *a: Func707(*a) * Func598(*a, **{
'sKey': 'PF5766' })))


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1138, (lambda *a: Func707(*a) * cl_action.CommonGetAssistKill(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_BOSS | WARRIOR_ELITE)))


class CPerform(CCustomPerform):
    m_SID = 5766
    m_Name = '精英杀手'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

