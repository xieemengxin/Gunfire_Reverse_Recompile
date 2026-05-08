# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50225.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50225.pyc
# Source Generated with Decompyle++
# File: p50225.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEVICECOMP_TYPE_HERO, DEVICE_UNIT_TYPE, DEVICE_USEPERFORM_POSTYPE_SERVANT, OBJ_ATTACK, PF_SUBMSG_DEVICEACTIVE
from cl_newformula import Func641

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeDevicePerformAttr(oWarrior, oLifeCycle, 7204, 'EnergyCost', 0, 5000)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_DEVICEACTIVE, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 7204, 0, 0):
        cl_evact.EventCBUnitUsePerformByPosType(oWarrior, oEventCB, 7204, DEVICE_UNIT_TYPE, DEVICE_USEPERFORM_POSTYPE_SERVANT, {
            'IgnoreCost': 1 })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func641(*a) * 2500), 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 50225
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
    m_ExclusiveDevice = (1001,)
    m_ExclusiveHero = (217,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

