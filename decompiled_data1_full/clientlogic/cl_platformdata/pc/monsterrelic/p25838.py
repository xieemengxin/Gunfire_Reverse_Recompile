# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25838.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25838.pyc
# Source Generated with Decompyle++
# File: p25838.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import OBJ_ATTACK, QUALITY_TYPE_LOW, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckDamFromSelf(oWarrior, oEventCB, 0) == 0 and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO) and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33423, 0, 0, 0) == 0:
            cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 500)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33423, 500, { }, 0, 0, 1)
            cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 1940, 0, { }, None)


class CPerform(CCustomPerform):
    m_SID = 25838
    m_Name = '睚眦必报'
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
    m_HeroRelic = 5838
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

