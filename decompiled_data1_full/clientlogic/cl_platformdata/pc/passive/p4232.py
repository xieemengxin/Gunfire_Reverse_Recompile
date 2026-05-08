# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4232.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4232.pyc
# Source Generated with Decompyle++
# File: p4232.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import HP_RADIO_SUB, OBJ_SELF
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 75, HP_RADIO_SUB, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_ENERGY, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PFNODEKILLED_BEFORE, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if oWarrior.Energy() <= 5000:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7994, 0, { }, 0, 0, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8022, 10, { }, -1, -1, None)
        cl_action.CommonNextFrameUpdateAI(oWarrior, oEventCB.GetCBLifeCycle())
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8022, 10, { }, -1, -1, None)
        cl_action.CommonNextFrameUpdateAI(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction1(oEventCB, oWarrior):
    if oWarrior.Energy() >= 7000:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8022, 10, { }, -1, -1, None)
        cl_action.CommonNextFrameUpdateAI(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction2(oEventCB, oWarrior):
    if oWarrior.Energy() >= 5000 and oWarrior.Energy() < 7000 and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('pf_4232') == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7994, 0, { }, 0, 0, None)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'pf_4232', 1)
    elif oWarrior.Energy() >= 7000:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8022, 10, { }, -1, -1, None)
        cl_action.CommonNextFrameUpdateAI(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventSetLimitDamage(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HP' }) - Func304(*a, **{
'sAttr': 'HPMax' }) * 0.75) + 1))


class CPerform(CCustomPerform):
    m_SID = 4232
    m_Name = '妖王-阶段1'
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

