# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13739.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13739.pyc
# Source Generated with Decompyle++
# File: p13739.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, FLAW_KILLLINE, MONSTER_PART_FLAW, MONSTER_PART_WEAKNESSFLAW, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33031, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_FLAW) or cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_WEAKNESSFLAW):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBAddTargetFlawAddition(oWarrior, oEventCB, FLAW_KILLLINE, 0, 100, 0)


class CPerform(CCustomPerform):
    m_SID = 13739
    m_Name = '#NT#提高斩杀线'
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
    m_Career = 116

