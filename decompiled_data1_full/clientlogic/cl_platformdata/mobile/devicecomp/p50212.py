# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50212.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50212.pyc
# Source Generated with Decompyle++
# File: p50212.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEVICECOMP_TYPE_HERO, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MARKTARGET, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1419: 1,
        8004: 1,
        8013: 1 }, 0, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1419, 0, 0):
            if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32500, 0, 1, 0):
                cl_evact.EventCBAddTargetToxicStateCount(oWarrior, oEventCB, {
                    'AddCount': 1 })
            if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DamageNum') >= 7:
                cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'DamageNum', 0)
                cl_evact.EventCBAddTargetToxicStateCount(oWarrior, oEventCB, {
                    'AddCount': 1 })
            else:
                cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'DamageNum', 1)
        elif oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DamageNum') >= 7:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'DamageNum', 0)
            cl_evact.EventCBAddTargetToxicStateCount(oWarrior, oEventCB, {
                'AddCount': 1 })
        else:
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'DamageNum', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventCBAddTargetToxicStateCount(oWarrior, oEventCB, {
        'AddCount': 1 })


class CPerform(CCustomPerform):
    m_SID = 50212
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
    m_BaseArgData = {
        'DamageNum': 0 }
    m_DieDisable = 0
    m_ExclusiveDevice = (1001,)
    m_ExclusiveHero = (212,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

