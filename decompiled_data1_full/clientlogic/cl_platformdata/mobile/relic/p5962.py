# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5962.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5962.pyc
# Source Generated with Decompyle++
# File: p5962.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import EXTRAPICKUPRULE_FROM_RELIC_5962, QUALITY_TYPE_CURSE, RELIC_SUBMSG_GENERATE_DROP, RELIC_TYPE_CURSE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddExtraPickUpRule(oWarrior, oLifeCycle, EXTRAPICKUPRULE_FROM_RELIC_5962)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORE_REMOVE_RELIC_DROP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_DROP, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBChangeRelicShareStatus(oWarrior, oEventCB, 0)


class CPerform(CCustomPerform):
    m_SID = 5962
    m_Name = '刚愎自用'
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
    m_RelicType = RELIC_TYPE_CURSE
    m_DropShape = 5531
    m_ValidRemove = 0
    m_BasePrice = 0
    m_bCanSell = 0
    m_Quality = QUALITY_TYPE_CURSE

