# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p7004.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p7004.pyc
# Source Generated with Decompyle++
# File: p7004.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func343, Func347, Func373
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func373(*a, **{
'sid': 50018 }))) == 1:
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 8013)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func373(*a, **{
'sid': 50018 }))) == 2:
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 8013)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func373(*a, **{
'sid': 50018 }))) == 3:
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 8013)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 9, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 12019, 1, 0):
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: 100 * Func343(*a, **{
'sid': 4508 }) / Func347(*a, **{
'sid': 4508 }))) >= 60 or cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 60):
            cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, -1, 0)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 8013, { }, None)
        elif cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 20):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 8013, { }, None)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 12019, 1, 0):
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: 100 * Func343(*a, **{
'sid': 4508 }) / Func347(*a, **{
'sid': 4508 }))) >= 60 or cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 80):
            cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, -1, 0)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 8013, { }, None)
        elif cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 30):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 8013, { }, None)


def DoCallBackAction9(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 12019, 1, 0):
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: 100 * Func343(*a, **{
'sid': 4508 }) / Func347(*a, **{
'sid': 4508 }))) >= 60:
            cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, -1, 0)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 8013, { }, None)
        elif cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 40):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 8013, { }, None)


class CPerform(CCustomPerform):
    m_SID = 7004
    m_Name = '秘卷觉醒飞花被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        5: DoCallBackAction5,
        9: DoCallBackAction9 }
    m_BaseArgData = { }
    m_DieDisable = 0

