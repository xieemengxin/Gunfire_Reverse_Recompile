# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13562.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13562.pyc
# Source Generated with Decompyle++
# File: p13562.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oWarrior, oLifeCycle, 'Radius', 10000, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33750, 0, {
        'WeaponDamRatio': 1500,
        'PerformDamRatio': 750 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB):
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 33780):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33750, 2, 1000)
        else:
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33750, 1, 1000)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33780):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33750, 2, 1000)
    else:
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33750, 1, 1000)


class CPerform(CCustomPerform):
    m_SID = 13562
    m_Name = '灵枢圣域'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 119

