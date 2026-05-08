# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5351.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5351.pyc
# Source Generated with Decompyle++
# File: p5351.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, PF_SUBMSG_FILLBULLET

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf5351_Hit', 0) == 0:
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'pf5351_Hit', 1, 0)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'hit', 1)
        if cl_evcon.CheckWeaponHasInscription(oWarrior, oEventCB, 13123) or cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'hit') >= 1:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'hit', 0)
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8160, 0, { }, 1)
        elif cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'hit') >= 2:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'hit', 0)
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8160, 0, { }, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8160, 0, { }, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'hit', 0)


class CPerform(CCustomPerform):
    m_SID = 5351
    m_Name = '#NT#狂猎迭代新增被动'
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
        3: DoCallBackAction3 }
    m_BaseArgData = {
        'hit': 0 }
    m_DieDisable = 0

