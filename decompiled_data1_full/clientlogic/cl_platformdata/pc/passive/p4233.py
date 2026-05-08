# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4233.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4233.pyc
# Source Generated with Decompyle++
# File: p4233.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import HP_RADIO_SUB, OBJ_SELF
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 40, HP_RADIO_SUB, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_ENERGY, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PFNODEKILLED_BEFORE, -1, 3, 0, 0)
    if cl_condition.CheckPerformRecord(oWarrior, oLifeCycle, 39246) == 0:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 7994, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if oWarrior.Energy() <= 17000:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7994, 0, { }, 0, 0, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8023, 10, { }, -1, -1, None)
        cl_action.CommonNextFrameUpdateAI(oWarrior, oEventCB.GetCBLifeCycle())
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8023, 10, { }, -1, -1, None)
        cl_action.CommonNextFrameUpdateAI(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction1(oEventCB, oWarrior):
    if oWarrior.Energy() >= 18000:
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 8023) == 0 and cl_condition.CheckPerformRecord(oWarrior, oEventCB.GetCBLifeCycle(), 39246) == 1:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 7992)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8023, 10, { }, -1, -1, None)
        cl_action.CommonNextFrameUpdateAI(oWarrior, oEventCB.GetCBLifeCycle())
    elif oWarrior.Energy() >= 17000 and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('pf_4233') == 0 and cl_evcon.CBCheckCastingSkill(oWarrior, oEventCB, 39246) == 1:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 7992)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'pf_4233', 1)
    elif oWarrior.Energy() >= 17000 and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('pf_4233') <= 1 and cl_evcon.CBCheckCastingSkill(oWarrior, oEventCB, 39246) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if not cl_condition.GetCustomData(oWarrior, oEventCB.GetCBLifeCycle(), 'UnusedSkill'):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7994, 0, { }, 0, 0, None)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'pf_4233', 2)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventSetLimitDamage(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HP' }) - Func304(*a, **{
'sAttr': 'HPMax' }) * 0.4) + 1))


class CPerform(CCustomPerform):
    m_SID = 4233
    m_Name = '妖王-阶段2'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

