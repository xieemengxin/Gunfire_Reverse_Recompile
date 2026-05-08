# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p5030.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p5030.pyc
# Source Generated with Decompyle++
# File: p5030.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import MAIN_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetWeaponForceAttr(oWarrior, oLifeCycle, 'CrazyEff', 40000, MAIN_HOLD, 0, 0)
    cl_action.CommonSetWeaponForceAttr(oWarrior, oLifeCycle, 'CrazyEff', 40000, -1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREREMOVEWEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDWEAPON, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBClearWeaponForceAttr(oWarrior, oEventCB, 'CrazyEff')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonSetWeaponForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'CrazyEff', 40000, MAIN_HOLD, 0, 0)
    cl_action.CommonSetWeaponForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'CrazyEff', 40000, -1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5030
    m_Name = '我说了算'
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
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 1
    m_Career = 113

