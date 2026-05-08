# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33867.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33867.pyc
# Source Generated with Decompyle++
# File: st33867.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ATTACK, OBJ_ENEMY, OBJ_VICTIM, STATE_ADD_REPLACE_SAMEATTACK, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func404, Func429, Func826

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxCnt'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, -1, 1, 1, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameAttacker(oTarget, oEventCB, 0, 0) and cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 8015, 1, 0):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'AddDamFactor' }) * 100), 0, 0, '')


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.EventCBCheckSeedOrPlantPos(oTarget, oEventCB, 1, (lambda *a: Func826(*a))):
        cl_evact.EventCBCreateSeed(oTarget, oEventCB, 1, (lambda *a: Func404(*a)), (lambda *a: Func826(*a)))
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33867
    m_Name = '#NT#园丁种子附着'
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE_SAMEATTACK
    m_TargetType = OBJ_ENEMY
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 1
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
        0: CallBack0,
        1: CallBack1 }

