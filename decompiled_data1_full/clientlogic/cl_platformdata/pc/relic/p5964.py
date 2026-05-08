# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5964.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5964.pyc
# Source Generated with Decompyle++
# File: p5964.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import OBJ_FRIEND_HERONOSELF, OBJ_SELF, QUALITY_TYPE_CURSE, RELIC_TYPE_CURSE

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 0, 50, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByTargetType(oWarrior, oEventCB, 15, OBJ_FRIEND_HERONOSELF, 0)
    if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 1790, 0, 0, None, None):
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1790, 1550, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 5964
    m_Name = '独木难支'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = {
        'StateSID': 33371 }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_CURSE
    m_DropShape = 5531
    m_ValidRemove = 0
    m_BasePrice = 0
    m_bCanSell = 0
    m_Quality = QUALITY_TYPE_CURSE

