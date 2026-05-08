# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4397.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4397.pyc
# Source Generated with Decompyle++
# File: p4397.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, PLAYMODE_SURVIVOR, SKILLCACHE_PERFORMMODE
from cl_newformula import Func611

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32967, 0, { }, 1)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    if cl_condition.CheckWarPlayMode(oWarrior, oLifeCycle, PLAYMODE_SURVIVOR):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33276, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1324: 1,
        1328: 1 }, 1, 0):
        if cl_evcon.EventCBCheckSkillCache(oWarrior, oEventCB, SKILLCACHE_PERFORMMODE) >= 1:
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 10000, 0, '')
        if cl_evcon.EventCBCheckDamageHasTag(oWarrior, oEventCB, 'Single'):
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: 15000 + Func611(*a) * 10), 0, 'Single')


class CPerform(CCustomPerform):
    m_SID = 4397
    m_Name = '处决大师被动'
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

