# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/levelline/levelnodeplug.pyc
# RelativePath: clientlogic/cl_warmgr/levelline/levelnodeplug.pyc
# Source Generated with Decompyle++
# File: levelnodeplug.pyc (Python 3.6)

from cl_commondefines import STATE_UNDER_ATTACK, GetPlayMode, PLAYMODE_NEWBIE, LEVEL_TYPE_HIDE, STATE_TIME_FOREVER, PLAYMODE_MOBILE_DEMO, WARRIOR_MONSTER
from cl_only import WeakProxy, Functor, PY_FLAG_DEAD
from cl_gamestatus import STAT_GAME_INIT
from cl_object.logging import LevelLog
import cl_framegame
import cl_state
import cl_object
import cl_msgcenter

class CBaseNodePlug(object):
    
    def __init__(self, oLevelNode):
        self.m_LevelNode = WeakProxy(oLevelNode)
        self.m_Game = oLevelNode.m_CtrlMgr.m_Game

    
    def Release(self):
        self.ReleaseMusicEvent()
        self.m_LevelNode = None
        self.m_Game = None

    
    def OnLevelInit(self):
        pass

    
    def OnLevelStart(self):
        pass

    
    def OnLevelGoal(self):
        self.InitMusicEvent()

    
    def OnLevelFinish(self):
        pass

    
    def OnLineStart(self):
        pass

    
    def OnLineGoal(self):
        pass

    
    def InitMusicEvent(self):
        self.m_Game.AddGlobalAttention(self.m_LevelNode.m_CtrlMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnMonsterDie, self.m_LevelNode.m_Level)

    
    def ReleaseMusicEvent(self):
        self.m_Game.DoneGlobalAttention(self.m_LevelNode.m_CtrlMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_LevelNode.m_Level)

    
    def OnHeroEnterLevel(self, lstHero):
        self.UpdateImmuneInjury(lstHero, True)
        self.StopUnderAttackState(lstHero)

    
    def OnPlayerMapLoadOK(self, lstHero):
        self.UpdateImmuneInjury(lstHero, False)

    
    def StopUnderAttackState(self, lstHero):
        iState = STATE_UNDER_ATTACK
        for iTarget in lstHero:
            oTarget = self.m_Game.GetObject(iTarget)
            if oTarget:
                cl_state.RemoveState(oTarget, iState)
        

    
    def UpdateImmuneInjury(self, lstHero, bAdd):
        iLayerNum = self.m_LevelNode.m_LayerNum
        iLevelNum = self.m_LevelNode.m_LevelNum
        if iLayerNum == 1 and iLevelNum == 0:
            return None
        for iHero in lstHero:
            oHero = self.m_Game.GetObject(iHero)
            if not bAdd or oHero.m_Agent:
                cl_state.RemoveState(oHero, 1204)
                continue
            oReason = cl_object.reason.CStrReason('切关卡免疫伤害')
            dArgs = {
                'AID': self.m_LevelNode.m_CtrlMgr.m_ID,
                'RS': oReason,
                'arg': { } }
            oState = cl_state.AddState(oHero, 1204, STATE_TIME_FOREVER, 0, dArgs)
            oState.Enable(oHero)
        

    
    def OnMonsterDie(self, oLevelCtrl, oWarrior, dMsgInfo):
        if oWarrior.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
            return None
        if self.m_LevelNode.m_Scene != oWarrior.m_Scene:
            return None
        oGame = oLevelCtrl.m_Game
        oScene = oGame.m_SceneMgr.GetScene(self.m_LevelNode.m_Scene)
        bAlive = False
        for iMonster in oScene.GetObjectsByType('Monster'):
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster:
                continue
            if oMonster.IsPetrochemical():
                continue
            bAlive = True
        
        if not bAlive:
            self.m_LevelNode.EndUnderAttack(oScene)

    
    def OverTimeStart(self):
        pass



class CLevelNodePlug(CBaseNodePlug):
    
    def OnLevelInit(self):
        oWarMgr = self.m_Game.m_WarMgr
        iPlayMode = GetPlayMode(oWarMgr.m_SID)
        if iPlayMode in (PLAYMODE_NEWBIE, PLAYMODE_MOBILE_DEMO):
            return None
        self.OverTimeStart()

    
    def OnLevelStart(self):
        self.CancelOverTimeStart()
        self.StartInitStep()

    
    def StartStep(self):
        self.m_Game.m_Status.StartStep()

    
    def StartInitStep(self):
        if self.m_Game.m_Status.m_Status == STAT_GAME_INIT:
            self.m_Game.m_Status.StartStep()

    
    def StopStep(self):
        self.m_Game.m_Status.StopStep()

    
    def CancelOverTimeStart(self):
        oGame = self.m_Game
        oGame.m_Timer.Logic_Remove_Call_Out('NodeOverTimeStart')

    
    def OverTimeStart(self):
        oGame = self.m_Game
        LevelLog.Debug('%s setovertimestart' % oGame.m_ID)
        oGame.m_Timer.Logic_Call_Out(Functor(OnOverTimeRevert, oGame.m_ID), 2000, 'NodeOverTimeStart')



def OnOverTimeRevert(iGameID):
    oGame = cl_framegame.GetGame(iGameID)
    if not oGame:
        return None
    oWarMgr = oGame.m_WarMgr
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    oLevel = oLevelCtrl.m_CurNode
    iLevel = oLevel.m_Level if oLevel else 0
    LevelLog.Debug('%s onovertimerevert %s' % (oGame.m_ID, iLevel))
    if oLevel:
        oLevel.LevelStart()


def GetLevelNodePlug(oLevelNode):
    if oLevelNode.m_LevelType == LEVEL_TYPE_HIDE:
        return CBaseNodePlug(oLevelNode)
    return CLevelNodePlug(oLevelNode)

