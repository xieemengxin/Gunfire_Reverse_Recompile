# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51672.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51672.pyc
# Source Generated with Decompyle++
# File: p51672.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import S7_MODULE_POINT_CHANGE
from cl_newformula import Func839

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39755, 0, {
        'RecoveryEff': 600,
        'ReduceRatio': 20,
        'EffectTime': 500 }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39755, 0, {
        'RecoveryEff': 700,
        'ReduceRatio': 15,
        'EffectTime': 500 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39755, 0, {
        'RecoveryEff': 800,
        'ReduceRatio': 10,
        'EffectTime': 300,
        'ExtraRecoveryEff': 20 }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39755, (lambda *a: Func839(*a) // 6), 1)


class CPerform(CCustomPerform):
    m_SID = 51672
    m_Name = '主要技能-休眠疗法'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

