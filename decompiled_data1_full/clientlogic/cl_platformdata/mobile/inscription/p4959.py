# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p4959.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p4959.pyc
# Source Generated with Decompyle++
# File: p4959.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1508, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1080, 1, 1, None) and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1508, 1, 1, None) and cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB) and cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1508, 1, 1) > 0:
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1080, -1, 1, 1, None)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1508, -1, 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 4959
    m_Name = '炎魔传说'
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
        'MaxBullet': (0, 5000, 0) }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1104,), ())
    m_ExcludeList = ((), (4907,), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

