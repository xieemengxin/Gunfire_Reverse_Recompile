# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p4879.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p4879.pyc
# Source Generated with Decompyle++
# File: p4879.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_HP, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, OBJ_SELF, PF_SUBMSG_FILLBULLET

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_FILLBULLET, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1176, None, None, None)
    if oWarrior.HP() >= 2100:
        cl_evact.EventTargetDamage(oWarrior, oEventCB, 2000, DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_HP, 1, 0, None, None, None, None, None, None, None, None, None)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1176, 0, { }, 1, None, None)


class CPerform(CCustomPerform):
    m_SID = 4879
    m_Name = '浸血弹药'
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
    m_LimitList = ((), (), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

