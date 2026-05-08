# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5963.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5963.pyc
# Source Generated with Decompyle++
# File: p5963.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_CURSE, RELIC_TYPE_CURSE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRelicType(oWarrior, oEventCB, RELIC_TYPE_CURSE) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
        cl_evact.EventCBCopyRelic(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 5963
    m_Name = '有难同当'
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

