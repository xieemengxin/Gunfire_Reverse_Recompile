# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50226.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50226.pyc
# Source Generated with Decompyle++
# File: p50226.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_HERO, HATEMETHOD_HERODIS, OBJECT_DEVICE, SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY
from cl_newformula import Func639

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonOwnObjAddPerform(oWarrior, oLifeCycle, 7207, OBJECT_DEVICE)
    cl_action.CommonOwnObjAddPerform(oWarrior, oLifeCycle, 7208, OBJECT_DEVICE)
    cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 1, 0, 0)
    cl_action.CommonChangeDevicePerformAttr(oWarrior, oLifeCycle, 7208, 'TriggerTimes', 4 * (cl_action.CommonGetTalentLevel(oWarrior, oLifeCycle, 3310) + 1), 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENABLE_DEVICECOMP_CHANGE, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 7150, 0, 0):
        cl_evact.EventCBGetLockEnemy(oWarrior, oEventCB, OBJECT_DEVICE, 1, SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY, HATEMETHOD_HERODIS, {
            'Range': (lambda *a: Func639(*a, **{
'sAttr': 'HitRange' })) })
        cl_evact.EventCBDeviceUsePerformEvtTarget(oWarrior, oEventCB, 7207, {
            'Att': (lambda *a: Func639(*a, **{
'sAttr': 'Att' })) }, None)
    elif cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 7151, 0, 0):
        cl_evact.EventCBGetLockEnemy(oWarrior, oEventCB, OBJECT_DEVICE, 1, SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY, HATEMETHOD_HERODIS, {
            'Range': (lambda *a: Func639(*a, **{
'sAttr': 'HitRange' })) })
        cl_evact.EventCBDeviceUsePerformEvtTarget(oWarrior, oEventCB, 7208, {
            'Att': (lambda *a: Func639(*a, **{
'sAttr': 'Att' })),
            'ChooseSelf': 1 }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckTalent(oWarrior, oEventCB, 3310):
        cl_action.CommonChangeDevicePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 7208, 'TriggerTimes', 4 * (cl_action.CommonGetTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 3310) + 1), 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_condition.CheckEnabledPerform(oWarrior, oEventCB.GetCBLifeCycle(), 50121):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33152, 0, { }, 1, 0, None)
    else:
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33152, 0)


class CPerform(CCustomPerform):
    m_SID = 50226
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1002,)
    m_ExclusiveHero = (217,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 1
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

