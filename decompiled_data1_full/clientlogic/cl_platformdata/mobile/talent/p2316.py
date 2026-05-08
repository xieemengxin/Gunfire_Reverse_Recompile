# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2316.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2316.pyc
# Source Generated with Decompyle++
# File: p2316.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1412, 'DamInterval', 0, 2)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1413, 'DamInterval', 0, 2)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 2)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1412, 'DamInterval', 0, 3)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1413, 'DamInterval', 0, 3)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 4)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1412, 'DamInterval', 0, 4)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1413, 'DamInterval', 0, 4)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 6)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 20028) and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1412: 1,
        1413: 1 }, 0, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventAddBagBullet(oWarrior, oEventCB, 4508, 1)


class CPerform(CCustomPerform):
    m_SID = 2316
    m_Name = '役电妙法'
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
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 104

