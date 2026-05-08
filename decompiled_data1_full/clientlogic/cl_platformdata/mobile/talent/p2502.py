# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2502.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2502.pyc
# Source Generated with Decompyle++
# File: p2502.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, DAM_TYPE_PERFORM, DAM_USE_ALL, WARRIOR_BARRIER, WARRIOR_MONSTER
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVESUMMON, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVESUMMON, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVESUMMON, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckSummonFightType(oWarrior, oEventCB, WARRIOR_BARRIER) and cl_evcon.GetSummonAttr(oWarrior, oEventCB, 'HP') <= 0:
        cl_evact.EventGetTargetByMsgInfoSummonID(oWarrior, oEventCB)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, cl_action.CommonGetTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 2502) * 2 + 8, WARRIOR_MONSTER, None, 1, 0, -1, None, None, None)
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2502) == 1:
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'EnergyMax' }) - Func304(*a, **{
'sAttr': 'Energy' })) * 3), DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 1, None, None, None, None, None, None, None, None)
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2502) == 2:
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'EnergyMax' }) - Func304(*a, **{
'sAttr': 'Energy' })) * 6), DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 1, None, None, None, None, None, None, None, None)
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2502) == 3:
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'EnergyMax' }) - Func304(*a, **{
'sAttr': 'Energy' })) * 9), DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 1, None, None, None, None, None, None, None, None)
    elif cl_evcon.CheckSummonFightType(oWarrior, oEventCB, WARRIOR_BARRIER):
        pass
    if cl_evcon.GetSummonAttr(oWarrior, oEventCB, 'HP') > 0:
        cl_evact.EventGetTargetByMsgInfoSummonID(oWarrior, oEventCB)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, cl_action.CommonGetTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 2502) * 2 + 8, WARRIOR_MONSTER, None, 1, 0, -1, None, None, None)
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2502) == 1:
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'EnergyMax' }) - Func304(*a, **{
'sAttr': 'Energy' })) * 2), DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 1, None, None, None, None, None, None, None, None)
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2502) == 2:
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'EnergyMax' }) - Func304(*a, **{
'sAttr': 'Energy' })) * 4), DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 1, None, None, None, None, None, None, None, None)
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2502) == 3:
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'EnergyMax' }) - Func304(*a, **{
'sAttr': 'Energy' })) * 6), DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 1, None, None, None, None, None, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 2502
    m_Name = '能量震荡'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 106

