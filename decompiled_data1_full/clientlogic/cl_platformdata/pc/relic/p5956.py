# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5956.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5956.pyc
# Source Generated with Decompyle++
# File: p5956.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_CURSE, RELIC_TYPE_CURSE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'ColdTime', 3000, 0)
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'ColdTime', 3000, 0, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_CAREER_PERFORM, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ColdTime', 3000, 0, None)


class CPerform(CCustomPerform):
    m_SID = 5956
    m_Name = '精疲力竭'
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
        'StateSID': 33363 }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_CURSE
    m_DropShape = 5531
    m_ValidRemove = 0
    m_BasePrice = 0
    m_bCanSell = 0
    m_Quality = QUALITY_TYPE_CURSE

