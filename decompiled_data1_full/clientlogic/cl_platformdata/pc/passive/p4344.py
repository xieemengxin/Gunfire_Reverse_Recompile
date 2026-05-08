# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4344.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4344.pyc
# Source Generated with Decompyle++
# File: p4344.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 7150)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 7150)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 7150)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7150, 'Att', 0, 120000)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7150, 'ColdTime', 0, -200)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 7150)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 7150)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7150, 'Att', 0, 240000)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7150, 'ColdTime', 0, -400)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 7150)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 7150, 1, 1) and cl_evcon.CheckHitVictimCnt(oWarrior, oEventCB, 1):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, 6000, 0, None, None)


class CPerform(CCustomPerform):
    m_SID = 4344
    m_Name = '御灵师仆从E6'
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

