# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4119.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4119.pyc
# Source Generated with Decompyle++
# File: p4119.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import HP_RADIO_SUB, OBJ_ATTACK, OBJ_SELF, WARRIOR_BOSS
from cl_newformula import Func205

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 70, HP_RADIO_SUB, 4)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 40, HP_RADIO_SUB, 5)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS) and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        39095: 1,
        39094: 1,
        1952: 1,
        1957: 1,
        1958: 1,
        1959: 1,
        39099: 1 }, 1, 0) == 0:
        if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 39091, 1, None):
            cl_evact.EventSetLimitDamage(oWarrior, oEventCB, (lambda *a: Func205(*a) * 300 + 100))
        elif cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 39096, 1, None):
            cl_evact.EventSetLimitDamage(oWarrior, oEventCB, (lambda *a: Func205(*a) * 300 + 200))
        else:
            cl_evact.EventSetLimitDamage(oWarrior, oEventCB, 1000)
    elif not cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1705, 1, 0):
        cl_evact.EventSetLimitDamage(oWarrior, oEventCB, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventClientBehavior(oWarrior, oEventCB, 70, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventClientBehavior(oWarrior, oEventCB, 73, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventClientBehavior(oWarrior, oEventCB, 74, 0)


class CPerform(CCustomPerform):
    m_SID = 4119
    m_Name = '石巨人召唤石柱受击效果'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0

