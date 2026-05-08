# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2911.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2911.pyc
# Source Generated with Decompyle++
# File: p2911.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_SELF
from cl_newformula import Func331, Func430

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'Radius', 0, 1)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'AttDistance', 0, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'Radius', 0, 2)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'AttDistance', 0, 2)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 1, 0, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'Radius', 0, 3)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'AttDistance', 0, 3)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 4347, 'FullEnergyTime', 300, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 0, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32775, (lambda *a: 2 * Func331(*a, **{
'sid': 2911 }) + 2), (lambda *a: 200 + Func430(*a, **{
'sid': 32853 })), -1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 0, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32775, 8, (lambda *a: 300 + Func430(*a, **{
'sid': 32853 })), -1)


class CPerform(CCustomPerform):
    m_SID = 2911
    m_Name = '逐积跬步'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 110

