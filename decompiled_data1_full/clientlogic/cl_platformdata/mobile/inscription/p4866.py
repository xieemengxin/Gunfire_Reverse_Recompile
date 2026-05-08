# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p4866.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p4866.pyc
# Source Generated with Decompyle++
# File: p4866.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import DAM_MASK_ELEMENT, INSCRIPTION_TYPE_RARE, ITEMPERFORM_ENABLE_HOLD, OBJ_VICTIM, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 8, WARRIOR_MONSTER, 1, 0, 0, 0, 0, 0, None)
        cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 0, 0, { }, 0, DAM_MASK_ELEMENT, None)


class CPerform(CCustomPerform):
    m_SID = 4866
    m_Name = '异常扩散'
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
    m_InscriptionType = INSCRIPTION_TYPE_RARE
    m_ElementType = None
    m_LimitList = ((), (), (4, 23))
    m_ExcludeList = ((), (), (1703,))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

