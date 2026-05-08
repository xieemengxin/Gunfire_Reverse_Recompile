# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3205.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3205.pyc
# Source Generated with Decompyle++
# File: p3205.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import PF_SUBMSG_THROW
from cl_newformula import Func560, Func563

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 10)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 10)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 2, 0, 10)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1424, 1, 0) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func560(*a))):
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'QualityNum', 2, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1424, 1, 0) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func560(*a))):
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'QualityNum', 3, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1424, 1, 0) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func560(*a))):
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'QualityNum', (lambda *a: Func563(*a)), None)


class CPerform(CCustomPerform):
    m_SID = 3205
    m_Name = '镜像手牌'
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
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 113

