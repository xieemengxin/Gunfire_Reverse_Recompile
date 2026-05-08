# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3218.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3218.pyc
# Source Generated with Decompyle++
# File: p3218.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.talent.customaction import CustomAction3218 as CustomAction
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, GAMBLER_CHOOSE_EQUITY, GAMBLER_REPLACE_DEFAULT
from cl_newformula import Func331, Func560, Func563

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func560(*a))) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32851) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32851, 200, { }, 1, -1, None)
        CustomAction(oWarrior, oEventCB, {
            'CardNum': 3,
            'Perform': 12008,
            'QualityNum': 1 })


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func560(*a))) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32851) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32851, 200, { }, 1, -1, None)
        CustomAction(oWarrior, oEventCB, {
            'CardNum': 3,
            'Perform': 12008,
            'QualityNum': 2 })


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func560(*a))) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32851) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32851, 120, { }, 1, -1, 0)
        cl_action.CommonAppendQuality(oWarrior, oEventCB.GetCBLifeCycle(), 0, GAMBLER_CHOOSE_EQUITY, 1, 1, GAMBLER_REPLACE_DEFAULT, 1)
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func331(*a, **{
'sid': 3205 }))) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func560(*a))):
            if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func331(*a, **{
'sid': 3205 }))) == 3:
                CustomAction(oWarrior, oEventCB, {
                    'CardNum': 3,
                    'Perform': 12008,
                    'QualityNum': (lambda *a: Func563(*a)),
                    'ThrowMsg': 1 })
            else:
                CustomAction(oWarrior, oEventCB, {
                    'CardNum': 3,
                    'Perform': 12008,
                    'QualityNum': (lambda *a: Func331(*a, **{
'sid': 3205 }) + 1),
                    'ThrowMsg': 1 })
        else:
            CustomAction(oWarrior, oEventCB, {
                'CardNum': 3,
                'Perform': 12008,
                'QualityNum': 1,
                'ThrowMsg': 1 })


class CPerform(CCustomPerform):
    m_SID = 3218
    m_Name = '枪林牌雨'
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
        2: DoCallBackAction2,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 113

