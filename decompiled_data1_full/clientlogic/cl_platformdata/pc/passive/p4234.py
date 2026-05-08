# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4234.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4234.pyc
# Source Generated with Decompyle++
# File: p4234.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction4234 as CustomAction
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_HP, HP_RADIO_SUB, OBJ_SELF
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_ENERGY, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PFNODEKILLED_BEFORE, -1, 3, 0, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 5, HP_RADIO_SUB, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 2, 0, 0)
    if cl_condition.CheckPerformRecord(oWarrior, oLifeCycle, 39246) == 1:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 7994, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_ADD_ENERGY, -1)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 8021, 10, { }, -1, -1, None)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8008, 200, { }, 0, -1, None)
    cl_action.CommonNextFrameUpdateAI(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction1(oEventCB, oWarrior):
    if oWarrior.Energy() >= 30000 and cl_evcon.CheckMonsterPhase(oWarrior, oEventCB, 3):
        cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 7992)
        cl_evact.EventCBSetPhase(oWarrior, oEventCB, 4)
        cl_action.CommonNextFrameUpdateAI(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction2(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, { })
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 0.05), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 0, 0)
    cl_evact.EventCBHaltFlow(oWarrior, oEventCB)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventSetLimitDamage(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HP' }) - Func304(*a, **{
'sAttr': 'HPMax' }) * 0.05) + 1))


class CPerform(CCustomPerform):
    m_SID = 4234
    m_Name = '妖王-阶段3'
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

