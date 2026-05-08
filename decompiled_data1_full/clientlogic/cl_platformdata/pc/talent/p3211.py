# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3211.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3211.pyc
# Source Generated with Decompyle++
# File: p3211.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import GAMBLER_CHOOSE_EQUITY, GAMBLER_REPLACE_LOWEST, QUALITY_TYPE_CURSE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonModifyGrooveNum(oWarrior, oLifeCycle, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOM_USEPERFORM_BEFORE, -1, 0, 0, 2)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonModifyGrooveNum(oWarrior, oLifeCycle, 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOM_USEPERFORM_BEFORE, -1, 1, 0, 2)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonModifyGrooveNum(oWarrior, oLifeCycle, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOM_USEPERFORM_BEFORE, -1, 2, 0, 2)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetComb(oWarrior, oEventCB) == 1:
        cl_action.CommonAppendQuality(oWarrior, oEventCB.GetCBLifeCycle(), QUALITY_TYPE_CURSE, GAMBLER_CHOOSE_EQUITY, 0, 1, GAMBLER_REPLACE_LOWEST, None)
    else:
        cl_evact.EventCBAddMessageInfo(oWarrior, oEventCB, 'DamFactor', 4500)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetComb(oWarrior, oEventCB) == 1:
        cl_action.CommonAppendQuality(oWarrior, oEventCB.GetCBLifeCycle(), QUALITY_TYPE_CURSE, GAMBLER_CHOOSE_EQUITY, 0, 2, GAMBLER_REPLACE_LOWEST, None)
    else:
        cl_evact.EventCBAddMessageInfo(oWarrior, oEventCB, 'DamFactor', 9000)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetComb(oWarrior, oEventCB) == 1:
        cl_action.CommonAppendQuality(oWarrior, oEventCB.GetCBLifeCycle(), QUALITY_TYPE_CURSE, GAMBLER_CHOOSE_EQUITY, 0, 3, GAMBLER_REPLACE_LOWEST, None)
    else:
        cl_evact.EventCBAddMessageInfo(oWarrior, oEventCB, 'DamFactor', 15000)


class CPerform(CCustomPerform):
    m_SID = 3211
    m_Name = '命运之线'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 113

