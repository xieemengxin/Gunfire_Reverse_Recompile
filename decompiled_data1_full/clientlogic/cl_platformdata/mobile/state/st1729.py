# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1729.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1729.pyc
# Source Generated with Decompyle++
# File: st1729.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ATTACK, OBJ_SELF, SKILLCACHE_INT, STATE_ADD_LONGORSYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB) and cl_evcon.EventCBCheckSkillCache(oTarget, oEventCB, SKILLCACHE_INT):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if not cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1730, 0, 0, 0, 1):
            if cl_evcon.CheckHitWeakness(oTarget, oEventCB, 0):
                cl_evact.StateAddSelfCount(oTarget, oEventCB, 3, None)
                cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'st1729')
                if cl_evcon.CheckWeaponHasInscription(oTarget, oEventCB, 13049) and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 24:
                    cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1730, 500, { }, (lambda *a: Func437(*a, **{
'sKey': 'st1729' })))
                    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
                    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1812, 500, 0, { }, 1, 1, None)
                    cl_evact.StateCBSelfRemove(oTarget, oEventCB)
                elif cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 24:
                    cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1730, 500, { }, None)
                    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
                    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1812, 500, 0, { }, 1, 1, None)
                    cl_evact.StateCBSelfRemove(oTarget, oEventCB)
            else:
                cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
                if cl_evcon.CheckWeaponHasInscription(oTarget, oEventCB, 13049) and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 24:
                    cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1730, 500, { }, (lambda *a: Func437(*a, **{
'sKey': 'st1729' })))
                    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
                    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1812, 500, 0, { }, 1, 1, None)
                    cl_evact.StateCBSelfRemove(oTarget, oEventCB)
                elif cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 24:
                    cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1730, 500, { }, None)
                    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
                    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1812, 500, 0, { }, 1, 1, None)
                    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1729
    m_Name = '机瞄步枪计数（boss）'
    m_DieRemove = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_LONGORSYNC
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 24
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_OnlyLocalShow = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

