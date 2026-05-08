# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p13079.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p13079.pyc
# Source Generated with Decompyle++
# File: p13079.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DPSUBMSG_NOFIRE, INSCRIPTION_TYPE_RARE, ITEMPERFORM_ENABLE_HOLD, OBJ_SELF, OBJ_VICTIM
from cl_newformula import Func369

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, DPSUBMSG_NOFIRE, 1, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, DPSUBMSG_NOFIRE, 2, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 3, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 25):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 50)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33288, 0, 1, 0, 0):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33288, 0, { }, 0, 0, 0)
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: 0.5 * Func369(*a))) > cl_evcon.EventCBCheckTargetStateStatistics(oWarrior, oEventCB, 33288, 'pf13079_Dam', 1, 0):
            cl_evact.EventCBSetTargetStateStatistics(oWarrior, oEventCB, 33288, 'pf13079_Dam', (lambda *a: 0.5 * Func369(*a)), 1, 0, 0)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33288, 1, 1, 0, 300)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'st33288_stop', 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'st33288_stop', 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB) and cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'st33288_stop', 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBDelTargetCustomData(oWarrior, oEventCB, 'st33288_stop')


class CPerform(CCustomPerform):
    m_SID = 13079
    m_Name = '法杖专属词条3'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_RARE
    m_ElementType = None
    m_LimitList = ((23, 24), (), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

