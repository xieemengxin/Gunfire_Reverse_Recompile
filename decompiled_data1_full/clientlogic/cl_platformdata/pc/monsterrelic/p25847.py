# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25847.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25847.pyc
# Source Generated with Decompyle++
# File: p25847.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, QUALITY_TYPE_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_MONSTERRELIC, -1, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1822, 0, { }, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 5000, 0, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetMonsterRelicNumByQuality(oWarrior, oEventCB, 0) >= 3:
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ADD_MONSTERRELIC, -1)
        cl_evact.EventCBMonsterUseExtraRelic(oWarrior, oEventCB, 25847, 1)


class CPerform(CCustomPerform):
    m_SID = 25847
    m_Name = '事不过三'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5847
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

