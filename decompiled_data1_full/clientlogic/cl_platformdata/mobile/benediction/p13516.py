# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13516.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13516.pyc
# Source Generated with Decompyle++
# File: p13516.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_VICTIM, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_NORBOX, WARRIOR_SUMMON_STELE
from cl_newformula import Func204, Func311, Func312, Func313, Func336

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_BOSS) or cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_ELITE) or cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORBOX) or cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_SUMMON_STELE) or cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1313: 1,
        8503: 1 }, 1, 0):
        if cl_condition.CheckHasPerform(oWarrior, oEventCB.GetCBLifeCycle(), 15060):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func336(*a, **{
'sKey': '1313-Curtimes' }) + 1) * min(int(Func311(*a) * 10 / 100 + Func312(*a) * 10 / 100 + Func313(*a) * 10 / 100), int(500000 * Func204(*a)))), DAM_TYPE_WEAPON | DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, 0, 0, 0, 0, 0, None, None, None)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func336(*a, **{
'sKey': '1313-Curtimes' }) + 1) * min(int(Func311(*a) * 10 / 100 + Func312(*a) * 0 / 100 + Func313(*a) * 0 / 100), int(500000 * Func204(*a)))), DAM_TYPE_WEAPON | DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, 0, 0, 0, 0, 0, None, None, None)
    elif cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1313: 1,
        8503: 1 }, 1, 0):
        if cl_condition.CheckHasPerform(oWarrior, oEventCB.GetCBLifeCycle(), 15060):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func311(*a) * 10 / 100 + Func312(*a) * 10 / 100 + Func313(*a) * 10 / 100) * (Func336(*a, **{
'sKey': '1313-Curtimes' }) + 1)), DAM_TYPE_WEAPON | DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, 0, 0, 0, 0, 0, None, None, None)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func311(*a) * 10 / 100 + Func312(*a) * 0 / 100 + Func313(*a) * 0 / 100) * (Func336(*a, **{
'sKey': '1313-Curtimes' }) + 1)), DAM_TYPE_WEAPON | DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, 0, 0, 0, 0, 0, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 13516
    m_Name = '刺骨飞剑'
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
    m_Career = 109

