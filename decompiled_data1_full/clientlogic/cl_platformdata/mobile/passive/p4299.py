# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4299.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4299.pyc
# Source Generated with Decompyle++
# File: p4299.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import HP_RADIO_SUB
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 85, HP_RADIO_SUB, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PFNODEKILLED_BEFORE, -1, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7085, 0, { }, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8084, 0, { }, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8096, 0, { }, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetPhase(oWarrior, oEventCB, 2)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventSetLimitDamage(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HP' }) - Func304(*a, **{
'sAttr': 'HPMax' }) * 0.85) + 1))


class CPerform(CCustomPerform):
    m_SID = 4299
    m_Name = '【诡谲雪山】罗睺-阶段1'
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

