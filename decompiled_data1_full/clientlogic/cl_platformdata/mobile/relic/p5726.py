# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5726.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5726.pyc
# Source Generated with Decompyle++
# File: p5726.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL, WARRIOR_SUMMON
from cl_newformula import Func410, Func598, Func707

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1099, 0, { }, 1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'PF5726' }))) > 0:
        cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 1099, (lambda *a: Func598(*a, **{
'sKey': 'PF5726' }) * Func707(*a)), None)
    else:
        cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, -1, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UPDATE_STATECOUNTEFF, -1, 3, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 1099, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1161, 0, { }, 1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'PF5726' }))) > 0:
        cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 1161, (lambda *a: Func598(*a, **{
'sKey': 'PF5726' }) * Func707(*a)), None)
    else:
        cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, -1, 8)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UPDATE_STATECOUNTEFF, -1, 7, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 1161, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if not cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_SUMMON) and cl_evcon.CheckTargetPointBaseSummon(oWarrior, oEventCB, 1083) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_action.CommonAddSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'PF5726', 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1099, (lambda *a: Func598(*a, **{
'sKey': 'PF5726' }) * Func707(*a)))


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1099, (lambda *a: Func598(*a, **{
'sKey': 'PF5726' }) * Func707(*a)))


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'PF5726', (lambda *a: Func410(*a, **{
'sid': 1099 })))


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if not cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_SUMMON) and cl_evcon.CheckTargetPointBaseSummon(oWarrior, oEventCB, 1083) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_action.CommonAddSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'PF5726', 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1161, (lambda *a: Func598(*a, **{
'sKey': 'PF5726' }) * Func707(*a)))


def DoCallBackAction7(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1161, (lambda *a: Func598(*a, **{
'sKey': 'PF5726' }) * Func707(*a)))


def DoCallBackAction8(oEventCB, oWarrior):
    cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'PF5726', (lambda *a: Func410(*a, **{
'sid': 1161 })))


class CPerform(CCustomPerform):
    m_SID = 5726
    m_Name = '双刃之剑'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        7: DoCallBackAction7,
        8: DoCallBackAction8 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

