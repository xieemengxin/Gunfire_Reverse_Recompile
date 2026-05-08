# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15174.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15174.pyc
# Source Generated with Decompyle++
# File: p15174.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func343, Func602

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def CDAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckCostBulletType(oWarrior, oEventCB, 4508) and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 0) == 0 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: (Func343(*a, **{
'sid': 4508 }) / Func602(*a)) * 100)) < 50:
        cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 500)
        cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func602(*a) * 20 / 100), 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 0) == 0 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: (Func343(*a, **{
'sid': 4508 }) / Func602(*a)) * 100)) < 50:
        cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 500)
        cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func602(*a) * 20 / 100), 0)


class CPerform(CCustomPerform):
    m_SID = 15174
    m_Name = '法术回复'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = {
        1: CDAction1 }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

