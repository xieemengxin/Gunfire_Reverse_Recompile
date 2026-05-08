# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25806.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25806.pyc
# Source Generated with Decompyle++
# File: p25806.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import OBJ_SELF, QUALITY_TYPE_LOW, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_MONSTER
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1717, 0, { }, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELITE):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeHP(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 0.4 / 100))
        cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 15, WARRIOR_MONSTER, 1, 0, 0, 0, 0, { }, -1, None, None, None, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeHP(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 2 / 100))
        cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 15, WARRIOR_MONSTER, 1, 0, 0, 0, 0, { }, -1, None, None, None, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 2)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1719, 0, { }, 1, -1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS) == 0:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1687, 0, { }, 1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 25806
    m_Name = '有福同享'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5806
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

