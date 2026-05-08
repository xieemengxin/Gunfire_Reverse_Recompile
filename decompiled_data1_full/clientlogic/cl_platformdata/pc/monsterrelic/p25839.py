# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25839.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25839.pyc
# Source Generated with Decompyle++
# File: p25839.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_item.defines import QUALITY_TYPE_LOW
from cl_commondefines import PF_SUBMSG_CAREERPF, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32563) == 0:
        cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 12, WARRIOR_HERO, 1, 1, 0, 1, 0, { }, 1)
        cl_evact.EventCBSubTargetCareerPerformColdTime(oWarrior, oEventCB, 0, 80)


class CPerform(CCustomPerform):
    m_SID = 25839
    m_Name = '顺水推舟'
    m_MaxLevel = 1
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
    m_HeroRelic = 0
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

