# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1047.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1047.pyc
# Source Generated with Decompyle++
# File: st1047.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_SPECIAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    CustomAction(oTarget, oLifeCycle, {
        'Perform': 21811 })
    cl_action.CommonForbid(oTarget, oLifeCycle, 1052)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBHaltAttackerPerform(oTarget, oEventCB, 21811)


class CState(cl_state.CState):
    m_SID = 1047
    m_Name = '#NT#玩家被锁链兵拉回'
    m_IsShow = 1
    m_Type = STATE_CLS_SPECIAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
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


def CustomAction(oTarget, oLifeCycle, dInfo):
    oCurState = oLifeCycle.GetObject()
    if not oCurState:
        return None
    iPerform = dInfo.get('Perform', 0)
    if not iPerform:
        return None
    oGame = oTarget.m_Game
    iStateSID = oCurState.m_SID
    lstState = oTarget.m_State.GetItems(iStateSID)
    for oState in lstState:
        if oState == oCurState:
            continue
        iAttack = oState.m_Attacker
        oAttack = oGame.GetObject(iAttack)
        if not oAttack:
            continue
        for iActNum, dCasting in oAttack.GetAllCasting():
            if dCasting['pfid'] != iPerform:
                continue
            cl_action.HaltCasting(oAttack, iActNum, oLifeCycle.Key())
        
    

