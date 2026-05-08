# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p4861.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p4861.pyc
# Source Generated with Decompyle++
# File: p4861.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_RARE, ITEMPERFORM_ENABLE_HOLD, OBJ_VICTIM, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB) and cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MONSTER, 1, 0, 0, None, None, None, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventTargetSputterDamage(oWarrior, oEventCB, 100, 1, None, None, None, None, None, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 4861
    m_Name = '公开处刑'
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
    m_InscriptionType = INSCRIPTION_TYPE_RARE
    m_ElementType = None
    m_LimitList = ((18,), (), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

