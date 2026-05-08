# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51620.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51620.pyc
# Source Generated with Decompyle++
# File: p51620.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, BOX_TREBLE_DAMAGE, DAM_TYPE_NORMAL, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_VICTIM
from cl_newformula import Func369, Func413, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 8)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 10)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 12)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Radius', 6)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExplodeThress', 5)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 15)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Radius', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExplodeThress', 5)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromWeapon(oWarrior, oEventCB, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExplodeThress'):
            if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 33932, 1, 0) <= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExplodeThress'):
                cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func369(*a) * Func413(*a, **{
'iState': 33932 }) * Func717(*a, **{
'sArg': 'DamRatio' }) / 100), DAM_TYPE_WEAPON | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 0, 0, 0, 0, 0, 0, BOX_TREBLE_DAMAGE, 0, None)
            elif cl_action.PassiveGetLiteCDRemainTime(oWarrior, oEventCB.GetCBLifeCycle()) == 0:
                cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 50)
                cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1748, {
                    'Radius': (lambda *a: Func717(*a, **{
'sArg': 'Radius' })),
                    'AttDam': (lambda *a: (Func717(*a, **{
'sArg': 'DamRatio' }) / 100) * Func369(*a) * Func413(*a, **{
'iState': 33932 })),
                    'vStart': cl_evact.EventCBGetHitPos(oWarrior, oEventCB) }, 0)
            elif cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 33932, 1, 0):
                cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func369(*a) * Func413(*a, **{
'iState': 33932 }) * Func717(*a, **{
'sArg': 'DamRatio' }) / 100), DAM_TYPE_WEAPON | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 0, 0, 0, 0, 0, 0, BOX_TREBLE_DAMAGE, 0, None)


class CPerform(CCustomPerform):
    m_SID = 51620
    m_Name = '毒雾-低频武器'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

