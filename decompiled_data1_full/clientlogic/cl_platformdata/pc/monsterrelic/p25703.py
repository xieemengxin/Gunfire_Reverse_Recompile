# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25703.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25703.pyc
# Source Generated with Decompyle++
# File: p25703.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import DEFEND_TREND_ARMOR, MONSTERRELIC_RULE_EXCLUDEMONSTER, MONSTERRELIC_RULE_LIMITMONSTER, MONSTERRELIC_SUBRULE_MONSTER, QUALITY_TYPE_NORMAL
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' }))) == 0 and cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'ArmorMax' }))) == 0:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    else:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckTargetDefendTrend(oWarrior, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 2), 0)
    else:
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 2), 0)
    cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', 100)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 10000, 0, 0)
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', 10000, 0, 0)
    cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', 100)


class CPerform(CCustomPerform):
    m_SID = 25703
    m_Name = '异能之躯'
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
    m_HeroRelic = 5703
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()
    m_MonsterRule = {
        MONSTERRELIC_RULE_EXCLUDEMONSTER: {
            MONSTERRELIC_SUBRULE_MONSTER: [
                2381,
                2382,
                2383,
                2385,
                2384,
                3381,
                3384,
                3382,
                3383,
                3283,
                2283,
                3242,
                3134] } }

