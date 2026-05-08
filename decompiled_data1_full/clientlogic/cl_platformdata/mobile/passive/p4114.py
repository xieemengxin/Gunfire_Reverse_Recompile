# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4114.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4114.pyc
# Source Generated with Decompyle++
# File: p4114.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_TYPE_NORMAL, DAM_TYPE_SCENE, DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, OBJ_SELF
from cl_newformula import Func304, Func311, Func312, Func313

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if oWarrior.HP() > 100 or oWarrior.Shield() > 0 or oWarrior.Armor() > 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' })) * 2 / 100 + 0), DAM_TYPE_SCENE | DAM_TYPE_NORMAL | DAM_USE_HP | DAM_USE_SHIELD | DAM_USE_ARMOR, 1, 1, None, 0, None, None, None, None, None, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 4114, 0, None):
        cl_evact.EventSetLimitDamage(oWarrior, oEventCB, (lambda *a: Func311(*a) * 100 / 100 + Func312(*a) * 100 / 100 + Func313(*a) * 100 / 100 + -100))


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetHeroTarget(oWarrior, oEventCB, 1, 1, None, None)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 3)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 1185, None, None, None, None) == 0:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1185, 200, { }, 0, None, None)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' })) * 10 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP | DAM_USE_SHIELD | DAM_USE_ARMOR, 1, None, None)
        cl_evact.EventClientBehavior(oWarrior, oEventCB, 1007, 0)


class CPerform(CCustomPerform):
    m_SID = 4114
    m_Name = '挑战事件越战越勇A'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

