# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4222.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4222.pyc
# Source Generated with Decompyle++
# File: p4222.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_WEAPON, HITPART_DIRECTPOS, MONSTER_PART_ATTACH, MONSTER_PART_ATTACH_HARDNESS, MONSTER_PART_ATTACH_WEAKNESS

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE_MAIN, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CREATEMONSTER, -1, 1, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_PHASE, -1, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBTransAttach(oWarrior, oEventCB, {
        'AttSpeed': 1,
        'HP': 1,
        'MoveSpeed': 1,
        'm_RunSpeedUpMul': 1,
        'm_SprintSpeedUpMul': 1 })
    if oWarrior.HP() > 0:
        cl_evact.EventCBSetPhase(oWarrior, oEventCB, 3)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBCreatePart(oWarrior, oEventCB, 23812, 2)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckMonsterPhase(oWarrior, oEventCB, 1):
        if cl_evcon.CheckHitPart(oWarrior, oEventCB, HITPART_DIRECTPOS) or cl_evcon.CheckDamIsExplosion(oWarrior, oEventCB):
            cl_evact.EventCBSetDamageRatio(oWarrior, oEventCB, 5000, 5000)
        elif cl_evcon.CheckHitPart(oWarrior, oEventCB, HITPART_DIRECTPOS) == 0 and cl_evcon.CheckDamIsExplosion(oWarrior, oEventCB) == 0 and cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_WEAPON) == 0 and cl_evcon.CheckMonsterPhase(oWarrior, oEventCB, 1):
            cl_evact.EventCBSetDamageRatio(oWarrior, oEventCB, 7500, 2500)
        elif cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_ATTACH) or cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_ATTACH_HARDNESS) or cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_ATTACH_WEAKNESS):
            cl_evact.EventCBSetDamageRatio(oWarrior, oEventCB, 0, 10000)
        else:
            cl_evact.EventCBSetDamageRatio(oWarrior, oEventCB, 10000, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'NewPhase') == 1:
        cl_action.CommonSetCustomData(oWarrior, oEventCB.GetCBLifeCycle(), 'UnbalanceResetState', 'reset')
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'NewPhase') == 2:
        cl_action.CommonSetCustomData(oWarrior, oEventCB.GetCBLifeCycle(), 'UnbalanceResetState', 'MountReconnect')
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'NewPhase') == 3:
        cl_action.CommonSetCustomData(oWarrior, oEventCB.GetCBLifeCycle(), 'UnbalanceResetState', 'KnightReconnect')


class CPerform(CCustomPerform):
    m_SID = 4222
    m_Name = '骑乘怪被动'
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
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0

