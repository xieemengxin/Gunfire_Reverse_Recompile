# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25811.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25811.pyc
# Source Generated with Decompyle++
# File: p25811.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, MONSTERPF_TYPE_ATTACK, OBJ_SELF, PF_TYPE_MONSTERACT, QUALITY_TYPE_NORMAL
from cl_newformula import Func304, Func374

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1703, 0, { }, -1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 5, 0, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'AttSpeed', -7000, 0, -1)
    cl_action.CommonChangeAllAtivePerformAttr(oWarrior, oLifeCycle, 'ColdTime', -7000, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckMonsterPFAttackType(oWarrior, oEventCB, MONSTERPF_TYPE_ATTACK):
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1703, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckMonsterPFAttackType(oWarrior, oEventCB, MONSTERPF_TYPE_ATTACK):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1703, -1, 0) != 1:
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1703, 0)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func374(*a) * 5 / 100), DAM_TYPE_WEAPON | DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 0, 0, 0, 0, -1, 0, 0, None, None, None)
            if cl_evcon.CheckDeadlyPredictDam(oWarrior, oEventCB, None):
                cl_evact.EventChangeHP(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 0 / 100 + 1))
            else:
                cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1703, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_MONSTERACT, None) and cl_evcon.CheckMonsterPFAttackType(oWarrior, oEventCB, MONSTERPF_TYPE_ATTACK):
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1703, 1)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_MONSTERACT, None) and cl_evcon.CheckMonsterPFAttackType(oWarrior, oEventCB, MONSTERPF_TYPE_ATTACK):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1703, -1, 0) != 1:
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1703, 0)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func374(*a) * 5 / 100), DAM_TYPE_WEAPON | DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 0, 0, 0, 0, -1, 0, 0, None, None, None)
            if cl_evcon.CheckDeadlyPredictDam(oWarrior, oEventCB, None):
                cl_evact.EventChangeHP(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 0 / 100 + 1))
            else:
                cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1703, 0)


class CPerform(CCustomPerform):
    m_SID = 25811
    m_Name = '能力透支'
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
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5811
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

