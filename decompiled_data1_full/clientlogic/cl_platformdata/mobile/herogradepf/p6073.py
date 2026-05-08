# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6073.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6073.pyc
# Source Generated with Decompyle++
# File: p6073.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import OBJ_SELF, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MARKTARGET, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckMonsterIsPetrochemical(oWarrior, oEventCB) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32510, 0, 0, None):
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32510, 1, 0)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32510, 0, { }, 1, 0, None)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 32510, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 6073
    m_Name = '改版桃lv.3'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

