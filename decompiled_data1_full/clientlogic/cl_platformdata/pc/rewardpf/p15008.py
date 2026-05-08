# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15008.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15008.pyc
# Source Generated with Decompyle++
# File: p15008.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, EQUIP_SHOTGUN, OBJ_VICTIM
from cl_newformula import Func204, Func302

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 1543, -1, 1, None, None):
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1543, 1, -1)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1543, -1, -1) >= 30:
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: min(int(Func302(*a, **{
'sAttr': 'HPMax' }) * 15 / 100), int(500000 * Func204(*a)))), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, -1, -1, 0, -1, -1, -1, None, None, None, None)
            cl_evact.EventCBSetTargetStateCount(oWarrior, oEventCB, 1543, 0, None)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1543, 0, { }, -1, -1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'Trajectory', 0, 2000, EQUIP_SHOTGUN)


class CPerform(CCustomPerform):
    m_SID = 15008
    m_Name = '破碎之击'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

