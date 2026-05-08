# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15204.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15204.pyc
# Source Generated with Decompyle++
# File: p15204.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.rewardpf.customaction import CustomAction15204 as CustomAction
from . import CPerform as CCustomPerform
from cl_commondefines import SUIT_HANDLE_EACHREPLACE, SUIT_HANDLE_REFRESH_WEAPONGRADE
from cl_newformula import Func207

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, SUIT_HANDLE_EACHREPLACE, 0, 0, 0)
    if cl_condition.CheckOpenElement(oWarrior, oLifeCycle, {
        'WeaponStoreElement': 1 }):
        cl_action.CommonSendSuitHandleInfo(oWarrior, oLifeCycle, SUIT_HANDLE_EACHREPLACE, { }, cl_action.CommonGetHistoryWeapon(oWarrior, oLifeCycle))


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckSuitChosenHistoryWeapon(oWarrior, oEventCB):
        cl_evact.EventCBSendNotify(oWarrior, oEventCB, 1, 9698, { })
    elif cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func207(*a))) >= 1200:
        cl_action.CommonAddWarCash(oWarrior, oEventCB.GetCBLifeCycle(), -1200)
        CustomAction(oWarrior, oEventCB, { })
        cl_evact.EventCBSendNotify(oWarrior, oEventCB, 1, 9695, { })
        cl_action.CommonSendSuitHandleInfo(oWarrior, oEventCB.GetCBLifeCycle(), SUIT_HANDLE_REFRESH_WEAPONGRADE, {
            'SuccessFlag': 1 }, None)


class CPerform(CCustomPerform):
    m_SID = 15204
    m_Name = '移形换月'
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

