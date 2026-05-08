# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p4482.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p4482.pyc
# Source Generated with Decompyle++
# File: p4482.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckDamIsExplosion(oWarrior, oEventCB):
        if cl_evcon.CheckHitVictimCnt(oWarrior, oEventCB, 1) or cl_evcon.CheckHitVictimCnt(oWarrior, oEventCB, 2):
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 5000, 0, 0, '')
            cl_evact.PassiveCBSetAttackIgnoreShield(oWarrior, oEventCB)
            cl_evact.PassiveCBSetAttackIgnoreArmor(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 4482
    m_Name = '爆炸无视护盾护甲'
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

