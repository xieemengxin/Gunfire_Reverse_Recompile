# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2513.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2513.pyc
# Source Generated with Decompyle++
# File: p2513.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import PF_SUBMSG_THROW
from cl_newformula import Func336

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1415, 'Att', 0, 2000)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1415, 'Att', 0, 3500)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1415, 'Att', 0, 5000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32385, (lambda *a: Func336(*a, **{
'sKey': 'KeepTime' })), {
        'LuckyHit': 20,
        'GainEffect': cl_evact.EventCBGetSkillCacheAttr(oWarrior, oEventCB, 'GainEffect') }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 2513
    m_Name = '暴烈药剂'
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
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 106

