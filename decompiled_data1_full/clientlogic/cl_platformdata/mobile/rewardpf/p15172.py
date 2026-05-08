# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15172.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15172.pyc
# Source Generated with Decompyle++
# File: p15172.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, BRIGHTEN_DAMAGE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 7, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 7, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 219):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 8, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 7, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 7, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 219):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 8, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 7, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 7, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 219):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 8, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 20):
        cl_action.CommonTriggerSeasonSuitPerformShow(oWarrior, oEventCB.GetCBLifeCycle(), 15181)
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 10000, 0, 0, 1, None)
        cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, 0, 50)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CD', 50)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 80):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 3000, 0, 0, 1, None)
    else:
        cl_action.CommonTriggerSeasonSuitPerformShow(oWarrior, oEventCB.GetCBLifeCycle(), 15181)
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 10000, 0, 0, 1, None)
        cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, 0, 75)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CD', 75)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 80):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 6000, 0, 0, 1, None)
        cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, 0, 20)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CD', 20)
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 33388):
            cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33388, 1, None)
        else:
            cl_action.CommonTriggerSeasonSuitPerformShow(oWarrior, oEventCB.GetCBLifeCycle(), 15181)
            cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 20000, 0, 0, 1, None)
            if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
                1301: 1,
                1305: 1,
                1325: 1,
                12013: 1 }, 1, 0):
                if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33388) == 0:
                    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33388, 0, { }, 1, 0, 0)
                else:
                    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33388, 0)
            elif cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33384) == 0:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33384, 0, { }, 1, 0, 0)


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_evcon.EventCBGetSkillDamFactorFormItem(oWarrior, oEventCB):
        cl_evact.EventCBAddShowTipsEffect(oWarrior, oEventCB, BRIGHTEN_DAMAGE)


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33044) and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CD') > 0:
        cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CD'))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CD', 0)


class CPerform(CCustomPerform):
    m_SID = 15172
    m_Name = '#NT#法术研习套装'
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
        2: DoCallBackAction2,
        7: DoCallBackAction7,
        8: DoCallBackAction8 }
    m_BaseArgData = { }
    m_DieDisable = 0

