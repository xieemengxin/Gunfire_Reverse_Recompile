# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2713.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2713.pyc
# Source Generated with Decompyle++
# File: p2713.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_war
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, WARRIOR_SUMMON

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 10):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32536, 0, 1, None) == 0 and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_SUMMON) == 0:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32536, 0, { }, 0, 1, None)
            CustomAction(oWarrior, oEventCB, {
                'PerformId': 8503,
                'MulAtt': 1 })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 10):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32536, 0, 1, None) == 0 and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_SUMMON) == 0:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32536, 0, { }, 0, 1, None)
            CustomAction(oWarrior, oEventCB, {
                'PerformId': 8503,
                'MulAtt': 1.5 })


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 10):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32536, 0, 1, None) == 0 and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_SUMMON) == 0:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32536, 0, { }, 0, 1, None)
            CustomAction(oWarrior, oEventCB, {
                'PerformId': 8503,
                'MulAtt': 2 })


class CPerform(CCustomPerform):
    m_SID = 2713
    m_Name = '人剑合一'
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
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 109


def CustomAction(oWarrior, oEventCB, dInfo):
    oPerform = oWarrior.GetPerform(dInfo['PerformId'])
    if not oPerform:
        return None
    dTransInfo = oEventCB.GetCBTransInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    lstTarget = dTransInfo['TargetList']
    if not lstTarget:
        return None
    iVictim = lstTarget[0]
    dData = { }
    dData['Custom'] = {
        'lstHitVictim': [
            iVictim],
        'MulAtt': dInfo['MulAtt'],
        'pfid': dEventInfo['pfid'] }
    cl_war.UsePerform(oWarrior, oPerform, dData)

