# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3204.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3204.pyc
# Source Generated with Decompyle++
# File: p3204.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import QUALITY_TYPE_CURSE, QUALITY_TYPE_HIGH, QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL
from cl_newformula import Func543

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_GET_QUALITY, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32849, 0, { }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_GET_QUALITY, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32849, 0, { }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_GET_QUALITY, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32849, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckQuality(oWarrior, oEventCB, QUALITY_TYPE_LOW):
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32849, 1)
    elif cl_evcon.EventCBCheckQuality(oWarrior, oEventCB, QUALITY_TYPE_NORMAL):
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32849, 2)
    elif cl_evcon.EventCBCheckQuality(oWarrior, oEventCB, QUALITY_TYPE_HIGH):
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32849, 3)
    elif cl_evcon.EventCBCheckQuality(oWarrior, oEventCB, QUALITY_TYPE_CURSE):
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32849, (lambda *a: Func543(*a, **{
'dWeight': {
1: 1,
2: 1,
3: 1 } })))


class CPerform(CCustomPerform):
    m_SID = 3204
    m_Name = '完美牌组'
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
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 113

