# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25848.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25848.pyc
# Source Generated with Decompyle++
# File: p25848.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, QUALITY_TYPE_NORMAL
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 100, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if oWarrior.HP() >= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 50 / 100)):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 7500, 0, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    if oWarrior.HP() >= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 50 / 100)):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1822, 100, { }, -1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 25848
    m_Name = '琉璃瞄具'
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
    m_HeroRelic = 5848
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

