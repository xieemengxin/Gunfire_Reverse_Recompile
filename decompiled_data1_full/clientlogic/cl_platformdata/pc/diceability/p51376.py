# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51376.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51376.pyc
# Source Generated with Decompyle++
# File: p51376.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_USE_HP, DICETAG_WEAPON, DICE_PUTOUT_POLL_ONE, OBJ_SELF
from cl_newformula import Func304, Func651, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CureRatio', 5)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CureRatio', 10)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LuckyHit', 30)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CureRatio', 30)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33837, 0, {
        'LuckyHit': (lambda *a: Func717(*a, **{
'sArg': 'LuckyHit' })) }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LuckyHit', 50)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CureRatio', 40)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33837, 0, {
        'LuckyHit': (lambda *a: Func717(*a, **{
'sArg': 'LuckyHit' })) }, 1)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LuckyHit', 80)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CureRatio', 60)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33837, 0, {
        'LuckyHit': (lambda *a: Func717(*a, **{
'sArg': 'LuckyHit' })) }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'NewBullet' }))):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * Func717(*a, **{
'sArg': 'CureRatio' }) // 100), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'LuckyHit' })))


class CPerform(CCustomPerform):
    m_SID = 51376
    m_Name = '幸运回复'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_WEAPON,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

