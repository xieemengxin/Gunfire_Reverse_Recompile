# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4258.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4258.pyc
# Source Generated with Decompyle++
# File: p4258.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, DAM_TYPE_PERFORM, DAM_USE_ALL, WARRIOR_ELITE, WARRIOR_HERO, WARRIOR_MONSTER, WARRIOR_OBSTACLE_NORMAL
from cl_newformula import Func304, Func350

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 25, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVESUMMON, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: Func350(*a)), WARRIOR_HERO, None, 0, 0, None, None, { }, None, None, None, None, None)
    cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'Att' }) * 100 / 100 + 0), DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 1, None, None, None, None, None, None, None, None)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7968, 25, { }, 0, 0, None)
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: Func350(*a)), WARRIOR_ELITE, None, 0, 0, None, None, { }, None, None, None, None, None)
    cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'Att' }) * 100 / 100 + 0), DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 1, None, None, None, None, None, None, None, None)
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: Func350(*a)), WARRIOR_MONSTER, None, 0, 0, None, None, { }, None, None, None, None, None)
    cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'Att' }) * 100 / 100 + 0), DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 1, None, None, None, None, None, None, None, None)
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: Func350(*a)), WARRIOR_OBSTACLE_NORMAL, None, 0, 0, None, None, { }, None, None, None, None, None)
    cl_evact.EventTargetDamage(oWarrior, oEventCB, 50, DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 1, None, None, None, None, None, None, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ModelRadius', 4)
    cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MinSpeed', 100)
    cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ChangeDistance', 3)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 4258, 0, None, None)


class CPerform(CCustomPerform):
    m_SID = 4258
    m_Name = '二幕陷阱龙卷风'
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
    m_DieDisable = 0

