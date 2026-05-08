# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51387.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51387.pyc
# Source Generated with Decompyle++
# File: p51387.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_PERFORM, DICE_PUTOUT_POLL_TWO

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 2000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 0, 0, 0)
    cl_action.CommonChangeThrowPerformColdTime(oWarrior, oLifeCycle, 0, 150)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 2000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 0, 0, 0)
    cl_action.CommonChangeThrowPerformColdTime(oWarrior, oLifeCycle, 0, 200)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 3000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 0, 0, 0)
    cl_action.CommonChangeThrowPerformColdTime(oWarrior, oLifeCycle, 0, 150)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 4000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 0, 0, 0)
    cl_action.CommonChangeThrowPerformColdTime(oWarrior, oLifeCycle, 0, 150)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 6000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 0, 0, 0)
    cl_action.CommonChangeThrowPerformColdTime(oWarrior, oLifeCycle, 0, 100)
    cl_action.CommonChangeThrowPerformAttr(oWarrior, oLifeCycle, 'Radius', 6000, 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AttRatio'), 0, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 51387
    m_Name = '重磅炸弹'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_PERFORM,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

