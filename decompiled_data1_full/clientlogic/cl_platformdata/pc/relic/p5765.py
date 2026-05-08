# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5765.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5765.pyc
# Source Generated with Decompyle++
# File: p5765.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL, WARRIOR_SUMMON
from cl_newformula import Func410, Func598, Func707

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1139, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'PF5765' }))) > 0:
        cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 1139, (lambda *a: Func598(*a, **{
'sKey': 'PF5765' }) * Func707(*a)), None)
    else:
        cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, -1, 7)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UPDATE_STATECOUNTEFF, -1, 5, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1350, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'PF5765' }))) > 0:
        cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 1350, (lambda *a: Func598(*a, **{
'sKey': 'PF5765' }) * Func707(*a)), None)
    else:
        cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, -1, 8)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UPDATE_STATECOUNTEFF, -1, 6, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if not cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_SUMMON) and cl_evcon.CheckTargetPointBaseSummon(oWarrior, oEventCB, 1083) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetDist(oWarrior, oEventCB, 7, None, None):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_action.CommonAddSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'PF5765', 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1139, (lambda *a: Func598(*a, **{
'sKey': 'PF5765' }) * Func707(*a)))


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if not cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_SUMMON) and cl_evcon.CheckTargetPointBaseSummon(oWarrior, oEventCB, 1083) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetDist(oWarrior, oEventCB, 7, None, None):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_action.CommonAddSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'PF5765', 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1350, (lambda *a: Func598(*a, **{
'sKey': 'PF5765' }) * Func707(*a)))


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1139, (lambda *a: Func598(*a, **{
'sKey': 'PF5765' }) * Func707(*a)))


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1350, (lambda *a: Func598(*a, **{
'sKey': 'PF5765' }) * Func707(*a)))


def DoCallBackAction7(oEventCB, oWarrior):
    cl_evact.EventCBSetSavedData(oWarrior, oEventCB, 'PF5765', (lambda *a: Func410(*a, **{
'sid': 1139 })), 1)


def DoCallBackAction8(oEventCB, oWarrior):
    cl_evact.EventCBSetSavedData(oWarrior, oEventCB, 'PF5765', (lambda *a: Func410(*a, **{
'sid': 1350 })), 1)


class CPerform(CCustomPerform):
    m_SID = 5765
    m_Name = '战场老兵'
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
        2: DoCallBackAction2,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7,
        8: DoCallBackAction8 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

