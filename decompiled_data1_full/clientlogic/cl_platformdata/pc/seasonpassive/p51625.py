# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51625.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51625.pyc
# Source Generated with Decompyle++
# File: p51625.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import DAM_TYPE_WEAPON, S7_MODULE_POINT_CHANGE
from cl_newformula import Func717, Func839

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 3000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 6000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 9000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraDamRatio', 150)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, (lambda *a: Func717(*a, **{
'sArg': 'DamRatio' })), DAM_TYPE_WEAPON, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, (lambda *a: Func717(*a, **{
'sArg': 'DamRatio' }) + min(30, int(Func839(*a))) * Func717(*a, **{
'sArg': 'ExtraDamRatio' })), DAM_TYPE_WEAPON, 1)


class CPerform(CCustomPerform):
    m_SID = 51625
    m_Name = '火力升级'
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
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

