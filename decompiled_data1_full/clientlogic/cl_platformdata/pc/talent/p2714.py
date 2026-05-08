# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2714.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2714.pyc
# Source Generated with Decompyle++
# File: p2714.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF
from cl_newformula import Func336

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1313, 1, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32532, 0, 0, None):
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32532, (lambda *a: Func336(*a, **{
'sKey': '1313-Curtimes' }) + 1), 800, 0)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32532, 0, { }, 1, 0, None)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32532, (lambda *a: Func336(*a, **{
'sKey': '1313-Curtimes' }) + 1), 800, 0)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 8503, 1, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32532, 0, 0, None):
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32532, (lambda *a: Func336(*a, **{
'sKey': '8503-TotalCount' })), 800, 0)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32532, 0, { }, 1, 0, None)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32532, (lambda *a: Func336(*a, **{
'sKey': '8503-TotalCount' })), 800, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1313, 1, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32532, 0, 0, None):
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32532, (lambda *a: Func336(*a, **{
'sKey': '1313-Curtimes' }) + 1), 1000, 0)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32532, 0, { }, 1, 0, None)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32532, (lambda *a: Func336(*a, **{
'sKey': '1313-Curtimes' }) + 1), 1000, 0)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 8503, 1, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32532, 0, 0, None):
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32532, (lambda *a: Func336(*a, **{
'sKey': '8503-TotalCount' })), 1000, 0)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32532, 0, { }, 1, 0, None)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32532, (lambda *a: Func336(*a, **{
'sKey': '8503-TotalCount' })), 1000, 0)


class CPerform(CCustomPerform):
    m_SID = 2714
    m_Name = '剑元通脉'
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
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 109

