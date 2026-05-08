# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50231.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50231.pyc
# Source Generated with Decompyle++
# File: p50231.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEVICECOMP_TYPE_HERO, OBJ_ATTACK
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33713, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY_BEFORE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 1) and cl_evcon.EventCBCheckDamageBuffByBarrier(oWarrior, oEventCB, 1):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 2000, 0, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33713, (lambda *a: Func304(*a, **{
'sAttr': 'DeviceEnergy' }) // 1000), 0)


class CPerform(CCustomPerform):
    m_SID = 50231
    m_Name = '英雄核心'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1003,)
    m_ExclusiveHero = (218,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

