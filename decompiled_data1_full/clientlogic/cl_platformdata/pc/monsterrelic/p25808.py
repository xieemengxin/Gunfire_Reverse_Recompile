# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25808.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25808.pyc
# Source Generated with Decompyle++
# File: p25808.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import MG_CASH, QUALITY_TYPE_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBChangeMonsterReward(oWarrior, oEventCB, MG_CASH, 206, 70)


class CPerform(CCustomPerform):
    m_SID = 25808
    m_Name = '刮地三尺'
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
    m_HeroRelic = 5808
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

