# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50578.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50578.pyc
# Source Generated with Decompyle++
# File: p50578.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_USE_HP, OBJ_ATTACK, OBJ_SELF, PET_ABILITY_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 2)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBRecordAllHPLoss(oWarrior, oEventCB, 200, DAM_USE_HP)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) > 10:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeDefValue(oWarrior, oEventCB, (0, None, ((304, 'HPMax'), (lambda a0: -a0 * 10 / 100))), DAM_USE_HP, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if not cl_evcon.EventCBCheckVictimForSelf(oWarrior, oEventCB):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (0, None, ((304, 'HPMax'), (lambda a0: (cl_action.CommonGetAllHPLossInfo(oWarrior, oEventCB.GetCBLifeCycle(), 200) / a0) * 10000 + 2000))), 0, '')


class CPerform(CCustomPerform):
    m_SID = 50578
    m_Name = '50578词条'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

