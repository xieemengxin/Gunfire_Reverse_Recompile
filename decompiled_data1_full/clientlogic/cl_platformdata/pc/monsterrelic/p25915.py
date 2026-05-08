# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25915.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25915.pyc
# Source Generated with Decompyle++
# File: p25915.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ACTIVE_SENDMESSAGE, QUALITY_TYPE_CURSE
from cl_newformula import Func213

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GOTDEFINALDEBUFF, ACTIVE_SENDMESSAGE, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckInPointState(oWarrior, oEventCB, {
        20026: 1,
        20027: 1,
        20028: 1 }):
        cl_evact.EventCBAddEventStateTime(oWarrior, oEventCB, (lambda *a: Func213(*a)), 2000)


class CPerform(CCustomPerform):
    m_SID = 25915
    m_Name = '元素咒能'
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
    m_RelicType = 0
    m_HeroRelic = 5915
    m_Quality = QUALITY_TYPE_CURSE
    m_ExcludeRelic = ()

