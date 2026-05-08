# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51357.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51357.pyc
# Source Generated with Decompyle++
# File: p51357.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import COST_BAGBULLET_THROW, DICETAG_PERFORM, DICE_PUTOUT_POLL_TWO, OBJ_SELF
from cl_newformula import Func529, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BAGBULLETCHANGE_BEFOR, -1, 2, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StateTime', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCost', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RandomRatio', 10)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BAGBULLETCHANGE_BEFOR, -1, 2, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 15)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StateTime', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCost', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RandomRatio', 20)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BAGBULLETCHANGE_BEFOR, -1, 2, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StateTime', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCost', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RandomRatio', 30)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BAGBULLETCHANGE_BEFOR, -1, 2, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 25)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StateTime', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCost', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RandomRatio', 40)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BAGBULLETCHANGE_BEFOR, -1, 2, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 40)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StateTime', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCost', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RandomRatio', 50)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func529(*a))) > 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33810, 1, 1, 0, 0):
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33810, (lambda *a: Func717(*a, **{
'sArg': 'StateTime' })), { }, 1)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33810, (lambda *a: Func717(*a, **{
'sArg': 'AddDam' }) * Func529(*a)), 1, 1, (lambda *a: Func717(*a, **{
'sArg': 'StateTime' })))


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckCostBulletType(oWarrior, oEventCB, 4508) and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, (lambda *a: Func717(*a, **{
'sArg': 'RandomRatio' }))):
        cl_evact.EventCBAddBulletCost(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'AddCost' })))


class CPerform(CCustomPerform):
    m_SID = 51357
    m_Name = '#NT#多重施法'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_PERFORM,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

