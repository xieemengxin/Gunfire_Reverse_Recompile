# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50235.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50235.pyc
# Source Generated with Decompyle++
# File: p50235.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ADD_PARASITIC, DEVICECOMP_TYPE_HERO, DEVICE_UNIT_TYPE, DEVICE_USEPERFORM_POSTYPE_ENDPOS, OBJECT_DEVICE, OBJ_VICTIM
from cl_newformula import Func637, Func651, Func717, Func819

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'd50235_KeepTime', 400)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'd50235_CD', 700)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'd50235_AddScale', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENABLE_DEVICECOMP_CHANGE, -1, 1, 0, 0)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 5)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PARASITIC, ADD_PARASITIC, 6, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'GardenThrowDes') or cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'd50235_CD' })))
        cl_evact.EventCBUnitUsePerformByPosType(oWarrior, oEventCB, 7204, DEVICE_UNIT_TYPE, DEVICE_USEPERFORM_POSTYPE_ENDPOS, {
            'KeepTime': (lambda *a: Func717(*a, **{
'sArg': 'd50235_KeepTime' })),
            'IgnoreCost': 1,
            'd50235_flag': 1 })
    elif cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'GardenThrowHit'):
        cl_evact.EventCBSetTargetByID(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'VID' })))
        if cl_evcon.EventCBCheckTargetCDByMark(oWarrior, oEventCB, 'dc50235', 1):
            cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'DamInterval', 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.GetPerformAttrFromOwn(oWarrior, oEventCB.GetCBLifeCycle(), 7204, 'CommonMaxCount', OBJECT_DEVICE) > cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func819(*a, **{
'sid': 7204,
'sAttr': 'CommonMaxCount' }))):
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1436, 'CommonMaxCount', 0, (lambda *a: (Func637(*a, **{
'sid': 7204,
'sAttr': 'CommonMaxCount' }) - Func819(*a, **{
'sid': 7204,
'sAttr': 'CommonMaxCount' })) * Func717(*a, **{
'sArg': 'd50235_AddScale' })))
    else:
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1436, 'CommonMaxCount', 0, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 7204, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBAddTargetCDByMark(oWarrior, oEventCB, 'dc50235', 52, 1)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.EventCBSetTargetByID(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'VID' })))
    if cl_evcon.CheckReason(oWarrior, oEventCB, 'ST33710', 1) and cl_evcon.EventCBCheckTargetCDByMark(oWarrior, oEventCB, 'dc50235', 1):
        cl_evact.EventCBAddMessageInfo(oWarrior, oEventCB, 'AddCount', (lambda *a: Func651(*a, **{
'sKey': 'AddCount' }) + 1))


class CPerform(CCustomPerform):
    m_SID = 50235
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
        1: DoCallBackAction1,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1001,)
    m_ExclusiveHero = (221,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

