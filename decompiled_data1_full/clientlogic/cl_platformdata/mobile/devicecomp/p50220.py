# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50220.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50220.pyc
# Source Generated with Decompyle++
# File: p50220.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_HERO, FROM_OWNER

def Action1(oWarrior, oLifeCycle):
    CustomAction(oWarrior, oLifeCycle, {
        'Phase': 2 })
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BARRIER_THROUGH, FROM_OWNER, 0)


def DisableAction1(oWarrior, oLifeCycle):
    CustomAction(oWarrior, oLifeCycle, {
        'Phase': 0 })


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'ExtraTimes', 2)


class CPerform(CCustomPerform):
    m_SID = 50220
    m_Name = '英雄核心'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1003,)
    m_ExclusiveHero = (214,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

