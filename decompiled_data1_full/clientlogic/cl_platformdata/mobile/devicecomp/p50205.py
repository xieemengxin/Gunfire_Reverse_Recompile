# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50205.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50205.pyc
# Source Generated with Decompyle++
# File: p50205.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_CORRISION, DAM_TYPE_ELEMENT, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, DEVICECOMP_TYPE_HERO, OBJ_ATTACK
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BARRIER_THROUGH, -1, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_ELEMENT, 1) == 0:
        cl_evact.EventSetSkillCache(oWarrior, oEventCB, 'ElementType', cl_condition.RandomChooseKey(oWarrior, oEventCB.GetCBLifeCycle(), {
            DAM_TYPE_THUNDER: 3334,
            DAM_TYPE_CORRISION: 3333,
            DAM_TYPE_FIRE: 3333 }))
        cl_evact.EventSetSkillCache(oWarrior, oEventCB, 'DebuffProb', 2000)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: ((Func304(*a, **{
'sAttr': 'MaxDeviceEnergy' }) - Func304(*a, **{
'sAttr': 'DeviceEnergy' })) / 100) * 250), 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 50205
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
    m_ExclusiveHero = (205,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

