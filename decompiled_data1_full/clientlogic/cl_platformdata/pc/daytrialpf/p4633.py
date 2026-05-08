# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p4633.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p4633.pyc
# Source Generated with Decompyle++
# File: p4633.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import OBJ_ATTACK, OBJ_VICTIM
from cl_newformula import Func207

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDCASH, -1, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1297, 0, { }, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, (lambda *a: Func207(*a) * 2), 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1297, (lambda *a: Func207(*a) * 0.02 // 1))


class CPerform(CCustomPerform):
    m_SID = 4633
    m_Name = '英雄额外受到金币数0.02%的伤害'
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

