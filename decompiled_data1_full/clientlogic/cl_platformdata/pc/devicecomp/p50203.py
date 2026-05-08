# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50203.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50203.pyc
# Source Generated with Decompyle++
# File: p50203.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_HERO, DEVICE_UNIT_TYPE, DEVICE_USEPERFORM_POSTYPE_ENDPOS
from cl_newformula import Func360

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1410: 1,
        8001: 1 }, 0, 0) and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 200)
        cl_evact.EventCBUnitUsePerformByPosType(oWarrior, oEventCB, 7204, DEVICE_UNIT_TYPE, DEVICE_USEPERFORM_POSTYPE_ENDPOS, {
            'KeepTime': (lambda *a: Func360(*a, **{
'sid': 1410,
'sAttr': 'KeepTime' }) // 3),
            'IgnoreCost': 1 })


class CPerform(CCustomPerform):
    m_SID = 50203
    m_Name = '英雄核心'
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
    m_ExclusiveDevice = (1001,)
    m_ExclusiveHero = (205,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

