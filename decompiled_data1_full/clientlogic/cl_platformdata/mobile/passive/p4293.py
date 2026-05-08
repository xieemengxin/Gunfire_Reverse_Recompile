# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4293.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4293.pyc
# Source Generated with Decompyle++
# File: p4293.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func686

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 3, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9513, 1, 0) and cl_evcon.EventCBGetSkillCacheBallisticType(oWarrior, oEventCB) == 1:
        cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'DebuffProb', 10000, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckShootStatus(oWarrior, oEventCB) and cl_evcon.GetPFBulletCount(oWarrior, oEventCB, 9513) >= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func686(*a, **{
'iPerform': 9513,
'sAttr': 'PFBulletUse' }))):
        cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'CrazyEff', 0, 5000)
    else:
        cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'CrazyEff', 0, 0)


class CPerform(CCustomPerform):
    m_SID = 4293
    m_Name = '电弧狙强化攻击'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

