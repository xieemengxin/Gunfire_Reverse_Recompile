# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16019.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16019.pyc
# Source Generated with Decompyle++
# File: p16019.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_VICTIM, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_NORBOX
from cl_newformula import Func311, Func312, Func313

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, -1) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 30) and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_ELITE) == 0 and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORBOX) == 0 and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_BOSS) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func311(*a) * 30 / 100 + Func312(*a) * 30 / 100 + Func313(*a) * 30 / 100 + 0), DAM_TYPE_WEAPON | DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, 0, 0, 1, 0, 0, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 16019
    m_Name = '抹灭之击'
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

