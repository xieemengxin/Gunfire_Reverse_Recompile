# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13550.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13550.pyc
# Source Generated with Decompyle++
# File: p13550.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, '1324ExtTarget') and cl_evcon.EventCBCheckPerformMode(oWarrior, oEventCB) > 0 and cl_evcon.PassiveCBGetExtraExecuteCount(oWarrior, oEventCB, 1328) < cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'times'):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 25, WARRIOR_MONSTER, 1, 0, 0, 0, 0, 0, None, None)
        cl_evact.PassiveCBExtraExecuteTarget(oWarrior, oEventCB, 1328, 32949, 95)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1328: 1,
        1324: 1 }, 1, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 5000, 0, '')


class CPerform(CCustomPerform):
    m_SID = 13550
    m_Name = '霜赐解脱'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = {
        'times': 1 }
    m_DieDisable = 0
    m_Career = 116

