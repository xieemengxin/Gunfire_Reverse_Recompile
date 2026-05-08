# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50214.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50214.pyc
# Source Generated with Decompyle++
# File: p50214.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_HERO, FROM_OWNER, USEPERFORM_POSTYPE_CARTOONEND
from cl_newformula import Func518

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 8013)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BARRIER_THROUGH, FROM_OWNER, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1313, 0, 0) and cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'ThroughBar1064'):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)
        cl_evact.EventChangeDeviceEnergy(oWarrior, oEventCB, (lambda *a: -400 * (100 - Func518(*a, **{
'sAttr': 'ReduceDeviceCost' })) // 100), 0)
        cl_evact.PassiveCBUsePerformAtMsgSkillPos(oWarrior, oEventCB, 8013, {
            'DirectPos': 1 }, USEPERFORM_POSTYPE_CARTOONEND)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBUpdateCustomPosInfo(oWarrior, oEventCB, {
        'ThroughBar1064': 1 })


class CPerform(CCustomPerform):
    m_SID = 50214
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
    m_ExclusiveHero = (212,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

