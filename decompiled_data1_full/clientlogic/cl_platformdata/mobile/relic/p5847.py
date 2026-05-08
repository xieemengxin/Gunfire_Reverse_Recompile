# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5847.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5847.pyc
# Source Generated with Decompyle++
# File: p5847.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1529, 0, { }, 1)
    if cl_condition.HasState(oWarrior, oLifeCycle, 33499):
        cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 1529, (lambda *a: Func410(*a, **{
'sid': 33499 })), None)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33499, 0, { }, 0)
        cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 33499, (lambda *a: Func410(*a, **{
'sid': 1529 })), None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1554, 0, { }, 1)
    if cl_condition.HasState(oWarrior, oLifeCycle, 33499):
        cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 1554, (lambda *a: Func410(*a, **{
'sid': 33499 })), None)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33499, 0, { }, 0)
        cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 33499, (lambda *a: Func410(*a, **{
'sid': 1554 })), None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 5000, 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 5847
    m_Name = '事不过三'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 0
    m_BasePrice = 80
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

