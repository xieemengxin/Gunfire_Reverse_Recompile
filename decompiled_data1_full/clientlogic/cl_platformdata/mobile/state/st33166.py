# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33166.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33166.pyc
# Source Generated with Decompyle++
# File: st33166.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func423

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckAttackInShield(oTarget, oEventCB) == 0:
        cl_evact.EventGetStateInfoTarget(oTarget, oEventCB)
        cl_evact.EventTargetShareDamage(oTarget, oEventCB, 3000, (lambda *a: Func423(*a)), 1, None, 1)
        cl_evact.EventCBReducePredictDam(oTarget, oEventCB, (lambda *a: Func423(*a) * 60 // 100), None)


class CState(cl_state.CState):
    m_SID = 33166
    m_Name = '#NT#妖化增幅-妖气荫庇'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
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
    m_CBFuncAction = {
        0: CallBack0 }

