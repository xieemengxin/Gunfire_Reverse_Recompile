# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p4856.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p4856.pyc
# Source Generated with Decompyle++
# File: p4856.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_NORMAL, ITEMPERFORM_ENABLE_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1154, 500, { }, 1, None, None)


class CPerform(CCustomPerform):
    m_SID = 4856
    m_Name = '急速追击'
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
    m_InscriptionType = INSCRIPTION_TYPE_NORMAL
    m_ElementType = None
    m_LimitList = ((), (), ())
    m_ExcludeList = ((9, 15, 17, 18, 19, 20), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

