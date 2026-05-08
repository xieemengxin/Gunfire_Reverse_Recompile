# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25828.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25828.pyc
# Source Generated with Decompyle++
# File: p25828.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_WEAPON, DAM_USE_ALL, MONSTERRELIC_RULE_LIMITMONSTER, MONSTERRELIC_SUBRULE_MONSTER, OBJ_VICTIM, QUALITY_TYPE_HIGH
from cl_newformula import Func438

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func438(*a) * 50 / 100), DAM_TYPE_WEAPON | DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 0, 0, 0, 0, -1, -1, -1, -1, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 25828
    m_Name = '元素弹夹'
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
    m_HeroRelic = 5828
    m_Quality = QUALITY_TYPE_HIGH
    m_ExcludeRelic = ()
    m_MonsterRule = {
        MONSTERRELIC_RULE_LIMITMONSTER: {
            MONSTERRELIC_SUBRULE_MONSTER: [
                2002,
                2003,
                2004,
                2062,
                2063,
                2064,
                2082,
                2085,
                2102,
                2106,
                2108,
                2109,
                2110,
                2111,
                2124,
                2142,
                2143,
                2162,
                2165,
                2201,
                2201,
                2202,
                2203,
                2222,
                2223,
                2224,
                2242,
                2243,
                2244,
                3004,
                3142,
                3164,
                3165,
                3201,
                3203,
                3242,
                3381] } }

