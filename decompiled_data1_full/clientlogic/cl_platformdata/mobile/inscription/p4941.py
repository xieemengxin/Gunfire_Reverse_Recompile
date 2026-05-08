# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p4941.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p4941.pyc
# Source Generated with Decompyle++
# File: p4941.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_FIRE, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1156, 1, 0, None):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1156, 0, { }, 0, 1, None)
        elif cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_THUNDER, 0):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1157, 1, 0, None):
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1157, 0, { }, 0, 1, None)
            elif cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_CORRISION, 0):
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
                if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1158, 1, 0, None):
                    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1158, 0, { }, 0, 1, None)


class CPerform(CCustomPerform):
    m_SID = 4941
    m_Name = '如律令'
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
    m_LimitList = ((), (1212,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

