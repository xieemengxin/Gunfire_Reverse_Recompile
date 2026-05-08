# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5878.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5878.pyc
# Source Generated with Decompyle++
# File: p5878.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import DAM_TYPE_PERFORM, OBJ_SELF, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL
from cl_newformula import Func343, Func535, Func602

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BAGBULLETCHANGE_BEFOR, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 5, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BAGBULLETCHANGE_BEFOR, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 6, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckCostBulletType(oWarrior, oEventCB, 4508) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func535(*a))) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func343(*a, **{
'sid': 4508 }) * 10)) < cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func602(*a) * 5)) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBTargetAddThrowBagBullet(oWarrior, oEventCB, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckCostBulletType(oWarrior, oEventCB, 4508) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func535(*a))) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBTargetAddThrowBagBullet(oWarrior, oEventCB, 1)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func343(*a, **{
'sid': 4508 }) * 10 - Func602(*a) * 5)) >= 0:
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 6000, 0, DAM_TYPE_PERFORM, 1, 1)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func343(*a, **{
'sid': 4508 }) * 10 - Func602(*a) * 5)) >= 0:
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 10000, 0, DAM_TYPE_PERFORM, 1, 1)


class CPerform(CCustomPerform):
    m_SID = 5878
    m_Name = '见机行事'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

