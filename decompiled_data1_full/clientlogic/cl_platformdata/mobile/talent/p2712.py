# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2712.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2712.pyc
# Source Generated with Decompyle++
# File: p2712.pyc (Python 3.6)

from cl_commondefines import BASEATTR_REFRESH
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_war
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, WARRIOR_SUMMON
from cl_newformula import Func410, Func428

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1419: 1,
        8013: 1 }, 1, 0) and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_SUMMON) == 0 and cl_evcon.CheckMonsterIsPetrochemical(oWarrior, oEventCB) == 0:
        cl_evact.EventSetSkillHitInfo(oWarrior, oEventCB)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1419: 1,
        8013: 1 }, 1, 0):
        cl_evact.EventGetTargetSkillHitInfo(oWarrior, oEventCB)
        cl_evact.EventRandomTargetExecCBFuncAction(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 32505 })), None)
        CustomAction(oWarrior, oEventCB, {
            'PerformId': 8503,
            'MulAtt': 1 })


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1419: 1,
        8013: 1 }, 1, 0):
        cl_evact.EventGetTargetSkillHitInfo(oWarrior, oEventCB)
        cl_evact.EventRandomTargetExecCBFuncAction(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 32505 }) * 2), None)
        CustomAction(oWarrior, oEventCB, {
            'PerformId': 8503,
            'MulAtt': 1 })


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1419: 1,
        8013: 1 }, 1, 0):
        cl_evact.EventGetTargetSkillHitInfo(oWarrior, oEventCB)
        cl_evact.EventRandomTargetExecCBFuncAction(oWarrior, oEventCB, (lambda *a: Func428(*a, **{
'sid': 32505 }) * 2.5 // 1), None)
        CustomAction(oWarrior, oEventCB, {
            'PerformId': 8503,
            'MulAtt': 1 })


class CPerform(CCustomPerform):
    m_SID = 2712
    m_Name = '花剑相随'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 109


def CustomAction(oWarrior, oEventCB, dInfo):
    dTransInfo = oEventCB.GetCBTransInfo()
    lstTarget = dTransInfo['TargetList']
    dCollectTarget = { }
    if not lstTarget:
        return None
    oPerform = oWarrior.GetPerform(dInfo['PerformId'])
    dData = { }
    dData['Custom'] = {
        'lstHitVictim': lstTarget,
        'MulAtt': dInfo['MulAtt'] }
    cl_war.UsePerform(oWarrior, oPerform, dData)

