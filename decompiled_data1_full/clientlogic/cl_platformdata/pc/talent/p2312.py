# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2312.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2312.pyc
# Source Generated with Decompyle++
# File: p2312.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1305, 'AddStateTime', 0, 300)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32006):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 5000, 0, 0, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32006):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 20028) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1670, -1, -1) == 0:
            cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1670, {
                'TransDamFactor': cl_action.CommonGetStateTransDamFactor(oWarrior, oEventCB.GetCBLifeCycle(), 32006) }, None)


class CPerform(CCustomPerform):
    m_SID = 2312
    m_Name = '电激雷引'
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
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 104

