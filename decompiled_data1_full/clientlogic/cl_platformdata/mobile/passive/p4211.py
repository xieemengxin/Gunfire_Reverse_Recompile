# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4211.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4211.pyc
# Source Generated with Decompyle++
# File: p4211.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_snetwar
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_HP, FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, FIGHT3_KEY_IGNOREVERTIGO, OBJ_SELF
from cl_newformula import Func368

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 1, 0, 0)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNORETHUMP)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNOREVERTIGO)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 2, 0, 0)
    cl_action.CommonSetHeightOffset(oWarrior, oLifeCycle, 2)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonSetSkillCheckArgs(oWarrior, oEventCB.GetCBLifeCycle(), 65, 40)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckReason(oWarrior, oEventCB, 'FollowDie', None) == 0:
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, 100, CURE_TYPE_PERFORM | DAM_USE_HP, 0, 0, 0)
    else:
        CustomAction(oWarrior, oEventCB, {
            'len': 3 })


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 1854) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 4211, 0, 0) == 0:
        cl_evact.EventCBGetTentacleOwnerAndOtherTentacle(oWarrior, oEventCB)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1854, (lambda *a: Func368(*a)), { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4211
    m_Name = '章鱼触手免死改校验与额外距离'
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


def CustomAction(oWarrior, oEventCB, dData):
    iLen = dData.get('len', 3)
    oOwner = oWarrior.m_Game.GetObject(oWarrior.Query('TentacleOwner', 0))
    if not oOwner:
        return None
    if oOwner.Query('LastDamedTentacle', 0) == oWarrior.m_ID:
        cl_snetwar.GS2CMonsterActionSM(oWarrior, 4, 'Type', 0)
    else:
        iFollowDieCnt = oOwner.Query('TentacleFollowDieCnt', 0)
        cl_snetwar.GS2CMonsterActionSM(oWarrior, 4, 'Type', iFollowDieCnt % iLen + 1)
        oOwner.Set('TentacleFollowDieCnt', iFollowDieCnt + 1)

