# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p6725.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p6725.pyc
# Source Generated with Decompyle++
# File: p6725.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, WARRIOR_BOSSCANNON, WARRIOR_SUMMON

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if not cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSSCANNON) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_SUMMON):
        cl_evact.EventCBDropTreasureDeadDrop(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 6725
    m_Name = '击杀怪物掉落宝珠'
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

