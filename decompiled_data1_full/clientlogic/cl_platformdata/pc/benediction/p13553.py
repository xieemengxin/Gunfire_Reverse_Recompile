# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13553.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13553.pyc
# Source Generated with Decompyle++
# File: p13553.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_newformula import Func564

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1429: 1,
        1432: 1,
        8010: 1,
        8016: 1 }, 1, 0):
        cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 1, 1, 20, 1, 1, { })
    elif cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1433, 1, 0) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: 100 / (cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Prob') / 100) ** Func564(*a))):
        cl_evact.PassiveCBRecordParentActNum(oWarrior, oEventCB)
        cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 1, 1, 20, 1, 1, { })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBExplodeRangeFlaw(oWarrior, oEventCB, 1433)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1429: 1,
        1432: 1,
        8010: 1,
        1433: 1 }, 1, 0):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, 0, 0, -1, None)


class CPerform(CCustomPerform):
    m_SID = 13553
    m_Name = '冰破残响'
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
        4: DoCallBackAction4 }
    m_BaseArgData = {
        'Prob': 200 }
    m_DieDisable = 0
    m_Career = 116

