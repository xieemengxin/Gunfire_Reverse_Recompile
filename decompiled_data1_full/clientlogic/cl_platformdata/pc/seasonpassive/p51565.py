# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51565.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51565.pyc
# Source Generated with Decompyle++
# File: p51565.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import OBJ_VICTIM, SIDE_TYPE_HERO, WARRIOR_PET, WARRIOR_PLANT, WARRIOR_SERVANT

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SaveTime', 800)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33905, 0, {
        'DamageAdd': 800,
        'SpeedAdd': 800 }, 1)
    cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33905, 3, 0, 1, 1)
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, SIDE_TYPE_HERO, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SaveTime', 800)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33905, 0, {
        'DamageAdd': 1200,
        'SpeedAdd': 1200 }, 1)
    cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33905, 3, 0, 1, 1)
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, SIDE_TYPE_HERO, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SaveTime', 800)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33905, 0, {
        'DamageAdd': 1600,
        'SpeedAdd': 1600 }, 1)
    cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33905, 5, 0, 1, 1)
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, SIDE_TYPE_HERO, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SaveTime', 800)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33905, 0, {
        'DamageAdd': 2000,
        'SpeedAdd': 2000 }, 1)
    cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33905, 5, 0, 1, 1)
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, SIDE_TYPE_HERO, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsSelfSummon(oWarrior, oEventCB, WARRIOR_SERVANT) or cl_evcon.CheckTargetIsSelfSummon(oWarrior, oEventCB, WARRIOR_PET) or cl_evcon.CheckTargetIsSelfSummon(oWarrior, oEventCB, WARRIOR_PLANT):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33905, 1, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SaveTime'))


class CPerform(CCustomPerform):
    m_SID = 51565
    m_Name = '#NT#亡语'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

