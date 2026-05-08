# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5303.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5303.pyc
# Source Generated with Decompyle++
# File: p5303.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CRT_RANGECHECK_ENTER, CRT_RANGECHECK_EXIT, OBJ_VICTIM, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCRT_RANGECHECK, CRT_RANGECHECK_ENTER, 0, 0, 1)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCRT_RANGECHECK, CRT_RANGECHECK_EXIT, 1, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER):
            if cl_evcon.CheckHasStateFromSelf(oWarrior, oEventCB, 1896) == 0:
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1896, 0, { }, 1, 0, None)
            else:
                cl_evact.EventCBSetTargetStateCount(oWarrior, oEventCB, 1896, 1, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventCBSetTargetStateStatistics(oWarrior, oEventCB, 1896, 'OnArea', 0, 1, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9701: 1,
        9792: 1 }, 0, 0) and cl_evcon.CheckAttackInShield(oWarrior, oEventCB) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER) and cl_evcon.CheckHasStateFromSelf(oWarrior, oEventCB, 1896) == 0:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1896, 0, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 5303
    m_Name = '标记法杖标记被动-版本2'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

