# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5830.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5830.pyc
# Source Generated with Decompyle++
# File: p5830.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_TYPE_AMULET, OBJ_VICTIM, QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL
from cl_newformula import Func207

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1421, 1, 1, None):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1421, 300, { }, 1, 1, None)
        cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 1936, 0, {
            'Att': (lambda *a: Func207(*a) * 200) }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1421, 1, 1, None):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1421, 200, { }, 1, 1, None)
        cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 1936, 0, {
            'Att': (lambda *a: Func207(*a) * 200) }, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponType(oWarrior, oEventCB, EQUIP_TYPE_AMULET):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1421, 1, 1, None):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1421, 300, { }, 1, 1, None)
            cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 1936, 0, {
                'Att': (lambda *a: Func207(*a) * 200) }, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponType(oWarrior, oEventCB, EQUIP_TYPE_AMULET):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1421, 1, 1, None):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1421, 200, { }, 1, 1, None)
            cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 1936, 0, {
                'Att': (lambda *a: Func207(*a) * 200) }, None)


class CPerform(CCustomPerform):
    m_SID = 5830
    m_Name = '贵气凌人'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

