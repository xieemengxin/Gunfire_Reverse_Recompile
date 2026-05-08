# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15103.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15103.pyc
# Source Generated with Decompyle++
# File: p15103.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import PF_SUBMSG_CAREERPF
from cl_newformula import Func332

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformForceAttr(oWarrior, oLifeCycle, 1310, 'ColdTime', 400)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 3, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformForceAttr(oWarrior, oLifeCycle, 1310, 'ColdTime', 200)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 4, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0):
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1949, 0, {
            '1949Att': (lambda *a: 60000 + 30000 * Func332(*a)) })


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0):
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1949, 0, {
            '1949Att': (lambda *a: 120000 + 60000 * Func332(*a)),
            '1949Add': 1 })


class CPerform(CCustomPerform):
    m_SID = 15103
    m_Name = '冲刺套装'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = {
        '15103Mul': 20000 }
    m_DieDisable = 0

