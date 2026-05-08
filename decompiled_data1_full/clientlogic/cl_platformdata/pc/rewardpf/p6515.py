# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p6515.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p6515.pyc
# Source Generated with Decompyle++
# File: p6515.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'ColdTime', (lambda *a: Func308(*a) * -500 + 0), 0, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_CAREER_PERFORM, -1, 0, 0, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'ColdTime', (lambda *a: Func308(*a) * -500 + 0), 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'ColdTime', (lambda *a: Func308(*a) * -500 + 0), 0, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_CAREER_PERFORM, -1, 0, 0, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'ColdTime', (lambda *a: Func308(*a) * -500 + 0), 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'ColdTime', (lambda *a: Func308(*a) * -500 + 0), 0, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_CAREER_PERFORM, -1, 0, 0, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'ColdTime', (lambda *a: Func308(*a) * -500 + 0), 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'ColdTime', (lambda *a: Func308(*a) * -500 + 0), 0, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_CAREER_PERFORM, -1, 0, 0, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'ColdTime', (lambda *a: Func308(*a) * -500 + 0), 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'ColdTime', (lambda *a: Func308(*a) * -500 + 0), 0, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_CAREER_PERFORM, -1, 0, 0, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'ColdTime', (lambda *a: Func308(*a) * -500 + 0), 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ColdTime', (lambda *a: Func308(*a) * -500 + 0), 0, None)


class CPerform(CCustomPerform):
    m_SID = 6515
    m_Name = '冷却时间'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

