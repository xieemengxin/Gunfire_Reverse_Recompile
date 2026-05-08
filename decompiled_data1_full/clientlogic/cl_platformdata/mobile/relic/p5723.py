# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5723.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5723.pyc
# Source Generated with Decompyle++
# File: p5723.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_VICTIM, PF_TYPE_CONSHOOT, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL, WARRIOR_HERO
from cl_newformula import Func204, Func302, Func311, Func312, Func313

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO) == 0 and cl_evcon.PassiveCBCheckCartoonValid(oWarrior, oEventCB) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 10):
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: min(int(Func311(*a) * 15 / 100 + Func312(*a) * 0 / 100 + Func313(*a) * 0 / 100 + 0), 200000)), DAM_TYPE_WEAPON | DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, -1, 0, 0, -1, -1, -1, -1, None, None, None)
        if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT, None) == 0:
            cl_evact.PassiveCBSetValidCartoon(oWarrior, oEventCB)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO) == 0 and cl_evcon.PassiveCBCheckCartoonValid(oWarrior, oEventCB) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 10):
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: min(int(Func302(*a, **{
'sAttr': 'HPMax' }) * 15 / 100), int(500000 * Func204(*a)))), DAM_TYPE_WEAPON | DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, -1, 0, 0, -1, -1, -1, -1, None, None, None)
        if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT, None) == 0:
            cl_evact.PassiveCBSetValidCartoon(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 5723
    m_Name = '巨人杀手'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 80
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

