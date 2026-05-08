# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33712.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33712.pyc
# Source Generated with Decompyle++
# File: st33712.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_math
from cl_only import PY_FLAG_DEAD, Functor
from cl_commondefines import GARDENER_HERO, ATT_SHAPE_SPHERE, WARRIOR_MONSTER, GARDENER_PARASITIC_STATE
from cl_pxlayer import PXMASK_MONSTER
from cl_platformdata import CheckValidGardenerAim
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE_SAMEATTACK, STATE_CLS_SPECIAL, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxStateCount'))
    if oLifeCycle.m_Owner.GetArgValue('StateTriggerInterval'):
        cl_action.StateChangeStateDelayInfo(oTarget, oLifeCycle, oLifeCycle.m_Owner.GetArgValue('StateTriggerInterval'), oLifeCycle.m_Owner.GetArgValue('StateTriggerInterval'), 0)
        cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
            'StateTriggerInterval': oLifeCycle.m_Owner.GetArgValue('StateTriggerInterval') })
    else:
        cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
            'StateTriggerInterval': 80 })
    CustomActionBoss(oTarget, oLifeCycle, {
        'BossDataSID': 3920,
        'DuplicateDataSID': 3921 })
    if oLifeCycle.m_Owner.GetArgValue('AddCanAimMonsterState'):
        CustomActionSetCountFunc(oTarget, oLifeCycle, {
            'CanAimState': 33865,
            'StateTime': 0 })


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    CustomAction(oTarget, oLifeCycle, {
        'Dis': 10,
        'SpreadCountRatio': 100,
        'CDTime': 200,
        'SpreadTalent': 3812,
        'MinSpreadCount': 5 })


def CallBack0(oEventCB, oTarget):
    if cl_condition.RandomTrigger(oTarget, oEventCB.GetCBLifeCycle(), 100, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('NotReduceRatio')):
        cl_evact.StateCBSelfAttackerUseOnlyServerPerform(oTarget, oEventCB, 8015, {
            'Mul': (lambda *a: Func404(*a)) })
    else:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        cl_evact.StateCBSelfAttackerUseOnlyServerPerform(oTarget, oEventCB, 8015, {
            'Mul': (lambda *a: Func404(*a) + 1) })
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) == 0:
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33712
    m_Name = '#NT#园丁寄生状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_SPECIAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE_SAMEATTACK
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
    m_SendExtraInfo = 1
    m_OnlyLocalShow = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0 }


def CustomAction(oTarget, oLifeCycle, dInfo):
    if not oTarget.IsDead():
        return None
    oState = oLifeCycle.GetObject()
    if not oState.GetArgValue('Spread'):
        return None
    iNowCount = oState.GetCount()
    if iNowCount < dInfo['MinSpreadCount']:
        return None
    oGame = oTarget.m_Game
    iAID = oState.m_Attacker
    oAttacker = oGame.GetObject(iAID)
    if not oAttacker or oAttacker.m_SID != GARDENER_HERO:
        return None
    pfobj = oAttacker.GetPerform(dInfo['SpreadTalent'])
    if not pfobj or pfobj.CheckLiteCD():
        return None
    pfobj.SetLiteCD(dInfo['CDTime'])
    oGardenerCon = oAttacker.m_GardenerCon
    dMask = {
        'Mask': PXMASK_MONSTER,
        'PassID': oTarget.m_ID,
        'ExcludeFlag': PY_FLAG_DEAD }
    vPos = oTarget.GetPos()
    iScene = oTarget.m_Scene
    setHitMonster = cl_math.GetAttackTargetList(oGame, iScene, ATT_SHAPE_SPHERE, [
        vPos,
        dInfo['Dis']], dMask)
    if not setHitMonster:
        return None
    dMonster = { }
    for iMonster in setHitMonster:
        oMonster = oGame.GetObject(iMonster)
        if not oMonster:
            continue
        oMonserState = oMonster.m_State.GetItemBySource(GARDENER_PARASITIC_STATE, iAID)
        if not oMonserState:
            dMonster[iMonster] = oState.m_MaxCount
            continue
        if oMonserState.IsCountFull():
            continue
        dMonster[iMonster] = oMonserState.m_MaxCount - oMonserState.GetCount()
    
    if not dMonster:
        return None
    iSpreadCount = int(iNowCount * (dInfo['SpreadCountRatio'] / 100))
    dMonster = { iCount: iMonster for iMonster, iCount in sorted(dMonster.items(), key = (lambda x: x[1])) }

    for iMonster, iCount in dMonster.items():
        iAddCount = min(iCount, iSpreadCount)
        iSpreadCount -= iAddCount
        oGardenerCon.AddParasiticState(iMonster, 'Spread', iAddCount)
        if iSpreadCount <= 0:
            break
    


def CustomActionBoss(oTarget, oLifeCycle, dInfo):
    
    def ClearEvent(oOwner, oLifeCycle):
        oGame.DoneGlobalAttention(iTarget, cl_msgcenter.MSG_WAR_CREATEMONSTER, sKey, iSub = -1)

    if not (oTarget.m_FightType & WARRIOR_MONSTER) or oTarget.m_DataSID != dInfo['BossDataSID']:
        return None
    sKey = oLifeCycle.Key()
    oState = oLifeCycle.GetObject()
    oGame = oTarget.m_Game
    iTarget = oTarget.m_ID
    iStateID = oState.m_ID
    oGame.AddGlobalAttention(iTarget, cl_msgcenter.MSG_WAR_CREATEMONSTER, Functor(OnCreateMonster, oState.m_Attacker, dInfo['DuplicateDataSID'], iStateID), sKey, iSub = -1)
    oLifeCycle.AddDisableFunc(ClearEvent)


def OnCreateMonster(iAID, iDuplicateDataSID, iStateID, oEntity, oDuplicate, dMsgInfo):
    if oDuplicate.m_DataSID != iDuplicateDataSID:
        return None
    oGame = oEntity.m_Game
    oAttacker = oGame.GetObject(iAID)
    if not oAttacker:
        return None
    oState = oEntity.m_State.GetItem(iStateID)
    if not oState:
        return None
    oGardenerCon = oAttacker.m_GardenerCon
    oGardenerCon.AddParasiticState(oDuplicate.m_ID, 'EntityAdd', oState.GetCount())


def CustomActionSetCountFunc(oTarget, oLifeCycle, dInfo):
    if not CheckValidGardenerAim(oTarget.m_Shape):
        return None
    oState = oLifeCycle.GetObject()
    oState.m_LifeCycle.RegisterFunc('Count', Functor(StateCountAction, dInfo['CanAimState'], dInfo['StateTime']))


def StateCountAction(iStateSID, iStateTime, oTarget, oLifeCycle):
    if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oLifeCycle):
        cl_action.StateAddState(oTarget, oLifeCycle, iStateSID, iStateTime, { })

