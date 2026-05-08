# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25748.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25748.pyc
# Source Generated with Decompyle++
# File: p25748.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, QUALITY_TYPE_NORMAL, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.EventCBCheckTargetNoSourceCDByMark(oWarrior, oEventCB, 'pf25748') == 0 and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_evact.EventCBAddTargetNoSourceCDByMark(oWarrior, oEventCB, 'pf25748', 200)
        if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33441, 0, 0, 0):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33441, 0, { }, 0, 1, 0)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33441, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 25748
    m_Name = '军火商人'
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
    m_HeroRelic = 5748
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

