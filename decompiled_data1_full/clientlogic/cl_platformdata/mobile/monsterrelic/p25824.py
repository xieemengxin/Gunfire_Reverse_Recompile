# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25824.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25824.pyc
# Source Generated with Decompyle++
# File: p25824.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, QUALITY_TYPE_CURSE, QUALITY_TYPE_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1716, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_MONSTERRELIC, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetMonsterRelicNumByQuality(oWarrior, oEventCB, QUALITY_TYPE_CURSE) == 0:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 3000, 0, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1716, cl_evact.EventGetTargetMonsterRelicNumByQuality(oWarrior, oEventCB, QUALITY_TYPE_CURSE))


class CPerform(CCustomPerform):
    m_SID = 25824
    m_Name = '亦正亦邪'
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
    m_HeroRelic = 5824
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

