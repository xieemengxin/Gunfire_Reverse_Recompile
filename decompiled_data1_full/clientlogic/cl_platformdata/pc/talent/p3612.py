# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3612.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3612.pyc
# Source Generated with Decompyle++
# File: p3612.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.talent.customaction import CustomAction3612 as CustomAction
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM
from cl_newformula import Func331, Func360, Func361, Func636

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetInInkArea(oWarrior, oEventCB):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: 3000 * Func636(*a)), 5000, 0, '')
    else:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: 3000 * Func636(*a)), 0, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        '1918_Radius': (lambda *a: Func360(*a, **{
'sid': 1918,
'sAttr': 'Radius' })),
        '1921_OuterRadius': (lambda *a: Func360(*a, **{
'sid': 1921,
'sAttr': 'Radius' })),
        '1921_InnerRadius': 8,
        'HeroStateTime': 0,
        'MonsterStateTime': 0,
        'MonsterEffect': (lambda *a: Func331(*a, **{
'sid': 3605 })),
        'DelayLeaveFrame': (lambda *a: Func361(*a, **{
'sid': 3605,
'sArgs': 'DelayLeaveFrame' })) })


def DoCallBackAction2(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'Clear': 1 })


class CPerform(CCustomPerform):
    m_SID = 3612
    m_Name = '乾坤墨移'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_MaxUpgradeTimes = 0
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 117

