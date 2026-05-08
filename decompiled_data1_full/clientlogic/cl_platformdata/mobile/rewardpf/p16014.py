# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16014.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16014.pyc
# Source Generated with Decompyle++
# File: p16014.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import EQUIP_TYPE_CLOSEWEAPON, MAIN_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckWeaponTypeByHoldType(oWarrior, oEventCB.GetCBLifeCycle(), MAIN_HOLD, EQUIP_TYPE_CLOSEWEAPON):
        cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'AttSpeed', 0, 3000, MAIN_HOLD, { })


class CPerform(CCustomPerform):
    m_SID = 16014
    m_Name = '狂风剑法'
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

