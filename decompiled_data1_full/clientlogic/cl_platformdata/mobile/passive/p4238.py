# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4238.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4238.pyc
# Source Generated with Decompyle++
# File: p4238.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MONSTER_PART_ATTACH, MONSTER_PART_ATTACH_HARDNESS, MONSTER_PART_ATTACH_WEAKNESS, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE_MAIN, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CREATEMONSTER, -1, 1, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_PHASE, -1, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBTransAttach(oWarrior, oEventCB, {
        'AttSpeed': 1,
        'HP': 1,
        'MoveSpeed': 1,
        'm_RunSpeedUpMul': 1,
        'm_SprintSpeedUpMul': 1 })
    if oWarrior.HP() > 0:
        cl_evact.EventCBSetPhase(oWarrior, oEventCB, 2)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBCreatePart(oWarrior, oEventCB, 33812, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_ATTACH) or cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_ATTACH_HARDNESS) or cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_ATTACH_WEAKNESS):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 2000, 0, '')


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBSetDamageRatio(oWarrior, oEventCB, 10000, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'NewPhase') == 2:
        cl_action.CommonSetCustomData(oWarrior, oEventCB.GetCBLifeCycle(), 'UnbalanceResetState', 'KnightReconnect')
    else:
        cl_action.CommonSetCustomData(oWarrior, oEventCB.GetCBLifeCycle(), 'UnbalanceResetState', 'reset')


class CPerform(CCustomPerform):
    m_SID = 4238
    m_Name = '精英骑乘怪被动'
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
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0

