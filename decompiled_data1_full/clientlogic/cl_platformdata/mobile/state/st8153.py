# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8153.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8153.pyc
# Source Generated with Decompyle++
# File: st8153.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, OBJ_SELF, PATHMODE_STAYSTATUS, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_DEBAR, WARRIOR_BOSS

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.HasState(oTarget, oLifeCycle, 8154):
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 8154, 0)
    cl_action.CommonSetImmobilize(oTarget, oLifeCycle)
    cl_action.CommonAddLogicKey(oTarget, oLifeCycle, FIGHT3_KEY_IGNORETHUMP)
    cl_action.CommonAddLogicKey(oTarget, oLifeCycle, FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.SwitchTargetPathMode(oTarget, oLifeCycle, PATHMODE_STAYSTATUS)
    if not cl_condition.CheckTargetFightType(oTarget, oLifeCycle, WARRIOR_BOSS):
        cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'CommonMonsterFly', 1)
        cl_action.CommonAddSkillCheckExtraArgs(oTarget, oLifeCycle, 0, 2.5)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.StateAddState(oTarget, oLifeCycle, 8154, 50, { }, 0)
    cl_action.CommonSendStateMessage(oTarget, oLifeCycle, 0, { })
    oTarget.Delete('CommonMonsterFly')


class CState(cl_state.CState):
    m_SID = 8153
    m_Name = '#NT#狮子强化困势升空状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_DEBAR
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 0
    m_Action = (StateActAction, StateRemoveAction)

