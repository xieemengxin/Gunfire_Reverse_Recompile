# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33596.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33596.pyc
# Source Generated with Decompyle++
# File: st33596.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, LEVEL_TYPE_BOSS, OBJECT_OWNER, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REFRESHORSYNC_SAMEITEM, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, oLifeCycle.m_Owner.GetArgValue('StateCount'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_BOSS) or cl_evcon.CheckTargetDist(oTarget, oEventCB, 40, 0, OBJECT_OWNER):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: 1000 * Func404(*a)), DAM_MASK_ELEMENT, '')
    elif cl_evcon.CheckTargetDist(oTarget, oEventCB, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect'), 0, OBJECT_OWNER):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: 1000 * Func404(*a)), DAM_MASK_ELEMENT, '')


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'ExcessiveDam': 40 })
    else:
        cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'ExcessiveDam': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect') })


class CState(cl_state.CState):
    m_SID = 33596
    m_Name = '近距增幅'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC_SAMEITEM
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

