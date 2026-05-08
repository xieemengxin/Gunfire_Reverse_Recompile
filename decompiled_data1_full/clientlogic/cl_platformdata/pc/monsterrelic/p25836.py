# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25836.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25836.pyc
# Source Generated with Decompyle++
# File: p25836.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, DEFEND_TREND_SHIELD, OBJ_ATTACK, OBJ_VICTIM, QUALITY_TYPE_LOW
from cl_newformula import Func302, Func312, Func313

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.EventCBCheckTargetDefendTrend(oWarrior, oEventCB, DEFEND_TREND_SHIELD):
        if cl_evcon.EventCBGetTargetCustomData(oWarrior, oEventCB, 'ShieldStatus'):
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 5000, 0, DAM_MASK_ELEMENT, '')
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33449, 500, { }, 0, 1, 0)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33449, 1, 0)
        elif cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func312(*a))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func302(*a, **{
'sAttr': 'ShieldMax' }))) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func302(*a, **{
'sAttr': 'ShieldMax' }))) > 0:
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 5000, 0, DAM_MASK_ELEMENT, '')
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33449, 500, { }, 0, 1, 0)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33449, 1, 0)
        elif cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func313(*a))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func302(*a, **{
'sAttr': 'ArmorMax' }))) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func302(*a, **{
'sAttr': 'ArmorMax' }))) > 0:
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 5000, 0, DAM_MASK_ELEMENT, '')
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33449, 500, { }, 0, 1, 0)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33449, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 25836
    m_Name = '趁其不备'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5836
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

