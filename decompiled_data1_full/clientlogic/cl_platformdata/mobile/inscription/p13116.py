# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13116.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13116.pyc
# Source Generated with Decompyle++
# File: p13116.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, MAIN_FIRECNT, OBJ_SELF
from cl_newformula import Func14

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFireCnt(oWarrior, oEventCB, MAIN_FIRECNT) == 0:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'FirstHitFrame', (lambda *a: Func14(*a) + 8))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'HitCount', 1)
    else:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HitCount', 1)
        if cl_evcon.GetFireCnt(oWarrior, oEventCB, MAIN_FIRECNT) == 3 and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HitCount') >= 4 and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'FirstHitFrame') >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func14(*a))):
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33768, 600, { }, 1)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33768, 1, 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 13116
    m_Name = '速射弓专属三'
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
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1516,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

