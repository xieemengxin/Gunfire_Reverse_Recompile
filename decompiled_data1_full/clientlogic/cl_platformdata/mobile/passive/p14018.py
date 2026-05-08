# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p14018.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p14018.pyc
# Source Generated with Decompyle++
# File: p14018.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_HARDNESS, MONSTER_PART_SHIELD, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 22051, 'Time', 500, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_SHIELD):
        cl_evact.EventCBAddHitPart(oWarrior, oEventCB, DAM_TYPE_HARDNESS)
    if not cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_SHIELD):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -6000, 0, '')


class CPerform(CCustomPerform):
    m_SID = 14018
    m_Name = '轮回9-流寇电击者（无伤害计数版）'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

