# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25831.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25831.pyc
# Source Generated with Decompyle++
# File: p25831.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_HIGH, WARRIOR_ELITE
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' }))) > 0:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 1707, 0, { }, 1)
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 1717, 0, { }, -1)
    if cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_ELITE):
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'RShield', -10000, 0, -1)
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 1724, 0, { }, -1)
    else:
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'RShield', -5000, 0, -1)


class CPerform(CCustomPerform):
    m_SID = 25831
    m_Name = '涌能护盾'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5831
    m_Quality = QUALITY_TYPE_HIGH
    m_ExcludeRelic = ()

