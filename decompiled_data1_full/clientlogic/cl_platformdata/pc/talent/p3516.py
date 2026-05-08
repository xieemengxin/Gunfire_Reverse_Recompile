# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3516.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3516.pyc
# Source Generated with Decompyle++
# File: p3516.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import USEPERFORM_POSTYPE_CARTOONSTART

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 8016)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1429: 1,
        8010: 1,
        1432: 1 }, 1, 0) and not cl_condition.GetUsingSkillNumBySID(oWarrior, oEventCB.GetCBLifeCycle(), 8016, 1):
        cl_evact.PassiveCBUsePerformAtMsgSkillPos(oWarrior, oEventCB, 8016, {
            'TransDamFactor': cl_evact.EventCBGetPFTransDamFactor(oWarrior, oEventCB) }, USEPERFORM_POSTYPE_CARTOONSTART)


class CPerform(CCustomPerform):
    m_SID = 3516
    m_Name = '冰雪涡流'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 116

