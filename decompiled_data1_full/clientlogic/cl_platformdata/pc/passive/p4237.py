# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4237.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4237.pyc
# Source Generated with Decompyle++
# File: p4237.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_snetwar
import cl_world
import cl_bezier
from cl_only import Functor
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, FIGHT3_KEY_IGNOREVERTIGO, HP_RADIO_SUB

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 80, HP_RADIO_SUB, 1)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 50, HP_RADIO_SUB, 1)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 30, HP_RADIO_SUB, 1)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNORETHUMP)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNOREVERTIGO)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7115, 6000, { }, -1)


def DoCallBackAction2(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB.GetCBLifeCycle(), {
        'Interval': 2 })
    cl_action.CommonSetSkillCheckArgs(oWarrior, oEventCB.GetCBLifeCycle(), 2.5, 1.8)


class CPerform(CCustomPerform):
    m_SID = 4237
    m_Name = '巨型召唤怪被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0


def CustomAction(oWarrior, oLifeCycle, dInfo):
    
    def ClearEvent(oOwner, oLifeCycle):
        oOwner.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, sKey, -1)
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_DIE, 'MonsterDie')

    oGame = oWarrior.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    sKey = oLifeCycle.Key()
    oGame.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, Functor(OnMapLoadOk, oWarrior), sKey, -1)
    cl_msgcenter.AddFunction(oWarrior, cl_msgcenter.MSG_WAR_DIE, OnDie, 'MonsterDie', -1, 0)
    SyncCannonID(oWarrior)
    oLifeCycle.AddDisableFunc(ClearEvent)
    InitBezierCurve(oWarrior)


def OnMapLoadOk(oWarrior, oLevelCtrl, oHero, dMsgInfo):
    oGame = oWarrior.m_Game
    iScene = oWarrior.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    iLevel = oScene.m_Level
    if iLevel == dMsgInfo['LevelID']:
        SyncCannonID(oWarrior)


def OnDie(oWarrior, oSender):
    oGame = oWarrior.m_Game
    dAffiliateMonster = oWarrior.Query('AffiliateMonster', { })
    for iMonster in dAffiliateMonster:
        oMonster = oGame.GetObject(iMonster)
        oMonster.Remove('OwnerDie')
    
    oWarrior.Set('AffiliateMonster', { })


def SyncCannonID(oWarrior):
    oGame = oWarrior.m_Game
    if oWarrior.IsDead():
        return None
    dAffiliateMonster = oWarrior.Query('AffiliateMonster', { })
    if not dAffiliateMonster:
        for _ in range(3):
            iMonster = oGame.NewNPCID()
            dAffiliateMonster[iMonster] = cl_world.CSceneObject(oGame, iMonster)
        
        oWarrior.Set('AffiliateMonster', dAffiliateMonster)
    cl_snetwar.GS2CMonsterAdditionInfo(oGame, oWarrior, list(dAffiliateMonster.keys()))


def InitBezierCurve(oWarrior):
    oAgent = oWarrior.m_Agent
    lstPos = oAgent.GetConfig('CurveMoveLine')
    if not lstPos:
        return None
    oWarrior.m_CurveCompute = cl_bezier.SecondBeizer(lstPos[0], lstPos[1], lstPos[2])

