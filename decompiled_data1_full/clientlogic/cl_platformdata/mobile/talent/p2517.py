# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2517.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2517.pyc
# Source Generated with Decompyle++
# File: p2517.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import PF_SUBMSG_THROW
from cl_newformula import Func331, Func336

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1415, 'AddStateTime', 0, 200)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 0, 0, 0)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'Adrenaline_REnergy', 500)


def DisableAction1(oWarrior, oLifeCycle):
    oWarrior.Delete('Adrenaline_REnergy')


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1415, 'AddStateTime', 0, 300)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 0, 0, 0)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'Adrenaline_REnergy', 700)


def DisableAction2(oWarrior, oLifeCycle):
    oWarrior.Delete('Adrenaline_REnergy')


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1415, 'AddStateTime', 0, 400)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 0, 0, 0)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'Adrenaline_REnergy', 900)


def DisableAction3(oWarrior, oLifeCycle):
    oWarrior.Delete('Adrenaline_REnergy')


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32398, (lambda *a: Func336(*a, **{
'sKey': 'KeepTime' })), {
        'TalentLevel': (lambda *a: Func331(*a, **{
'sid': 2517 })) }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 2517
    m_Name = '持久药剂'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 106

