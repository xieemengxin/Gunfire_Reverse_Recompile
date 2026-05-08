# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15019.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15019.pyc
# Source Generated with Decompyle++
# File: p15019.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import COST_BAGBULLET_THROW, JUMPFIGURE_KILLMONSTER
from cl_newformula import Func207, Func529, Func535

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1409, 'Att', 6000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, COST_BAGBULLET_THROW, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func535(*a))) > 0:
        cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: Func535(*a)), 1, JUMPFIGURE_KILLMONSTER, (lambda *a: Func535(*a)), None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckCostBulletType(oWarrior, oEventCB, 4508):
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 0 + Func207(*a))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func529(*a))):
            cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: -1 * Func529(*a)), 1, JUMPFIGURE_KILLMONSTER, (lambda *a: -1 * Func529(*a)), None)
        else:
            cl_evact.EventCBAddCash(oWarrior, oEventCB, (lambda *a: -Func207(*a)), 1, JUMPFIGURE_KILLMONSTER, (lambda *a: -1 * Func529(*a)), None)


class CPerform(CCustomPerform):
    m_SID = 15019
    m_Name = '铜币易爆'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

