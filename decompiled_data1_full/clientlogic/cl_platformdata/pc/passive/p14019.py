# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14019.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14019.pyc
# Source Generated with Decompyle++
# File: p14019.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import HP_RADIO_ADD, HP_RADIO_SUB, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 50, HP_RADIO_SUB, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 50, HP_RADIO_ADD, 2)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'Toughness', 10, 5000, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -4000, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 1500, 0, -1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 0, 0, -1)


class CPerform(CCustomPerform):
    m_SID = 14019
    m_Name = '轮回9-荒漠泰坦（无伤害计数版）'
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

