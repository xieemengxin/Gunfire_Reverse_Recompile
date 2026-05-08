# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1773.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1773.pyc
# Source Generated with Decompyle++
# File: st1773.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import LEVEL_TYPE_BOSS, MONSTERPF_TYPE_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func572

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.StateRefreshMonsterRelicCnt(oTarget, oLifeCycle, 25823)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckMonsterPFAttackType(oTarget, oEventCB, MONSTERPF_TYPE_ATTACK) and cl_evcon.CheckHasState(oTarget, oEventCB, 1774) == 0 and cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_BOSS) == 0:
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1774, 200, { }, None)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 10, None)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 20:
            cl_evact.EventCBMonsterRelicCreateMonster(oTarget, oEventCB, 25823, 1, (lambda *a: Func572(*a) * 3), 1904, 1774, 1, 10, 1, 179, {
                25823: 1,
                25822: 1 })


class CState(cl_state.CState):
    m_SID = 1773
    m_Name = '#NT#秘密魔匣（怪物遗物）'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 20
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

