# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p4891.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p4891.pyc
# Source Generated with Decompyle++
# File: p4891.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckSourceWeaponClassifyTag(oWarrior, oLifeCycle, 12):
        cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    else:
        cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1217, 1, 1, None):
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1217, 1, 1)
        cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 1217, 300, 300)
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1217, 300, { }, 1, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1832, 1, 1, -1):
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1832, 1, 1)
        cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 1832, 300, 300)
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1832, 300, { }, 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 4891
    m_Name = '幸运叠加'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (), ())
    m_ExcludeList = ((19,), (), (1303,))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

