# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51308.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51308.pyc
# Source Generated with Decompyle++
# File: p51308.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DICETAG_PERFORM, DICE_PUTOUT_POLL_ONE
from cl_newformula import Func303, Func717, Func804

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectInterval', 2500)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectInterval', 2000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectInterval', 1500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 300)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 4, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectInterval', 1200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 800)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ReduceCDWhenKill', 50)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 4, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectInterval', 600)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 1500)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ReduceCDWhenKill', 100)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 4, 0, 0)
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'MaxCover', 0, 1, 1)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EffectInterval'), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EffectInterval'), 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonAddCareerPfTempUseTimes(oWarrior, oEventCB.GetCBLifeCycle(), 1, 1, 1, 1)
    cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
        'pfid': 51308,
        'Item': (lambda *a: Func804(*a)) })


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.PassiveChangeCurCycleTime(oWarrior, oEventCB.GetCBLifeCycle(), -100)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'AttRatio' }) * Func303(*a, **{
'sAttr': 'MaxCover' })), 0, 0, 1, 1)


class CPerform(CCustomPerform):
    m_SID = 51308
    m_Name = '额外能源'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_PERFORM,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

