# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51709.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51709.pyc
# Source Generated with Decompyle++
# File: p51709.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, COMMONACTIVE_TAG_S8_ATTACKPERFORM, DAM_MASK_ELEMENT, OBJ_ATTACK, PF_TYPE_S8THIRDACTIVE
from cl_newformula import Func717, Func804

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamMul', -5000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39742, 0, {
        'PerDamTime': 7,
        'TriggerProb': 50,
        'TriggerTime': 1,
        'TriggerCD': 50,
        'DetectCD': 50 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamMul', -5000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39742, 0, {
        'PerDamTime': 7,
        'TriggerProb': 100,
        'TriggerTime': 1,
        'TriggerCD': 50,
        'DetectCD': 50 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamMul', -5000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39742, 0, {
        'PerDamTime': 7,
        'TriggerProb': 100,
        'TriggerTime': 2,
        'TriggerCD': 50,
        'DetectCD': 50 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckPerfromInActivePerformTag(oWarrior, oEventCB, COMMONACTIVE_TAG_S8_ATTACKPERFORM) or cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_S8THIRDACTIVE, 0):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39742, 1, 0)
    elif cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'TriggerOrigin') == cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func804(*a))):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func717(*a, **{
'sArg': 'DamMul' })), DAM_MASK_ELEMENT, '')


class CPerform(CCustomPerform):
    m_SID = 51709
    m_Name = '次要伤害'
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

