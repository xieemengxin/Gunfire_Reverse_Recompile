# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50230.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50230.pyc
# Source Generated with Decompyle++
# File: p50230.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEVICECOMP_TYPE_HERO, OBJ_VICTIM
from cl_newformula import Func637, Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HIT_FLAW_BEFORE, -1, 0, 0, 0)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEVICEACTIVE_COST_BEFORE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckBreakFlaw(oWarrior, oEventCB, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBDeviceUsePerformEvtTarget(oWarrior, oEventCB, 7200, {
            'ExtraUse': 1 }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1910, 1, 0) == 0:
        cl_evact.EventCBHitUnbalance(oWarrior, oEventCB, 2500)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 7200, 1, 0) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'ExtraUse' }))):
        cl_evact.EventSetEnergyCost(oWarrior, oEventCB, (lambda *a: Func637(*a, **{
'sid': 7200,
'sAttr': 'EnergyCost' }) * 2))


class CPerform(CCustomPerform):
    m_SID = 50230
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1002,)
    m_ExclusiveHero = (218,)
    m_ExcludeComp = ()
    m_DropShape = 5561
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_HERO
    m_FirstChooseExtWeight = 0

