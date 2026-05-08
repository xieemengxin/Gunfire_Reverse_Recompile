# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13052.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13052.pyc
# Source Generated with Decompyle++
# File: p13052.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, INSCRIPTION_TYPE_GEMINI, ITEMPERFORM_ENABLE_HOLD, OBJ_ATTACK, OBJ_VICTIM
from cl_newformula import Func505, Func506

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetLinkAttr(oWarrior, oLifeCycle, 'MaxBullet', None)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: cl_evcon.GetFormula(oWarrior, oEventCB, Func506(*a)) / 3)) and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1739, -1, -1, None) <= 0:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func505(*a) * 500), DAM_TYPE_WEAPON, '')
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1739, 100, { }, -1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 13052
    m_Name = '弹夹连结2'
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
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_GEMINI
    m_ElementType = None
    m_LimitList = ((), (), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

