# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32562.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32562.pyc
# Source Generated with Decompyle++
# File: st32562.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_war
import cl_state
from cl_commondefines import OBJ_ENEMY, STATE_ADD_SYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSelfAttackerUsePerform(oTarget, oEventCB, 8004, {
        'HitTimes': 1,
        'DamageMul': 100 }, 1)
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 32562
    m_Name = '#NT#飞花之棘'
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
    m_TargetType = OBJ_ENEMY
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 1000,
        'firsttime': 600,
        'cnt': 1 }
    m_CBFuncAction = {
        0: CallBack0 }


def CustomAction(oWarrior, oLifeCycle, dArgs):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oEventCB = oState.m_EventCB
    dEventInfo = oEventCB.GetCBEventInfo()
    iAttacker = dEventInfo['StateInfo']['AID']
    oAttacker = oWarrior.m_Game.GetObject(iAttacker)
    if not oAttacker:
        return None
    iKey = 'MonsterHit' + str(dEventInfo['StateInfo']['pfid'])
    dMonsterHit = oAttacker.Query(iKey, { })
    iMonsterID = oWarrior.m_ID
    if iMonsterID not in dMonsterHit:
        return None
    iHitTimes = dMonsterHit[iMonsterID]
    oInfoPerform = oAttacker.GetPerform(dArgs['InfoPerformID'])
    iAtt = oInfoPerform.CalAttr('Att') * iHitTimes
    oUsePerform = oAttacker.GetPerformIfNoThenNew(dArgs['UsePerformId'])
    dPerform = {
        'Custom': {
            'vEnd': oWarrior.GetPos(),
            'Att': iAtt } }
    dPerform['VID'] = iMonsterID
    cl_war.UsePerform(oAttacker, oUsePerform, dPerform)
    dMonsterHit.pop(iMonsterID)
    oAttacker.Set(iKey, dMonsterHit)

