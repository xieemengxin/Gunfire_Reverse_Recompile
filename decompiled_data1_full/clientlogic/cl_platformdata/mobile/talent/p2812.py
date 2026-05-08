# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2812.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2812.pyc
# Source Generated with Decompyle++
# File: p2812.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_SELF, PF_SUBMSG_THROW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 3, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1418, 0, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventGetTargetMaskMonsterAsTarget(oWarrior, oEventCB, 'MarkMonster32427', None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32454, 510, {
            'GainEffect': 700 + cl_action.CommonGetTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 2807) * 400 }, 0, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1418, 0, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventGetTargetMaskMonsterAsTarget(oWarrior, oEventCB, 'MarkMonster32427', None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32455, 710, {
            'GainEffect': 700 + cl_action.CommonGetTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 2807) * 400 }, 0, 0, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1418, 0, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventGetTargetMaskMonsterAsTarget(oWarrior, oEventCB, 'MarkMonster32427', None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32456, 1010, {
            'GainEffect': 700 + cl_action.CommonGetTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 2807) * 400 }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 2812
    m_Name = '妖星B6'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 108

