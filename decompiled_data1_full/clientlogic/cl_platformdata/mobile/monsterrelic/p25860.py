# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25860.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25860.pyc
# Source Generated with Decompyle++
# File: p25860.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.monsterrelic.customaction import CustomAction25860 as CustomAction
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, QUALITY_TYPE_NORMAL, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO) and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        CustomAction(oWarrior, oEventCB, {
            'CostCash': cl_condition.RandomChooseKey(oWarrior, oEventCB.GetCBLifeCycle(), {
                3: 1,
                2: 1,
                1: 1,
                -1: 1,
                -2: 1,
                -3: 1,
                -4: 1,
                -5: 1,
                -6: 1,
                -7: 1 }) })
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)


class CPerform(CCustomPerform):
    m_SID = 25860
    m_Name = '幸运轮盘'
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
    m_HeroRelic = 5860
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

