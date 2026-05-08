# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51902.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51902.pyc
# Source Generated with Decompyle++
# File: p51902.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'PF52002_att', 80000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'PF52002_att', 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'PF52002_att', 160000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'PF52002_att', 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'PF52002_att', 320000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'PF52002_att', 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBModifyS8ThirdItemEnergy(oWarrior, oEventCB, 5)


class CPerform(CCustomPerform):
    m_SID = 51902
    m_Name = '超级蘑菇'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

