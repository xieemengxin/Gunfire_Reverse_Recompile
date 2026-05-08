# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5320.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5320.pyc
# Source Generated with Decompyle++
# File: p5320.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, SKILLCACHE_CHARGELEVEL

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33554, 0, { }, 1)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0):
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'HitCrazy', 1, 0)
        if cl_evcon.EventCBCheckSkillCache(oWarrior, oEventCB, SKILLCACHE_CHARGELEVEL) != 1:
            cl_evact.PassiveCBAddEqualSouceWeaponStateCount(oWarrior, oEventCB, 33554, 1)


class CPerform(CCustomPerform):
    m_SID = 5320
    m_Name = '机瞄手枪被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

