# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5886.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5886.pyc
# Source Generated with Decompyle++
# File: p5886.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, DEFEND_TREND_ARMOR, MG_SOURCE_KILLMONSTER, OBJ_VICTIM, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL
from cl_newformula import Func304, Func308, Func334, Func357, Func390, Func391

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32405, 0, { }, 1)
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_ARMOR):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUREED, -1, 7, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUREED, -1, 8, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32405, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_ARMOR):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUREED, -1, 9, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUREED, -1, 10, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.CommonCBTargetDropReward(oWarrior, oEventCB, {
        401: 1 }, {
        401: 2000 }, 0, MG_SOURCE_KILLMONSTER, 1, 0)


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func357(*a) - Func334(*a))) > 0:
        if cl_evcon.CheckTotalCureSource(oWarrior, oEventCB, 1069, DAM_USE_ARMOR) or cl_evcon.CheckTotalCureSource(oWarrior, oEventCB, 1069, DAM_USE_HP):
            cl_evact.EventCBAddExcessAttr(oWarrior, oEventCB, 'Armor', (lambda *a: min(int((Func357(*a) - Func334(*a)) * (50 + 50 * Func308(*a)) / 100), int((Func304(*a, **{
'sAttr': 'ArmorMax' }) - Func390(*a)) * 10 / 100))), 0, 0)


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func357(*a) - Func334(*a))) > 0:
        if cl_evcon.CheckTotalCureSource(oWarrior, oEventCB, 1069, DAM_USE_HP) or cl_evcon.CheckTotalCureSource(oWarrior, oEventCB, 1069, DAM_USE_SHIELD):
            cl_evact.EventCBAddExcessAttr(oWarrior, oEventCB, 'Shield', (lambda *a: min(int((Func357(*a) - Func334(*a)) * (50 + 50 * Func308(*a)) / 100), int((Func304(*a, **{
'sAttr': 'ShieldMax' }) - Func391(*a)) * 10 / 100))), 0, 0)


def DoCallBackAction9(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func357(*a) - Func334(*a))) > 0:
        if cl_evcon.CheckTotalCureSource(oWarrior, oEventCB, 1069, DAM_USE_ARMOR) or cl_evcon.CheckTotalCureSource(oWarrior, oEventCB, 1069, DAM_USE_HP):
            cl_evact.EventCBAddExcessAttr(oWarrior, oEventCB, 'Armor', (lambda *a: min(int((Func357(*a) - Func334(*a)) * (50 + 50 * Func308(*a)) / 100), int((Func304(*a, **{
'sAttr': 'ArmorMax' }) - Func390(*a)) * 15 / 100))), 0, 0)


def DoCallBackAction10(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func357(*a) - Func334(*a))) > 0:
        if cl_evcon.CheckTotalCureSource(oWarrior, oEventCB, 1069, DAM_USE_HP) or cl_evcon.CheckTotalCureSource(oWarrior, oEventCB, 1069, DAM_USE_SHIELD):
            cl_evact.EventCBAddExcessAttr(oWarrior, oEventCB, 'Shield', (lambda *a: min(int((Func357(*a) - Func334(*a)) * (50 + 50 * Func308(*a)) / 100), int((Func304(*a, **{
'sAttr': 'ShieldMax' }) - Func391(*a)) * 15 / 100))), 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5886
    m_Name = '大饱口福'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        3: DoCallBackAction3,
        7: DoCallBackAction7,
        8: DoCallBackAction8,
        9: DoCallBackAction9,
        10: DoCallBackAction10 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 0
    m_Quality = QUALITY_TYPE_NORMAL

