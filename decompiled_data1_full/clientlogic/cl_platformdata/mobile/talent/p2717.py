# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2717.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2717.pyc
# Source Generated with Decompyle++
# File: p2717.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_SHIELD, OBJ_SELF, PF_SUBMSG_CAREERPF
from cl_newformula import Func308, Func331, Func336

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1313, 1, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32512, 0, 0, None):
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32512, (lambda *a: Func336(*a, **{
'sKey': '1313-Curtimes' }) + 1), (lambda *a: 500 + Func308(*a) * 100), 0)
            cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func331(*a, **{
'sid': 2717 }) * 100 + 100), CURE_TYPE_PERFORM | DAM_USE_SHIELD, 0, 0, None)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32512, 0, { }, 1, 0, None)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32512, (lambda *a: Func336(*a, **{
'sKey': '1313-Curtimes' }) + 1), (lambda *a: 500 + Func308(*a) * 100), 0)
            cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func331(*a, **{
'sid': 2717 }) * 100 + 100), CURE_TYPE_PERFORM | DAM_USE_SHIELD, 0, 0, None)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 8503, 1, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32512, 0, 0, None):
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32512, (lambda *a: Func336(*a, **{
'sKey': '8503-TotalCount' })), (lambda *a: 500 + Func308(*a) * 100), 0)
            cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func331(*a, **{
'sid': 2717 }) * 100 + 100), CURE_TYPE_PERFORM | DAM_USE_SHIELD, 0, 0, None)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32512, 0, { }, 1, 0, None)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32512, (lambda *a: Func336(*a, **{
'sKey': '8503-TotalCount' })), (lambda *a: 500 + Func308(*a) * 100), 0)
            cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func331(*a, **{
'sid': 2717 }) * 100 + 100), CURE_TYPE_PERFORM | DAM_USE_SHIELD, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 2717
    m_Name = '剑元固体'
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
    m_Career = 109

