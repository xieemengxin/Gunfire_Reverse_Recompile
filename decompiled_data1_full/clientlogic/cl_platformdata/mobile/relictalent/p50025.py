# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relictalent/p50025.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relictalent/p50025.pyc
# Source Generated with Decompyle++
# File: p50025.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_ATTACK, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1914, 'LockedTime', (0, None, ((361, 50025, 'Level1LockedTime'), (lambda a0: a0))))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50025, 'DamAddition', (0, None, ((361, 50025, 'Level1DamAddition'), (lambda a0: a0))))


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1914, 'LockedTime', (0, None, ((361, 50025, 'Level2LockedTime'), (lambda a0: a0))))


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1914, 'LockedTime', (0, None, ((361, 50025, 'Level3LockedTime'), (lambda a0: a0))))


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1914, 1, 0) and cl_evcon.EventCBCheckAddImmobilize(oWarrior, oEventCB):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'DamAddition'), 0, DAM_TYPE_PERFORM)


class CPerform(CCustomPerform):
    m_SID = 50025
    m_Name = '步步惊雷迭代版觉醒三'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = {
        'Level1LockedTime': 100,
        'Level2LockedTime': 200,
        'Level3LockedTime': 300,
        'Level1DamAddition': 5000,
        'Level2DamAddition': 7000,
        'Level3DamAddition': 9000 }
    m_DieDisable = 0
    m_GrowPF = []

