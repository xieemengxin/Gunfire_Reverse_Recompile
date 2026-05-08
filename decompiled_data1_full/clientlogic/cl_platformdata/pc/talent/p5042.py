# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p5042.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p5042.pyc
# Source Generated with Decompyle++
# File: p5042.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, BOX_TREBLE_DAMAGE, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_SELF, OBJ_VICTIM, PF_TYPE_SHOOT
from cl_newformula import Func360, Func361, Func369

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1439, 1, 0) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p5042', 0) == 0:
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'p5042', 1, 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Source', cl_evact.EventGetTargeID(oWarrior, oEventCB))
        cl_evact.EventCBLionLockStateSearchEnemy(oWarrior, oEventCB, 12, 1, 1, 0, 1, 0, {
            cl_evact.EventGetTargeID(oWarrior, oEventCB): 1 }, 1)
        if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
            cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 8020, 0, {
                'Source': (lambda *a: Func361(*a, **{
'sid': 5042,
'sArgs': 'Source' })),
                'StateTime': (lambda *a: Func360(*a, **{
'sid': 1439,
'sAttr': 'KeepTime' })),
                'LockStateKeepTime': (lambda *a: Func360(*a, **{
'sid': 1439,
'sAttr': 'AddStateTime' })) }, None)
        else:
            cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), 6000, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_SHOOT, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.EventCBCheckAffectedByLion(oWarrior, oEventCB, 1, 1, 1):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventGetTargetMaskMonsterAsTarget(oWarrior, oEventCB, 'StrengthLockState', 1)
            cl_evact.EventCBRemoveFromTargetList(oWarrior, oEventCB, cl_evact.EventGetTargeIDtByType(oWarrior, oEventCB, OBJ_VICTIM))
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func369(*a)), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 0, 0, 0, 0, BOX_TREBLE_DAMAGE, None, None)


class CPerform(CCustomPerform):
    m_SID = 5042
    m_Name = '云囚镇渊'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 1
    m_Career = 118

