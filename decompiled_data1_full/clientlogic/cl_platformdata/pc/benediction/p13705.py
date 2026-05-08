# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13705.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13705.pyc
# Source Generated with Decompyle++
# File: p13705.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import DAM_TYPE_PERFORM, PF_SUBMSG_THROW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 16)
    cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 3)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        1: 7500,
        2: 2500 }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, 10000, DAM_TYPE_PERFORM, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, 20000, DAM_TYPE_PERFORM, None, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        7144: 1,
        7151: 1 }, 0, 0):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            1: 7500,
            2: 2500 }, None)


class CPerform(CCustomPerform):
    m_SID = 13705
    m_Name = '技高一筹'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = None

