# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25872.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25872.pyc
# Source Generated with Decompyle++
# File: p25872.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import MONSTERRELIC_RULE_EXCLUDEMONSTER, MONSTERRELIC_RULE_LIMITMONSTER, MONSTERRELIC_SUBRULE_MONSTER, QUALITY_TYPE_LOW, WARRIOR_HERO, WARRIOR_SERVANT

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 0, 100, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_HERO | WARRIOR_SERVANT, 1, 0, 0, 0, 0, { }, 1, None, None, None, None)
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 500)
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1942, 0, { })


class CPerform(CCustomPerform):
    m_SID = 25872
    m_Name = '临危不惧'
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
    m_HeroRelic = 5872
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()
    m_MonsterRule = {
        MONSTERRELIC_RULE_EXCLUDEMONSTER: {
            MONSTERRELIC_SUBRULE_MONSTER: [
                2221,
                2222,
                2223,
                2224,
                2004,
                3004,
                2421] } }

