# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16046.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16046.pyc
# Source Generated with Decompyle++
# File: p16046.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_EXCLUSIVE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GREATEWEAPON, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBChangeWeaponInscriptionNumBySource(oWarrior, oEventCB, INSCRIPTION_TYPE_EXCLUSIVE, 1, {
        1: 1,
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1 }, None)


class CPerform(CCustomPerform):
    m_SID = 16046
    m_Name = '顶级客户'
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

