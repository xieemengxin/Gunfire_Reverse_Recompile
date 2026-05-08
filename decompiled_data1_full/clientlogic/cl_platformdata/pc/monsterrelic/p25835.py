# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25835.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25835.pyc
# Source Generated with Decompyle++
# File: p25835.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ALL_PLAYER, OBJ_VICTIM, QUALITY_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 15) and cl_evcon.CheckTargetSideType(oWarrior, oEventCB, OBJ_ALL_PLAYER):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 200)
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1941, { }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 15) and cl_evcon.CheckTargetSideType(oWarrior, oEventCB, OBJ_ALL_PLAYER):
            cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 200)
            cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1941, { }, None)


class CPerform(CCustomPerform):
    m_SID = 25835
    m_Name = '意外过载'
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
    m_HeroRelic = 5835
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

