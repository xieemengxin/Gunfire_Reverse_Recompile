# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4205.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4205.pyc
# Source Generated with Decompyle++
# File: p4205.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_betree.monsteragent as magent
from cl_only import PY_FLAG_DEAD, Functor
from cl_commondefines import WARRIOR_MONSTER, WARRIOR_SUMMON
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import FIGHT_KEY_WUDI
from cl_newformula import Func204, Func221

def Action1(oWarrior, oLifeCycle):
    CustomAction(oWarrior, oLifeCycle, {
        3921: 1,
        1053: 1 })
    cl_action.CommonAddSpecialKey(oWarrior, oLifeCycle, FIGHT_KEY_WUDI, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func221(*a))) >= 1 and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func204(*a))) == 3:
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', -3000, 0, None)
    elif cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func221(*a))) >= 1 and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func204(*a))) == 4:
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', -3600, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4205
    m_Name = '章鱼触手生命连接及轮回血量特殊处理'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 1


def CustomAction(oWarrior, oLifeCycle, dData):
    
    def ClearEvent(oOwner, oLifeCycle):
        oScene = oOwner.m_Game.m_SceneMgr.GetScene(oOwner.m_Scene)
        if oScene:
            oScene.m_CustomData.pop('TentaclePos', None)
            oScene.m_CustomData.pop('TentacleID', None)
        oOwner.m_Game.DoneGlobalAttention(iTarget, cl_msgcenter.MSG_WAR_CREATEMONSTER, sKey, -1)
        oOwner.m_Game.DoneGlobalAttention(iTarget, cl_msgcenter.MSG_WAR_REMOVEOBJ, sKey, -1)
        oOwner.m_Game.DoneGlobalAttention(iTarget, cl_msgcenter.MSG_WAR_DIE, sKey, -1)

    iTarget = oWarrior.m_ID
    sKey = oLifeCycle.Key()
    oWarrior.m_Game.AddGlobalAttention(iTarget, cl_msgcenter.MSG_WAR_CREATEMONSTER, Functor(OnCreateMonster, dData), sKey, -1)
    oWarrior.m_Game.AddGlobalAttention(iTarget, cl_msgcenter.MSG_WAR_REMOVEOBJ, Functor(OnRemoveMonster, dData), sKey, -1)
    oWarrior.m_Game.AddGlobalAttention(iTarget, cl_msgcenter.MSG_WAR_DIE, Functor(OnRemoveMonster, dData), sKey, -1)
    oLifeCycle.AddDisableFunc(ClearEvent)


def OnCreateMonster(dData, oListener, oSender, dMsgInfo):
    if oSender.m_DataSID not in dData:
        return None
    pfobj = oListener.GetPerform(CPerform.m_SID)
    if not pfobj:
        return None
    sKey = '%s-%s' % (pfobj.Key(), oSender.m_ID)
    cl_msgcenter.AddAttentionFunc(oListener, oSender.m_ID, cl_msgcenter.MSG_WAR_HP_CHANGE, OnMonsterHPChange, sKey)
    oSender.Set('TentacleOwner', oListener.m_ID)


def OnRemoveMonster(dData, oListener, oSender, dMsgInfo):
    iTarget = oSender.m_ID
    if oSender.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
        if iTarget not in oListener.m_MonsterSummon:
            return None
        oListener.m_MonsterSummon.pop(iTarget)
    elif not oSender.m_FightType & WARRIOR_SUMMON == WARRIOR_SUMMON:
        return None
    if oSender.m_DataSID not in dData:
        return None
    oGame = oListener.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if not oScene:
        return None
    dAllTentacle = oScene.m_CustomData.get('TentaclePos', None)
    dID = oScene.m_CustomData.get('TentacleID', None)
    if not dAllTentacle or not dID:
        return None
    tIndex = dID.pop(iTarget, None)
    if tIndex is None:
        return None
    (key, iIndex) = tIndex
    dAllTentacle.get(key, { }).pop(iIndex, None)


def OnMonsterHPChange(oListener, oSender, dMsgInfo):
    if oListener.IsDead():
        return None
    if oSender.m_ID not in oListener.m_MonsterSummon:
        return None
    iAttack = dMsgInfo['AID']
    iFactor = -1 if dMsgInfo['IsDam'] else 1
    oListener.Set('LastDamedTentacle', oSender.m_ID)
    iTotalDam = 0
    if dMsgInfo['IsDam']:
        iCurFrame = oListener.m_Game.GetFrameNum()
        oListener.Set('Injured%d' % iAttack, iCurFrame)
    for iTrueChange, oReason in dMsgInfo['TrueChange']:
        oListener.HPDirectModify('HP', iAttack, iFactor * iTrueChange, oReason)
        iTotalDam += iTrueChange
    
    if oListener.m_Agent and dMsgInfo['IsDam']:
        magent.DamHateVal(oListener, {
            'IsDam': dMsgInfo['IsDam'],
            'AID': iAttack,
            'TotalDam': [
                iTotalDam] })

