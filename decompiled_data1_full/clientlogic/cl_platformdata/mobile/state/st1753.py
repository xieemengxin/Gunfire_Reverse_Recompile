# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1753.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1753.pyc
# Source Generated with Decompyle++
# File: st1753.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_NONE, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_NORMAL
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', -7000, 0, -1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIEDIST, -1, 0, 0, 0)
    if cl_condition.CheckTargetFightType(oTarget, oLifeCycle, WARRIOR_NORMAL):
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, 500)
    if cl_condition.CheckTargetFightType(oTarget, oLifeCycle, WARRIOR_ELITE):
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, 250)
    if cl_condition.CheckTargetFightType(oTarget, oLifeCycle, WARRIOR_BOSS):
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, 100)


def DelayAction(oTarget, oLifeCycle):
    cl_action.StatePullOwnerToPos(oTarget, oLifeCycle, (lambda *a: Func404(*a)), 150, 0.3, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonSendStateMessage(oTarget, oEventCB.GetCBLifeCycle(), 0, {
        'ActNum': cl_action.StateGetFromSkillActNum(oTarget, oEventCB.GetCBLifeCycle()) })


class CState(cl_state.CState):
    m_SID = 1753
    m_Name = '#NT#狱裂骨龙强化吸附（已废弃）'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
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
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100 }
    m_CBFuncAction = {
        0: CallBack0 }

