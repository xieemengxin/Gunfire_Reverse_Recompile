# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15164.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15164.pyc
# Source Generated with Decompyle++
# File: p15164.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM
from cl_newformula import Func214

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckReason(oWarrior, oEventCB, 'attackcost', 0) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 25):
        cl_evact.EventCBCostSourceWeaponBullet(oWarrior, oEventCB, 1, 1)
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'DamageCnt', 1, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckReason(oWarrior, oEventCB, 'attackcost', 0) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func214(*a))) > 0 and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 25):
        cl_evact.EventCBCostSourceWeaponBagBullet(oWarrior, oEventCB, 1)
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'DamageCnt', 1, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetInSkillCollect(oWarrior, oEventCB, 'RC15164') == 0 and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'DamageCnt', 1):
        cl_evact.EventCBRecordSkillCollectTarget(oWarrior, oEventCB, 'RC15164', 0)
        cl_evact.EventTargetSputterDamage(oWarrior, oEventCB, 50, 1, 0, 1, 1, 1, 1, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 15164
    m_Name = '融合弹药'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

