# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13509.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13509.pyc
# Source Generated with Decompyle++
# File: p13509.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_VICTIM, PF_SUBMSG_THROW, WARRIOR_BOSS, WARRIOR_MONSTER
from cl_newformula import Func302, Func343, Func421

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 6, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_MONSTER) and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1411: 1,
        8012: 1 }, 1, 1):
        if cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_BOSS) or cl_evcon.GetVictimHPRatio(oWarrior, oEventCB) <= 15:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func302(*a, **{
'sAttr': 'HPMax' }) * 16 / 100), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, -1, -1, -1, None, None, None)
        elif cl_evcon.GetVictimHPRatio(oWarrior, oEventCB) <= 25:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func302(*a, **{
'sAttr': 'HPMax' }) * 26 / 100), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, -1, -1, -1, None, None, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if not cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_MONSTER) and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1411: 1,
        8012: 1 }, 1, 1) and cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 1479):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: 3000 * (Func421(*a) + Func343(*a, **{
'sid': 4508 }))), 0, DAM_TYPE_PERFORM, None, None)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func343(*a, **{
'sid': 4508 }))) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1479, 10, { }, 1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 13509
    m_Name = '淘汰之刃'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        4: DoCallBackAction4,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 103

