# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3119.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3119.pyc
# Source Generated with Decompyle++
# File: p3119.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, FIREFALL_MULTI_DAMAGE, OBJ_ATTACK, PF_TYPE_THROW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 10, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 14, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 19, 0, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventCBSetDamShowTipsType(oWarrior, oEventCB, FIREFALL_MULTI_DAMAGE)


def DoCallBackAction10(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None):
        if cl_evcon.CheckTalent(oWarrior, oEventCB, 5023) or cl_evcon.EventCBGetHitVictimCnt(oWarrior, oEventCB) <= 3:
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 10000, DAM_TYPE_PERFORM, '')
            cl_evact.EventCBSetDamShowTipsType(oWarrior, oEventCB, FIREFALL_MULTI_DAMAGE)
        elif cl_evcon.EventCBGetHitVictimCnt(oWarrior, oEventCB) <= 1:
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 10000, DAM_TYPE_PERFORM, '')
            cl_evact.EventCBSetDamShowTipsType(oWarrior, oEventCB, FIREFALL_MULTI_DAMAGE)


def DoCallBackAction14(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None):
        if cl_evcon.CheckTalent(oWarrior, oEventCB, 5023) or cl_evcon.EventCBGetHitVictimCnt(oWarrior, oEventCB) <= 3:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
            if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 20000, DAM_TYPE_PERFORM, '')
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 30000, DAM_TYPE_PERFORM, '')
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 20000, DAM_TYPE_PERFORM, '')
            else:
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 10000, DAM_TYPE_PERFORM, '')
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 20000, DAM_TYPE_PERFORM, '')
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 10000, DAM_TYPE_PERFORM, '')
            cl_evact.EventCBSetDamShowTipsType(oWarrior, oEventCB, FIREFALL_MULTI_DAMAGE)
        elif cl_evcon.EventCBGetHitVictimCnt(oWarrior, oEventCB) <= 1:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
            if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 20000, DAM_TYPE_PERFORM, '')
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 30000, DAM_TYPE_PERFORM, '')
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 20000, DAM_TYPE_PERFORM, '')
            else:
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 10000, DAM_TYPE_PERFORM, '')
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 20000, DAM_TYPE_PERFORM, '')
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 10000, DAM_TYPE_PERFORM, '')
            cl_evact.EventCBSetDamShowTipsType(oWarrior, oEventCB, FIREFALL_MULTI_DAMAGE)


def DoCallBackAction19(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None):
        if cl_evcon.CheckTalent(oWarrior, oEventCB, 5023) or cl_evcon.EventCBGetHitVictimCnt(oWarrior, oEventCB) <= 6:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
            if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 20):
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 30000, DAM_TYPE_PERFORM, '')
            else:
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 20000, DAM_TYPE_PERFORM, '')
            cl_evact.EventCBSetDamShowTipsType(oWarrior, oEventCB, FIREFALL_MULTI_DAMAGE)
        elif cl_evcon.EventCBGetHitVictimCnt(oWarrior, oEventCB) <= 1:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
            if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 20):
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 30000, DAM_TYPE_PERFORM, '')
            else:
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 20000, DAM_TYPE_PERFORM, '')
            cl_evact.EventCBSetDamShowTipsType(oWarrior, oEventCB, FIREFALL_MULTI_DAMAGE)


class CPerform(CCustomPerform):
    m_SID = 3119
    m_Name = '降世之焱'
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
        5: DoCallBackAction5,
        10: DoCallBackAction10,
        14: DoCallBackAction14,
        19: DoCallBackAction19 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 112

