# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25750.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25750.pyc
# Source Generated with Decompyle++
# File: p25750.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import OBJ_SELF, QUALITY_TYPE_HIGH, WARRIOR_ELITE
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' }))) > 0 or cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'ArmorMax' }))) > 0:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELITE):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1721, 0, { }, -1, -1, None)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1665, 0, { }, -1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 25750
    m_Name = '幽魂皮肤'
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
    m_HeroRelic = 5750
    m_Quality = QUALITY_TYPE_HIGH
    m_ExcludeRelic = ()

