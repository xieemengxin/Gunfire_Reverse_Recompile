# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/bossrelic/p51000.pyc
# RelativePath: clientlogic/cl_platformdata/pc/bossrelic/p51000.pyc
# Source Generated with Decompyle++
# File: p51000.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.bossrelic import CBossRelic as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1952)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 600)
        cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 1952, { })


class CPerform(CCustomPerform):
    m_SID = 51000
    m_Name = '吞天试炼'
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
    m_DieDisable = 1
    m_HeroRelic = 15800
    m_LimitMonster = { }
    m_ExcludeMonster = {
        3902: 1,
        3904: 1,
        3910: 1,
        3911: 1 }

