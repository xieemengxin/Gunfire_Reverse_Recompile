# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15121.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15121.pyc
# Source Generated with Decompyle++
# File: p15121.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.rewardpf.customaction import CustomAction15121 as CustomAction
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, FIGHT_KEY_WUDI, OBJECT_SELFOWNER, OBJ_SELF, OBJ_VICTIM
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfColdTime(oWarrior, oLifeCycle, 1500)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfColdTime(oWarrior, oLifeCycle, 1500)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfColdTime(oWarrior, oLifeCycle, 1500)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1973, 1, 1):
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'PF15121', 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 0) == 0 and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'PF15121', 0) and cl_evcon.EventCheckTargetSpecialKey(oWarrior, oEventCB, FIGHT_KEY_WUDI) == 0:
        cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 1500)
        cl_action.CommonTriggerSeasonSuitPerformShow(oWarrior, oEventCB.GetCBLifeCycle(), 15111)
        if cl_evcon.EventCBCheckIsMonsterGroup(oWarrior, oEventCB, {
            39211: 1 }):
            cl_evact.EventTargetGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_SELFOWNER)
            if cl_evcon.CheckTargetHasStateByAttacker(oWarrior, oEventCB, 33551, 0):
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33551, (lambda *a: 600 + 200 * Func308(*a)), {
                    'TalentLevel': (lambda *a: Func308(*a)),
                    'StateCount': 1,
                    'Att': 100,
                    'AbnormalSourceDam': cl_evact.EventGetTargeIDtByType(oWarrior, oEventCB, OBJ_SELF) }, 1, 1, 0)
            else:
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
                cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1733, {
                    'AID': cl_evact.EventGetTargeIDtByType(oWarrior, oEventCB, OBJ_SELF),
                    'TransmitDam': 100,
                    'StateCount': 1,
                    'DamReduce': 1,
                    'ChooseSelf': 1,
                    'TalentLevel': (lambda *a: Func308(*a)) }, None)
                cl_evact.EventTargetGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_SELFOWNER)
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33551, (lambda *a: 600 + 200 * Func308(*a)), {
                    'TalentLevel': (lambda *a: Func308(*a)),
                    'StateCount': 1,
                    'Att': 100,
                    'AbnormalSourceDam': cl_evact.EventGetTargeIDtByType(oWarrior, oEventCB, OBJ_SELF) }, 1, 1, 0)
        else:
            cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1733, {
                'AID': cl_evact.EventGetTargeIDtByType(oWarrior, oEventCB, OBJ_SELF),
                'TransmitDam': 100,
                'StateCount': 1,
                'DamReduce': 1,
                'ChooseSelf': 1,
                'TalentLevel': (lambda *a: Func308(*a)) }, None)


class CPerform(CCustomPerform):
    m_SID = 15121
    m_Name = '#NT#风行草偃'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

