# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25821.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25821.pyc
# Source Generated with Decompyle++
# File: p25821.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_LOW, WARRIOR_ELITE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        if cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELITE):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1720, 504, { }, 1, -1, None)
            cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 1000)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1699, 504, { }, 1, -1, None)
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 1000)


class CPerform(CCustomPerform):
    m_SID = 25821
    m_Name = '坚忍之躯'
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
    m_HeroRelic = 5821
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

