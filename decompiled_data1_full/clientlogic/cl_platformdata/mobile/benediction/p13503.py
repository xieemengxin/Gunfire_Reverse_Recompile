# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13503.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13503.pyc
# Source Generated with Decompyle++
# File: p13503.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11133, 1)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1409, 1, 0):
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1394, 0, 0, None):
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 1395, 1, 100, 0)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1394, 0, { }, 1, 0, None)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1395, 0, { }, 1, 0, None)
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 1395, 1, 100, 0)


class CPerform(CCustomPerform):
    m_SID = 13503
    m_Name = '乾坤一掷'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 101

