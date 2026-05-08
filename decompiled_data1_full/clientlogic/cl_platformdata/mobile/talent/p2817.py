# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2817.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2817.pyc
# Source Generated with Decompyle++
# File: p2817.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_NORMAL, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_VICTIM
from cl_newformula import Func303

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_WEAPON) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32424):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func303(*a, **{
'sAttr': 'Att' }) * 0.3 + 1500), DAM_TYPE_WEAPON | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 0, 1, 0, None, None, None, None, None, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32424) and cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_WEAPON):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func303(*a, **{
'sAttr': 'Att' }) * 0.6 + 3000), DAM_TYPE_WEAPON | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 0, 1, 0, None, None, None, None, None, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32424) and cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_WEAPON):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func303(*a, **{
'sAttr': 'Att' }) + 6000), DAM_TYPE_WEAPON | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 0, 1, 0, None, None, None, None, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 2817
    m_Name = '妖星C5'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 108

