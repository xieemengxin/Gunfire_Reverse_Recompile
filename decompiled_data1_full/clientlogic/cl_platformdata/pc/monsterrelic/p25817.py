# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25817.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25817.pyc
# Source Generated with Decompyle++
# File: p25817.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, QUALITY_TYPE_LOW, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_HERO) and cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 20026) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 200)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBModifyTargetBagBulletByRatio(oWarrior, oEventCB, {
            4502: 10,
            4503: 10,
            4504: 10 }, -0.03)


class CPerform(CCustomPerform):
    m_SID = 25817
    m_Name = '备弹之光'
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
    m_HeroRelic = 5817
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

