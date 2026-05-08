# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32300.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32300.pyc
# Source Generated with Decompyle++
# File: st32300.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_WEAPON, EQUIP_SNIPER, OBJ_ENEMY, OBJ_VICTIM, STATE_ADD_SYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_SNIPER) and cl_evcon.CheckStateAddByIs(oTarget, oEventCB, None):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, (lambda *a: Func404(*a) * 2500), 0, DAM_TYPE_WEAPON, '')


class CState(cl_state.CState):
    m_SID = 32300
    m_Name = '#NT#虹积骨销2(怪物)'
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
    m_TargetType = OBJ_ENEMY
    m_MinCount = 0
    m_MaxCount = 4
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

