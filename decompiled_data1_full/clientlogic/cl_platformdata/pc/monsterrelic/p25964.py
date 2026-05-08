# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25964.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25964.pyc
# Source Generated with Decompyle++
# File: p25964.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import MONSTERRELIC_RULE_EXCLUDEMONSTER, MONSTERRELIC_RULE_LIMITMONSTER, MONSTERRELIC_SUBRULE_MONSTERSOURCE, MONSTERRELIC_SUBRULE_MONSTERTYPE, QUALITY_TYPE_CURSE, WARRIOR_ELITE
from cl_newformula import Func304, Func379, Func710

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonHPModify(oWarrior, oLifeCycle, 'HP', (lambda *a: max(int(20 * Func304(*a, **{
'sAttr': 'HPMax' }) // 100), int(Func710(*a) * Func304(*a, **{
'sAttr': 'HPMax' }) // 100))), None)
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, (lambda *a: (-Func379(*a) // 10) * 500), 0, 0, 1)
    cl_action.CommonAddMonsterModelSize(oWarrior, oLifeCycle, (lambda *a: (-Func379(*a) // 10) * 5), 1)


class CPerform(CCustomPerform):
    m_SID = 25964
    m_Name = '独木难支'
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
    m_HeroRelic = 5964
    m_Quality = QUALITY_TYPE_CURSE
    m_ExcludeRelic = (25950,)
    m_MonsterRule = {
        MONSTERRELIC_RULE_EXCLUDEMONSTER: {
            MONSTERRELIC_SUBRULE_MONSTERTYPE: [
                WARRIOR_ELITE] },
        MONSTERRELIC_RULE_LIMITMONSTER: {
            MONSTERRELIC_SUBRULE_MONSTERSOURCE: [
                'Room'] } }

