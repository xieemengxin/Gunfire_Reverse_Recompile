# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5349.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5349.pyc
# Source Generated with Decompyle++
# File: p5349.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, PF_SUBMSG_FILLBULLET, WARRIOR_MONSTER
from cl_newformula import Func444, Func780

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 2000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 9, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveSubSourceWeaponPointPerformColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 9507, 132, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func444(*a))) > 0:
        if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32246, 1, 0, 0) and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
                cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 50)
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33912, 24, { }, 0, 1, 0)
            cl_evact.EventCBSetUsePerformData(oWarrior, oEventCB, 'TargetPos', cl_evact.EventCBGetTargetHitPos(oWarrior, oEventCB), 1, 1)
            cl_evact.EventCBCustomUsePerform(oWarrior, oEventCB, 2000, { }, {
                'Radius': (lambda *a: 8 + Func780(*a, **{
'sKey': '13119ExtraRadius' })),
                'ExtraDiffuse': (lambda *a: Func780(*a, **{
'sKey': '13120ExtraDiffuse' })) }, 0)
            cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: 8 + Func780(*a, **{
'sKey': '13119ExtraRadius' })), WARRIOR_MONSTER, 1, 0, 0, 0, 0, 0, None)
            cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 6)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32246, 350, { }, 0, 1, 0)
        cl_evact.EventCBAddTargetFromSameItemStateStatistics(oWarrior, oEventCB, (lambda *a: Func444(*a) * (100 + Func780(*a, **{
'sKey': '13120RecordDamMul' })) // 1000), 32246, 'st32246_TotalDam')


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) and cl_condition.CommonCheckItemTmpData(oWarrior, oEventCB.GetCBLifeCycle(), '13119ExtraAddState') and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32246, 1, 0, 0):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33912, 24, { }, 0, 1, 0)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32246, 350, { }, 0, 1, 0)
    cl_evact.EventCBAddTargetFromSameItemStateStatistics(oWarrior, oEventCB, (lambda *a: Func444(*a) * (100 + Func780(*a, **{
'sKey': '13120RecordDamMul' })) * (1 + Func780(*a, **{
'sKey': '13120ExtraDiffuse' })) // 1000), 32246, 'st32246_TotalDam')


def DoCallBackAction9(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        cl_action.PassiveSubSourceWeaponPointPerformColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 9507, 132, 0)


class CPerform(CCustomPerform):
    m_SID = 5349
    m_Name = '#NT#迭代棱刺流血状态和切枪减CD'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        6: DoCallBackAction6,
        9: DoCallBackAction9 }
    m_BaseArgData = { }
    m_DieDisable = 0

