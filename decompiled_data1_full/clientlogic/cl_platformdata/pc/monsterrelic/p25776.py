# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25776.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25776.pyc
# Source Generated with Decompyle++
# File: p25776.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, QUALITY_TYPE_HIGH, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
            cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 300)
            cl_evact.PassiveCBTargetAddRandomCurseRelicToState(oWarrior, oEventCB, 1, 500, 1, {
                5906: 1,
                5948: 1,
                5962: 1,
                5963: 1,
                5966: 1 })


class CPerform(CCustomPerform):
    m_SID = 25776
    m_Name = '驱邪护符'
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
    m_HeroRelic = 5776
    m_Quality = QUALITY_TYPE_HIGH
    m_ExcludeRelic = ()

