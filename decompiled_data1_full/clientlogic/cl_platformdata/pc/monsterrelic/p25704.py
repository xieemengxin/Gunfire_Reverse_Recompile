# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25704.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25704.pyc
# Source Generated with Decompyle++
# File: p25704.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import MONSTERRELIC_RULE_EXCLUDEMONSTER, MONSTERRELIC_RULE_LIMITMONSTER, MONSTERRELIC_SUBRULE_MONSTER, QUALITY_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ShieldMax', 0)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ArmorMax', 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'ShieldMax', -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'ArmorMax', -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1706, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBShieldAndArmor2HP(oWarrior, oEventCB, None)


class CPerform(CCustomPerform):
    m_SID = 25704
    m_Name = '血肉之躯'
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
    m_HeroRelic = 5704
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()
    m_MonsterRule = {
        MONSTERRELIC_RULE_EXCLUDEMONSTER: {
            MONSTERRELIC_SUBRULE_MONSTER: [
                3134] } }

