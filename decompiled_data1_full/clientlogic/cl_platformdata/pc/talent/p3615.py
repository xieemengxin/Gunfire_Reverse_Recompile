# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3615.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3615.pyc
# Source Generated with Decompyle++
# File: p3615.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func3, Func308, Func361, Func385, Func386

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3615, 'MaxCount', 3, None)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 1000, 1000, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 5, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3615, 'MaxCount', 4, None)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 900, 900, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 5, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3615, 'MaxCount', 4, None)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 800, 800, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33266, 600, { }, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33266, 600, { }, 1, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'PFBulletCost', (lambda *a: Func385(*a)))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func3(*a, **{
'a': int(Func386(*a, **{
'sAttr': 'MaxPFBullet' }) * (375 - Func308(*a) * 25)),
'b': 100 }))):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CostThreshold', (lambda *a: Func386(*a, **{
'sAttr': 'MaxPFBullet' }) * (375 - Func308(*a) * 25) // 100 + 1))
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CostThreshold', (lambda *a: Func386(*a, **{
'sAttr': 'MaxPFBullet' }) * (325 - Func308(*a) * 25) // 100))
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'PFBulletCost') >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 3615,
'sArgs': 'CostThreshold' }))):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'PFBulletCost', 0)
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 33268):
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33268, 1, 0)
        else:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33268, 0, {
                'MaxCount': (lambda *a: Func361(*a, **{
'sid': 3615,
'sArgs': 'MaxCount' })) }, 1)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33268):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33268, 1, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33268, 0, {
            'MaxCount': (lambda *a: Func361(*a, **{
'sid': 3615,
'sArgs': 'MaxCount' })) }, 1)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'PFBulletCost', 0)


class CPerform(CCustomPerform):
    m_SID = 3615
    m_Name = '墨染凡尘'
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
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 117

