# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25832.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25832.pyc
# Source Generated with Decompyle++
# File: p25832.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 1426):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1426, 4500, { }, 0)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1688, 1200, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 25832
    m_Name = '防弹痂壳'
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
    m_HeroRelic = 5832
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

