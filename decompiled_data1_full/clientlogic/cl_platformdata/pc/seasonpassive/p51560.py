# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51560.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51560.pyc
# Source Generated with Decompyle++
# File: p51560.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, PF_TYPE_THROW
from cl_newformula import Func308, Func336, Func453

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214) or cl_condition.CheckHero(oWarrior, oLifeCycle, 207):
        cl_action.CommonChangeThrowPerformAttr(oWarrior, oLifeCycle, 'DamInterval', 2000, 0, None)
    else:
        cl_action.CommonChangeThrowPerformAttr(oWarrior, oLifeCycle, 'Radius', 2000, 0, None)


def Action2(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214) or cl_condition.CheckHero(oWarrior, oLifeCycle, 207):
        cl_action.CommonChangeThrowPerformAttr(oWarrior, oLifeCycle, 'DamInterval', 3000, 0, None)
    else:
        cl_action.CommonChangeThrowPerformAttr(oWarrior, oLifeCycle, 'Radius', 3000, 0, None)


def Action3(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214) or cl_condition.CheckHero(oWarrior, oLifeCycle, 207):
        cl_action.CommonChangeThrowPerformAttr(oWarrior, oLifeCycle, 'DamInterval', 4000, 0, None)
    else:
        cl_action.CommonChangeThrowPerformAttr(oWarrior, oLifeCycle, 'Radius', 4000, 0, None)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 219) or cl_condition.CheckHero(oWarrior, oLifeCycle, 207):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, '51311_HitTimes', 1, 0)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func308(*a))) == 5 or cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func453(*a) * Func336(*a, **{
'sKey': '51311_HitTimes' }) * 4000), 0, 0, '')
    elif cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func453(*a) * Func336(*a, **{
'sKey': '51311_HitTimes' }) * (Func308(*a) - 2) * 1000), 0, 0, '')


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func453(*a) * (Func308(*a) - 2) * 1000), 0, 0, '')


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func453(*a) * 4000), 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 51560
    m_Name = '#NT#灵气膨胀'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0

