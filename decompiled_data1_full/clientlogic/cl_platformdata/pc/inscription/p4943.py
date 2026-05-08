# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4943.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4943.pyc
# Source Generated with Decompyle++
# File: p4943.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1758, 200, { }, 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 4943
    m_Name = '地狱'
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
    m_ItemAttr = {
        'Trajectory': (0, 3000, 0) }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1302,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

