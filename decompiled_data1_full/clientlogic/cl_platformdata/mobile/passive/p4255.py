# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4255.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4255.pyc
# Source Generated with Decompyle++
# File: p4255.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_WEAPON, OBJ_ATTACK, STATE_EFF_DEBAR, STATE_EFF_SUBSPD, STATE_EFF_VERTIGO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)
    cl_action.CommonIgnoreStateEffectAdd(oWarrior, oLifeCycle, STATE_EFF_DEBAR, None)
    cl_action.CommonIgnoreStateEffectAdd(oWarrior, oLifeCycle, STATE_EFF_SUBSPD, None)
    cl_action.CommonIgnoreStateEffectAdd(oWarrior, oLifeCycle, STATE_EFF_VERTIGO, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 20652, 0, { })


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 20652, 1, None) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 20651, 1, None) or cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_WEAPON) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1422, 1, 1):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, -10000, 0, '')


class CPerform(CCustomPerform):
    m_SID = 4255
    m_Name = '四幕投雷怪鱼雷死亡爆炸'
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

