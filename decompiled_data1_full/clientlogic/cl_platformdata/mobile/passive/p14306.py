# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p14306.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p14306.pyc
# Source Generated with Decompyle++
# File: p14306.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MONSTER_PART_ATTACH, MONSTER_PART_ATTACH_HARDNESS, MONSTER_PART_ATTACH_WEAKNESS, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_ATTACH) or cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_ATTACH_HARDNESS) or cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_ATTACH_WEAKNESS):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 2000, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSetDamageRatio(oWarrior, oEventCB, 10000, 0)


class CPerform(CCustomPerform):
    m_SID = 14306
    m_Name = '精英骑乘怪坐骑-轮回10被动'
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

